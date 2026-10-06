---
name: arc42-knowledge-graph
description: "Konvertiert eine arc42-Architekturdokumentation (beliebiges Layout) in einen Wissensgraphen im GraphML-Format, der von den arc42-Review- und Konfliktanalyse-Agenten anstelle der rohen Markdown-Dateien analysiert werden kann. Definiert Entitätstypen, Relationstypen, Provenienz-Attribute und Communities je Sektion. Use when: arc42 in Wissensgraph umwandeln, GraphML erzeugen, Knowledge Graph für Review-Agenten, Dokumentation graphifizieren, arc42-Graph aktualisieren."
---

# arc42-Knowledge-Graph Skill

Dieser Skill beschreibt, wie eine arc42-Architekturdokumentation (in beliebigem Layout gemäß Skill `arc42-doc-layout`) in einen **Wissensgraphen im GraphML-Format** überführt wird. Der Graph ist so konzipiert, dass er **alle Informationen enthält, die die arc42-Review- und Konfliktanalyse-Agenten (`.agents/arc42-review*.agent.md`) heute durch Lesen der rohen Markdown-Dateien ermitteln** — insbesondere die sektionsübergreifende Traceability, die die Konflikt-Agenten sonst manuell durch paralleles Lesen mehrerer Dateien rekonstruieren müssen.

## Zweck und Nutzen

Die 24 Agenten in `.agents/` arbeiten heute direkt auf den Markdown-Dateien:

- 12 **Sektions-Agenten** (`arc42-review-s01…s12`) prüfen jeweils eine Sektion formal und inhaltlich.
- 7 **Konflikt-Agenten** (`arc42-review-conflict-*`) prüfen sektionsübergreifende Konsistenz (z.B. Qualitätsziele ↔ Strategie ↔ Qualitätsszenarien) — dafür müssen sie heute mehrere Sektionen parallel einlesen und Entitäten (Ziele, Ansätze, Entscheidungen, Bausteine, Risiken, …) manuell über Freitext hinweg zuordnen.
- 3 **Orchestratoren** (`arc42-review`, `arc42-review-branch`, `arc42-review-conflict`) koordinieren die Delegation und konsolidieren Ergebnisse.

Ein Wissensgraph macht die **Zuordnungsmatrizen, Zuordnungs- und Kreuzreferenz-Tabellen**, die praktisch jeder Konflikt-Agent in seinem Ausgabeformat produziert (siehe Skill `arc42-review-format`), zu einer **strukturellen Abfrage über Knoten und Kanten** statt einer manuellen Textanalyse über mehrere Dateien. Die Sektions-Agenten profitieren zusätzlich davon, dass Metadaten (ADR-Status, Priorität, Kategorie, Messbarkeit) als Knotenattribute statt als Freitext vorliegen.

Der Graph **ersetzt nicht** die inhaltliche Bewertung (Widerspruch? Lücke? Redundanz? — das bleibt Aufgabe der Agenten), sondern liefert ihnen **strukturierte Fakten und Provenienz**, aus denen sie ihre Befunde ableiten und weiterhin konkrete Datei-/Textzitate liefern können.

## Verwandte Skills

- **`arc42-doc-layout`**: Wird in Schritt 1 (Struktur-Erkennung) wiederverwendet, um alle Sektionsdateien unabhängig vom Layout (Multi-Folder/Flat-Files/Single-File) zu finden.
- **`arc42-review-format`**: Definiert die Befund-Formate, für die dieser Graph die Datengrundlage liefert (Zuordnungsmatrizen, Zitate mit Dateipfad).
- **`arc42-orchestrator-format`**: Die Konfliktkarte und Übersichtstabellen der Orchestratoren lassen sich direkt aus den Communities/Kanten dieses Graphen ableiten.

## Schema und Validierung (maßgeblich)

Der Vertrag für Entitätstypen, Relationstypen, Pflichtattribute, Enumerationen, Kantensignaturen, Evidence-Regeln, Communities und Manifest-Format liegt maschinenlesbar in [`schema.json`](schema.json) (im selben Ordner wie diese Datei). Die Tabellen unten sind eine Lesehilfe dazu; bei Abweichungen gilt `schema.json`.

Das Skript [`scripts/validate_graph.py`](scripts/validate_graph.py) (nur Python-Standardbibliothek) prüft einen erzeugten Graphen gegen dieses Schema:

```
python3 <skill-ordner>/scripts/validate_graph.py <repo>/.arc42-graph/<name>.graphml --doc <doku-pfad> --manifest <repo>/.arc42-graph/<name>.manifest.json
```

Exit-Code `1` bedeutet mindestens einen Fehler (z. B. unzulässiger Typ, Kantensignatur, Enumerationswert, fehlendes Pflichtattribut, hängende Kante, veralteter Hash). Warnungen und Hinweise sind keine Abbruchkriterien, sollten aber gesichtet werden. Der Hinweis `graph-duenn` meldet auffällig dünne Graphen (z. B. wenige `contains`-Kanten bei vielen Bausteinen, Risiken ohne `mitigates`, kaum verknüpfte Glossarbegriffe); prüfe dann, ob die Extraktion Beziehungen aus der Quelle ausgelassen hat.

Steht kein Python oder keine Terminalausführung zur Verfügung, schreibe GraphML und Manifest direkt gemäß `schema.json` (inklusive Communities, `member_of`-Kanten, Kanten-IDs und Hashes) und weise im Ergebnis darauf hin, dass die automatische Validierung nicht gelaufen ist.

### Aufbau-Skript und Extraktionsformat

Du schreibst den Graphen **nicht** selbst als GraphML. Du extrahierst nur Knoten und semantische Kanten in eine JSON-Datei (Format: `schema.json`, Abschnitt `extraction`); [`scripts/build_graph.py`](scripts/build_graph.py) erzeugt daraus GraphML und Manifest:

```
python3 <skill-ordner>/scripts/build_graph.py <extraktion>.json --doc <doku-pfad> --out-dir <repo>/.arc42-graph
```

Das Skript ergänzt Communities (Sektionen und Konfliktdimensionen), `member_of`-Kanten, Kanten-IDs, SHA-256-Hashes und das Manifest, validiert das Ergebnis und ersetzt bestehende Ausgabedateien nur bei fehlerfreier Validierung. Bei Fehlern korrigiere die Extraktionsdatei und führe das Skript erneut aus.

Sprache und Format: `label`, `description` und `source_anchor` folgen der Sprache der Dokumentation. Typen, Relationen, Enumerationswerte (z. B. `hoch`/`mittel`/`niedrig`) und Evidence-Werte sind unabhängig davon fest und stehen in `schema.json`. `--doc` darf ein Ordner (Multi-Folder, Flat-Files) oder eine einzelne Datei (Single-File) sein; berücksichtigt werden die Endungen aus `doc_extensions`.

Extraktionsformat (Beispiel):

```json
{
  "nodes": [
    {"id": "s01-qg-effizienz", "type": "QualityGoal", "label": "Schnelles Antworten auf Züge (Effizienz)",
     "section": "1.2", "priority": "5", "description": "Berechnung der Spielzüge erfolgt rasch, da live demonstriert.",
     "source_file": "01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md", "source_anchor": "## 1.2 Qualitätsziele"}
  ],
  "edges": [
    {"source": "s04-sa-reactive", "target": "s01-qg-effizienz", "label": "addresses", "evidence": "explicit",
     "description": "Tabelle 4.1: „Reactive Extensions für nebenläufige Berechnung“ gehört zum Ziel Effizienz."}
  ]
}
```

Nicht in die Extraktion gehören `Community`-Knoten und `member_of`-Kanten.

## Speicherort und Namenskonvention

- Ermittle den Dokumentationspfad wie gewohnt (Nutzer-Prompt > `AGENTS.md` > Rückfrage).
- Lege den Graphen **außerhalb** des Dokumentationsverzeichnisses ab, da er ein generiertes Artefakt ist:
  ```
  <Repository-Root>/.arc42-graph/<doc-ordner-name>.graphml
  <Repository-Root>/.arc42-graph/<doc-ordner-name>.manifest.json
  <Repository-Root>/.arc42-graph/<doc-ordner-name>.extraction.json
  ```
  Beispiel bei Dokumentationspfad `arc-doc/`: `.arc42-graph/arc-doc.graphml` und `.arc42-graph/arc-doc.manifest.json`. Die Extraktionsdatei legt `build_graph.py` bei jedem erfolgreichen Lauf mit ab; sie ist Grundlage für die inkrementelle Aktualisierung.
- Das Manifest speichert je Quelldatei Pfad, SHA-256-Hash und die Liste der von ihr erzeugten Knoten- und Kanten-IDs — Grundlage für inkrementelle Aktualisierung (siehe unten). Format: Objekt mit `doc_path`, `graph` und `files`; `files` bildet den Pfad relativ zum Dokumentationspfad auf `{"sha256", "nodes", "edges"}` ab (siehe `schema.json`, Abschnitt `manifest`). Jede Kante braucht dafür eine eindeutige `id` (frei im Format, empfohlen stabil: `<quelle>--<label>--<ziel>`).
- Überschreibe eine bestehende Graph-Datei nur nach erfolgreicher Validierung (siehe Schritt 5); bei Fehlern die alte Version nicht verwerfen.

## Gesamtprozess

1. **Struktur erkennen**: Wende Skill `arc42-doc-layout` (Teil A) an, um Layout-Typ (A/B/C) und Sektion-zu-Datei-Mapping zu ermitteln.
2. **Entitäten je Sektion extrahieren**: Lies jede Sektionsdatei und extrahiere Knoten gemäß der Tabelle „Entitätstypen je Sektion" unten. Jeder Knoten erhält Provenienz (`source_file`, `source_anchor`).
3. **Cross-Section-Relationen extrahieren**: Suche gezielt nach expliziten Querverweisen (Markdown-Links „→ Abschnitt X.Y", „siehe ADR 9-01", Tabellenzuordnungen wie in Sektion 4.1 „Qualitätsziel → Ansatz") und bilde daraus Kanten gemäß der Tabelle „Relationstypen" unten. Ergänze nur dort **inferierte** Kanten (Stichwort-/Themenübereinstimmung), wo keine explizite Referenz existiert — markiere diese klar mit `evidence=inferred`.
4. **Extraktionsdatei schreiben**: Fasse Knoten (Schritt 2) und Kanten (Schritt 3) in einer JSON-Datei zusammen (Format siehe „Aufbau-Skript und Extraktionsformat“). Communities und `member_of`-Kanten werden nicht extrahiert, sie erzeugt das Skript (Pflicht: eine Community je Sektion; empfohlen: je Konfliktdimension — siehe „Communities“ unten).
5. **Graph bauen und validieren**: Führe `scripts/build_graph.py` aus. Es schreibt GraphML und Manifest (Format siehe „Speicherort und Namenskonvention“), prüft Wohlgeformtheit, Knoten-IDs, hängende Kanten, Vokabular, Pflichtattribute, Enumerationen, Kantensignaturen, Evidence-Regeln, Communities und Manifest-Hashes und verwirft das Ergebnis bei Fehlern. Behebe alle Fehler in der Extraktionsdatei, bis das Skript mit Exit-Code `0` endet; sichte die Warnungen.
6. **Nachprüfen (optional)**: `scripts/validate_graph.py` prüft eine vorhandene Graph-Datei unabhängig vom Aufbau erneut (z. B. nach manueller Änderung oder im Delta-Modus).

## GraphML-Schema

Ein einziges, für alle Entitäts- und Relationstypen wiederverwendetes Schlüssel-Set (analog zu einem Property Graph):

### Knoten-Attribute (`for="node"`)

| Key | Attribut | Typ | Bedeutung |
|---|---|---|---|
| `d0` | `label` | string | Anzeigename der Entität |
| `d1` | `type` | string | Entitätstyp aus dem kontrollierten Vokabular (siehe unten), z.B. `QualityGoal`, `ArchitectureDecision`, `Community` |
| `d2` | `section` | string | arc42-Sektionsnummer/-ordner, z.B. `1.2`, `9`, `10.2`, `05-Bausteinsicht` |
| `d3` | `description` | string | Zusammenfassender Volltext/Definition der Entität (für Sektions-Agenten: reicht, um ohne Dateizugriff zu prüfen) |
| `d4` | `status` | string | Nur wo zutreffend: ADR-Status (`proposed`/`accepted`/`deprecated`/`superseded`), sonst leer |
| `d5` | `priority` | string | Rang/Schweregrad/Ebene, z.B. `1` (höchste Priorität), `hoch`/`mittel`/`niedrig`, Bausteinsicht-Ebene `1`/`2` |
| `d6` | `category` | string | Sub-Klassifikation je Typ, z.B. Randbedingung: `technisch`/`organisatorisch`/`konvention`; Szenario: `usage`/`change`/`fault`; Partner: `mensch`/`system` |
| `d7` | `source_file` | string | Pfad zur Quelldatei relativ zum Dokumentationspfad |
| `d8` | `source_anchor` | string | Überschrift/ID im Quelldokument (z.B. `## 1.2 Qualitätsziele`, `ADR 9-01`) — Grundlage für Datei-Zitate im Befund-Format |
| `d9` | `changed` | boolean | Nur im Delta-Modus gesetzt: `true`, wenn Knoten durch die aktuelle Änderung neu/verändert ist |
| `d10` | `change_type` | string | Nur im Delta-Modus: `added`/`modified`/`deleted`/`unchanged` |

### Kanten-Attribute (`for="edge"`)

| Key | Attribut | Typ | Bedeutung |
|---|---|---|---|
| `e0` | `label` | string | Relationstyp aus dem kontrollierten Vokabular (siehe unten) |
| `e1` | `description` | string | Konkrete, instanzbezogene Erklärung der Relation (dient als Zitat im Befund) |
| `e2` | `evidence` | string | `explicit` (expliziter Querverweis/Tabelle im Dokument), `structural` (Enthaltensein/Hierarchie), oder `inferred` (Themen-/Stichwortübereinstimmung ohne expliziten Verweis) |
| `e3` | `changed` | boolean | Nur im Delta-Modus: `true`, wenn Kante neu/verändert ist |

> Verwende für Community-Zugehörigkeit dieselben Kanten-Keys mit `label=member_of`.

## Kontrolliertes Vokabular: Entitätstypen je Sektion

Jede Zeile beschreibt einen Knotentyp, die Sektion, in der er typischerweise vorkommt, und welche Attribute (über die Basis-Keys hinaus) zwingend zu befüllen sind.

> **Die Dokumentation gibt keine Form vor.** Die Extraktionsregeln sprechen von „Zeilen“ und „Tabellen“, weil viele arc42-Dokumentationen so gegliedert sind. Gemeint ist jeweils jeder Einzeleintrag — ob Tabellenzeile, Listenpunkt, Überschrift mit Absatz oder Fließtext. Nicht jede Dokumentation hat jede Sektion, eine Zuordnungstabelle wie in Sektion 4.1, ADRs im Nygard-Format, ein Glossar als Tabelle oder Diagramme mit Inhalt, der nur dort steht. Fehlt etwas, entstehen keine Knoten dafür; ordne nichts zu, was das Dokument nicht sagt (siehe Evidence-Regel).

| Sektion | `type` | Extraktionsregel | Pflichtattribute |
|---|---|---|---|
| S1 | `Requirement` | Ein Eintrag/Absatz aus dem Anforderungsüberblick (1.1) | `description` |
| S1 | `QualityGoal` | Jede Zeile der Qualitätsziel-Tabelle (1.2) | `description`, `priority` (Rang 1..n gemäß Reihenfolge in der Tabelle) |
| S1 | `Stakeholder` | Jede Zeile der Stakeholder-Tabelle (1.3) | `description` (Erwartungen), `category` (Rollen-Gruppe) |
| S2 | `Constraint` | Jede Zeile der Randbedingungen-/Konventionen-Tabelle (2.1–2.3) | `description`, `category` (`technisch`/`organisatorisch`/`konvention`) |
| S3 | `ExternalPartner` | Jeder im fachlichen/technischen Kontext genannte Kommunikationspartner | `description`, `category` (`mensch`/`system`) |
| S4 | `StrategyApproach` | Jeder eigenständige Lösungsansatz/jede Technologieentscheidung in Sektion 4 | `description`; `priority` optional, wenn Ansatz explizit einem Qualitätsziel-Rang zugeordnet ist |
| S5 | `BuildingBlock` | Jede Blackbox/Whitebox auf jeder Ebene | `description` (Zweck/Verantwortlichkeit), `priority` (Ebene: `1`, `2`, …; auch die Whitebox einer Ebene ist ein Baustein mit `category=whitebox`), `category` (`blackbox`/`whitebox`); `contains` nur zwischen Bausteinen, nicht von `System` |
| S5 | `InternalInterface` | Jede benannte interne Schnittstelle zwischen Bausteinen (falls im Text eigenständig beschrieben) | `description` |
| S6 | `RuntimeScenario` | Jedes Laufzeitszenario/jeder Walkthrough | `description`, `category` (`normal`/`fehler`/`betrieb`) |
| S7 | `InfrastructureNode` | Jeder Infrastrukturknoten (Ebene 1/2) | `description`, `priority` (Ebene `1`/`2`) |
| S8 | `CrossCuttingConcept` | Jedes querschnittliche Konzept (8.x) | `description`, `category` (`muster`/`regel`/`prinzip`/`domänenmodell`/…) |
| S8 | `DomainModelElement` | Jede Klasse/jeder Begriff des Domänenmodells | `description` |
| S9 | `ArchitectureDecision` | Jede ADR | `description` (fasst Context, Decision, Consequences zusammen — z.B. `"Context: … | Decision: … | Consequences: …"`), `status` (nur Enumerationswert, ein Datum gehört in `description`), `source_anchor` = ADR-Titel/-Nummer |
| S10 | `QualityScenario` | Jedes Qualitätsszenario | `description` (Stimulus/Kontext/Metrik), `category` (`usage`/`change`/`fault`) |
| S11 | `Risk` | Jedes Risiko/jede technische Schuld | `description` (inkl. Maßnahme, falls nicht als eigener Knoten modelliert), `priority` (`hoch`/`mittel`/`niedrig` nur, wenn die Doku das Risiko bewertet, sonst `nicht angegeben` — nichts schätzen; Wahrscheinlichkeit und Auswirkung gehören in `description`), `category` (Risikoquelle) |
| S11 | `Mitigation` | Nur wenn eine Maßnahme substanziell und wiederverwendet wird (sonst Teil von `Risk.description`) | `description` |
| S12 | `GlossaryTerm` | Jeder Glossareintrag | `description` (Definition) |
| optional (S0/Überblick) | `System` | Das dokumentierte Gesamtsystem, falls ein Überblickskapitel existiert | `description` |
| immer | `Community` | Ein Knoten je Sektion (Pflicht) bzw. je Konfliktdimension (optional) | `description` (siehe „Communities") |

**ID-Konvention:** `s<NN>-<kurzform>-<slug>`, z.B. `s01-qg-analysierbarkeit`, `s09-adr-01-frontend-anbindung`, `s05-bb-engine`, `s11-risk-02-aufwand`. Stabile, aus Sektion + Kurzform + Slug des Titels abgeleitete IDs sind Voraussetzung für inkrementelle Updates (Diff über Läufe hinweg).

## Kontrolliertes Vokabular: Relationstypen (sektionsübergreifend)

Diese Kanten bilden die Traceability ab, die die Konflikt-Agenten heute manuell rekonstruieren. Jede Zeile nennt Quelle → Ziel, Bedeutung und welche(r) Agent(en) sie konsumieren.

| `label` | Quelltyp → Zieltyp | Bedeutung | Konsumierende Agenten |
|---|---|---|---|
| `addresses` | `StrategyApproach` → `QualityGoal` | Lösungsansatz adressiert Qualitätsziel | `arc42-review-s04-solution-strategy`, `arc42-review-conflict-quality-strategy` (K1–K3) |
| `concretizes` | `QualityScenario` → `QualityGoal` | Szenario konkretisiert/misst Qualitätsziel | `arc42-review-s10-quality`, `arc42-review-conflict-quality-strategy` (K1, K4, K5) |
| `realizes` | `ArchitectureDecision` → `StrategyApproach` | Entscheidung setzt strategische Festlegung um | `arc42-review-s09-decisions`, `arc42-review-conflict-strategy-decisions` (K1–K4) |
| `supersedes` | `ArchitectureDecision` → `ArchitectureDecision` | Nachfolge-Entscheidung (ADR-Status `superseded`) | `arc42-review-s09-decisions`, `arc42-review-conflict-strategy-decisions` (K5) |
| `constrains` | `Constraint` → `StrategyApproach` \| `CrossCuttingConcept` \| `ArchitectureDecision` \| `BuildingBlock` | Randbedingung gilt für/schränkt ein | `arc42-review-conflict-constraints-compliance` (K1–K5) |
| `communicates_with` | `ExternalPartner` ↔ `BuildingBlock` | Externe Schnittstelle/Kommunikationspartner wird von Baustein (Ebene 1) bedient | `arc42-review-s03-context`, `arc42-review-s05-building-blocks`, `arc42-review-conflict-context-building-blocks` (K1–K5) |
| `contains` | `BuildingBlock` → `BuildingBlock` | Whitebox-Verfeinerung (Ebene N → Ebene N+1) | `arc42-review-s05-building-blocks` |
| `provides` / `consumes` | `BuildingBlock` ↔ `InternalInterface` | Interne Schnittstellennutzung | `arc42-review-s05-building-blocks` |
| `involves` | `RuntimeScenario` → `BuildingBlock` | Baustein tritt im Szenario auf | `arc42-review-s06-runtime`, `arc42-review-conflict-views-consistency` (K1, K3, K5, K6) |
| `deployed_on` | `BuildingBlock` → `InfrastructureNode` | Software-Hardware-Mapping | `arc42-review-s07-deployment`, `arc42-review-conflict-views-consistency` (K2, K3) |
| `refines` | `InfrastructureNode` → `InfrastructureNode` | Infrastruktur-Ebene 1 → Ebene 2 | `arc42-review-s07-deployment` |
| `affects` | `CrossCuttingConcept` → `BuildingBlock` | Konzept betrifft Baustein (Querschnittlichkeit) | `arc42-review-s08-concepts` |
| `models` | `CrossCuttingConcept` → `DomainModelElement` | Konzept beschreibt Domänenmodell-Element | `arc42-review-s08-concepts`, `arc42-review-s12-glossary` |
| `based_on` | `CrossCuttingConcept` → `ArchitectureDecision` | Konzept baut auf Entscheidung auf | `arc42-review-conflict-concepts-decisions` (K1, K4) |
| `requires_concept` | `ArchitectureDecision` → `CrossCuttingConcept` | Entscheidung erfordert Konzeptumsetzung | `arc42-review-conflict-concepts-decisions` (K5) |
| `threatens` | `Risk` → `QualityGoal` | Risiko gefährdet Qualitätsziel | `arc42-review-s11-risks`, `arc42-review-conflict-risks-quality` (K1, K2, K5) |
| `mitigates` | `Risk` \| `Mitigation` → `StrategyApproach` \| `QualityScenario` \| `BuildingBlock` | Gegenmaßnahme wirkt auf | `arc42-review-conflict-risks-quality` (K2, K3) |
| `contradicts` | `Risk` \| `Mitigation` → `QualityScenario` | Maßnahme widerspricht Qualitätsszenario | `arc42-review-conflict-risks-quality` (K3) |
| `defines_term_for` | `GlossaryTerm` → beliebig | Begriff erklärt/wird verwendet in Entität | `arc42-review-s12-glossary` |
| `references` | beliebig → beliebig | Genereller expliziter Querverweis („→ Abschnitt X.Y"), wenn kein spezifischerer Typ passt | alle |
| `member_of` | beliebig → `Community` | Zugehörigkeit zu Kapitel- oder Konfliktdimensions-Community | alle Orchestratoren |

**Evidence-Regel:** Setze `evidence=explicit` nur, wenn im Quelltext ein direkter Verweis (Markdown-Link, ADR-Nummer-Erwähnung, Tabellenzeile wie „Qualitätsziel → Ansatz") existiert, und übernimm den Verweistext in `description`. Setze `evidence=structural` für reine Enthaltensein-/Hierarchie-Kanten (`contains`, `refines`, `member_of`). Setze `evidence=inferred` nur, wenn die Zuordnung ausschließlich über thematische/lexikalische Nähe erschlossen wurde (z.B. beide Texte erwähnen „Stellungsbewertung") — Konflikt-Agenten sollen `inferred`-Kanten mit geringerem Vertrauen behandeln und bei Bedarf den Originaltext gegenprüfen. Die bloße Verwendung eines Begriffs im Text ist kein direkter Verweis; `defines_term_for` ist daher in der Regel `inferred`. Welche Evidence-Werte je Relationstyp zulässig sind, legt `schema.json` fest.

## Communities

### Pflicht: eine Community je arc42-Sektion

Ein Community-Knoten (`type=Community`) je Sektion (00 optional, 01–12), analog zum Sektion-zu-Datei-Mapping aus `arc42-doc-layout`. Jede Entität erhält eine `member_of`-Kante zu ihrer Sektions-Community (`evidence=structural`). Das ermöglicht Sektions-Agenten, mit einer einzigen Filterung (`section` bzw. `member_of`-Ziel) exakt „ihre" Entitäten zu erhalten — ohne Dateipfade zu kennen.

### Empfohlen: eine Community je Konfliktdimension

Zusätzlich zu den Sektions-Communities kann je Konfliktdimension eine sekundäre Community gebildet werden, die alle Entitäten der beteiligten Sektionen bündelt. Das erspart den Konflikt-Agenten das Zusammenführen mehrerer Sektions-Communities:

| Community-ID | Dimension | Enthaltene Sektionen | Konsumierender Agent |
|---|---|---|---|
| `c-qs` | Qualitätsstrang | S1, S4, S10 | `arc42-review-conflict-quality-strategy` |
| `c-sd` | Strategie ↔ Entscheidungen | S4, S9 | `arc42-review-conflict-strategy-decisions` |
| `c-cc` | Constraint-Compliance | S2, S4, S8, S9 | `arc42-review-conflict-constraints-compliance` |
| `c-cb` | Kontext ↔ Bausteinsicht | S3, S5 | `arc42-review-conflict-context-building-blocks` |
| `c-vc` | Sichten-Konsistenz | S5, S6, S7 | `arc42-review-conflict-views-consistency` |
| `c-ke` | Konzepte ↔ Entscheidungen | S8, S9 | `arc42-review-conflict-concepts-decisions` |
| `c-rq` | Risiken ↔ Qualität | S1, S10, S11 | `arc42-review-conflict-risks-quality` |

Eine Entität kann somit mehrere `member_of`-Kanten haben (eine zur Sektions-Community, weitere zu 0–2 Konfliktdimensions-Communities).

## Provenienz und Zitierfähigkeit

Damit die Agenten weiterhin im geforderten Befund-Format (`arc42-review-format`) mit `**Datei:** \`pfad/zur/datei.md\`` bzw. `**Betroffene Dateien:** - \`datei1.md\` — Aussage` zitieren können, MUSS jeder Knoten und jede Kante mit signifikanter Aussagekraft folgende Angaben tragen:

- `source_file`: Pfad relativ zum Dokumentationspfad (z.B. `01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md`). Bei Single-File-Layouts: Pfad der einen Datei.
- `source_anchor`: Überschrift oder ID, unter der die Aussage steht (z.B. `## 1.2 Qualitätsziele`, `ADR 9-01`). Ermöglicht gezieltes Nachschlagen ohne die ganze Datei erneut zu lesen.
- `description`/`e1 description`: Enthält nach Möglichkeit ein kurzes, wörtliches oder nah am Original liegendes Zitat — nicht nur eine Paraphrase —, damit Agenten es direkt in ihren Befund übernehmen können.

## Extraktionsregeln: Treue zur Quelle

Der Graph ist nur so gut wie die Fakten, die er behält. Konflikt-Agenten finden Widersprüche an Einschränkungen und Zusicherungen — gehen diese bei der Verdichtung verloren, bleibt der Widerspruch unsichtbar.

Die Beispiele stammen aus der Beispiel-Dokumentation DokChess und dienen nur der Illustration. Aufbau und Stilmittel anderer Dokumentationen weichen ab (andere Tabellen oder keine, Listen statt Tabellen, Diagramme statt Text, anderes ADR-Format, andere Sprache, AsciiDoc statt Markdown). Die Regeln gelten sinngemäß.

1. **Einschränkungen, Ausschlüsse und Lücken wörtlich erhalten.** Übernimm Aussagen mit „nicht“, „kein“, „ausschließlich“, „zunächst“, „im Extremfall“, „Stand 2011“, „falls erkannt“ und ähnliche sowie bekannte Lücken („Offene Punkte“) und Zusicherungen („keine Konsequenzen bezüglich der Korrektheit“) mit ihrem Wortlaut in `description`. Verkürze sie nicht zu einer neutralen Zusammenfassung. Beispiel: „Inhaltlich prüft es die Bibliothek jedoch nicht … Im Extremfall antwortet die Engine mit einem ungültigen Zug“ darf nicht zu „nur auf Lesbarkeit geprüft“ werden. Das gilt besonders für Konzepte (S8), Entscheidungen (S9), Risiken (S11) und Bausteinbeschreibungen (S5).
2. **Zeichen unverändert lassen.** Umlaute und ß in `label`, `description` und `source_anchor` nicht transliterieren (kein „ae“, „ue“, „ss“). IDs dürfen ASCII sein. Steht die Quelle selbst transliteriert, übernimm sie wie sie ist.
3. **Wörtliche Anker.** `source_anchor` ist die tatsächliche Überschrift oder ID in der Quelldatei, kein beschreibender Titel.
4. **Granularität.** Jeder Einzeleintrag einer Zuordnung (Tabellenzeile, Listenpunkt, Absatz) ergibt einen eigenen Knoten. Fasse ähnlich klingende, aber verschieden zugeordnete Einträge nicht zusammen. Beispiel aus DokChess: „Explizites Domänenmodell“ (Analysierbarkeit) und „Effiziente Implementierung des Domänenmodells“ (Effizienz) sind zwei Ansätze, deren Spannung sichtbar bleiben muss.
5. **Evidence ehrlich vergeben.** `explicit` nur, wenn die Zuordnung im Text oder in einer Tabelle steht, bei Diagrammen nur, wenn du das Diagramm tatsächlich ausgewertet hast; sonst `inferred`. Ein Knoten, der zwei Quellaussagen vermischt, darf keine `explicit`-Kante für beide tragen.
6. **Artefakte als Infrastruktur.** Deployment-Artefakte der Verteilungssicht (z. B. JAR, Startskript) sind eigene `InfrastructureNode`; `deployed_on` zeigt auf das Artefakt, das den Baustein enthält.

## Aktualitätsprüfung

Ob ein vorhandener Graph noch zur Dokumentation passt, prüft `validate_graph.py` mit `--doc` und `--manifest` anhand der SHA-256-Hashes aus dem Manifest:

- Fehler `manifest-hash` oder `manifest-datei`: Quelldatei geändert oder gelöscht, Graph veraltet.
- Warnung `manifest-abdeckung`: neue Quelldatei, die im Manifest fehlt, Graph veraltet.
- Keines davon (und Exit-Code `0`): Graph aktuell, ohne Neuaufbau wiederverwendbar.

Andere Fehler dieses Aufrufs (Schema, Kanten) bedeuten einen defekten Graphen; baue ihn dann neu.

## Inkrementelle Aktualisierung (Delta-/Branch-Review-Modus)

Für den Branch-Review-Orchestrator (`arc42-review-branch`) soll der Graph nicht komplett neu extrahiert werden müssen. Grundlage ist die Extraktionsdatei `.arc42-graph/<name>.extraction.json` des letzten Aufbaus; GraphML und Manifest schreibst du weiterhin nicht selbst:

1. Ermittle geänderte Dateien wie im Agent beschrieben (`git diff --name-status origin/main...HEAD -- <doc-pfad>/`).
2. Entferne aus der Extraktionsdatei alle Knoten, deren `source_file` eine geänderte oder gelöschte Datei ist, sowie alle Kanten, die an diesen Knoten hängen (`source` oder `target`). Das Manifest nennt zusätzlich je Datei die erzeugten Knoten- und Kanten-IDs.
3. Extrahiere die geänderten und neuen Dateien neu (Schritte 2–3 des Gesamtprozesses) und füge Knoten und Kanten ein. Kanten von unveränderten zu geänderten Knoten bleiben bestehen, sofern das Ziel per ID weiter existiert.
4. Baue neu, mit einem `--changed` je geänderter Datei:
   ```
   python3 <skill-ordner>/scripts/build_graph.py <repo>/.arc42-graph/<name>.extraction.json --doc <doku-pfad> --out-dir <repo>/.arc42-graph --changed <datei>:modified --changed <datei2>:added
   ```
   Das Skript setzt `changed=true` und `change_type` (`added`/`modified`) an Knoten dieser Dateien sowie `changed=true` an allen Kanten, die einen solchen Knoten berühren. Hängende Kanten (Ziel gelöscht) meldet es als Fehler. Das ist der Hinweis auf „Verweis auf gelöschten Inhalt“: Halte ihn als Befund fest, bevor du die Kante entfernst oder umhängst.
5. Gelöschte Dateien haben nach Schritt 2 keine Knoten mehr und werden nicht mit `--changed` angegeben. Melde sie aus dem Git-Diff direkt an die Review-Agenten.
6. Das Manifest und die Hashes erzeugt das Skript neu.

Auf diese Weise kann `arc42-review-branch` gezielt nur die Umgebung der `changed=true`-Knoten (ihre Nachbarschaft über 1–2 Kanten) für die Konfliktanalyse heranziehen, statt den ganzen Graphen erneut zu durchsuchen. Ohne `--changed` entsteht ein Graph ohne Delta-Markierung.

## Beispielausschnitt (verkürzt)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns">
  <key id="d0" for="node" attr.name="label" attr.type="string"/>
  <key id="d1" for="node" attr.name="type" attr.type="string"/>
  <key id="d2" for="node" attr.name="section" attr.type="string"/>
  <key id="d3" for="node" attr.name="description" attr.type="string"/>
  <key id="d4" for="node" attr.name="status" attr.type="string"/>
  <key id="d5" for="node" attr.name="priority" attr.type="string"/>
  <key id="d6" for="node" attr.name="category" attr.type="string"/>
  <key id="d7" for="node" attr.name="source_file" attr.type="string"/>
  <key id="d8" for="node" attr.name="source_anchor" attr.type="string"/>
  <key id="e0" for="edge" attr.name="label" attr.type="string"/>
  <key id="e1" for="edge" attr.name="description" attr.type="string"/>
  <key id="e2" for="edge" attr.name="evidence" attr.type="string"/>

  <graph id="Arc42KnowledgeGraph" edgedefault="directed">
    <node id="s01-qg-effizienz">
      <data key="d0">Qualitätsziel: Effizienz</data>
      <data key="d1">QualityGoal</data>
      <data key="d2">1.2</data>
      <data key="d3">Schnelles Antworten auf Züge, da live demonstriert.</data>
      <data key="d5">5</data>
      <data key="d7">01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md</data>
      <data key="d8">## 1.2 Qualitätsziele</data>
    </node>
    <node id="s04-sa-reactive">
      <data key="d0">Reactive Extensions für nebenläufige Berechnung</data>
      <data key="d1">StrategyApproach</data>
      <data key="d2">4</data>
      <data key="d3">Asynchrone Rückmeldung besserer Züge über Observer-Pattern.</data>
      <data key="d7">04-Loesungsstrategie/04-01-Einstieg.md</data>
      <data key="d8">## 4.1 Einstieg</data>
    </node>
    <edge source="s04-sa-reactive" target="s01-qg-effizienz">
      <data key="e0">addresses</data>
      <data key="e1">Tabelle 4.1 ordnet den Ansatz explizit dem Qualitätsziel Effizienz zu (Spalte "Dem zuträgliche Ansätze").</data>
      <data key="e2">explicit</data>
    </edge>
  </graph>
</graphml>
```

## Nutzung durch Review-Agenten

Dieser Skill erzeugt den Graphen; die Review-Agenten (`.agents/arc42-review*.agent.md`) konsumieren ihn im GRAPH-MODUS. Orientierung, welcher Agent welche Knoten-/Kantentypen benötigt:

| Agent | Benötigte `type`-Knoten | Benötigte `label`-Kanten |
|---|---|---|
| `arc42-review-s01-introduction` | `Requirement`, `QualityGoal`, `Stakeholder` | `concretizes` (rückwärts, zur Vollständigkeitsprüfung) |
| `arc42-review-s02-constraints` | `Constraint` | `constrains` |
| `arc42-review-s03-context` | `ExternalPartner`, `BuildingBlock` | `communicates_with` |
| `arc42-review-s04-solution-strategy` | `StrategyApproach`, `QualityGoal` | `addresses` |
| `arc42-review-s05-building-blocks` | `BuildingBlock`, `InternalInterface`, `ExternalPartner` | `contains`, `provides`, `consumes`, `communicates_with` |
| `arc42-review-s06-runtime` | `RuntimeScenario`, `BuildingBlock` | `involves` |
| `arc42-review-s07-deployment` | `InfrastructureNode`, `BuildingBlock` | `deployed_on`, `refines` |
| `arc42-review-s08-concepts` | `CrossCuttingConcept`, `DomainModelElement`, `BuildingBlock` | `affects`, `models`, `based_on` |
| `arc42-review-s09-decisions` | `ArchitectureDecision` | `realizes`, `supersedes`, `requires_concept` |
| `arc42-review-s10-quality` | `QualityScenario`, `QualityGoal` | `concretizes` |
| `arc42-review-s11-risks` | `Risk`, `Mitigation`, `QualityGoal` | `threatens`, `mitigates` |
| `arc42-review-s12-glossary` | `GlossaryTerm`, `DomainModelElement` | `defines_term_for` |
| `arc42-review-conflict-quality-strategy` | `QualityGoal`, `StrategyApproach`, `QualityScenario` | `addresses`, `concretizes` |
| `arc42-review-conflict-strategy-decisions` | `StrategyApproach`, `ArchitectureDecision` | `realizes`, `supersedes` |
| `arc42-review-conflict-constraints-compliance` | `Constraint`, `StrategyApproach`, `CrossCuttingConcept`, `ArchitectureDecision` | `constrains` |
| `arc42-review-conflict-context-building-blocks` | `ExternalPartner`, `BuildingBlock` | `communicates_with` |
| `arc42-review-conflict-views-consistency` | `BuildingBlock`, `RuntimeScenario`, `InfrastructureNode` | `involves`, `deployed_on` |
| `arc42-review-conflict-concepts-decisions` | `CrossCuttingConcept`, `ArchitectureDecision` | `based_on`, `requires_concept` |
| `arc42-review-conflict-risks-quality` | `Risk`, `QualityGoal`, `QualityScenario` | `threatens`, `mitigates`, `contradicts` |

## Einschränkungen

- Der Graph bildet **Fakten und explizite Querverweise** ab, keine vorab berechneten Konfliktverdikte („Widerspruch", „Lücke") — diese Bewertung bleibt Aufgabe der Review-/Konflikt-Agenten.
- `inferred`-Kanten sind eine Hilfestellung, kein Ersatz für das Lesen des Originaltexts bei kritischen Befunden — Agenten sollen bei `evidence=inferred` den `source_file`/`source_anchor` gegenprüfen, bevor sie einen 🔴-Befund melden.
- Der Graph muss nach jeder inhaltlichen Änderung der Dokumentation neu generiert oder inkrementell aktualisiert werden (siehe „Inkrementelle Aktualisierung") — ein veralteter Graph darf nicht stillschweigend weiterverwendet werden. Prüfe daher vor der Nutzung, ob das Manifest neuer ist als alle Quelldateien.
- Sprache der Beschreibungen und Zitate folgt der Sprache der Quelldokumentation (i.d.R. Deutsch), analog zu den Review-Agenten.
