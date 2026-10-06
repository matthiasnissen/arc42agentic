#!/usr/bin/env python3
"""Validiert einen arc42-Wissensgraphen (GraphML) gegen schema.json. Nur Standardbibliothek."""
import argparse
import collections
import hashlib
import json
import pathlib
import re
import sys
import xml.etree.ElementTree as ET

HERE = pathlib.Path(__file__).resolve().parent
DEFAULT_SCHEMA = HERE.parent / "schema.json"


class Report:
    def __init__(self):
        self.items = collections.OrderedDict()

    def add(self, level, rule, message):
        self.items.setdefault((level, rule), []).append(message)

    def count(self, level):
        return sum(len(v) for (lvl, _), v in self.items.items() if lvl == level)

    def print(self, limit):
        for level in ("error", "warning", "info"):
            groups = [(rule, msgs) for (lvl, rule), msgs in self.items.items() if lvl == level]
            for rule, msgs in groups:
                print("[%s] %s (%d)" % (level.upper(), rule, len(msgs)))
                for m in msgs[:limit]:
                    print("    - " + m)
                if len(msgs) > limit:
                    print("    ... %d weitere" % (len(msgs) - limit))
        print("Ergebnis: %d Fehler, %d Warnungen, %d Hinweise" % (
            self.count("error"), self.count("warning"), self.count("info")))


def section_number(value):
    m = re.match(r"^(\d{1,2})(?:[.\-_ ]|$)", value or "")
    return int(m.group(1)) if m else None


def doc_base(doc, schema):
    """Liefert (Basisordner, relative Quelldateien) für Ordner- oder Einzeldatei-Dokumentation."""
    if doc is None:
        return None, set()
    if doc.is_file():
        return doc.parent, {doc.name}
    exts = tuple(e.lower() for e in schema.get("doc_extensions", [".md"]))
    return doc, {p.relative_to(doc).as_posix() for p in doc.rglob("*") if p.is_file() and p.suffix.lower() in exts}


def load_graph(path, schema, rep):
    ns = {"g": schema["graphml"]["namespace"]}
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as exc:
        rep.add("error", "xml-wohlgeformt", "XML nicht parsebar: %s" % exc)
        return None
    graph = root.find("g:graph", ns)
    if graph is None:
        rep.add("error", "graph-element", "Kein <graph>-Element im GraphML-Namespace gefunden")
        return None
    if graph.get("id") != schema["graphml"]["graph_id"]:
        rep.add("warning", "graph-id", "graph id ist %r, erwartet %r" % (graph.get("id"), schema["graphml"]["graph_id"]))
    if graph.get("edgedefault") != schema["graphml"]["edgedefault"]:
        rep.add("error", "edgedefault", "edgedefault ist %r, erwartet %r" % (graph.get("edgedefault"), schema["graphml"]["edgedefault"]))

    declared = {"node": {}, "edge": {}}
    for k in root.findall("g:key", ns):
        declared.setdefault(k.get("for"), {})[k.get("id")] = (k.get("attr.name"), k.get("attr.type"))
    for target in ("node", "edge"):
        for kid, spec in schema["graphml"]["keys"][target].items():
            got = declared[target].get(kid)
            if got is None:
                if spec["required"]:
                    rep.add("error", "key-deklariert", "%s-Key %s (%s) fehlt" % (target, kid, spec["name"]))
            elif got != (spec["name"], spec["type"]):
                rep.add("error", "key-deklariert", "%s-Key %s ist %s, erwartet %s" % (target, kid, got, (spec["name"], spec["type"])))
        for kid in declared[target]:
            if kid not in schema["graphml"]["keys"][target]:
                rep.add("warning", "key-unbekannt", "%s-Key %s ist im Schema nicht vorgesehen" % (target, kid))

    nodes, edges = collections.OrderedDict(), []
    for n in graph.findall("g:node", ns):
        nid = n.get("id")
        if nid in nodes:
            rep.add("error", "knoten-id-eindeutig", "Doppelte Knoten-ID %s" % nid)
        data = {}
        for x in n.findall("g:data", ns):
            name = declared["node"].get(x.get("key"), (x.get("key"), None))[0]
            data[name] = x.text or ""
        nodes[nid] = data
    seen_edge_ids = set()
    for e in graph.findall("g:edge", ns):
        data = {}
        for x in e.findall("g:data", ns):
            name = declared["edge"].get(x.get("key"), (x.get("key"), None))[0]
            data[name] = x.text or ""
        eid = e.get("id")
        if not eid:
            rep.add("error", "kanten-id", "Kante %s -> %s ohne id-Attribut" % (e.get("source"), e.get("target")))
        else:
            if not re.match(schema["graphml"]["edge_id_pattern"], eid):
                rep.add("error", "kanten-id", "Kanten-ID %r entspricht nicht %s" % (eid, schema["graphml"]["edge_id_pattern"]))
            if eid in seen_edge_ids:
                rep.add("error", "kanten-id", "Doppelte Kanten-ID %s" % eid)
            seen_edge_ids.add(eid)
        edges.append((eid, e.get("source"), e.get("target"), data))
    return nodes, edges


def check_nodes(nodes, schema, doc, rep):
    base, _ = doc_base(doc, schema)
    types = schema["node_types"]
    for nid, d in nodes.items():
        t = d.get("type", "")
        spec = types.get(t)
        if spec is None:
            rep.add("error", "knotentyp", "%s: Typ %r nicht im Vokabular" % (nid, t))
            continue
        if t == "Community":
            if not re.match(schema["id_patterns"]["community"], nid):
                rep.add("error", "id-konvention", "Community-ID %s entspricht nicht %s" % (nid, schema["id_patterns"]["community"]))
            for a in spec["required"]:
                if not d.get(a, "").strip():
                    rep.add("error", "pflichtattribut", "%s (Community): %s fehlt" % (nid, a))
            continue
        if not re.match(schema["id_patterns"]["node"], nid):
            rep.add("error", "id-konvention", "%s (%s): ID entspricht nicht %s" % (nid, t, schema["id_patterns"]["node"]))
        for a in schema["provenance_required"]:
            if not d.get(a, "").strip():
                rep.add("error", "provenienz", "%s (%s): %s fehlt" % (nid, t, a))
        for a in spec["required"]:
            if not d.get(a, "").strip():
                rep.add("error", "pflichtattribut", "%s (%s): %s fehlt" % (nid, t, a))
        for a, allowed in spec.get("enums", {}).items():
            v = d.get(a, "")
            if v.strip() and v not in allowed:
                rep.add("error", "enumeration", "%s (%s): %s=%r nicht in %s" % (nid, t, a, v, allowed))
        for a, pat in spec.get("patterns", {}).items():
            v = d.get(a, "")
            if v.strip() and not re.match(pat, v):
                rep.add("error", "wertemuster", "%s (%s): %s=%r passt nicht auf %s" % (nid, t, a, v, pat))
        for a, sugg in spec.get("suggested", {}).items():
            v = d.get(a, "")
            if v.strip() and v not in sugg:
                rep.add("info", "empfohlener-wert", "%s (%s): %s=%r, empfohlen %s" % (nid, t, a, v, sugg))
        sec = d.get("section", "")
        if sec and not re.match(schema["section_attribute_pattern"], sec):
            rep.add("error", "sektionsformat", "%s: section=%r ungültig" % (nid, sec))
        num = section_number(sec)
        if spec["sections"] and num is not None and num not in spec["sections"]:
            rep.add("warning", "typ-in-sektion", "%s (%s): section=%s, erwartet %s" % (nid, t, sec, spec["sections"]))
        sf = d.get("source_file", "")
        fm = re.match(r"^(\d{2})[-_]", sf)
        if fm and num is not None and int(fm.group(1)) != num:
            rep.add("warning", "sektion-zu-datei", "%s: section=%s, source_file=%s" % (nid, sec, sf))
        if base and sf and not (base / sf).is_file():
            rep.add("error", "quelldatei", "%s: source_file %s existiert nicht unter %s" % (nid, sf, base))
        if base and sf and (base / sf).is_file() and d.get("source_anchor", "").strip():
            text = re.sub(r"\s+", " ", (base / sf).read_text(encoding="utf-8", errors="ignore"))
            parts = [p.strip().lstrip("#=").strip() for p in d["source_anchor"].split(" / ")]
            if not any(re.sub(r"\s+", " ", p) in text for p in parts if p):
                rep.add("warning", "anker-gefunden", "%s: source_anchor %r nicht in %s gefunden" % (nid, d["source_anchor"], sf))


def check_edges(nodes, edges, schema, rep):
    etypes = schema["edge_types"]
    seen = collections.Counter()
    markers = schema["explicit_description_markers"]
    for eid, s, t, d in edges:
        label = d.get("label", "")
        spec = etypes.get(label)
        if s not in nodes or t not in nodes:
            rep.add("error", "kante-haengend", "%s: %s -> %s verweist auf unbekannten Knoten" % (eid, s, t))
            continue
        if spec is None:
            rep.add("error", "relationstyp", "%s: Label %r nicht im Vokabular" % (eid, label))
            continue
        st, tt = nodes[s].get("type"), nodes[t].get("type")

        def fits(src, tgt):
            return (("*" in spec["source"] or src in spec["source"]) and ("*" in spec["target"] or tgt in spec["target"]))

        ok = fits(st, tt) or (spec.get("bidirectional") and fits(tt, st))
        if not ok:
            rep.add("error", "kantensignatur", "%s: %s %s(%s) -> %s(%s), erlaubt %s -> %s" % (
                eid, label, s, st, t, tt, spec["source"], spec["target"]))
        ev = d.get("evidence", "")
        if ev not in schema["evidence_values"]:
            rep.add("error", "evidence", "%s: evidence=%r ungültig" % (eid, ev))
        elif ev not in spec["evidence"]:
            rep.add("error", "evidence-regel", "%s: %s darf nicht evidence=%s haben (erlaubt %s)" % (eid, label, ev, spec["evidence"]))
        if label != "member_of":
            desc = d.get("description", "").strip()
            if not desc:
                rep.add("error", "kantenbeschreibung", "%s: %s %s -> %s ohne description" % (eid, label, s, t))
            elif ev == "explicit" and not any(m in desc for m in markers):
                rep.add("warning", "explicit-ohne-verweistext", "%s: %s %s -> %s: explicit ohne Verweistext/Zitat" % (eid, label, s, t))
        if s == t:
            rep.add("warning", "selbstkante", "%s: %s %s -> sich selbst" % (eid, label, s))
        seen[(s, t, label)] += 1
    for (s, t, label), n in seen.items():
        if n > 1:
            rep.add("warning", "doppelte-kante", "%s %s -> %s kommt %d-mal vor" % (label, s, t, n))


def check_communities(nodes, edges, schema, rep):
    comm = schema["communities"]
    present = {nid for nid, d in nodes.items() if d.get("type") == "Community"}
    for cid, spec in comm["sections"].items():
        if cid not in present and spec["required"]:
            rep.add("error", "community-sektion", "Pflicht-Community %s fehlt" % cid)
    for cid in comm["conflict_dimensions"]:
        if cid not in present:
            rep.add("warning", "community-konflikt", "Empfohlene Konfliktdimension %s fehlt" % cid)
    for cid in present:
        if cid not in comm["sections"] and cid not in comm["conflict_dimensions"]:
            rep.add("warning", "community-unbekannt", "Community %s ist im Schema nicht vorgesehen" % cid)
    members = collections.defaultdict(set)
    for eid, s, t, d in edges:
        if d.get("label") == "member_of" and s in nodes and t in nodes:
            members[s].add(t)
    sec_to_comm = {spec["section"]: cid for cid, spec in comm["sections"].items()}
    for nid, d in nodes.items():
        if d.get("type") == "Community":
            continue
        num = section_number(d.get("section", ""))
        mine = members.get(nid, set())
        sect = [c for c in mine if c in comm["sections"]]
        if len(sect) != 1:
            rep.add("error", "community-zugehoerigkeit", "%s: %d Sektions-Communities (erwartet genau 1)" % (nid, len(sect)))
        elif num is not None and comm["sections"][sect[0]]["section"] != num:
            rep.add("error", "community-zugehoerigkeit", "%s: section=%s, aber Mitglied von %s" % (nid, d.get("section"), sect[0]))
        for cid, spec in comm["conflict_dimensions"].items():
            if cid not in present or num is None:
                continue
            inside = num in spec["sections"]
            if inside and cid not in mine:
                rep.add("warning", "konflikt-community-fehlt", "%s (S%d) fehlt in %s" % (nid, num, cid))
            if not inside and cid in mine:
                rep.add("warning", "konflikt-community-fremd", "%s (S%d) gehört nicht in %s" % (nid, num, cid))


def check_connectivity(nodes, edges, rep):
    deg = collections.Counter()
    for eid, s, t, d in edges:
        if d.get("label") != "member_of":
            deg[s] += 1
            deg[t] += 1
    for nid, d in nodes.items():
        if d.get("type") != "Community" and deg[nid] == 0:
            rep.add("info", "ohne-semantische-kante", "%s (%s)" % (nid, d.get("type")))


def check_density(nodes, edges, rep):
    """Hinweise auf auffällig dünne Graphen; nur Info, da Dokumentationen unterschiedlich aufgebaut sind."""
    count = collections.Counter(d.get("type") for d in nodes.values())
    labels = collections.Counter(d.get("label") for _, _, _, d in edges)
    blocks = count["BuildingBlock"]
    if blocks >= 3 and labels["contains"] < blocks - 1:
        rep.add("info", "graph-duenn", "%d BuildingBlock-Knoten, aber nur %d contains-Kanten (Hierarchie unvollständig?)" % (blocks, labels["contains"]))
    if count["Risk"] and not labels["mitigates"]:
        rep.add("info", "graph-duenn", "%d Risk-Knoten, aber keine mitigates-Kante (Maßnahmen nur als Text?)" % count["Risk"])
    terms = count["GlossaryTerm"]
    if terms >= 5:
        linked = {s for _, s, _, d in edges if d.get("label") == "defines_term_for"}
        if len(linked) * 2 < terms:
            rep.add("info", "graph-duenn", "nur %d von %d Glossarbegriffen sind per defines_term_for verknüpft" % (len(linked), terms))


def check_manifest(path, nodes, edges, schema, doc, rep):
    try:
        m = json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        rep.add("error", "manifest", "Manifest nicht lesbar: %s" % exc)
        return
    for k in schema["manifest"]["top_level_required"]:
        if k not in m:
            rep.add("error", "manifest-form", "Top-Level-Schlüssel %r fehlt" % k)
    files = m.get("files")
    if not isinstance(files, dict):
        rep.add("error", "manifest-form", "'files' muss ein Objekt Pfad -> Eintrag sein")
        return
    node_ids, edge_ids = set(nodes), {e[0] for e in edges}
    listed_nodes, listed_edges = set(), set()
    for rel, ent in files.items():
        for k in schema["manifest"]["file_entry_required"]:
            if k not in ent:
                rep.add("error", "manifest-form", "%s: Feld %r fehlt" % (rel, k))
        if doc:
            fp = doc_base(doc, schema)[0] / rel
            if not fp.is_file():
                rep.add("error", "manifest-datei", "%s existiert nicht" % rel)
            elif ent.get("sha256") and hashlib.sha256(fp.read_bytes()).hexdigest() != ent["sha256"]:
                rep.add("error", "manifest-hash", "%s: SHA-256 weicht von der Datei ab (Graph veraltet)" % rel)
        for nid in ent.get("nodes", []):
            listed_nodes.add(nid)
            if nid not in node_ids:
                rep.add("error", "manifest-knoten", "%s: Knoten %s nicht im Graphen" % (rel, nid))
        for eid in ent.get("edges", []):
            listed_edges.add(eid)
            if eid not in edge_ids:
                rep.add("error", "manifest-kante", "%s: Kante %s nicht im Graphen" % (rel, eid))
    for nid, d in nodes.items():
        if d.get("type") != "Community" and nid not in listed_nodes:
            rep.add("warning", "manifest-unvollstaendig", "Knoten %s in keinem Manifest-Eintrag" % nid)
    for eid in edge_ids - listed_edges:
        rep.add("warning", "manifest-unvollstaendig", "Kante %s in keinem Manifest-Eintrag" % eid)
    if doc:
        sections = doc_base(doc, schema)[1]
        for rel in sorted(sections - set(files)):
            rep.add("warning", "manifest-abdeckung", "Quelldatei %s fehlt im Manifest" % rel)


def run_checks(graph_path, schema, doc=None, manifest_path=None):
    """Führt alle Prüfungen aus und liefert (Report, geladener Graph oder None)."""
    rep = Report()
    loaded = load_graph(graph_path, schema, rep)
    if loaded:
        nodes, edges = loaded
        check_nodes(nodes, schema, doc, rep)
        check_edges(nodes, edges, schema, rep)
        check_communities(nodes, edges, schema, rep)
        check_connectivity(nodes, edges, rep)
        check_density(nodes, edges, rep)
        if manifest_path:
            check_manifest(manifest_path, nodes, edges, schema, doc, rep)
    return rep, loaded


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("graph", help="Pfad zur .graphml-Datei")
    ap.add_argument("--schema", default=str(DEFAULT_SCHEMA), help="Pfad zu schema.json")
    ap.add_argument("--doc", help="Dokumentationspfad (prüft source_file, Anker und Manifest-Hashes)")
    ap.add_argument("--manifest", help="Pfad zum Manifest (.manifest.json)")
    ap.add_argument("--strict", action="store_true", help="Warnungen wie Fehler behandeln")
    ap.add_argument("--limit", type=int, default=5, help="Beispiele je Regel")
    args = ap.parse_args()

    schema = json.loads(pathlib.Path(args.schema).read_text(encoding="utf-8"))
    doc = pathlib.Path(args.doc) if args.doc else None
    rep, loaded = run_checks(args.graph, schema, doc, args.manifest)
    if loaded:
        print("Graph: %d Knoten, %d Kanten (Schema %s)" % (len(loaded[0]), len(loaded[1]), schema["schema_version"]))
    rep.print(args.limit)
    failed = rep.count("error") > 0 or (args.strict and rep.count("warning") > 0)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
