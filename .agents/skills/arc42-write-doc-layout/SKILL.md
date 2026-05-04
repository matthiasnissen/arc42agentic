---
name: arc42-write-doc-layout
description: "Verzeichnisstruktur und Dateikonventionen für arc42-Dokumentationen beim Schreiben. Definiert Standard-Ordnerstruktur, Dateinamen-Konventionen und Erkennung bestehender Strukturen. Use when: arc42 Ordnerstruktur anlegen, Dateien benennen, bestehende Struktur erkennen, Verzeichnisse erstellen."
---

# arc42-Write-Doc-Layout Skill

Dieser Skill definiert die Standard-Verzeichnisstruktur und Dateinamen-Konventionen für das Schreiben von arc42-Dokumentationen.

## Standard-Verzeichnisstruktur (Multi-Folder)

```
<doc-root>/
├── 00-Ueberblick/
│   └── 00-00-Overview.md
├── 01-Einfuehrung-und-Ziele/
│   ├── 01-01-Aufgabenstellung.md
│   ├── 01-02-Qualitaetsziele.md
│   └── 01-03-Stakeholder.md
├── 02-Randbedingungen/
│   ├── 02-01-Technisch.md
│   ├── 02-02-Organisatorisch.md
│   └── 02-03-Konventionen.md
├── 03-Kontextabgrenzung/
│   ├── 03-01-Fachlicher-Kontext.md
│   └── 03-02-Technischer-Kontext.md
├── 04-Loesungsstrategie/
│   └── 04-01-Strategie.md
├── 05-Bausteinsicht/
│   ├── 05-01-Ebene-1.md
│   └── 05-02-Ebene-2-<Name>.md
├── 06-Laufzeitsicht/
│   └── 06-01-<Szenario>.md
├── 07-Verteilungssicht/
│   └── 07-01-Infrastruktur.md
├── 08-Konzepte/
│   └── 08-XX-<Konzeptname>.md
├── 09-Entscheidungen/
│   └── 09-XX-<Entscheidung>.md
├── 10-Qualitaetsanforderungen/
│   ├── 10-01-Qualitaetsbaum.md
│   └── 10-02-Qualitaetsszenarien.md
├── 11-Risiken/
│   └── 11-XX-<Risiko>.md
├── 12-Glossar/
│   └── 12-01-Begriffe.md
└── images/
```

## Dateinamen-Konventionen

- Format: `<SS>-<NN>-<Name>.md`
  - `SS` = Zweistellige Sektionsnummer (01-12)
  - `NN` = Zweistellige laufende Nummer innerhalb der Sektion
  - `<Name>` = Sprechender Kurzname, Kebab-Case, keine Umlaute
- Beispiele: `08-03-Fehlerbehandlung.md`, `09-01-Anbindung.md`
- Sonderzeichen vermeiden: Umlaute durch ae/oe/ue/ss ersetzen
- Sprache: Deutsch (analog zu den Ordnernamen)

## Bestehende Struktur erkennen

Bevor du Dateien anlegst, prüfe ob im Zielpfad bereits eine Struktur existiert:

1. **Verzeichnis auflisten**: Prüfe den Zielpfad auf existierende Ordner/Dateien
2. **Wenn existierend**: Ergänze fehlende Sektionen, überschreibe NICHT existierende Dateien ohne Rückfrage
3. **Wenn leer**: Lege die vollständige Struktur an

## Ordner-Mapping

| Sektion | Ordnername | Skill |
|---------|-----------|-------|
| S0 | `00-Ueberblick/` | — |
| S1 | `01-Einfuehrung-und-Ziele/` | `arc42-write-s01-introduction` |
| S2 | `02-Randbedingungen/` | `arc42-write-s02-constraints` |
| S3 | `03-Kontextabgrenzung/` | `arc42-write-s03-context` |
| S4 | `04-Loesungsstrategie/` | `arc42-write-s04-solution-strategy` |
| S5 | `05-Bausteinsicht/` | `arc42-write-s05-building-blocks` |
| S6 | `06-Laufzeitsicht/` | `arc42-write-s06-runtime` |
| S7 | `07-Verteilungssicht/` | `arc42-write-s07-deployment` |
| S8 | `08-Konzepte/` | `arc42-write-s08-concepts` |
| S9 | `09-Entscheidungen/` | `arc42-write-s09-decisions` |
| S10 | `10-Qualitaetsanforderungen/` | `arc42-write-s10-quality` |
| S11 | `11-Risiken/` | `arc42-write-s11-risks` |
| S12 | `12-Glossar/` | `arc42-write-s12-glossary` |

## Alternative Layouts

Falls der User ein anderes Layout wünscht:

### Flat-Files

```
<doc-root>/
├── 01-Einfuehrung-und-Ziele.md
├── 02-Randbedingungen.md
├── ...
└── 12-Glossar.md
```

### Single-File

```
<doc-root>/
└── architektur.md
```

Verwende `## 1. Einführung und Ziele` als Überschriften-Ebene für Sektionen.

