"""Regressionstests für Graph-Skripte und Review-Prüfung. Aufruf: python3 -m unittest discover -s tests -v"""
import collections
import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILL = ROOT / ".agents" / "skills" / "arc42-knowledge-graph"
CHECK_REVIEW = ROOT / ".agents" / "skills" / "arc42-review-format" / "scripts" / "check_review.py"
sys.path.insert(0, str(SKILL / "scripts"))
import validate_graph as vg  # noqa: E402

DOC = ROOT / "arc-doc"
RUNS = sorted((ROOT / ".arc42-graph_demo_results").glob("FullReviewRun*"))
SCHEMA = json.loads((SKILL / "schema.json").read_text(encoding="utf-8"))


def run(*args):
    return subprocess.run([sys.executable, *map(str, args)], capture_output=True, text=True, cwd=ROOT)


def build(extraction, out_dir, *extra, doc=DOC, name="t"):
    return run(SKILL / "scripts" / "build_graph.py", extraction, "--doc", doc, "--out-dir", out_dir, "--name", name, *extra)


@unittest.skipUnless(RUNS and DOC.is_dir(), "Demo-Graphen oder arc-doc fehlen")
class DemoGraphs(unittest.TestCase):
    def test_committed_graphs_are_valid(self):
        for r in RUNS:
            with self.subTest(run=r.name):
                rep, loaded = vg.run_checks(str(r / "arc-doc.graphml"), SCHEMA, DOC, str(r / "arc-doc.manifest.json"))
                self.assertIsNotNone(loaded)
                self.assertEqual(rep.count("error"), 0, rep.items)
                self.assertEqual(rep.count("warning"), 0, rep.items)

    def test_rebuild_reproduces_graph(self):
        for r in RUNS:
            with self.subTest(run=r.name), tempfile.TemporaryDirectory() as tmp:
                result = build(r / "arc-doc.extraction.json", tmp)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                old = vg.load_graph(str(r / "arc-doc.graphml"), SCHEMA, vg.Report())
                new = vg.load_graph(str(pathlib.Path(tmp) / "t.graphml"), SCHEMA, vg.Report())
                self.assertEqual((len(old[0]), len(old[1])), (len(new[0]), len(new[1])))

    def test_delta_marks_nodes_and_edges(self):
        r = RUNS[0]
        data = json.loads((r / "arc-doc.extraction.json").read_text(encoding="utf-8"))
        source = collections.Counter(n["source_file"] for n in data["nodes"]).most_common(1)[0][0]
        expected = sum(1 for n in data["nodes"] if n["source_file"] == source)
        with tempfile.TemporaryDirectory() as tmp:
            result = build(r / "arc-doc.extraction.json", tmp, "--changed", source + ":added")
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            nodes, edges = vg.load_graph(str(pathlib.Path(tmp) / "t.graphml"), SCHEMA, vg.Report())
            changed = [d for d in nodes.values() if d.get("changed") == "true"]
            self.assertEqual(len(changed), expected)
            self.assertTrue(all(d.get("change_type") == "added" for d in changed))
            self.assertTrue(any(d.get("changed") == "true" for _, _, _, d in edges))

    def test_build_without_delta_has_no_delta_keys(self):
        with tempfile.TemporaryDirectory() as tmp:
            build(RUNS[0] / "arc-doc.extraction.json", tmp)
            self.assertNotIn('attr.name="changed"', (pathlib.Path(tmp) / "t.graphml").read_text(encoding="utf-8"))

    def test_invalid_change_type_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = build(RUNS[0] / "arc-doc.extraction.json", tmp, "--changed", "x.md:deleted")
            self.assertNotEqual(result.returncode, 0)

    def test_density_hint_for_sparse_graph(self):
        hints = {}
        for r in RUNS:
            rep, _ = vg.run_checks(str(r / "arc-doc.graphml"), SCHEMA)
            hints[r.name] = len(rep.items.get(("info", "graph-duenn"), []))
        sparse = [n for n in hints if "GPT" in n]
        dense = [n for n in hints if "GPT" not in n]
        self.assertTrue(all(hints[n] > 0 for n in sparse), hints)
        self.assertTrue(all(hints[n] == 0 for n in dense), hints)


class SingleFileDoc(unittest.TestCase):
    def test_single_file_documentation(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = pathlib.Path(tmp)
            (tmp / "doc.md").write_text("## 1 Einführung\n\nDas System ist X.\n\n## 2 Randbedingungen\n\nKein Cloud.\n", encoding="utf-8")
            node = {"description": "d", "source_file": "doc.md"}
            extraction = {"nodes": [
                dict(node, id="s01-req-x", type="Requirement", label="X", section="1", source_anchor="## 1 Einführung"),
                dict(node, id="s02-con-cloud", type="Constraint", label="Kein Cloud", section="2", source_anchor="## 2 Randbedingungen", category="technisch"),
            ], "edges": []}
            (tmp / "ex.json").write_text(json.dumps(extraction), encoding="utf-8")
            result = build(tmp / "ex.json", tmp / "out", doc=tmp / "doc.md", name="doc")
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            manifest = json.loads((tmp / "out" / "doc.manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(list(manifest["files"]), ["doc.md"])


class ReviewChecker(unittest.TestCase):
    def test_graph_reviews_pass(self):
        reports = sorted(ROOT.glob("FullReviewResultGraph*.md"))
        if not reports or not DOC.is_dir():
            self.skipTest("keine Review-Berichte")
        result = run(CHECK_REVIEW, *reports, "--doc", DOC)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_detects_wrong_summary_and_duplicate_ids(self):
        report = (
            "# Review\n\n#### [S01-01] A\n\n**Schwere:** 🔴 Kritisch\n\n**Änderungsvorschlag:** x\n\n"
            "#### [S01-01] B\n\n**Schwere:** 🟢 Hinweis\n\n**Änderungsvorschlag:** y\n\n"
            "## Zusammenfassung\n\n| Kategorie | Anzahl |\n|---|---|\n| 🔴 Kritische Befunde | 2 |\n| 🟡 Warnungen | 0 |\n| 🟢 Hinweise | 1 |\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = pathlib.Path(tmp) / "r.md"
            path.write_text(report, encoding="utf-8")
            result = run(CHECK_REVIEW, path, "--doc", ROOT / "arc-doc")
            self.assertEqual(result.returncode, 1)
            self.assertIn("kommt 2-mal vor", result.stdout)
            self.assertIn("Zusammenfassung nennt kritisch 2", result.stdout)


if __name__ == "__main__":
    unittest.main()
