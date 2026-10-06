#!/usr/bin/env python3
"""Baut aus einer Extraktionsdatei (JSON) den arc42-Wissensgraphen (GraphML) und das Manifest.

Das Modell liefert nur Knoten und semantische Kanten. Dieses Skript erzeugt Communities,
member_of-Kanten, Kanten-IDs, SHA-256-Hashes und das Manifest und validiert das Ergebnis
gegen schema.json. Bestehende Ausgabedateien werden nur bei fehlerfreier Validierung ersetzt.
Nur Standardbibliothek.
"""
import argparse
import collections
import hashlib
import json
import os
import pathlib
import re
import sys
import xml.etree.ElementTree as ET

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import validate_graph as vg  # noqa: E402

NODE_ATTRS = ["label", "type", "section", "description", "status", "priority", "category", "source_file", "source_anchor", "changed", "change_type"]
EDGE_ATTRS = ["label", "description", "evidence", "changed"]
CHANGE_TYPES = ("added", "modified")


def check_extraction(data, schema, rep):
    ex = schema["extraction"]
    if not isinstance(data, dict):
        rep.add("error", "extraktion-form", "Wurzel muss ein Objekt sein")
        return False
    for k in data:
        if k not in ex["top_level"]:
            rep.add("error", "extraktion-form", "Unbekannter Top-Level-Schlüssel %r (erlaubt %s)" % (k, ex["top_level"]))
    for k in ex["top_level"]:
        if not isinstance(data.get(k), list):
            rep.add("error", "extraktion-form", "%r fehlt oder ist keine Liste" % k)
    if rep.count("error"):
        return False

    ids = set()
    for i, n in enumerate(data["nodes"]):
        ref = "nodes[%d]" % i
        if not isinstance(n, dict):
            rep.add("error", "extraktion-knoten", "%s ist kein Objekt" % ref)
            continue
        ref = "%s (%s)" % (ref, n.get("id", "?"))
        allowed = set(ex["node_fields"]["required"]) | set(ex["node_fields"]["optional"])
        for k in n:
            if k not in allowed:
                rep.add("error", "extraktion-knoten", "%s: unbekanntes Feld %r" % (ref, k))
        for k in ex["node_fields"]["required"]:
            if not isinstance(n.get(k), str) or not n[k].strip():
                rep.add("error", "extraktion-knoten", "%s: Pflichtfeld %r fehlt oder ist leer" % (ref, k))
        for k in ex["node_fields"]["optional"]:
            if k in n and not isinstance(n[k], str):
                rep.add("error", "extraktion-knoten", "%s: %r muss ein String sein" % (ref, k))
        if n.get("type") in ex["forbidden_node_types"]:
            rep.add("error", "extraktion-knoten", "%s: Typ %s erzeugt das Skript selbst" % (ref, n["type"]))
        if isinstance(n.get("section"), str) and vg.section_number(n["section"]) is None:
            rep.add("error", "extraktion-knoten", "%s: section %r nicht auswertbar" % (ref, n["section"]))
        if n.get("id") in ids:
            rep.add("error", "extraktion-knoten", "%s: doppelte ID" % ref)
        ids.add(n.get("id"))

    seen = set()
    for i, e in enumerate(data["edges"]):
        ref = "edges[%d]" % i
        if not isinstance(e, dict):
            rep.add("error", "extraktion-kante", "%s ist kein Objekt" % ref)
            continue
        allowed = set(ex["edge_fields"]["required"]) | set(ex["edge_fields"]["optional"])
        for k in e:
            if k not in allowed:
                rep.add("error", "extraktion-kante", "%s: unbekanntes Feld %r" % (ref, k))
        for k in ex["edge_fields"]["required"]:
            if not isinstance(e.get(k), str) or not e[k].strip():
                rep.add("error", "extraktion-kante", "%s: Pflichtfeld %r fehlt oder ist leer" % (ref, k))
        if e.get("label") in ex["forbidden_edge_labels"]:
            rep.add("error", "extraktion-kante", "%s: %s erzeugt das Skript selbst" % (ref, e["label"]))
        for end in ("source", "target"):
            if e.get(end) not in ids:
                rep.add("error", "extraktion-kante", "%s: %s %r ist kein Knoten der Extraktion" % (ref, end, e.get(end)))
        key = (e.get("source"), e.get("label"), e.get("target"))
        if key in seen:
            rep.add("error", "extraktion-kante", "%s: Duplikat %s --%s--> %s" % (ref, key[0], key[1], key[2]))
        seen.add(key)
    return rep.count("error") == 0


def assemble(data, schema):
    """Ergänzt Communities und member_of-Kanten. Liefert (nodes, edges) im Format von validate_graph."""
    comm = schema["communities"]
    nodes = collections.OrderedDict()
    used = {vg.section_number(n["section"]) for n in data["nodes"]}

    for cid, spec in comm["sections"].items():
        if spec["required"] or spec["section"] in used:
            nodes[cid] = {"label": spec["label"], "type": "Community", "section": str(spec["section"]),
                          "description": "Alle Entitäten von %s." % spec["label"]}
    for cid, spec in comm["conflict_dimensions"].items():
        nodes[cid] = {"label": spec["label"], "type": "Community",
                      "description": "Entitäten der Sektionen %s für die Konfliktdimension %s." % (
                          ", ".join(str(s) for s in spec["sections"]), spec["label"])}
    for n in data["nodes"]:
        nodes[n["id"]] = {k: n.get(k, "") for k in NODE_ATTRS if k != "label"}
        nodes[n["id"]]["label"] = n["label"]

    edges = []
    for e in data["edges"]:
        edges.append(("%s--%s--%s" % (e["source"], e["label"], e["target"]), e["source"], e["target"],
                      {"label": e["label"], "description": e["description"], "evidence": e["evidence"]}))
    sec_to_comm = {spec["section"]: cid for cid, spec in comm["sections"].items()}
    for n in data["nodes"]:
        num = vg.section_number(n["section"])
        targets = [sec_to_comm[num]] if num in sec_to_comm else []
        targets += [cid for cid, spec in comm["conflict_dimensions"].items() if num in spec["sections"]]
        for cid in targets:
            edges.append(("%s--member_of--%s" % (n["id"], cid), n["id"], cid,
                          {"label": "member_of", "evidence": "structural",
                           "description": "Zugehörigkeit zu %s" % nodes[cid]["label"]}))
    return nodes, edges


def write_graphml(path, nodes, edges, schema):
    ns = schema["graphml"]["namespace"]
    ET.register_namespace("", ns)
    root = ET.Element("{%s}graphml" % ns)
    key_of = {}
    used = {"node": {a for d in nodes.values() for a in d if d[a]}, "edge": {a for _, _, _, d in edges for a in d if d[a]}}
    for target in ("node", "edge"):
        for kid, spec in schema["graphml"]["keys"][target].items():
            if spec["required"] or spec["name"] in used[target]:
                ET.SubElement(root, "{%s}key" % ns, {"id": kid, "for": target, "attr.name": spec["name"], "attr.type": spec["type"]})
                key_of[(target, spec["name"])] = kid
    graph = ET.SubElement(root, "{%s}graph" % ns, {"id": schema["graphml"]["graph_id"], "edgedefault": schema["graphml"]["edgedefault"]})
    for nid, d in nodes.items():
        el = ET.SubElement(graph, "{%s}node" % ns, {"id": nid})
        for name in NODE_ATTRS:
            if d.get(name):
                ET.SubElement(el, "{%s}data" % ns, {"key": key_of[("node", name)]}).text = d[name]
    for eid, s, t, d in edges:
        el = ET.SubElement(graph, "{%s}edge" % ns, {"id": eid, "source": s, "target": t})
        for name in EDGE_ATTRS:
            if d.get(name):
                ET.SubElement(el, "{%s}data" % ns, {"key": key_of[("edge", name)]}).text = d[name]
    if hasattr(ET, "indent"):
        ET.indent(root)
    ET.ElementTree(root).write(path, encoding="utf-8", xml_declaration=True)


def build_manifest(doc, doc_arg, graph_name, nodes, edges, schema):
    files = collections.OrderedDict()
    base, found = vg.doc_base(doc, schema)
    rels = sorted(found)
    for d in nodes.values():
        sf = d.get("source_file")
        if sf and sf not in rels:
            rels.append(sf)
    for rel in rels:
        fp = base / rel
        digest = hashlib.sha256(fp.read_bytes()).hexdigest() if fp.is_file() else ""
        files[rel] = {"sha256": digest, "nodes": [], "edges": []}
    file_of = {}
    for nid, d in nodes.items():
        if d.get("type") != "Community" and d.get("source_file") in files:
            files[d["source_file"]]["nodes"].append(nid)
            file_of[nid] = d["source_file"]
    for eid, s, t, d in edges:
        if s in file_of:
            files[file_of[s]]["edges"].append(eid)
    return {"doc_path": doc_arg.replace(os.sep, "/"), "graph": graph_name,
            "generator": "scripts/build_graph.py", "schema_version": schema["schema_version"], "files": files}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("extraction", help="Extraktionsdatei (JSON mit nodes und edges)")
    ap.add_argument("--doc", required=True, help="Dokumentationspfad (Ordner oder einzelne Datei)")
    ap.add_argument("--out-dir", default=".arc42-graph", help="Ausgabeordner (Standard: .arc42-graph)")
    ap.add_argument("--name", help="Basisname der Ausgabe (Standard: Ordner- bzw. Dateiname ohne Endung)")
    ap.add_argument("--changed", action="append", default=[], metavar="DATEI[:TYP]",
                    help="Delta-Modus: Quelldatei (relativ zum Dokumentationspfad) als geändert markieren, "
                         "TYP = added|modified (Standard modified); mehrfach angebbar")
    ap.add_argument("--schema", default=str(vg.DEFAULT_SCHEMA), help="Pfad zu schema.json")
    ap.add_argument("--strict", action="store_true", help="Warnungen wie Fehler behandeln")
    ap.add_argument("--limit", type=int, default=5, help="Beispiele je Regel")
    args = ap.parse_args()

    schema = json.loads(pathlib.Path(args.schema).read_text(encoding="utf-8"))
    doc = pathlib.Path(args.doc).resolve()
    if not doc.exists():
        sys.exit("Dokumentationspfad nicht gefunden: %s" % args.doc)
    name = args.name or (doc.stem if doc.is_file() else doc.name)
    out = pathlib.Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    graph_final, manifest_final = out / (name + ".graphml"), out / (name + ".manifest.json")
    graph_tmp, manifest_tmp = out / (name + ".graphml.tmp"), out / (name + ".manifest.json.tmp")

    try:
        data = json.loads(pathlib.Path(args.extraction).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        sys.exit("Extraktionsdatei nicht lesbar: %s" % exc)

    rep = vg.Report()
    if not check_extraction(data, schema, rep):
        rep.print(args.limit)
        sys.exit(1)

    nodes, edges = assemble(data, schema)
    changes = {}
    for spec in args.changed:
        rel, _, ctype = spec.partition(":")
        ctype = ctype or "modified"
        if ctype not in CHANGE_TYPES:
            sys.exit("--changed %s: Typ muss %s sein" % (spec, "|".join(CHANGE_TYPES)))
        changes[rel.replace(os.sep, "/")] = ctype
    if changes:
        marked = set()
        for nid, d in nodes.items():
            if d.get("source_file") in changes:
                d["changed"], d["change_type"] = "true", changes[d["source_file"]]
                marked.add(nid)
        for _, s, t, d in edges:
            if d["label"] != "member_of" and (s in marked or t in marked):
                d["changed"] = "true"
    write_graphml(graph_tmp, nodes, edges, schema)
    manifest = build_manifest(doc, args.doc, graph_final.name, nodes, edges, schema)
    manifest_tmp.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    rep, loaded = vg.run_checks(str(graph_tmp), schema, doc, str(manifest_tmp))
    rep.print(args.limit)
    if rep.count("error") or (args.strict and rep.count("warning")):
        for p in (graph_tmp, manifest_tmp):
            p.unlink()
        print("Validierung fehlgeschlagen: bestehende Ausgabedateien bleiben unverändert.")
        sys.exit(1)
    extraction_final = out / (name + ".extraction.json")
    extraction_tmp = out / (name + ".extraction.json.tmp")
    extraction_tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(graph_tmp, graph_final)
    os.replace(manifest_tmp, manifest_final)
    os.replace(extraction_tmp, extraction_final)
    print("Geschrieben: %s (%d Knoten, %d Kanten), %s und %s" % (graph_final, len(nodes), len(edges), manifest_final, extraction_final))


if __name__ == "__main__":
    main()
