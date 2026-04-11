---
name: arc42-write-s04-solution-strategy
description: "Schreibt arc42 Sektion 4 (Lösungsstrategie): Fundamentale Entwurfsentscheidungen, Technologieentscheidungen, Top-Level-Zerlegung, Ansätze zur Erreichung von Qualitätszielen. Use when: Sektion 4 schreiben, Lösungsstrategie, Solution Strategy, Technologieentscheidungen, Architekturansätze dokumentieren."
---

# arc42 Sektion 4: Lösungsstrategie schreiben

## Zweck

Kurze Zusammenfassung und Erklärung der fundamentalen Entwurfsentscheidungen und Lösungsansätze, die die Architektur des Systems formen:
- Technologieentscheidungen
- Entscheidungen über die Top-Level-Zerlegung (Architekturmuster)
- Ansätze zur Erreichung wesentlicher Qualitätsziele
- Relevante Organisationsentscheidungen

## Dateistruktur

```
04-Loesungsstrategie/
└── 04-01-Strategie.md
```

Bei umfangreichen Strategien optional aufteilbar:

```
04-Loesungsstrategie/
├── 04-01-Technologieentscheidungen.md
├── 04-02-Architekturansatz.md
├── 04-03-Qualitaetsziel-Ansaetze.md
└── 04-04-Organisatorische-Ansaetze.md
```

## Interaktive Fragen an den User

1. **Welches Architekturmuster wurde gewählt?** (Microservices, Monolith, Modular Monolith, Event-Driven, Hexagonal, Layered etc.)
2. **Warum dieses Muster?** Was war die Hauptmotivation?
3. **Welche Technologien bilden das Fundament?** (Programmiersprache, Framework, Datenbank, Cloud-Provider)
4. **Wie wird Qualitätsziel X erreicht?** (Pro Qualitätsziel aus Sektion 1.2 einen Ansatz)
5. **Gibt es eine Top-Level-Zerlegungsstrategie?** (z.B. nach Domäne, nach Layer, nach Feature)
6. **Welche organisatorischen Entscheidungen beeinflussen die Architektur?** (z.B. Team-Topologie, Conway's Law)

## Codebase-Analyse-Hinweise

- **Architekturmuster**: Aus Package-Struktur (layers vs. features vs. modules), Multi-Modul-Projekte (→ Microservices/Modular)
- **Technologien**: Aus Build-Files und Dependencies direkt ableitbar
- **Top-Level-Zerlegung**: Aus der obersten Package/Modul-Ebene
- **Qualitätsziel-Ansätze**: Aus Libraries (Cache → Performance, Circuit-Breaker → Resilience, Test-Frameworks → Testbarkeit)

## Templates

### 04-01-Strategie.md

```markdown
# Lösungsstrategie

## Technologieentscheidungen

| Technologie | Entscheidung | Begründung |
|------------|-------------|-----------|
| Programmiersprache | <z.B. Kotlin> | <Warum?> |
| Framework | <z.B. Spring Boot 3> | <Warum?> |
| Datenbank | <z.B. PostgreSQL> | <Warum?> |
| Messaging | <z.B. Apache Kafka> | <Warum?> |
| Cloud | <z.B. AWS> | <Warum?> |

## Top-Level-Zerlegung

<Beschreibung des gewählten Architekturansatzes und der Zerlegungsstrategie>

**Gewähltes Architekturmuster:** <z.B. Modular Monolith mit DDD-Bounded-Contexts>

**Begründung:** <Warum dieses Muster? Welche Alternativen wurden betrachtet?>

## Ansätze zur Erreichung der Qualitätsziele

| Qualitätsziel | Ansatz | Details |
|--------------|--------|---------|
| <Qualitätsziel aus S1.2> | <Strategischer Ansatz> | <Verweis auf Konzept/Entscheidung> |
| <Qualitätsziel aus S1.2> | <Strategischer Ansatz> | <Verweis> |

## Organisatorische Entscheidungen

- <z.B. Entwicklungsprozess: Trunk-Based Development mit Feature-Flags>
- <z.B. Team-Struktur: Cross-funktionale Teams entlang von Domänengrenzen>
```

## Best Practices (aus arc42-Tipps)

- **Kompakt halten**: Strategie als Keyword-Liste oder Tabelle, keine langen Prosa-Texte
- **Qualitätsziele verknüpfen**: Jeden Ansatz einem Qualitätsziel aus Sektion 1.2 zuordnen
- **Auf Details verweisen**: Detailliertere Erklärungen in Sektion 5 (Struktur), Sektion 8 (Konzepte) oder Sektion 9 (Entscheidungen)
- **Iterativ wachsen lassen**: Muss nicht von Anfang an vollständig sein
- **Begründungen liefern**: Nicht nur WAS entschieden wurde, sondern WARUM
- **Alternativen erwähnen**: Kurz andeuten, welche Alternativen existierten

## Querverweise

- ← **Sektion 1.2** (Qualitätsziele): Die Strategie muss die Qualitätsziele adressieren
- → **Sektion 5** (Bausteinsicht): Strukturelle Details zur Zerlegungsstrategie
- → **Sektion 8** (Konzepte): Detaillierte Ausarbeitung der Lösungsansätze
- → **Sektion 9** (Entscheidungen): ADRs für die fundamentalen Entscheidungen
- ← **Sektion 2** (Randbedingungen): Strategie muss im Rahmen der Constraints bleiben
