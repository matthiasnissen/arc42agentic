---
name: arc42-doc-layout
description: "Struktur-Erkennung und Delegations-Protokoll für arc42-Dokumentationen in verschiedenen Layouts. Use when: arc42 Doku-Layout erkennen, Multi-Folder, Flat-Files, Single-File, Dokumentationspfad auflösen, Section-Dateien finden, Delegation mit Pfaden oder Inline-Content."
---

# arc42-Doc-Layout Skill

Dieser Skill definiert das gemeinsame Protokoll für **Orchestratoren** (Struktur erkennen und korrekt delegieren) und **Section-/Konflikt-Agenten** (entgegennehmen was geliefert wird).

---

## Teil A — Für Orchestratoren: Struktur-Erkennung und Delegation

### Schritt 1: Dokumentationspfad ermitteln

Den Pfad zum Wurzelverzeichnis der Dokumentation entnimmst du aus:
1. Dem Nutzer-Prompt (hat höchste Priorität)
2. Der `AGENTS.md` im Repository-Root
3. Falls beides fehlt: Frage den Nutzer

### Schritt 2: Strukturtyp erkennen

Scanne das Verzeichnis (und eine Ebene tiefer). Verwende folgende Erkennungsregeln:

#### Multi-Folder (Typ A)

**Erkennungsmerkmal:** Das Dokumentationsverzeichnis enthält **Unterordner**, deren Namen mit einer zweistelligen Zahl beginnen oder arc42-Sektionsnamen enthalten:

Beispiele: `01-Einfuehrung-und-Ziele/`, `02-Randbedingungen/`, `05-Bausteinsicht/`

→ **Gängigste Struktur** bei Dokumentationen im arc42-Repository-Format.

#### Flat-Files (Typ B)

**Erkennungsmerkmal:** Das Dokumentationsverzeichnis enthält **nur `.md`-Dateien** (keine Unterordner für Sektionen), deren Namen eine Zahl oder ein arc42-Sektions-Schlüsselwort enthalten:

Schlüsselwörter: `anforderungen`, `einfuehrung`, `ziele`, `randbedingungen`, `kontext`, `strategie`, `loesung`, `baustein`, `bausteine`, `laufzeit`, `verteilung`, `konzepte`, `entscheidungen`, `qualitaet`, `risiken`, `glossar`

Beispiele: `chap-01-Anforderungen.md`, `chap-02-Randbedingungen.md`, `01-Einfuehrung.md`

→ **Typisch** für aus HTML konvertierte oder extern heruntergeladene Dokumentationen.

#### Single-File (Typ C)

**Erkennungsmerkmal:** Das Dokumentationsverzeichnis (oder ein explizit angegebener Pfad) enthält **eine einzige (oder wenige) `.md`-Datei(en)**, die alle arc42-Kapitel als `##`-Überschriften enthalten. Erkennbar daran, dass Überschriften wie `## 1.`, `## Einführung`, `## 2. Randbedingungen` o.ä. in einer Datei vorkommen.

Beispiele: `biking2-architecture.md`, `architecture.md`

→ **Typisch** für AsciiDoc/Confluence-Exporte oder kompakte Einzeldokumente.

---

### Schritt 3: Sektion-zu-Datei-Mapping erstellen

**Für Typ A (Multi-Folder):** Verwende die Unterordner direkt als Sektionspfade.

Standard-Mapping (weiche bei Abweichungen vom Tatsächlichen ab):

| Sektion | Standard-Ordner |
|---------|----------------|
| S1 | `01-Einfuehrung-und-Ziele/` |
| S2 | `02-Randbedingungen/` |
| S3 | `03-Kontextabgrenzung/` |
| S4 | `04-Loesungsstrategie/` |
| S5 | `05-Bausteinsicht/` |
| S6 | `06-Laufzeitsicht/` |
| S7 | `07-Verteilungssicht/` |
| S8 | `08-Konzepte/` |
| S9 | `09-Entscheidungen/` |
| S10 | `10-Qualitaetsanforderungen/` |
| S11 | `11-Risiken/` |
| S12 | `12-Glossar/` |

**Für Typ B (Flat-Files):** Lies alle `.md`-Dateien im Verzeichnis auf und ordne sie anhand von Schlüsselwort-Abgleich den Sektionen zu:

| Schlüsselwörter im Dateinamen | Sektion |
|-------------------------------|---------|
| `anforderung`, `einfuehrung`, `ziel`, `einleitung`, `01` | S1 |
| `randbedingung`, `02` | S2 |
| `kontext`, `abgrenzung`, `03` | S3 |
| `strategie`, `loesung`, `04` | S4 |
| `baustein`, `komponente`, `05` | S5 |
| `laufzeit`, `06` | S6 |
| `verteilung`, `infrastruktur`, `07` | S7 |
| `konzept`, `querschnitt`, `08` | S8 |
| `entscheidung`, `09` | S9 |
| `qualitaet`, `10` | S10 |
| `risiko`, `schulden`, `11` | S11 |
| `glossar`, `12` | S12 |

**Für Typ C (Single-File):** Lese die Datei vollständig. Extrahiere für jede Sektion den Textblock zwischen der zugehörigen Überschrift und der nächsten Überschrift gleicher oder höherer Ebene (`##` oder `#`). Zuordnung nach Überschriften-Inhalt analog zur Schlüsselwort-Tabelle oben.

---

### Schritt 4: Delegation

Gib jedem aufgerufenen Section-/Konflikt-Agenten die ermittelten Dateiinformationen **explizit** mit:

#### Delegation bei Typ A und B

Füge dem Delegations-Prompt hinzu:

```
Zu prüfende Datei(en) für deine Sektion:
- `<absoluter-oder-relativer-pfad>/datei.md`
- `<absoluter-oder-relativer-pfad>/datei2.md`  (falls mehrere)

Lies diese Dateien und führe deine Prüfung durch.
```

#### Delegation bei Typ C (Single-File)

Extrahiere den Abschnitt aus der Datei und übergib ihn inline:

```
Zu prüfender Inhalt für deine Sektion (aus <dateiname>, Abschnitt "<Heading>"):

---
<extrahierter Sektionstext>
---

Führe deine Prüfung auf Basis dieses Inhalts durch.
Beachte: Die Quelle ist eine Single-File-Dokumentation — Querverweise auf andere Sektionen können im selben Dokument unter anderen Überschriften stehen.
```

---

## Teil B — Für Section- und Konflikt-Agenten: Empfangs-Protokoll

### Wie Dateien/Inhalte empfangen werden

Prüfe zu Beginn deiner Arbeit, was der Aufrufer mitgeliefert hat:

**Fall 1: Dateipfad(e) explizit genannt**
→ Lies diese Dateien direkt. Ignoriere etwaige hardcodierte Standardordner.

**Fall 2: Inline-Content im Prompt geliefert** (zwischen `---`-Trennlinien)
→ Analysiere diesen Inhalt direkt, ohne Dateien zu lesen.
→ Beachte: Querverweise zu anderen Sektionen können im selben übergeordneten Dokument vorhanden sein.

**Fall 3: Weder Pfade noch Content geliefert (Standalone-Aufruf)**
→ Lies die `AGENTS.md` im Repository-Root, um den Dokumentationspfad zu ermitteln.
→ Wende dann den Erkennungsalgorithmus aus Teil A an, um die zugehörigen Dateien zu finden.
→ Falls kein Pfad ermittelbar: Frage den Nutzer.

### Hinweise zur Single-File-Analyse

Wenn du Inline-Content aus einer Single-File-Dokumentation erhältst:
- Querverweise wie "siehe Sektion 4" beziehen sich auf andere Abschnitte im selben Quelldokument
- Fehlende Unterabschnitte müssen differenziert bewertet werden: Prüfe, ob der Inhalt unter dem übergeordneten Heading steht, bevor du fehlende Gliederung bemängelst
- Die Granularität der Gliederung kann bei Single-File-Dokumentationen geringer sein — das ist kein Befund, sondern eine Eigenschaft des Formats

