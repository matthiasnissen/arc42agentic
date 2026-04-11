---
name: arc42-write-s09-decisions
description: "Schreibt arc42 Sektion 9 (Architekturentscheidungen): ADRs im Nygard-Format, Entscheidungsdokumentation, Begründungen, Alternativen. Use when: Sektion 9 schreiben, Entscheidungen, Architecture Decisions, ADR, Nygard, Architekturentscheidung dokumentieren."
---

# arc42 Sektion 9: Architekturentscheidungen schreiben

## Zweck

Wichtige, teure, kritische oder riskante Architekturentscheidungen mit zentraler Bedeutung für das Gesamtsystem, inklusive Begründungen. Empfohlenes Format: Architecture Decision Records (ADRs) im Nygard-Format.

## Dateistruktur

```
09-Entscheidungen/
├── 09-01-<Entscheidung-1>.md
├── 09-02-<Entscheidung-2>.md
└── 09-XX-<Entscheidung-X>.md
```

Ein ADR pro Datei. Dateiname enthält eine laufende Nummer und einen sprechenden Kurznamen.

## Interaktive Fragen an den User

1. **Welche grundlegenden Architekturentscheidungen wurden getroffen?** (z.B. Technologiewahl, Architekturmuster, Build-vs-Buy)
2. **Was war der Kontext/die Situation bei der Entscheidung?**
3. **Welche Alternativen standen zur Auswahl?**
4. **Warum wurde diese Alternative gewählt?** (Entscheidungskriterien)
5. **Was sind die Konsequenzen?** (Positiv und negativ)
6. **Wer hat die Entscheidung getroffen und wann?**
7. **Gibt es Entscheidungen aus Sektion 4, die als ADR detailliert werden sollten?**

## Codebase-Analyse-Hinweise

- **Technologieentscheidungen**: Aus Build-Files (welches Framework, welche DB, welche Libraries)
- **Architekturmuster**: Aus Package-Struktur, Dependency-Richtungen
- **Bestehende ADRs**: Suche nach `doc/adr/`, `docs/decisions/`, `ADR-*.md` im Repository
- **Git-Historie**: Große Refactorings oder Technologiewechsel aus der Historie ableitbar
- **Achtung**: Die GRÜNDE für Entscheidungen sind selten aus Code ableitbar → Rückfrage nötig

## Templates

### 09-XX-Entscheidung.md (Nygard-Format)

```markdown
# ADR-<Nr>: <Titel der Entscheidung>

**Status:** <proposed | accepted | deprecated | superseded>

**Datum:** <YYYY-MM-DD>

## Kontext

<Beschreibung der Situation, einschließlich technischer, politischer, sozialer und Projekt-Aspekte. Die wirkenden Kräfte können in Spannung zueinander stehen.>

## Entscheidung

<Was ist unsere Entscheidung? Wie antworten wir auf die im Kontext beschriebenen Kräfte?>

## Konsequenzen

### Positiv
- <Positive Konsequenz 1>
- <Positive Konsequenz 2>

### Negativ
- <Negative Konsequenz 1>
- <Negative Konsequenz 2>

### Neutral
- <Neutrale Konsequenz / Trade-Off>
```

### Alternatives Tabellenformat (für Entscheidungsvergleiche)

```markdown
# ADR-<Nr>: <Titel>

**Status:** accepted | **Datum:** YYYY-MM-DD

## Kontext

<Situationsbeschreibung>

## Alternativen

| Kriterium | Alternative A | Alternative B | Alternative C |
|-----------|--------------|--------------|--------------|
| <Kriterium 1> | <Bewertung> | <Bewertung> | <Bewertung> |
| <Kriterium 2> | <Bewertung> | <Bewertung> | <Bewertung> |
| **Gesamt** | ○○● | ○●● | ●●● |

## Entscheidung

<Gewählt: Alternative C, weil...>

## Konsequenzen

- <Konsequenz 1>
- <Konsequenz 2>
```

## Typische Entscheidungsthemen

- Wahl der Programmiersprache / des Frameworks
- Wahl des Architekturstils (Microservices vs. Monolith)
- Wahl der Datenbank (SQL vs. NoSQL, welches Produkt)
- Wahl des Kommunikationsmusters (sync vs. async, REST vs. Messaging)
- Build vs. Buy (Eigenentwicklung vs. Standardsoftware)
- Cloud-Provider-Wahl
- Authentifizierungs-/Autorisierungsstrategie
- Teststrategie
- Deployment-Strategie

## Best Practices (aus arc42-Tipps)

- **Nur architektonisch relevante Entscheidungen**: Keine trivialen oder rein technischen Detail-Entscheidungen
- **Entscheidungskriterien dokumentieren**: Wie wurde bewertet? Welche Kriterien waren ausschlaggebend?
- **Begründungen liefern**: WARUM wurde so entschieden, nicht nur WAS
- **Verworfene Alternativen dokumentieren**: Hilft beim Nachvollziehen und verhindert Diskussions-Schleifen
- **Timestamp**: Jede Entscheidung braucht ein Datum
- **Status pflegen**: accepted/deprecated/superseded aktuell halten
- **Redundanz vermeiden**: Entscheidungen aus Sektion 4 nicht 1:1 wiederholen, sondern referenzieren und vertiefen
- **ADR-Nummern**: Laufende Nummerierung, nicht wiederverwenden

## Querverweise

- ← **Sektion 4** (Lösungsstrategie): Strategie enthält die Kurzfassung, ADRs die Langfassung
- ← **Sektion 2** (Randbedingungen): Entscheidungen müssen sich im Rahmen der Constraints bewegen
- ↔ **Sektion 8** (Konzepte): Klare Abgrenzung: ADR = WHAT+WHY, Konzept = HOW
- → **Sektion 5** (Bausteinsicht): Entscheidungen beeinflussen die Systemstruktur
