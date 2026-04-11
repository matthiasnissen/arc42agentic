---
name: arc42-write-s01-introduction
description: "Schreibt arc42 Sektion 1 (Einführung und Ziele): Aufgabenstellung, Qualitätsziele, Stakeholder. Use when: Sektion 1 schreiben, Einführung, Ziele, Requirements Overview, Quality Goals, Stakeholder erstellen, Anforderungsüberblick dokumentieren."
---

# arc42 Sektion 1: Einführung und Ziele schreiben

## Zweck

Diese Sektion beschreibt die relevanten Anforderungen und treibenden Kräfte, die Softwarearchitekten und das Entwicklungsteam berücksichtigen müssen:
- Grundlegende Business-Ziele, wesentliche Features und funktionale Anforderungen
- Qualitätsziele für die Architektur
- Relevante Stakeholder und deren Erwartungen

## Dateistruktur

```
01-Einfuehrung-und-Ziele/
├── 01-01-Aufgabenstellung.md
├── 01-02-Qualitaetsziele.md
└── 01-03-Stakeholder.md
```

## Interaktive Fragen an den User

### Für 1.1 Aufgabenstellung

1. **Was ist der Zweck des Systems?** Was wird gebaut und warum?
2. **Welche Business-Ziele verfolgt das System?** Welche Geschäftsprozesse werden unterstützt?
3. **Was sind die wichtigsten Features/Use-Cases?** Top 5-10 wesentliche Funktionen
4. **Gibt es bestehende Anforderungsdokumente?** (Verweis oder Link)
5. **Wer sind die Nutzer des Systems?** Welche Rollen gibt es?

### Für 1.2 Qualitätsziele

1. **Was sind die Top 3-5 Qualitätseigenschaften für die Architektur?** (z.B. Performance, Sicherheit, Skalierbarkeit, Wartbarkeit, Verfügbarkeit)
2. **Wie misst man den Erfolg dieser Qualitätsziele?** Konkrete Szenarien oder Metriken
3. **Welche Qualitätseigenschaften sind am wichtigsten für die Stakeholder?**
4. **Gibt es Qualitätskonflikte?** (z.B. Performance vs. Sicherheit)

### Für 1.3 Stakeholder

1. **Wer muss die Architektur kennen?** (z.B. Entwickler, Architekten, PO)
2. **Wer muss von der Architektur überzeugt werden?** (z.B. Management, Kunden)
3. **Wer arbeitet mit der Architektur oder dem Code?** (z.B. Entwickler, DevOps)
4. **Wer braucht die Dokumentation?** (z.B. Neue Teammitglieder, Auditoren)
5. **Wer trifft Entscheidungen über das System?** (z.B. CTO, PO, Architekt)

## Codebase-Analyse-Hinweise

Bei Codebase-Analyse kannst du folgendes ableiten:
- **Aufgabenstellung**: Aus README.md, package.json `description`, Maven `<name>`/`<description>`, API-Endpunkten
- **Qualitätsziele**: Aus Test-Coverage-Konfiguration (Performance-Tests → Performance wichtig), Security-Libraries (→ Sicherheit wichtig), Monitoring-Setup (→ Verfügbarkeit wichtig)
- **Stakeholder**: Meist NICHT aus Code ableitbar → Rückfrage nötig

## Templates

### 01-01-Aufgabenstellung.md

```markdown
# Aufgabenstellung

## Kurzbeschreibung

<1-3 Sätze: Was ist das System und wozu dient es?>

## Business-Ziele

- <Ziel 1>
- <Ziel 2>
- <Ziel 3>

## Wesentliche funktionale Anforderungen

| ID | Anforderung | Beschreibung |
|----|------------|--------------|
| F1 | <Name> | <Kurzbeschreibung> |
| F2 | <Name> | <Kurzbeschreibung> |

## Verweise

- <Link zu Anforderungsdokumenten, Jira, Confluence etc.>
```

### 01-02-Qualitaetsziele.md

```markdown
# Qualitätsziele

Die folgenden Qualitätsziele haben höchste architektonische Relevanz:

| Priorität | Qualitätsziel | Szenario |
|-----------|--------------|----------|
| 1 | <z.B. Performance> | <Konkretes Szenario: "Das System antwortet auf 95% der Anfragen innerhalb von 200ms"> |
| 2 | <z.B. Sicherheit> | <Konkretes Szenario> |
| 3 | <z.B. Wartbarkeit> | <Konkretes Szenario> |

> Detaillierte Qualitätsanforderungen und -szenarien finden sich in [Sektion 10](../10-Qualitaetsanforderungen/).
```

### 01-03-Stakeholder.md

```markdown
# Stakeholder

| Rolle | Beschreibung | Erwartung an Architektur |
|-------|-------------|------------------------|
| <Rolle 1> | <Kurzbeschreibung> | <Was erwartet diese Rolle?> |
| <Rolle 2> | <Kurzbeschreibung> | <Was erwartet diese Rolle?> |
```

## Best Practices (aus arc42-Tipps)

- **Kompakt halten**: Anforderungsüberblick soll ein kurzer Extrakt sein, kein vollständiges Requirements-Dokument
- **Business-Ziele hervorheben**: Nicht nur Features listen, sondern den Geschäftswert betonen
- **Qualitätsziele konkret machen**: Keine Buzzwords wie "performant" — stattdessen messbare Szenarien
- **Maximal 3-5 Qualitätsziele**: Nur die architektonisch relevantesten, Details in Sektion 10
- **Stakeholder breit suchen**: Nicht nur offensichtliche Rollen, auch indirekte Betroffene berücksichtigen
- **Erwartungen dokumentieren**: Zu jedem Stakeholder die konkreten Erwartungen an Architektur und Dokumentation angeben
- **Qualitätsziele mit Lösungsstrategie verbinden**: Verweis auf Sektion 4, wie die Ziele erreicht werden

## Querverweise

- → **Sektion 4** (Lösungsstrategie): Qualitätsziele aus 1.2 müssen durch strategische Ansätze in S4 adressiert werden
- → **Sektion 10** (Qualitätsanforderungen): Detaillierte Szenarien zu den Qualitätszielen aus 1.2
- → **Sektion 12** (Glossar): Domänenbegriffe aus der Aufgabenstellung sollten im Glossar definiert sein
