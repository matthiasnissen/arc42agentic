#!/usr/bin/env python3
"""Scorecard: vergleicht erzeugte arc42-Graphen mit Soll-Werten aus arc-doc und mit schema.json.

Aufruf: python3 tools/graph_scorecard.py <name>=<graphml> [<name>=<graphml> ...] [--doc arc-doc]
Soll-Werte sind aus arc-doc/ (DokChess) abgeleitet und gelten nur für diese Doku.
"""
import collections
import pathlib
import re
import sys
import json

SKILL = pathlib.Path(__file__).resolve().parent.parent / ".agents" / "skills" / "arc42-knowledge-graph"
sys.path.insert(0, str(SKILL / "scripts"))
import validate_graph as vg  # noqa: E402

# (Typ, Soll, Modus) Modus "=" exakt, ">=" mindestens
NODE_GOLD = [
    ("QualityGoal", 5, "="), ("Stakeholder", 4, "="), ("Constraint", 15, "="), ("QualityScenario", 15, "="),
    ("ArchitectureDecision", 2, "="), ("Risk", 3, "="), ("GlossaryTerm", 24, "="), ("CrossCuttingConcept", 7, "="),
    ("RuntimeScenario", 1, "="), ("ExternalPartner", 6, "="), ("BuildingBlock", 8, "="), ("InfrastructureNode", 5, "="),
    ("DomainModelElement", 6, "="), ("StrategyApproach", 18, ">="), ("InternalInterface", 6, ">="), ("Requirement", 4, ">="),
]
EDGE_GOLD = [
    ("concretizes", 13, ">="), ("addresses", 18, ">="), ("involves", 4, ">="), ("deployed_on", 4, ">="),
    ("models", 6, "="), ("based_on", 2, "="), ("realizes", 2, ">="), ("contains", 7, "="), ("threatens", 4, ">="),
]


def _nodes(n, *types):
    return [d for d in n.values() if d.get("type") in types]


def _txt(d):
    return d.get("label", "") + " " + d.get("description", "")


# Fakten, aus denen ein Review-Agent die Hauptwidersprüche der DokChess-Doku ableitet.
FACTS = [
    ("A FIDE vollständig (Requirement)", lambda n, e: any("FIDE" in _txt(d) for d in _nodes(n, "Requirement"))),
    ("A 50-Züge/Stellungswdh. nicht implementiert", lambda n, e: any(re.search(r"50-Z(ü|ue)ge", _txt(d)) for d in _nodes(n, "BuildingBlock", "Risk", "Mitigation"))),
    ("A 11.2: 'keine Konsequenz' für Korrektheit", lambda n, e: any(re.search(r"keine\b[^.;]{0,60}orrekt", _txt(d)) for d in _nodes(n, "Risk", "Mitigation"))),
    ("B Z02 unzulässige Stellung erkennen", lambda n, e: any(re.search(r"nzul(ä|ae)ssig\w*\s+(Anfangs|Ausgangs)?[sS]tellung", _txt(d)) for d in _nodes(n, "QualityScenario"))),
    ("B 8.4: Zulässigkeit der Position nicht geprüft", lambda n, e: any(re.search(r"Stellung\w*[^.;]{0,80}(nur|nicht)[^.;]{0,80}(zul|inhaltlich|Protokoll)", d.get("description", ""), re.I) for d in _nodes(n, "CrossCuttingConcept"))),
    ("C 8.4: ungültiger Buchzug/Extremfall", lambda n, e: any(re.search(r"(ung(ü|ue)ltig\w*\s+(Buch)?[zZ](ü|ue)ge?|Extremfall)", d.get("description", "")) for d in _nodes(n, "CrossCuttingConcept"))),
    ("C F01 regelkonformer Zug", lambda n, e: any("regelkonform" in _txt(d) for d in _nodes(n, "QualityScenario"))),
    ("S4 Spannung Lesbarkeit/Effizienz (getrennte Ansätze)", lambda n, e: any(re.search(r"Effizient\w* Implementierung", d.get("label", "")) for d in _nodes(n, "StrategyApproach")) and any(re.search(r"(Domänen|Domaenen)modell", d.get("label", "")) and not re.search(r"Effizient", d.get("label", "")) for d in _nodes(n, "StrategyApproach"))),
    ("ADR 9.1: Stand 2011 festgehalten", lambda n, e: any("2011" in d.get("description", "") for d in _nodes(n, "ArchitectureDecision"))),
]


def ok(n, goal, mode):
    return n == goal if mode == "=" else n >= goal


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    doc = pathlib.Path("arc-doc")
    if "--doc" in sys.argv:
        doc = pathlib.Path(sys.argv[sys.argv.index("--doc") + 1])
        args = [a for a in args if a != str(doc)]
    schema = json.loads((SKILL / "schema.json").read_text(encoding="utf-8"))
    runs = {}
    for a in args:
        name, path = a.split("=", 1)
        rep, loaded = vg.run_checks(path, schema, doc, None)
        runs[name] = (rep, loaded)

    names = list(runs)
    w = max(len(n) for n in names + ["Soll"]) + 2
    print("%-28s %-6s" % ("Knoten je Typ", "Soll") + "".join("%-*s" % (w, n) for n in names))
    hits = collections.Counter()
    for t, goal, mode in NODE_GOLD:
        row = "%-28s %-6s" % (t, ("%s%d" % (">=" if mode == ">=" else "", goal)))
        for n in names:
            loaded = runs[n][1]
            c = sum(1 for d in loaded[0].values() if d.get("type") == t) if loaded else 0
            row += "%-*s" % (w, "%d%s" % (c, " ok" if ok(c, goal, mode) else " !"))
            hits[n] += ok(c, goal, mode)
        print(row)
    print()
    print("%-28s %-6s" % ("Kanten je Label", "Soll") + "".join("%-*s" % (w, n) for n in names))
    for l, goal, mode in EDGE_GOLD:
        row = "%-28s %-6s" % (l, ("%s%d" % (">=" if mode == ">=" else "", goal)))
        for n in names:
            loaded = runs[n][1]
            c = sum(1 for e in loaded[1] if e[3].get("label") == l) if loaded else 0
            row += "%-*s" % (w, "%d%s" % (c, " ok" if ok(c, goal, mode) else " !"))
            hits[n] += ok(c, goal, mode)
        print(row)
    total = len(NODE_GOLD) + len(EDGE_GOLD)
    print()
    print("%-28s %-6s" % ("Qualität", "") + "".join("%-*s" % (w, n) for n in names))
    rows = [("Soll-Treffer", lambda n: "%d/%d" % (hits[n], total))]

    def stat(n):
        rep, loaded = runs[n]
        return rep.count("error"), rep.count("warning"), loaded

    rows.append(("Schemafehler", lambda n: str(stat(n)[0])))
    rows.append(("Warnungen", lambda n: str(stat(n)[1])))

    def sem(n):
        loaded = runs[n][1]
        if not loaded:
            return "-"
        e = [x for x in loaded[1] if x[3].get("label") not in ("member_of",)]
        inf = sum(1 for x in e if x[3].get("evidence") == "inferred")
        return "%d (%d%% inferred)" % (len(e), round(100 * inf / len(e))) if e else "0"
    rows.append(("Semantische Kanten", sem))

    def quote(n):
        loaded = runs[n][1]
        if not loaded:
            return "-"
        ex = [x for x in loaded[1] if x[3].get("evidence") == "explicit"]
        q = sum(1 for x in ex if any(m in x[3].get("description", "") for m in schema["explicit_description_markers"]))
        return "%d%%" % round(100 * q / len(ex)) if ex else "-"
    rows.append(("explicit mit Verweistext", quote))

    def trap(n):
        loaded = runs[n][1]
        if not loaded:
            return "-"
        bad = [d["label"] for d in loaded[0].values() if d.get("type") == "QualityGoal" and "ttraktiv" in d.get("label", "")]
        return "Fehler" if bad else "ok"
    rows.append(("Zielname 4.1/1.2 normalisiert", trap))
    for label, f in rows:
        print("%-28s %-6s" % (label, "") + "".join("%-*s" % (w, f(n)) for n in names))

    print()
    print("%-52s" % "Widerspruchsfakten (A/B/C u. a.)" + "".join("%-*s" % (w, n) for n in names))
    fact_hits = collections.Counter()
    for label, fn in FACTS:
        row = "%-52s" % label
        for n in names:
            loaded = runs[n][1]
            hit = bool(loaded) and fn(loaded[0], loaded[1])
            fact_hits[n] += hit
            row += "%-*s" % (w, "ja" if hit else "-")
        print(row)
    print("%-52s" % "Summe" + "".join("%-*s" % (w, "%d/%d" % (fact_hits[n], len(FACTS))) for n in names))


if __name__ == "__main__":
    main()
