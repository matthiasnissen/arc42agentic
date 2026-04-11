---
name: arc42-write-s02-constraints
description: "Schreibt arc42 Sektion 2 (Randbedingungen): Technische, organisatorische und politische Constraints sowie Konventionen. Use when: Sektion 2 schreiben, Randbedingungen, Constraints, Konventionen dokumentieren, Einschränkungen erfassen."
---

# arc42 Sektion 2: Randbedingungen schreiben

## Zweck

Alle Anforderungen, die Softwarearchitekten in ihren Entwurfs- und Implementierungsentscheidungen einschränken. Diese Constraints gehen manchmal über einzelne Systeme hinaus und gelten für ganze Organisationen.

## Dateistruktur

```
02-Randbedingungen/
├── 02-01-Technisch.md
├── 02-02-Organisatorisch.md
└── 02-03-Konventionen.md
```

## Interaktive Fragen an den User

### Für 2.1 Technische Randbedingungen

1. **Welche Programmiersprachen/Frameworks sind vorgegeben?**
2. **Gibt es vorgegebene Betriebssysteme oder Plattformen?**
3. **Welche Datenbanken/Middleware ist vorgegeben?**
4. **Gibt es Vorgaben zu Laufzeitumgebungen?** (z.B. JVM-Version, Node-Version, Container-Runtime)
5. **Gibt es Einschränkungen bei der Hardware/Infrastruktur?**
6. **Welche externen Systeme/Schnittstellen sind vorgegeben?**
7. **Gibt es Vorgaben zu Bibliotheken oder Lizenzen?** (z.B. keine GPL, nur OSS)

### Für 2.2 Organisatorische Randbedingungen

1. **Wie ist das Team organisiert?** (Größe, Verteilung, Erfahrung)
2. **Welche Entwicklungsprozesse gelten?** (Scrum, Kanban, SAFe etc.)
3. **Gibt es Zeitvorgaben oder Budget-Constraints?**
4. **Gibt es regulatorische Anforderungen?** (DSGVO, ISO 27001, PCI-DSS etc.)
5. **Gibt es unternehmensweite Architektur-Vorgaben?** (Enterprise Architecture, Referenzarchitekturen)

### Für 2.3 Konventionen

1. **Gibt es Coding-Standards?** (Style Guides, Linting-Regeln)
2. **Welche Dokumentationskonventionen gelten?** (Sprache, Format)
3. **Gibt es Versionierungsvorgaben?** (Branching-Modell, Semantic Versioning)
4. **Gibt es Naming-Conventions?** (Packages, Klassen, APIs)
5. **Gibt es Test-Vorgaben?** (Mindest-Coverage, Test-Arten)

## Codebase-Analyse-Hinweise

- **Technische Constraints**: Aus Build-Files (pom.xml → Java-Version, package.json → Node/TS-Version), Compiler-Einstellungen, Docker base images
- **Konventionen**: Aus `.editorconfig`, `.eslintrc`, `checkstyle.xml`, `.prettierrc`, Commit-Message-Templates, `.gitignore`
- **Lizenzen**: Aus `LICENSE`, Dependency-Lizenzen in Lock-Files
- **CI/CD**: Aus `.github/workflows/`, `Jenkinsfile`, `.gitlab-ci.yml`
- **Organisatorische Constraints**: Meist NICHT aus Code ableitbar → Rückfrage nötig

## Templates

### 02-01-Technisch.md

```markdown
# Technische Randbedingungen

| Randbedingung | Beschreibung | Hintergrund/Motivation |
|--------------|-------------|----------------------|
| Programmiersprache: <Sprache> | <Version, Details> | <Warum diese Vorgabe?> |
| Framework: <Name> | <Version, Details> | <Warum?> |
| Datenbank: <Name> | <Version, Details> | <Warum?> |
| Laufzeitumgebung: <Name> | <Details> | <Warum?> |
| Betriebssystem: <Name> | <Details> | <Warum?> |
```

### 02-02-Organisatorisch.md

```markdown
# Organisatorische Randbedingungen

| Randbedingung | Beschreibung | Hintergrund/Motivation |
|--------------|-------------|----------------------|
| Teamstruktur | <Beschreibung> | <Auswirkung auf Architektur> |
| Entwicklungsprozess | <z.B. Scrum, 2-Wochen-Sprints> | <Auswirkung> |
| Zeitrahmen | <z.B. MVP bis Q3/2026> | <Auswirkung> |
| Regulierung | <z.B. DSGVO-Konformität erforderlich> | <Auswirkung auf Architektur> |
```

### 02-03-Konventionen.md

```markdown
# Konventionen

| Konvention | Beschreibung | Verbindlichkeit |
|-----------|-------------|-----------------|
| Coding-Standard | <z.B. Google Java Style Guide> | verbindlich |
| Versionierung | <z.B. Semantic Versioning 2.0> | verbindlich |
| Dokumentation | <z.B. arc42, deutsch, Markdown> | verbindlich |
| Branching | <z.B. Git Flow> | empfohlen |
| Test-Coverage | <z.B. >= 80% Zeilencoverage> | verbindlich |
```

## Best Practices (aus arc42-Tipps)

- **Konsequenzen klären**: Zu jeder Randbedingung die Auswirkung auf die Architektur dokumentieren
- **Kategorien trennen**: Technische, organisatorische und politische Constraints getrennt halten
- **Organisationsweite Constraints berücksichtigen**: Nicht nur projekt-spezifische, auch übergreifende der Organisation
- **Verhandlungsbarkeit angeben**: Welche Constraints sind fix, welche verhandelbar?
- **Einfache Tabellen**: Tabellenformat ist das effektivste Format für Constraints

## Querverweise

- → **Sektion 4** (Lösungsstrategie): Strategie muss sich im Rahmen der Constraints bewegen
- → **Sektion 8** (Konzepte): Konzepte müssen Constraints respektieren
- → **Sektion 9** (Entscheidungen): Entscheidungen dürfen Constraints nicht verletzen
