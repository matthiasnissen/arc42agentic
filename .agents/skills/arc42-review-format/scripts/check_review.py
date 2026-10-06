#!/usr/bin/env python3
"""Prüft einen arc42-Review-Bericht formal gegen die Dokumentation, ohne LLM.

Fehler (Exit-Code 1): doppelte Befund-IDs, Schweregrad-Summen weichen von der Zusammenfassung ab,
verlinkte Dateien fehlen. Warnungen: Zeilenanker hinter dem Dateiende, Zitate ohne wörtliche
Entsprechung, Befunde ohne Vorschlag. Mit --gold dokchess werden zusätzlich die Hauptwidersprüche
der Beispiel-Dokumentation DokChess (A, B, C) im Bericht gesucht. Nur Standardbibliothek.

Aufruf: python3 <skill-ordner>/scripts/check_review.py <bericht.md> [...] [--doc arc-doc] [--gold dokchess]
"""
import argparse
import collections
import pathlib
import re
import sys

HEADING = re.compile(r"^#{3,5} \[?([A-Z]{1,3}\d{0,2}-\d{1,2})\]?\s*(.*)$")
SEVERITY = re.compile(r"Schwere:?\*{0,2}:?\s*(🔴|🟡|🟢)")
SUMMARY_ROW = re.compile(r"^\|\s*(🔴|🟡|🟢)[^|]*\|(.*)\|\s*$")
LINK = re.compile(r"\]\(([^)\s]+)\)")
QUOTE = re.compile(r"„([^“”]{12,300})[“”]")
SUGGESTION = re.compile(r"(Änderungsvorschlag|Lösungsvorschlag|Vorschlag)")
SEVERITY_ORDER = {"🔴": 0, "🟡": 1, "🟢": 2}
SEVERITY_NAME = {"🔴": "kritisch", "🟡": "Warnung", "🟢": "Hinweis"}
DOC_SUFFIXES = {".md", ".markdown", ".adoc", ".asciidoc", ".rst"}

# Hauptwidersprüche der Beispiel-Dokumentation DokChess; gilt nicht für andere Dokumentationen.
GOLD_DOKCHESS = {
    "A FIDE-Umfang gegen fehlende Remisregeln": [r"FIDE", r"50-Z(ü|ue)ge|Remis"],
    "B Z02 gegen 8.4 (Zulässigkeit der Stellung)": [r"Z02", r"zul(ä|ae)ssig"],
    "C F01 gegen ungültige Buchzüge": [r"F01", r"Buchz(ü|ue)g|Bibliothek|Extremfall"],
}


def norm(text):
    text = text.replace("“", '"').replace("”", '"').replace("„", '"').replace("‚", "'").replace("‘", "'").replace("’", "'")
    text = re.sub(r"[*_`]", "", text)
    return re.sub(r"\s+", " ", text).strip().lower()


def split_findings(lines):
    """Liefert [(id, titel, [zeilen])]; ein Befund endet an der nächsten Überschrift."""
    findings, current = [], None
    for line in lines:
        m = HEADING.match(line)
        if m:
            current = (m.group(1), m.group(2).strip(), [])
            findings.append(current)
        elif line.startswith("#"):
            current = None
        elif current is not None:
            current[2].append(line)
    return findings


def summary_counts(text):
    if "## Zusammenfassung" not in text:
        return None
    part = text.split("## Zusammenfassung", 1)[1].split("\n## ", 1)[0]
    counts = {}
    for line in part.split("\n"):
        m = SUMMARY_ROW.match(line)
        if m:
            numbers = re.findall(r"\d+", m.group(2).split("|")[-1])
            if numbers:
                counts[m.group(1)] = int(numbers[0])
    return counts or None


def doc_corpus(doc):
    files = [doc] if doc.is_file() else [p for p in doc.rglob("*") if p.is_file() and p.suffix.lower() in DOC_SUFFIXES]
    return files, norm(" ".join(p.read_text(encoding="utf-8", errors="ignore") for p in files))


def check(report_path, doc, gold, out):
    root = report_path.parent
    text = report_path.read_text(encoding="utf-8")
    lines = text.split("\n")
    errors, warnings = [], []
    findings = split_findings(lines)

    ids = [f[0] for f in findings]
    for fid, n in collections.Counter(ids).items():
        if n > 1:
            errors.append("Befund-ID %s kommt %d-mal vor" % (fid, n))

    sev_of = {}
    for fid, _, body in findings:
        found = SEVERITY.findall("\n".join(body))
        if not found:
            errors.append("%s: keine Schwere angegeben" % fid)
        else:
            sev_of[fid] = found[0]
        if not SUGGESTION.search("\n".join(body)):
            warnings.append("%s: kein Änderungs- oder Lösungsvorschlag" % fid)
    counted = collections.Counter(sev_of.values())
    summary = summary_counts(text)
    if summary is None:
        warnings.append("Zusammenfassungstabelle mit Schweregraden nicht gefunden")
    else:
        for sym in SEVERITY_ORDER:
            if summary.get(sym) != counted.get(sym, 0):
                errors.append("Zusammenfassung nennt %s %s, gezählt wurden %d" % (SEVERITY_NAME[sym], summary.get(sym), counted.get(sym, 0)))

    docs, corpus = doc_corpus(doc)
    line_counts = {}
    link_total = anchor_total = 0
    prose = "\n".join(l for l in lines if not l.startswith(">"))
    for target in LINK.findall(prose):
        if re.match(r"^(https?:|mailto:|#)", target):
            continue
        path, _, anchor = target.partition("#")
        link_total += 1
        file = (root / path.replace("%20", " ")).resolve()
        if not file.exists():
            if path.startswith(".arc42-graph"):
                warnings.append("Graph-Artefakt nicht vorhanden: %s" % path)
            else:
                errors.append("Link auf fehlende Datei: %s" % path)
            continue
        m = re.fullmatch(r"L(\d+)", anchor)
        if m and file.is_file():
            anchor_total += 1
            if file not in line_counts:
                line_counts[file] = len(file.read_text(encoding="utf-8", errors="ignore").split("\n"))
            if int(m.group(1)) > line_counts[file]:
                warnings.append("Zeilenanker hinter dem Dateiende: %s#%s (Datei hat %d Zeilen)" % (path, anchor, line_counts[file]))

    quote_total, quote_bad = 0, []
    for line in lines:
        if line.startswith(">"):
            continue
        for q in QUOTE.findall(line):
            for part in re.split(r"\[…\]|\.\.\.|…", q):
                if len(part.strip()) < 10:
                    continue
                quote_total += 1
                if norm(part).strip(" .,;:") not in corpus:
                    quote_bad.append(part.strip())
    for q in quote_bad:
        warnings.append("Zitat ohne wörtliche Entsprechung: „%s“" % q[:90])

    out.append("== %s" % report_path.name)
    out.append("Befunde: %d (%s), Links: %d, Zeilenanker: %d, Zitate: %d" % (
        len(ids), ", ".join("%s %d" % (SEVERITY_NAME[s], counted.get(s, 0)) for s in SEVERITY_ORDER), link_total, anchor_total, quote_total))
    for e in errors:
        out.append("  [FEHLER] " + e)
    for w in warnings:
        out.append("  [WARNUNG] " + w)
    if gold:
        for name, patterns in gold.items():
            hits = [(fid, sev_of.get(fid)) for fid, title, body in findings
                    if all(re.search(p, title + "\n" + "\n".join(body), re.I) for p in patterns)]
            hits = [h for h in hits if h[1]]
            if hits:
                best = min(hits, key=lambda h: SEVERITY_ORDER[h[1]])
                out.append("  [GOLD] %s: %s (%s)" % (name, SEVERITY_NAME[best[1]], ", ".join(h[0] for h in hits[:4])))
            else:
                out.append("  [GOLD] %s: nicht gefunden" % name)
    return len(errors)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("reports", nargs="+", help="Review-Berichte (.md)")
    ap.add_argument("--doc", default="arc-doc", help="Dokumentationspfad (Standard: arc-doc)")
    ap.add_argument("--gold", choices=["dokchess"], help="Hauptwidersprüche der Beispiel-Dokumentation suchen")
    args = ap.parse_args()
    doc = pathlib.Path(args.doc)
    if not doc.exists():
        sys.exit("Dokumentationspfad nicht gefunden: %s" % args.doc)
    out, failed = [], 0
    for r in args.reports:
        failed += check(pathlib.Path(r), doc, GOLD_DOKCHESS if args.gold else None, out)
    print("\n".join(out))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
