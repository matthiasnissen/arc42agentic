# arc42 Dokumentations-Review — DokChess

**Datum:** 2026-03-10  
**Modell:** Claude Opus 4.6  
**Geprüfter Bestand:** `src/` — Sektionen 1–12 vollständig vorhanden

---

## Gesamtübersicht

| Sektion | Status | Befunde |
|---------|--------|---------|
| 1. Einführung und Ziele | 🟡 | Solide Grundlage; Business-Ziele nicht explizit, Stakeholder-Tabelle formal unvollständig |
| 2. Randbedingungen | 🟢 | Gut strukturiert; Konsequenzen der Constraints und Freiheitsgrade fehlen |
| 3. Kontextabgrenzung | 🟡 | Fachliche Ein-/Ausgaben fehlen, kein Mapping fachlich↔technisch |
| 4. Lösungsstrategie | 🟡 | Überwiegend gut; Namenskonflikt beim Qualitätsziel „Spielstärke", fehlende Klammer |
| 5. Bausteinsicht | 🟢 | Gute Hierarchie und Templates; Zerlegungsbegründung fehlt |
| 6. Laufzeitsicht | 🟡 | Vorhandenes Szenario gut, aber nur ein einziges — Fehler-/Startszenarien fehlen |
| 7. Verteilungssicht | 🟡 | Grundlegend vorhanden; Software-Hardware-Mapping fehlt, nur Windows dokumentiert |
| 8. Querschnittliche Konzepte | 🟡 | Konzepte gut erklärt; Rückverweise auf Bausteinsicht (S5) fehlen durchgängig |
| 9. Architekturentscheidungen | 🟢 | ADRs formal vorbildlich; weitere strategische Entscheidungen fehlen als ADR |
| 10. Qualitätsanforderungen | 🟡 | Alle Qualitätsziele durch Szenarien abgedeckt; Qualitätsbaum nur als Bild |
| 11. Risiken und techn. Schulden | 🔴 | Keine Übersicht, keine Priorisierung, technische Schulden nicht dokumentiert |
| 12. Glossar | 🟢 | Gut strukturiert; Domänenmodell-Begriffe und architekturrelevante Terme fehlen |

---

## Kritische Befunde

Die folgenden Befunde erfordern vorrangige Bearbeitung:

### Sektion 3 — Kontextabgrenzung

**[B-01] Fehlende Ein-/Ausgabe-Spezifikation im fachlichen Kontext**  
Die Kommunikationspartner werden beschrieben, aber es fehlt eine explizite Auflistung der fachlichen Ein- und Ausgaben pro Partner (Züge, Remisangebote, Spielergebnis etc.).

> **Vorschlag:** Nach jedem Kommunikationspartner eine Ein-/Ausgabe-Tabelle ergänzen:
> ```
> | Richtung | Daten |
> |---|---|
> | Eingabe (Gegner → DokChess) | Züge, Spielstart, Remisangebote, Aufgabe |
> | Ausgabe (DokChess → Gegner) | Züge, Remisangebote, Spielergebnis |
> ```

**[B-04] Fehlendes Mapping fachlich ↔ technisch**  
Der technische Kontext nennt XBoard-Protokoll und Polyglot Opening Book, stellt aber kein explizites Mapping zu den fachlichen Partnern aus 3.1 her.

> **Vorschlag:** Am Anfang von 3.2 eine Mapping-Tabelle ergänzen:
> ```
> | Fachlicher Partner (3.1) | Technische Realisierung | Protokoll/Format |
> |---|---|---|
> | Menschlicher Gegner / Computergegner | XBoard-kompatibler Client | XBoard-Protokoll (stdin/stdout) |
> | Eröffnungsbibliothek | Polyglot Opening Book | Binäres Dateiformat (lesend) |
> | Endspielbibliothek | (nicht implementiert) | — |
> ```

### Sektion 6 — Laufzeitsicht

**[S06-04] Nur ein einziges Szenario vorhanden**  
Die gesamte Laufzeitsicht besteht aus nur einem Szenario (Zugermittlung). Mindestens weitere Szenarien für Eröffnungstreffer, Systemstart und Fehlerfälle (ungültiger Zug) sollten ergänzt werden.

### Sektion 7 — Verteilungssicht

**[B7-03] Unvollständiges Software-Hardware-Mapping**  
Die vier Subsysteme aus Sektion 5 werden pauschal als „DokChess.jar" erwähnt. Ein explizites Mapping der Bausteine auf Deployment-Artefakte fehlt.

> **Vorschlag:** Artefakt-Mapping-Tabelle ergänzen:
> ```
> | Baustein (Sektion 5) | Deployment-Artefakt | Infrastruktur-Element |
> |---|---|---|
> | XBoard-Protokoll | DokChess.jar | JVM auf Windows-PC |
> | Spielregeln | DokChess.jar | JVM auf Windows-PC |
> | Engine | DokChess.jar | JVM auf Windows-PC |
> | Eröffnung | DokChess.jar + externe .bin-Datei | JVM / Dateisystem |
> ```

### Sektion 8 — Querschnittliche Konzepte

**[S08-B01/B02] Fehlende Querverweise von Konzepten zu Bausteinen**  
Die Konzepte 08-01 (Abhängigkeiten) und 08-02 (Domänenmodell) verweisen auf keinen einzigen Baustein aus Sektion 5, obwohl die Gegenrichtung (S5→S8) gut gepflegt ist. Dies erschwert die Navigation und schwächt die konzeptuelle Integrität.

### Sektion 11 — Risiken und technische Schulden

**[R11-01] Fehlende Gesamtübersicht der Risiken**  
Es gibt keine zusammenfassende Übersichtsseite mit Tabelle aller Risiken. Für Management-Stakeholder fehlt ein schneller Überblick.

**[R11-02] Fehlende Priorisierung der Risiken**  
Die Risiken sind lediglich nummeriert, aber nicht nach Eintrittswahrscheinlichkeit oder Schadenspotenzial bewertet.

**[R11-03] Technische Schulden nicht dokumentiert**  
Obwohl die Sektion „Risiken **und technische Schulden**" heißt, werden keine technischen Schulden explizit aufgeführt. Bewusst eingegangene Schulden (fehlende 50-Züge-Regel, keine Endspieldatenbanken, kein UCI) sind in anderen Sektionen verstreut.

---

## Empfehlungen

### Sektion 1 — Einführung und Ziele

- **Business-Ziele explizit machen:** Vor den „Wesentlichen Features" einen Abschnitt „Treibende Kräfte" einfügen (Lehrmaterial, Experimentierplattform, Demonstrationsfähigkeit).
- **Stakeholder-Tabelle auf 3 Spalten erweitern:** Rolle, Kontakt, Erwartungen an Architektur/Dokumentation trennen.
- **Fehlende Stakeholder:** Schachspieler (Endanwender) ergänzen oder deren Ausschluss begründen.

### Sektion 2 — Randbedingungen

- **Konsequenzen-Spalte ergänzen:** Für technische und organisatorische Constraints die architektonischen Auswirkungen dokumentieren.
- **Verbindlichkeit kennzeichnen:** Hart vs. weich (nicht verhandelbar vs. wünschenswert) systematisch unterscheiden.
- **Tippfehler:** „Schulungsunternehmenin" → „Schulungsunternehmen in" (02-02-Organisatorisch.md).

### Sektion 3 — Kontextabgrenzung

- **Zusammenfassende Schnittstellentabelle** im fachlichen Kontext ergänzen.
- **Datenflussrichtung** bei Eröffnungen und Endspielen explizit benennen.
- **Protokollbeschreibung für XBoard** (stdin/stdout, textbasiert, zeilenorientiert) im technischen Kontext ergänzen.

### Sektion 4 — Lösungsstrategie

- **Namenskonflikt beheben:** In 04-01-Einstieg.md „Attraktive Spielstärke (Attraktivität)" → „Akzeptable Spielstärke (Funktionale Eignung)" angleichen.
- **Fehlende Klammer:** In 04-02-Aufbau.md schließende Klammer bei Querverweis ergänzen.

### Sektion 5 — Bausteinsicht

- **Begründung der Zerlegung** auf Ebene 1 ergänzen (fachliche Trennung, Austauschbarkeit, Testbarkeit).
- **Tippfehler:** „Püft" → „Prüft" in 05-03-Spielregeln.md.
- **Hinweis auf nicht implementierte Endspiele** in Ebene 1 aufnehmen.

### Sektion 6 — Laufzeitsicht

- **Ebene-2-Bausteine** (Zugsuche, Stellungsbewertung) im Szenario explizit namentlich referenzieren.
- **Weitere Szenarien ergänzen:** Eröffnungstreffer, ungültiger Zug, Systemstart/Initialisierung.

### Sektion 7 — Verteilungssicht

- **Motivation für Deployment-Struktur** (Single-PC, Über-jar) kurz begründen.
- **Übertragbarkeit auf andere Plattformen** (Linux, macOS mit Shell-Skript) dokumentieren.
- **Zweites Verteilungsszenario** mit Eröffnungsbibliothek ergänzen.

### Sektion 8 — Querschnittliche Konzepte

- **Rückverweise auf Sektion 5** in den Konzepten 08-01, 08-02, 08-04, 08-05 und 08-07 ergänzen.
- **Entscheidungsanteile auslagern:** Die eingebetteten Entscheidungen in 08-01 (kein DI-Framework) und 08-06 (kein Logging-Framework) als eigene ADRs in Sektion 9 dokumentieren.

### Sektion 9 — Architekturentscheidungen

- **Zeitstempel klären:** Ursprungsdatum der Entscheidung vom Dokumentationsdatum unterscheiden.
- **Weitere ADRs erwägen:** Insbesondere für Reactive Extensions, DI-Muster/Framework, Minimax-Algorithmus und Logging-Strategie.

### Sektion 10 — Qualitätsanforderungen

- **Textuelle Darstellung des Qualitätsbaums** als Tabelle unterhalb des Bildes ergänzen.
- **Szenario-Struktur präzisieren:** Optional Stimulus/Metrik-Spalten hinzufügen.
- **Kategorisierungsspalte** (Qualitätsmerkmal) in der Szenario-Tabelle ergänzen.

### Sektion 11 — Risiken und technische Schulden

- **Risikoübersicht** als neue Datei `11-00-Uebersicht.md` mit priorisierter Tabelle anlegen.
- **Risikobewertung** (Eintrittswahrscheinlichkeit, Schadenspotenzial, Priorität) pro Risiko ergänzen.
- **Technische Schulden** als eigene Datei dokumentieren (50-Züge-Regel, Stellungswiederholung, Endspieldatenbanken, UCI).
- **Risiken für Top-Qualitätsziele** (Analysierbarkeit, Änderbarkeit) ergänzen.

### Sektion 12 — Glossar

- **Domänenmodell-Begriffe aufnehmen:** Stellung, Zug, Feld, Figur.
- **Architekturrelevante Begriffe ergänzen:** Eröffnungsbibliothek, Spielregeln, UCI-Protokoll.
- **Querverweis auf Domänenmodell (8.2)** im Glossar-Einstieg ergänzen.

---

## Sektionsübergreifende Konflikte

| Konfliktdimension | Status | Befunde |
|---|---|---|
| Qualitätsstrang (S1↔S4↔S10) | ⚠️ | Inkonsistente Benennung „Spielstärke" (S1: „Akzeptable"/Funktionale Eignung vs. S4: „Attraktive"/Attraktivität); Zuverlässigkeitsszenarien Z01/Z02 ohne korrespondierendes Qualitätsziel; leichte Prioritätsumkehr bei Szenario-Abdeckung |
| Strategie↔Entscheidungen (S4↔S9) | ⚠️ | Kein direkter Widerspruch, aber asymmetrische Dokumentationstiefe: XBoard und Immutabilität als ADR dokumentiert, Java, Reactive Extensions und Minimax fehlen als ADR; Immutabilität in 3 S4-Dateien erwähnt, nur einmal mit Querverweis auf ADR 09-02 |
| Constraint-Compliance (S2↔S4/S8/S9) | ✅ | Hohe Compliance (13/15 Constraints konform). Klärungsbedarf: Reactive Extensions — externe Bibliothek oder eigene Implementierung unklar; XBoard-Entscheidung begründet mit Cross-Platform, Deployment nur Windows-spezifisch |
| Kontext↔Bausteine (S3↔S5) | ⚠️ | Endspiele im fachlichen Kontext definiert, fehlen in Bausteinsicht; Remisangebote im Kontext versprochen, in XBoard-Subsystem als nicht unterstützt gelistet; Computergegner nicht explizit in Bausteinsicht zugeordnet; Terminologie-Inkonsistenz bei Eröffnungs-Schnittstelle |
| Sichten-Konsistenz (S5↔S6↔S7) | ⚠️ | Namensinkonsistenz „Eröffnung" (S5) vs. „Eröffnungsbibliothek" (S6); Verteilungsszenario zeigt Deployment ohne Eröffnungsbibliothek, Laufzeitszenario nutzt sie; Ebene-2-Module ohne eigene Laufzeitszenarien; Verteilungssicht mappt keine einzelnen Subsysteme |
| Konzepte↔Entscheidungen (S8↔S9) | ⚠️ | Entscheidung gegen DI-Framework in 08-01 versteckt statt als ADR in S9; zwei Entscheidungen (kein Logging-Framework, kein Tracing) in 08-06 eingebettet; Immutabilitäts-Scope im Konzept 08-02 weiter als in ADR 09-02 |
| Risiken↔Qualität (S11↔S1/S10) | ❌ | Systematische Lücke: Die beiden höchstpriorisierten Qualitätsziele (Analysierbarkeit Prio 1, Änderbarkeit Prio 2) haben keine zugehörigen Risiken; Effizienz nur unscharf durch R11.3 adressiert; R11.3 formuliert Zielkonflikt einseitig als Spielstärke-Risiko |

---

## Detaillierte Konfliktanalysen

### Qualitätsstrang (S1 ↔ S4 ↔ S10)

| ID | Schwere | Beschreibung |
|---|---|---|
| KQS-01 | 🟡 | **Inkonsistente Benennung „Spielstärke":** S1 nennt „Akzeptable Spielstärke (Funktionale Eignung)", S4 nennt „Attraktive Spielstärke (Attraktivität)" — doppelter Widerspruch bei Adjektiv und ISO-25010-Merkmal |
| KQS-02 | 🟡 | **Verwaiste Szenarien:** Z01/Z02 (Zuverlässigkeit) adressieren ein Qualitätsmerkmal, das in S1.2 nicht als Qualitätsziel vorkommt und in S4 keine strategische Antwort hat |
| KQS-03 | 🟢 | **Leichte Prioritätsumkehr:** Das viertpriorisierte Ziel (Funktionale Eignung) hat mit 4 Szenarien die höchste Abdeckung, das erstpriorisierte (Analysierbarkeit) nur 3 |

**Positiv:** Trade-off Lesbarkeit vs. Effizienz transparent dokumentiert (04-02-Aufbau.md). Alle 5 Qualitätsziele haben strategische Antworten und messbare Szenarien.

### Strategie ↔ Entscheidungen (S4 ↔ S9)

| ID | Schwere | Beschreibung |
|---|---|---|
| KSE-01 | 🟢 | Immutabilität in 3 S4-Dateien erwähnt, nur einmal mit Querverweis auf ADR 09-02 |
| KSE-02 | 🟢 | XBoard in S4-01 ohne Querverweis auf ADR 09-01 |
| KSE-03 | 🟡 | Programmiersprache Java — grundlegende Entscheidung ohne ADR |
| KSE-04 | 🟡 | Reactive Extensions — architekturprägende Entscheidung ohne ADR |
| KSE-05 | 🟡 | Minimax-Algorithmus — zentrale fachliche Kernentscheidung ohne ADR |
| KSE-06 | 🟢 | Polyglot Opening Book — Format-Wahl ohne ADR (durch Austauschbarkeit gemildert) |

**Positiv:** Die beiden vorhandenen ADRs (09-01, 09-02) sind vollständig konsistent mit S4. Saubere Arbeitsteilung ohne inhaltliche Redundanz.

### Constraint-Compliance (S2 ↔ S4/S8/S9)

| ID | Schwere | Beschreibung |
|---|---|---|
| KRC-01 | 🟡 | Reactive Extensions: externe Bibliothek (RxJava?) oder eigene Observer-Implementierung unklar — steht im Widerspruch zum Designprinzip der Abhängigkeitsminimierung aus S8 |
| KRC-02 | 🟢 | `onError` als englischer Methodenname, Konvention KV3 fordert deutsche Bezeichner |
| KRC-03 | 🟢 | XBoard-Entscheidung wird mit Cross-Platform begründet, Deployment ist nur Windows-spezifisch |

**Positiv:** 13 von 15 Constraints vollständig konform. Keine harten Verletzungen.

### Kontext ↔ Bausteine (S3 ↔ S5)

| ID | Schwere | Beschreibung |
|---|---|---|
| KKB-01 | 🟡 | Endspiele im fachlichen Kontext als Partner definiert, in Bausteinsicht vollständig fehlend |
| KKB-02 | 🟢 | Vier verschiedene Bezeichnungen für Eröffnungs-Schnittstelle (Eröffnungen, Polyglot Opening Book, Eröffnung, Eroeffnungsbibliothek) |
| KKB-03 | 🟢 | Computergegner nicht explizit der Bausteinsicht zugeordnet |
| KKB-04 | 🟡 | Remisangebote im fachlichen Kontext als Datenaustausch beschrieben, im XBoard-Subsystem als nicht unterstütztes Feature gelistet |
| KKB-05 | 🟢 | Bausteinsicht verweist nur auf technischen, nicht auf fachlichen Kontext |

### Sichten-Konsistenz (S5 ↔ S6 ↔ S7)

| ID | Schwere | Beschreibung |
|---|---|---|
| KSV-01 | 🟡 | Subsystem heißt „Eröffnung" (S5), Laufzeitsicht nennt „Eröffnungsbibliothek" (S6) |
| KSV-02 | 🟡 | Einziges Verteilungsszenario ohne Eröffnungsbibliothek, einziges Laufzeitszenario nutzt sie |
| KSV-03 | 🟢 | Ebene-2-Module (Zugsuche, Stellungsbewertung) ohne eigene Laufzeitszenarien |
| KSV-04 | 🟢 | Verteilungssicht mappt keine einzelnen Subsysteme auf Infrastruktur |
| KSV-05 | 🟢 | Nur ein einziges Laufzeitszenario für vier Subsysteme |

### Konzepte ↔ Entscheidungen (S8 ↔ S9)

| ID | Schwere | Beschreibung |
|---|---|---|
| KKE-01 | 🟡 | Entscheidung gegen DI-Framework in Konzept 08-01 versteckt statt als ADR in S9 |
| KKE-02 | 🟡 | Zwei Entscheidungen (kein Logging-Framework, kein Tracing) in Konzept 08-06 eingebettet |
| KKE-03 | 🟡 | Dependency Injection als Muster gewählt ohne ADR (Alternativen: Service Locator, Factory) |
| KKE-04 | 🟢 | Immutabilitäts-Scope im Konzept 08-02 breiter als in ADR 09-02 (nur Stellung vs. ganzes Domänenmodell) |
| KKE-05 | 🟡 | Logging-Konzept enthält tragende Entscheidung, die nicht als eigene ADR existiert |

**Empfehlung:** Zwei neue ADRs anlegen: `09-03-Abhaengigkeitsmanagement.md` (DI-Muster + kein Framework) und `09-04-Logging-Strategie.md` (kein Logging-Framework + kein Tracing).

### Risiken ↔ Qualität (S11 ↔ S1/S10)

| ID | Schwere | Beschreibung |
|---|---|---|
| KRQ-01 | 🟡 | Höchstpriorisiertes Qualitätsziel „Analysierbarkeit" (Prio 1) ohne Risikobetrachtung |
| KRQ-02 | 🟡 | Qualitätsziel „Änderbarkeit" (Prio 2) ohne Risikobetrachtung |
| KRQ-03 | 🟡 | Qualitätsziel „Effizienz" nur unscharf durch R11.3 adressiert, keine explizite Zeitmaßnahme |
| KRQ-04 | 🟢 | R11.2-Maßnahme (Regelvereinfachung) kann im Endspiel zu Endlosschleifen führen |
| KRQ-05 | 🟢 | Robustheits-Szenarien Z01/Z02 implizieren ungenanntes Risiko |
| KRQ-06 | 🔴 | **Systematische Lücke:** Top-2-Qualitätsziele ohne Risiko, niedrigere Ziele gut abgedeckt — inkonsistente Priorisierung |

**Kernerkenntnis:** Die Risikoanalyse konzentriert sich auf technische Machbarkeit (Prio 3–5). Die beiden strategisch wichtigsten Qualitätsziele — Analysierbarkeit und Änderbarkeit — sind in der Risikobetrachtung systematisch unterrepräsentiert.

---

## Statistik

| Kategorie | Anzahl |
|---|---|
| 🔴 Kritische Befunde (Sektionen) | 8 |
| 🟡 Empfehlungen (Sektionen) | ~28 |
| 🟢 Hinweise (Sektionen) | ~18 |
| Konflikte gesamt | 30 |
| davon 🔴 Kritisch | 1 (KRQ-06) |
| davon 🟡 Warnung | 16 |
| davon 🟢 Hinweis | 13 |

---

## Fazit

Die DokChess arc42-Dokumentation ist insgesamt **solide und als Lehrbeispiel gut geeignet**. Die Stärken liegen in der vollständigen Abdeckung aller 12 Sektionen, den vorbildlich strukturierten ADRs (Sektion 9), der konsistenten Bausteinsicht (Sektion 5) und dem durchdachten Qualitätsziel-Framework (Sektionen 1/4/10).

Die **Hauptdefizite** konzentrieren sich auf drei Bereiche:

1. **Sektion 11 (Risiken):** Fehlende Gesamtübersicht, Priorisierung und technische Schulden. Die systematische Lücke bei den Top-Qualitätszielen (Analysierbarkeit, Änderbarkeit) ohne zugehörige Risiken ist der gravierendste übergreifende Befund.

2. **Querverweise und Navigation:** Die Konzepte (S8) verweisen nicht auf die Bausteine (S5), obwohl die Gegenrichtung gut gepflegt ist. Terminologie-Inkonsistenzen (insbesondere „Eröffnung" vs. „Eröffnungsbibliothek") erschweren die Navigation.

3. **Szenario-Abdeckung:** Die Laufzeitsicht (S6) und Verteilungssicht (S7) zeigen jeweils nur ein einziges Szenario. Fehlerszenarien, Initialisierung und alternative Pfade fehlen.

**Prioritäre Maßnahmen (Top 5):**
1. Risikoübersicht mit Priorisierung und technischen Schulden in Sektion 11 anlegen
2. Risiken für Analysierbarkeit und Änderbarkeit ergänzen (KRQ-06)
3. Namenskonflikt „Spielstärke" in S4 korrigieren (KQS-01)
4. Rückverweise von Konzepten (S8) auf Bausteine (S5) ergänzen
5. Mindestens 2 weitere Laufzeitszenarien ergänzen (Eröffnungstreffer, Fehlerfall)
