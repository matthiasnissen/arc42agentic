---
name: arc42-write-s12-glossary
description: "Schreibt arc42 Sektion 12 (Glossar): Begriffsdefinitionen, Terminologie, Domänenbegriffe, technische Begriffe, Übersetzungstabellen. Use when: Sektion 12 schreiben, Glossar, Glossary, Begriffe, Definitionen, Terminologie dokumentieren."
---

# arc42 Sektion 12: Glossar schreiben

## Zweck

Die wichtigsten Domänen- und Fachbegriffe, die Stakeholder kennen sollten, wenn sie über die Architektur des Systems diskutieren. Optional auch Übersetzungstabellen bei mehrsprachigen Umgebungen.

## Dateistruktur

```
12-Glossar/
└── 12-01-Begriffe.md
```

Optional bei umfangreichem Glossar:

```
12-Glossar/
├── 12-01-Domaenenbegriffe.md
├── 12-02-Technische-Begriffe.md
└── 12-03-Abkuerzungen.md
```

## Interaktive Fragen an den User

1. **Welche Fachbegriffe aus der Domäne sind für das Verständnis des Systems wichtig?**
2. **Gibt es Begriffe, die im Team unterschiedlich verstanden werden?**
3. **Gibt es Abkürzungen, die erklärt werden müssen?**
4. **Wird in einer mehrsprachigen Umgebung gearbeitet?** (Dann Übersetzungstabelle nötig)
5. **Gibt es Synonyme, die vereinheitlicht werden sollten?** (z.B. "Auftrag" vs. "Bestellung" vs. "Order")
6. **Gibt es technische Begriffe, die für nicht-technische Stakeholder erklärt werden müssen?**

## Codebase-Analyse-Hinweise

- **Domänenbegriffe**: Aus Entity-Klassennamen, Enum-Werten, Package-Namen im Domain-Layer
- **Technische Begriffe**: Aus Framework-spezifischen Konzepten, die im Code referenziert werden
- **Abkürzungen**: Aus Klassennamen, Variablennamen, Kommentaren
- **Ubiquitous Language (DDD)**: Aus Value-Objects, Aggregate-Roots, Domain-Events

## Templates

### 12-01-Begriffe.md

```markdown
# Glossar

| Begriff | Definition |
|---------|-----------|
| <Begriff 1> | <Prägnante Definition im Kontext dieses Systems> |
| <Begriff 2> | <Definition> |
| <Abkürzung> | <Ausgeschriebene Form + kurze Erklärung> |
```

### Mit Übersetzung

```markdown
# Glossar

| Begriff (DE) | Begriff (EN) | Definition |
|-------------|-------------|-----------|
| Bestellung | Order | <Definition> |
| Kunde | Customer | <Definition> |
| Rechnung | Invoice | <Definition> |
```

### Ausführlichere Variante

```markdown
# Glossar

## Domänenbegriffe

| Begriff | Definition | Synonym(e) | Verwandte Begriffe |
|---------|-----------|------------|-------------------|
| <Begriff> | <Definition> | <ggf. Alternativbezeichnungen> | <Verwandte Begriffe> |

## Technische Begriffe

| Begriff | Definition | Kontext |
|---------|-----------|---------|
| <Tech-Begriff> | <Definition> | <Wo wird das im System verwendet?> |

## Abkürzungen

| Abkürzung | Bedeutung |
|-----------|-----------|
| ADR | Architecture Decision Record |
| API | Application Programming Interface |
```

## Best Practices (aus arc42-Tipps)

- **Glossar ernst nehmen**: Es sichert ein gemeinsames Verständnis im Team
- **Tabellenformat**: Einfache Tabelle mit Begriff + Definition ist am effektivsten
- **Kompakt halten**: Keine trivialen oder allgemein bekannten Begriffe aufnehmen
- **Domäne fokussieren**: Primär Domänenbegriffe, nicht allgemeine IT-Begriffe
- **Synonyme klären**: Wenn verschiedene Stakeholder verschiedene Begriffe verwenden
- **Übersetzungen hinzufügen**: Bei internationalen Teams oder Offshore-Entwicklung
- **Mit Domänenmodell kombinieren**: Begriffe aus dem Domänenmodell (S8) gehören ins Glossar
- **Verantwortung zuweisen**: Product Owner oder fachlicher Ansprechpartner sollte das Glossar pflegen

## Querverweise

- ← **Sektion 8** (Konzepte): Domänenmodell-Begriffe ins Glossar aufnehmen
- ← **Sektion 1** (Einführung): Fachbegriffe aus der Aufgabenstellung
- ← **Alle Sektionen**: Jeder in der Dokumentation verwendete spezifische Begriff sollte im Glossar stehen
