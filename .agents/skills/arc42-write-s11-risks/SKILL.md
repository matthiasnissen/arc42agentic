---
name: arc42-write-s11-risks
description: "Schreibt arc42 Sektion 11 (Risiken und technische Schulden): Risikoliste, technische Schulden, Maßnahmen, Bewertung. Use when: Sektion 11 schreiben, Risiken, Risks, technische Schulden, Technical Debt, Probleme dokumentieren."
---

# arc42 Sektion 11: Risiken und technische Schulden schreiben

## Zweck

Eine nach Priorität geordnete Liste identifizierter technischer Risiken und technischer Schulden, inklusive vorgeschlagener Maßnahmen zur Minimierung, Vermeidung oder Reduktion.

"Risk management is project management for grown-ups" (Tim Lister)

## Dateistruktur

Option A — Ein File pro Risiko (bei vielen Risiken):

```
11-Risiken/
├── 11-01-<Risiko-1>.md
├── 11-02-<Risiko-2>.md
└── 11-XX-<Risiko-X>.md
```

Option B — Konsolidiert (bei wenigen Risiken):

```
11-Risiken/
└── 11-01-Risiken.md
```

## Interaktive Fragen an den User

1. **Welche technischen Risiken sehen Sie?** (z.B. Technologie-Risiken, Performance-Risiken, Verfügbarkeitsrisiken)
2. **Gibt es bekannte technische Schulden?** (z.B. veraltete Libraries, fehlende Tests, Code-Smells)
3. **Welche externen Abhängigkeiten sind risikobehaftet?** (z.B. Single-Points-of-Failure, Vendor-Lock-in)
4. **Gibt es Wissenslücken im Team?** (z.B. neue Technologie, fehlende Dokumentation)
5. **Welche Qualitätsanforderungen könnten gefährdet sein?**
6. **Gibt es organisatorische Risiken?** (z.B. Key-Person-Dependency, Teamfluktuation)
7. **Welche Maßnahmen sind geplant oder möglich?**

## Codebase-Analyse-Hinweise

- **Veraltete Dependencies**: Aus Lock-Files (outdated packages), Dependabot-Alerts, deprecation warnings
- **Fehlende Tests**: Aus Coverage-Berichten, Verzeichnissen ohne Tests
- **Code-Smells**: Aus Linter-Warnungen, ESLint/SonarQube-Reports
- **Security-Risiken**: Aus `npm audit`, OWASP-dependency-check, CVE-Datenbanken
- **Technische Schulden**: Aus TODO/FIXME/HACK-Kommentaren im Code
- **Komplexität**: Aus zyklischer Abhängigkeitsanalyse, große Dateien/Klassen

## Templates

### 11-01-Risiken.md (Tabellenformat)

```markdown
# Risiken und technische Schulden

## Risiken

| ID | Risiko | Eintrittswahrscheinlichkeit | Auswirkung | Maßnahme |
|----|--------|---------------------------|-----------|----------|
| R1 | <Beschreibung des Risikos> | <hoch/mittel/niedrig> | <hoch/mittel/niedrig> | <Geplante Maßnahme> |
| R2 | <Beschreibung> | <Bewertung> | <Bewertung> | <Maßnahme> |

## Technische Schulden

| ID | Schuld | Bereich | Aufwand zur Behebung | Priorität |
|----|--------|---------|---------------------|-----------|
| TD1 | <Beschreibung der technischen Schuld> | <Betroffener Baustein/Bereich> | <Schätzung> | <hoch/mittel/niedrig> |
| TD2 | <Beschreibung> | <Bereich> | <Schätzung> | <Priorität> |
```

### 11-XX-Risiko.md (Detailformat pro Risiko)

```markdown
# R<Nr>: <Titel des Risikos>

## Beschreibung

<Detaillierte Beschreibung des Risikos>

## Eintrittswahrscheinlichkeit

<hoch | mittel | niedrig> — <Begründung>

## Auswirkung bei Eintritt

<hoch | mittel | niedrig> — <Was passiert konkret?>

## Betroffene Qualitätsziele

- <Verweis auf gefährdetes Qualitätsziel aus S1.2 / S10>

## Maßnahmen

| Maßnahme | Typ | Status |
|----------|-----|--------|
| <Maßnahme 1> | <vermeidend/mindernd/reaktiv> | <geplant/in Umsetzung/umgesetzt> |
| <Maßnahme 2> | <Typ> | <Status> |

## Verantwortlich

<Wer ist für die Überwachung/Maßnahmen verantwortlich?>
```

## Typische Risiken

- **Vendor-Lock-in**: Starke Abhängigkeit von einem Cloud-Provider oder Produkt
- **Single-Point-of-Failure**: Zentrale Komponente ohne Redundanz
- **Performance-Engpass**: Bekannte Flaschenhälse unter Last
- **Security-Lücken**: Bekannte oder potenzielle Sicherheitsprobleme
- **Fehlende Tests**: Bereiche ohne ausreichende Testabdeckung
- **Key-Person-Dependency**: Wissen nur bei einer Person
- **Veraltete Technologie**: Libraries/Frameworks am End-of-Life
- **Komplexität**: Schwer wartbare oder verständliche Codebereiche

## Best Practices (aus arc42-Tipps)

- **Breit suchen**: Risiken mit verschiedenen Stakeholdern identifizieren
- **Schnittstellen analysieren**: Externe Schnittstellen sind häufige Risikoquellen
- **Prozesse analysieren**: Nicht nur technische, auch prozessuale Risiken erfassen
- **Qualitativ bewerten**: Eintrittswahrscheinlichkeit × Auswirkung = Priorität
- **Maßnahmen vorschlagen**: Zu jedem Risiko mindestens einen Maßnahmenvorschlag
- **Quellcode analysieren**: Code-Metriken und -Qualität als Risiko-Indikator nutzen
- **Priorisieren**: Nach Auswirkung und Wahrscheinlichkeit sortieren

## Querverweise

- ← **Sektion 1.2** (Qualitätsziele): Risiken, die Qualitätsziele gefährden
- ← **Sektion 10** (Qualitätsanforderungen): Nicht erfüllbare Qualitätsszenarien → Risiko
- ← **Sektion 3** (Kontext): Risiken an externen Schnittstellen
