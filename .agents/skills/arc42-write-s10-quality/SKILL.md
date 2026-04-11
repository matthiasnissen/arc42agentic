---
name: arc42-write-s10-quality
description: "Schreibt arc42 Sektion 10 (Qualitätsanforderungen): Qualitätsbaum, Qualitätsszenarien, Qualitätsübersicht, ISO 25010, Q42-Modell. Use when: Sektion 10 schreiben, Qualitätsanforderungen, Quality Requirements, Qualitätsbaum, Qualitätsszenarien dokumentieren."
---

# arc42 Sektion 10: Qualitätsanforderungen schreiben

## Zweck

Alle relevanten Qualitätsanforderungen. Die wichtigsten davon wurden bereits in Sektion 1.2 (Qualitätsziele) beschrieben und sollten hier nur referenziert werden. In Sektion 10 werden auch Qualitätsanforderungen mit geringerer Priorität aufgenommen.

## Dateistruktur

```
10-Qualitaetsanforderungen/
├── 10-01-Qualitaetsbaum.md
└── 10-02-Qualitaetsszenarien.md
```

## Interaktive Fragen an den User

### Für 10.1 Qualitätsbaum

1. **Welche Qualitätskategorien sind relevant?** (Referenz: ISO 25010 / Q42-Modell)
   - #reliable (Zuverlässigkeit)
   - #efficient (Effizienz/Performance)
   - #usable (Benutzbarkeit)
   - #secure (Sicherheit)
   - #flexible (Änderbarkeit/Wartbarkeit)
   - #operable (Betreibbarkeit)
   - #testable (Testbarkeit)
   - #safe (Betriebssicherheit)
2. **Gibt es weitere Qualitätsaspekte jenseits der Top-3-5 aus Sektion 1.2?**
3. **Wie priorisieren sich die Qualitätsanforderungen untereinander?**

### Für 10.2 Qualitätsszenarien

Pro Qualitätsanforderung:
1. **Was ist der Auslöser/Stimulus?** (z.B. "1000 gleichzeitige Nutzer senden Anfragen")
2. **Unter welchen Bedingungen?** (z.B. "im Normalbetrieb", "bei Lastspitzen")
3. **Was ist die erwartete Reaktion?** (z.B. "Antwort innerhalb 200ms")
4. **Wie wird gemessen?** (Metrik, Akzeptanzkriterium)

## Codebase-Analyse-Hinweise

- **Performance**: Aus Load-Test-Konfigurationen (Gatling, k6, JMeter), SLA-Definitionen
- **Sicherheit**: Aus Security-Scan-Konfigurationen, Penetration-Test-Setups
- **Testbarkeit**: Aus Test-Coverage-Thresholds, Testcontainers-Konfigurationen
- **Verfügbarkeit**: Aus Health-Check-Endpunkte, Liveness/Readiness-Probes
- **Monitoring**: Aus Metrics-Endpoints, Prometheus-Konfigurationen, Alerting-Rules

## Templates

### 10-01-Qualitaetsbaum.md

```markdown
# Qualitätsbaum

## Übersicht

<!-- Übersicht der relevanten Qualitätskategorien mit zugeordneten Anforderungen -->

| Kategorie | Qualitätsanforderung | Priorität | Szenario-ID |
|-----------|---------------------|-----------|-------------|
| #efficient | Antwortzeit < 200ms für 95% der Requests | Hoch | QS-01 |
| #reliable | 99.9% Verfügbarkeit im Jahresmittel | Hoch | QS-02 |
| #secure | Alle Daten verschlüsselt at-rest und in-transit | Hoch | QS-03 |
| #flexible | Neue Features in < 2 Wochen deploybar | Mittel | QS-04 |
| #testable | 80% Zeilencoverage, alle APIs E2E-getestet | Mittel | QS-05 |

> Die Top-3 Qualitätsziele sind in [Sektion 1.2](../01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md) beschrieben.
```

### 10-02-Qualitaetsszenarien.md

```markdown
# Qualitätsszenarien

## QS-01: <Performance — Antwortzeit>

| Aspekt | Beschreibung |
|--------|-------------|
| **Qualitätskategorie** | #efficient |
| **Quelle/Stimulus** | <z.B. 1000 gleichzeitige Benutzer senden Suchanfragen> |
| **Umgebung** | <z.B. Produktivsystem unter Normallast> |
| **Artefakt** | <z.B. Such-Service, API-Gateway> |
| **Reaktion** | <z.B. Suchergebnisse werden korrekt zurückgeliefert> |
| **Metrik** | <z.B. 95-Perzentil der Antwortzeit < 200ms> |

---

## QS-02: <Verfügbarkeit>

| Aspekt | Beschreibung |
|--------|-------------|
| **Qualitätskategorie** | #reliable |
| **Quelle/Stimulus** | <z.B. Ein Application-Server fällt aus> |
| **Umgebung** | <z.B. Produktivsystem> |
| **Artefakt** | <z.B. Gesamtsystem> |
| **Reaktion** | <z.B. Anfragen werden automatisch auf verbleibende Server umgeleitet> |
| **Metrik** | <z.B. < 30 Sekunden Unterbrechung, kein Datenverlust> |

<!-- Wiederhole das Template für jedes Qualitätsszenario -->
```

### Kurzformat (Q42-Stil)

```markdown
## QS-01: Performance — Antwortzeit

**Kontext:** Web-Anwendung mit Echtzeit-Suchergebnissen
**Stimulus:** 1000 gleichzeitige Suchanfragen
**Metrik:** 95-Perzentil Antwortzeit < 200ms
```

## Best Practices (aus arc42-Tipps)

- **Qualitätsziele kurz halten (S1.2)**: Top-3-5 in Sektion 1, Details hier in Sektion 10
- **Szenarien statt Buzzwords**: "Das System ist performant" → konkretes Szenario mit Metrik
- **Drei Arten von Szenarien**: Nutzungsszenarien, Änderungsszenarien, Fehlerszenarien
- **Q42/ISO 25010 als Checkliste**: Systematisch alle Kategorien durchgehen
- **Messbar formulieren**: Jedes Szenario braucht ein Akzeptanzkriterium
- **Für Architektur-Evaluierung nutzbar**: Szenarien so formulieren, dass sie zur Bewertung der Architektur taugen

## Querverweise

- ← **Sektion 1.2** (Qualitätsziele): Top-3-5 hier detaillieren, nicht wiederholen
- ← **Sektion 4** (Lösungsstrategie): Strategische Ansätze zur Erreichung der Qualitätsziele
- → **Sektion 11** (Risiken): Qualitätsanforderungen, die nicht erfüllt werden, als Risiko dokumentieren
