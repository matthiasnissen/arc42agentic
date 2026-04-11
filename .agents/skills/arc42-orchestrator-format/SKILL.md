---
name: arc42-orchestrator-format
description: "Gemeinsames Ausgabeformat für arc42-Orchestrator-Agenten (Vollständiges Review, Branch-Review, Konfliktanalyse). Definiert Ampellogik, Übersichtstabellen, Zusammenfassungsblock und Templates für konsolidierte Berichte. Use when: arc42 Orchestrator-Ausgabe, Review-Bericht, Konsolidierung, Ampelfarben, Zusammenfassung, Gesamtübersicht."
---

# arc42 Orchestrator-Ausgabeformat

Dieses Skill definiert die gemeinsamen Ausgabeformate für die drei arc42-Orchestrator-Agenten: Vollständiges Review, Branch-Review und Konfliktanalyse.

## Ampellogik

Die Statusbestimmung erfolgt einheitlich auf Basis der Befunde der Spezial-Agenten:

| Status | Bedingung |
|--------|-----------|
| 🔴 | Mindestens ein **kritischer** Befund (🔴 Kritisch) wurde gefunden |
| 🟡 | Kein kritischer Befund, aber mindestens eine **Warnung/Empfehlung** (🟡) |
| 🟢 | Nur **Hinweise** (🟢) oder keine Befunde |

Diese Logik gilt für:
- Sektions-Status in Übersichtstabellen
- Konfliktdimensions-Status in Konflikttabellen
- Gesamtstatus-Bestimmung

## Gemeinsame Bausteine

### Sektions-Übersichtstabelle

Wird vom **Vollständigen Review** und **Branch-Review** verwendet:

```markdown
| Sektion | Status | Befunde |
|---------|--------|---------|
| 1. Einführung und Ziele | 🟢/🟡/🔴 | Kurzbeschreibung |
| 2. Randbedingungen | 🟢/🟡/🔴 | Kurzbeschreibung |
| ... | ... | ... |
```

Regeln:
- Nur Sektionen auflisten, die tatsächlich geprüft wurden
- Kurzbeschreibung fasst die wesentlichen Befunde in einem Satz zusammen
- Status wird gemäß Ampellogik aus den Befunden des Sektions-Agenten abgeleitet

### Konflikt-Übersichtstabelle

Wird von allen drei Orchestratoren verwendet (sofern Konflikte geprüft werden):

```markdown
| Konfliktdimension | Status | Befunde |
|---|---|---|
| Qualitätsstrang (S1 ↔ S4 ↔ S10) | 🟢/🟡/🔴 | Kurzbeschreibung |
| Strategie ↔ Entscheidungen (S4 ↔ S9) | 🟢/🟡/🔴 | Kurzbeschreibung |
| Constraint-Compliance (S2 ↔ S4/S8/S9) | 🟢/🟡/🔴 | Kurzbeschreibung |
| Kontext ↔ Bausteine (S3 ↔ S5) | 🟢/🟡/🔴 | Kurzbeschreibung |
| Sichten-Konsistenz (S5 ↔ S6 ↔ S7) | 🟢/🟡/🔴 | Kurzbeschreibung |
| Konzepte ↔ Entscheidungen (S8 ↔ S9) | 🟢/🟡/🔴 | Kurzbeschreibung |
| Risiken ↔ Qualität (S11 ↔ S1/S10) | 🟢/🟡/🔴 | Kurzbeschreibung |
```

Regeln:
- Nur Dimensionen auflisten, die tatsächlich geprüft wurden
- Übersprungene Dimensionen (z.B. weil eine Sektion fehlt) nicht aufführen

### Zusammenfassungsblock

Zählt alle Befunde über alle Agenten hinweg:

```markdown
| Kategorie | Anzahl |
|---|---|
| 🔴 Kritische Befunde | n |
| 🟡 Warnungen / Empfehlungen | n |
| 🟢 Hinweise | n |
```

### Konfliktkarte

Übersicht, welche Sektionen in den meisten Konflikten involviert sind. Wird vom **Vollständigen Review** und der **Konfliktanalyse** ausgegeben:

```markdown
## Konfliktkarte

| Sektion | Involviert in Konflikten |
|---|---|
| S1 — Einführung/Ziele | n |
| S2 — Randbedingungen | n |
| ... | ... |
```

Regeln:
- Nur Sektionen auflisten, die in mindestens einem Konflikt involviert sind
- Sortierung absteigend nach Anzahl der Konflikte

### Handlungsempfehlungen

Priorisierte Liste der wichtigsten Maßnahmen, abgeleitet aus den kritischen Befunden:

```markdown
### Handlungsempfehlungen
1. [Höchste Priorität — aus 🔴 Befunden]
2. ...
```

## Orchestrator-Templates

### Vollständiges Review (`arc42-review`)

```markdown
# arc42 Dokumentations-Review

## Gesamtübersicht

<Sektions-Übersichtstabelle>

## Sektions-Reviews

### Sektion 1: Einführung und Ziele
<Ergebnisse des Sektions-Agenten>

### Sektion 2: Randbedingungen
<Ergebnisse des Sektions-Agenten>

[... weitere Sektionen ...]

## Sektionsübergreifende Konflikte

<Konflikt-Übersichtstabelle>

### 1. Qualitätsstrang (S1 ↔ S4 ↔ S10)
<Ergebnis des Konflikt-Agenten>

[... weitere Dimensionen ...]

## Konfliktkarte

<Konfliktkarte>

## Zusammenfassung

<Zusammenfassungsblock>

### Handlungsempfehlungen
1. ...
```

### Branch-Review (`arc42-review-branch`)

```markdown
# arc42 Branch-Review

## Überblick

**Branch:** `<branch-name>`
**Basis:** `<base-branch>`
**Geänderte Dateien:** <Anzahl>
**Betroffene Sektionen:** <Liste>

## Geänderte Dateien

| Datei | Änderungstyp | Sektion |
|---|---|---|
| `pfad/zur/datei.md` | Added/Modified/Deleted | Sektion X |

## Sektions-Reviews

### Sektion X: <Name>
<Ergebnisse des Sektions-Agenten, fokussiert auf die Änderungen>

[... weitere betroffene Sektionen ...]

## Konfliktanalyse

<Konflikt-Übersichtstabelle — nur ausgelöste Dimensionen>

### <Konfliktdimension>
<Ergebnis des Konflikt-Agenten>

[... weitere ausgelöste Dimensionen ...]

## Zusammenfassung

<Zusammenfassungsblock>

### Handlungsempfehlungen
1. ...
```

### Konfliktanalyse (`arc42-review-conflict`)

```markdown
# arc42 Sektionsübergreifende Konfliktanalyse

## Überblick

<Konflikt-Übersichtstabelle — erweitert um Spalte "Anzahl Konflikte">

| Konfliktdimension | Status | Anzahl Konflikte |
|---|---|---|
| Qualitätsstrang (S1 ↔ S4 ↔ S10) | 🟢/🟡/🔴 | n |
| ... | ... | ... |

**Gesamt:** n Konflikte (davon n kritisch, n Warnungen, n Hinweise)

## Detailergebnisse

### 1. Qualitätsstrang (S1 ↔ S4 ↔ S10)
<Ergebnis des Konflikt-Agenten>

[... weitere Dimensionen ...]

## Kritische Konflikte (Sofortmaßnahmen erforderlich)
<Alle Befunde mit 🔴 aus allen Agenten>

<Konfliktkarte>

### Empfohlene Reihenfolge der Behebung
1. ...
```
