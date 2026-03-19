# arc42 Sektionsübergreifende Konfliktanalyse

**Projekt:** DokChess
**Datum:** 19.03.2026
**Modell:** Claude Opus 4.6

## Überblick

| Konfliktdimension | Agent | Status | Anzahl Konflikte |
|---|---|---|---|
| Qualitätsstrang (S1 ↔ S4 ↔ S10) | arc42-conflict-quality-strategy | ⚠️ | 5 (2🟡 3🔵) |
| Strategie-Entscheidungen (S4 ↔ S9) | arc42-conflict-strategy-decisions | ⚠️ | 6 (2🟡 4🔵) |
| Constraint-Compliance (S2 ↔ S4/S8/S9) | arc42-conflict-constraints-compliance | ⚠️ | 5 (2🟡 3🔵) |
| Kontext-Bausteine (S3 ↔ S5) | arc42-conflict-context-building-blocks | ⚠️ | 4 (2🟡 2🔵) |
| Sichten-Konsistenz (S5 ↔ S6 ↔ S7) | arc42-conflict-views-consistency | ⚠️ | 6 (3🟡 3🔵) |
| Konzepte-Entscheidungen (S8 ↔ S9) | arc42-conflict-concepts-decisions | ⚠️ | 5 (2🟡 3🔵) |
| Risiken-Qualität (S11 ↔ S1/S10) | arc42-conflict-risks-quality | ⚠️ | 7 (4🟡 3🔵) |

**Gesamt:** 38 Konflikte (davon 0 kritisch, 17 Warnungen, 21 Hinweise)

---

## Detailergebnisse

### 1. Qualitätsstrang (S1 ↔ S4 ↔ S10)

#### Zuordnungsmatrix

| # | Qualitätsziel (S1.2) | Strategieansätze (S4) | Szenarien (S10) | Status |
|---|---|---|---|---|
| 1 | Zugängliches Beispiel (Analysierbarkeit) | arc42-Gliederung, OO-Domänenmodell, deutsche Namen, javadoc (S4.1); Lesbarkeit vor Effizienz (S4.2) | W01, W02, W03 | ✅ Konsistent |
| 2 | Einladende Experimentierplattform (Änderbarkeit) | Java, Schnittstellen, unveränderliche Objekte, DI, hohe Testabdeckung (S4.1); Austauschbarkeit (S4.2, S4.3) | W04, W05 | ✅ Konsistent |
| 3 | Bestehende Frontends nutzen (Interoperabilität) | xboard-Protokoll, portables Java (S4.1); Anbindung (S4.4) | K01, P01 | ✅ Konsistent |
| 4 | **Akzeptable** Spielstärke (**Funktionale Eignung**) | Eröffnungsbibliotheken, Minimax, Stellungsbewertung, Integrationstests (S4.1, S4.3) — aber dort als **„Attraktive Spielstärke (Attraktivität)"** bezeichnet | F01, F02, F03, F04 | ⚠️ Namens- und Klassifikationskonflikt |
| 5 | Schnelles Antworten auf Züge (Effizienz) | Reactive Extensions, Alpha-Beta-Suche, effizientes Domänenmodell, Integrationstests mit Zeitvorgaben (S4.1, S4.3, S4.4) | E01, E02 | ✅ Konsistent |
| — | *(kein Qualitätsziel)* | *(keine Strategie)* | Z01, Z02 | ❌ Verwaiste Szenarien |

#### Konflikte

**[KQS-01] Namens- und Klassifikationsinkonsistenz beim Qualitätsziel Spielstärke** 🟡

- **Betroffene Dateien:** [01-02-Qualitaetsziele.md](src/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md) — „**Akzeptable** Spielstärke (**Funktionale Eignung**)" vs. [04-01-Einstieg.md](src/04-Loesungsstrategie/04-01-Einstieg.md) — „**Attraktive** Spielstärke (**Attraktivität**)"
- **Beschreibung:** Das vierte Qualitätsziel wird in S1.2 und S4.1 unterschiedlich benannt — sowohl im Adjektiv als auch in der ISO-25010-Zuordnung. Die Adjektive implizieren unterschiedliche Ansprüche: „akzeptabel" setzt die Messlatte bewusst niedrig, „attraktiv" deutet auf eine höhere Erwartung hin. Die ISO-Zuordnungen sind fachlich grundverschieden — Funktionale Eignung misst Korrektheit und Vollständigkeit des Verhaltens, Attraktivität misst Nutzerzufriedenheit. Die Szenarien F01–F04 stützen die Formulierung aus S1.2.
- **Empfehlung:** Benennung in S4.1 an S1.2 angleichen: „**Akzeptable Spielstärke (Funktionale Eignung)**".

**[KQS-02] Verwaiste Szenarien Z01 und Z02 ohne zugeordnetes Qualitätsziel** 🟡

- **Betroffene Dateien:** [01-02-Qualitaetsziele.md](src/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md), [10-02-Qualitaetsszenarien.md](src/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md)
- **Beschreibung:** Die Szenarien Z01 (unzulässiger Zug) und Z02 (unzulässige Stellung) adressieren **Zuverlässigkeit**. In S1.2 existiert kein entsprechendes Qualitätsziel, in S4 wird keine Strategie dafür beschrieben.
- **Empfehlung:** Z01/Z02 explizit der „Funktionalen Eignung" zuordnen oder ein Qualitätsziel „Zuverlässigkeit" in S1.2 ergänzen.

**[KQS-03] Leichte Prioritätsumkehr bei Szenarioverteilung** 🔵

- **Beschreibung:** Das Qualitätsziel mit der vierthöchsten Priorität (Funktionale Eignung) hat die meisten Szenarien (4), während das höchstpriorisierte Ziel (Analysierbarkeit) nur 3 hat. Die Umkehr ist mild und nicht zwingend ein Problem.

**[KQS-04] Trade-off Verständlichkeit vs. Effizienz nur in S4 dokumentiert** 🔵

- **Beschreibung:** Der bewusste Trade-off „Lesbarkeit vor Effizienz" erscheint ausschließlich in S4.2. Weder in S1.2 noch in S10.1 wird der Zielkonflikt thematisiert.
- **Empfehlung:** In S1.2 kurzen Hinweis auf bewusste Trade-offs ergänzen.

**[KQS-05] Szenario W02 hat schwaches Akzeptanzkriterium** 🔵

- **Beschreibung:** W02 verwendet „unverzüglich" statt eines konkreten Zeitrahmens. Im Vergleich zu anderen Szenarien schwer falsifizierbar.
- **Empfehlung:** W02 um konkreten Zeitrahmen ergänzen, z. B. „innerhalb von einer Minute".

---

### 2. Strategie-Entscheidungs-Alignment (S4 ↔ S9)

#### Zuordnungsmatrix

| Strategische Festlegung (S4) | Entscheidung (S9) | Status |
|---|---|---|
| SF-01: Java als Sprache | — (Randbedingung S2.1) | ✅ Korrekt verortet |
| SF-02: Dependency Injection | — | 🔲 Keine Entscheidung |
| SF-03: XBoard-Protokoll | ADR-01 (09-01) | ✅ Aligned |
| SF-04: Unveränderliche Objekte | ADR-02 (09-02) | ✅ Aligned |
| SF-05: Minimax + Alpha-Beta | — | 🔲 Keine Entscheidung |
| SF-06: Reactive Extensions | — | 🔲 Keine Entscheidung |
| SF-07: Polyglot Opening Book | — | 🔲 Keine Entscheidung |
| SF-08: Lesbarkeit vor Effizienz | ADR-02 (teilweise) | ⚠️ Teilweise |
| SF-09: Modulzerlegung über Schnittstellen | — | 🔲 Keine Entscheidung |
| SF-10: Materialbasis Stellungsbewertung | — | 🔲 Keine Entscheidung |

#### Konflikte

**[KSE-01] Kernalgorithmus (Minimax/Alpha-Beta) ohne formale Entscheidungsdokumentation** 🟡

- **Betroffene Dateien:** [04-01-Einstieg.md](src/04-Loesungsstrategie/04-01-Einstieg.md), [04-03-Spielstrategie.md](src/04-Loesungsstrategie/04-03-Spielstrategie.md)
- **Beschreibung:** Die zentrale Algorithmenwahl beeinflusst Spielstärke, Effizienz und Engine-Architektur. Es existiert kein ADR, der Alternativen (Monte-Carlo-Tree-Search, neuronale Bewertung, iterative Tiefensuche) und die Begründung dokumentiert.
- **Empfehlung:** ADR für Minimax/Alpha-Beta-Wahl erstellen.

**[KSE-02] Reactive Extensions als Architekturansatz ohne Entscheidungsdokumentation** 🟡

- **Betroffene Dateien:** [04-01-Einstieg.md](src/04-Loesungsstrategie/04-01-Einstieg.md), [04-04-Anbindung.md](src/04-Loesungsstrategie/04-04-Anbindung.md)
- **Beschreibung:** Architektonisch weitreichende Entscheidung über den Kommunikationsstil zwischen Engine und Anbindung. Es fehlt ein ADR mit Alternativenabwägung (Callback, Future/Promise, synchron).
- **Empfehlung:** ADR für den reaktiven Ansatz erstellen.

**[KSE-03] Polyglot Opening Book-Format ohne Entscheidungsdokumentation** 🔵

- **Beschreibung:** Formatwahl ist bewusste Implementierungsentscheidung, nicht als ADR dokumentiert. Geringe Schwere, da Austauschbarkeit über Schnittstellenabstraktion gewährleistet.

**[KSE-04] „Lesbarkeit vor Effizienz" nur teilweise durch ADR abgedeckt** 🔵

- **Beschreibung:** ADR-02 adressiert den Trade-off nur für Stellungsobjekte, nicht für das gesamte Domänenmodell.
- **Empfehlung:** Im ADR-02 oder neuem ADR als übergreifende Designentscheidung dokumentieren.

**[KSE-05] Moderate Redundanz zwischen S4-04 und ADR-01 zur XBoard-Wahl** 🔵

- **Beschreibung:** S4-04 enthält technische Details, die auch im ADR stehen. Wartungsrisiko bei Änderungen.

**[KSE-06] Dependency Injection ohne formale Entscheidungsdokumentation** 🔵

- **Beschreibung:** DI wird als zentrales Architekturprinzip benannt, aber es fehlt ein ADR (ob Framework oder manuell).

---

### 3. Constraint-Compliance (S2 ↔ S4/S8/S9)

#### Constraint-Compliance-Matrix

| Constraint (S2) | S4 | S8 | S9 | Status |
|---|---|---|---|---|
| T1 – Moderate Hardware | ✅ | ✅ | ⚠️ | 🔵 Hinweis |
| T2 – Windows Desktop | ✅ | ✅ | ✅ | ✅ Konform |
| T3 – Java | ✅ | ✅ | ✅ | ✅ Konform |
| T4 – Fremdsoftware frei | ✅ | ✅ | ✅ | ✅ Konform |
| O1–O7 – Organisatorisch | ✅ | ✅ | ⚠️ | ✅/🟡 |
| K1 – arc42 dt. Terminologie | ✅ | ✅ | ❌ | 🟡 Warnung |
| K2 – Sun/Oracle Conventions | ✅ | ✅ | ✅ | ✅ Konform |
| K3 – Deutsch in Doku & Code | ✅ | ✅ | ⚠️ | 🟡 Warnung |
| K4 – Etablierte Schachformate | ✅ | ✅ | ✅ | 🔵 Hinweis |

#### Konflikte

**[KRC-01] Englische ADR-Strukturbegriffe in S9 vs. deutsche arc42-Terminologie** 🟡

- **Betroffene Dateien:** [02-03-Konventionen.md](src/02-Randbedingungen/02-03-Konventionen.md), [09-01-Anbindung.md](src/09-Entscheidungen/09-01-Anbindung.md), [09-02-Stellungsobjekte.md](src/09-Entscheidungen/09-02-Stellungsobjekte.md)
- **Beschreibung:** Constraint K1 fordert deutsche Terminologie nach arc42-Template v6.0. Beide ADRs verwenden durchgängig englische Überschriften (`Context`, `Decision`, `Consequences`).
- **Empfehlung:** ADR-Überschriften auf Deutsch umstellen oder als akzeptierte Ausnahme in K1 vermerken.

**[KRC-02] Fehlende Umlaute in S9 vs. deutsche Sprachkonvention** 🟡

- **Betroffene Dateien:** [09-01-Anbindung.md](src/09-Entscheidungen/09-01-Anbindung.md), [09-02-Stellungsobjekte.md](src/09-Entscheidungen/09-02-Stellungsobjekte.md)
- **Beschreibung:** Beide S9-Dokumente ersetzen systematisch Umlaute durch ASCII-Digraphen (ä→ae, ö→oe, ü→ue). Alle anderen Sektionen verwenden korrekte Umlaute.
- **Empfehlung:** Umlaute in S9-Dokumenten korrigieren.

**[KRC-03] Unveränderliche Stellungsobjekte erzeugen Spannung mit moderater Hardware** 🔵

- **Beschreibung:** ADR-02 führt zu ca. 30% längerer Laufzeit. Kein direkter Verstoß gegen T1, aber Ausreizung des Spielraums. Trade-off ist dokumentiert.

**[KRC-04] Reactive Extensions – Abhängigkeit vs. Minimierungsphilosophie** 🔵

- **Beschreibung:** S4 referenziert Reactive Extensions, S8 vermeidet bewusst externe Bibliotheken (kein log4j, kein DI-Framework). Unklar, ob RxJava oder Java-Bordmittel verwendet werden.
- **Empfehlung:** In S4 oder S8 klarstellen, ob externe Bibliothek oder Java-Bordmittel.

**[KRC-05] Polyglot Opening Book – Offenheit des Formats** 🔵

- **Beschreibung:** Polyglot ist verbreitet und frei dokumentiert, aber kein formal standardisiertes offenes Format. Grauzone gegenüber K4. Durch Schnittstellenabstraktion entschärft.

---

### 4. Kontext-Baustein-Konsistenz (S3 ↔ S5)

#### Schnittstellenvergleich

| Externer Partner | In S3 | In S5 | Status |
|---|---|---|---|
| Menschlicher Gegner | ✅ S3.1 | ✅ Via XBoard-Protokoll | ✅ Konsistent |
| Computergegner | ✅ S3.1 | ⚠️ Implizit via XBoard | 🔵 Implizit |
| XBoard Client | ✅ S3.2 | ✅ Subsystem XBoard-Protokoll | ✅ Konsistent |
| Eröffnungen / Polyglot | ✅ S3.1 + S3.2 | ✅ Subsystem Eröffnung | ✅ Konsistent |
| Endspiele | ✅ S3.1 | ❌ Fehlt vollständig | ⚠️ Lücke |

#### Konflikte

**[KKB-01] Endspiele im fachlichen Kontext vorhanden, in Bausteinsicht fehlend** 🟡

- **Betroffene Dateien:** [03-01-Fachlicher-Kontext.md](src/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md), [05-01-Ebene-1.md](src/05-Bausteinsicht/05-01-Ebene-1.md)
- **Beschreibung:** Der fachliche Kontext führt „Endspiele" als vollwertigen Kommunikationspartner. Der technische Kontext vermerkt, dass die Implementierung entfallen ist. In S5 existiert kein Subsystem oder Erweiterungspunkt.
- **Empfehlung:** Im fachlichen Kontext als nicht realisiert kennzeichnen (analog S3.2).

**[KKB-04] Remisangebote im fachlichen Kontext erwähnt, in S5 als nicht unterstützt** 🟡

- **Betroffene Dateien:** [03-01-Fachlicher-Kontext.md](src/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md), [05-02-XBoard-Protokoll.md](src/05-Bausteinsicht/05-02-XBoard-Protokoll.md)
- **Beschreibung:** Der fachliche Kontext nennt Remisangebote als Beispiel für den Informationsaustausch. In S5.2 sind „Remis-Angebote und Aufgabe" explizit als nicht unterstützt aufgelistet.
- **Empfehlung:** Formulierung in S3.1 einschränken oder Hinweis auf offene Punkte.

**[KKB-02] Computergegner ohne explizite Zuordnung in Bausteinsicht** 🔵

- **Beschreibung:** S3.1 unterscheidet Mensch und Computergegner als separate Akteure. S5.2 spricht nur von „Client" ohne die Möglichkeit eines Computergegners zu erwähnen.

**[KKB-03] Terminologie-Inkonsistenz bei Eröffnungsbibliothek** 🔵

- **Beschreibung:** Wechselnde Bezeichnungen: „Eröffnungen" (S3.1), „Polyglot Opening Book" (S3.2), „Eröffnung" (S5.1), „Eröffnungsbibliothek" (S5.5, Interface).

---

### 5. Sichten-Konsistenz (S5 ↔ S6 ↔ S7)

#### Baustein-Kreuzreferenz

| Baustein | S5 | S6 | S7 | Status |
|---|---|---|---|---|
| XBoard-Protokoll | ✅ | ✅ | ✅ Implizit in JAR | ✅ |
| Spielregeln | ✅ | ✅ | ✅ Implizit in JAR | ✅ |
| Engine | ✅ | ✅ | ✅ Implizit in JAR | ✅ |
| Eröffnung | ✅ | ⚠️ Als „Eröffnungsbibliothek" | ⚠️ Explizit ausgeschlossen | ⚠️ |
| Zugsuche (Ebene 2) | ✅ | ⚠️ Verhalten beschrieben, nicht benannt | ❌ | 🔵 |
| Stellungsbewertung (Ebene 2) | ✅ | ⚠️ Verhalten beschrieben, nicht benannt | ❌ | 🔵 |

#### Konflikte

**[KSV-01] Namensinkonsistenz „Eröffnung" vs. „Eröffnungsbibliothek"** 🟡

- **Betroffene Dateien:** [05-01-Ebene-1.md](src/05-Bausteinsicht/05-01-Ebene-1.md) — „Eröffnung", [06-01-Zugermittlung.md](src/06-Laufzeitsicht/06-01-Zugermittlung.md) — „Eröffnungsbibliothek"
- **Empfehlung:** Einheitliche Benennung in S6 verwenden.

**[KSV-02] Fehlendes Deployment-Szenario mit Eröffnungsbibliothek** 🟡

- **Betroffene Dateien:** [05-05-Eroeffnung.md](src/05-Bausteinsicht/05-05-Eroeffnung.md), [07-01-Infrastruktur-Windows.md](src/07-Verteilungssicht/07-01-Infrastruktur-Windows.md)
- **Beschreibung:** S5 beschreibt Eröffnungs-Subsystem ausführlich, S6 zeigt Szenario mit Eröffnungsabfrage, S7 zeigt nur Deployment **ohne** Eröffnungsbibliothek.
- **Empfehlung:** Zweites Deployment-Szenario mit Eröffnungsbibliothek ergänzen.

**[KSV-05] Nur ein einziges Laufzeitszenario dokumentiert** 🟡

- **Betroffene Dateien:** [06-01-Zugermittlung.md](src/06-Laufzeitsicht/06-01-Zugermittlung.md)
- **Beschreibung:** Mehrere architekturrelevante Abläufe (Partie-Start, Matt/Patt-Erkennung, Eröffnungstreffer, Engine schließen) fehlen als Szenarien.
- **Empfehlung:** Mindestens ein weiteres Szenario ergänzen (z. B. Eröffnungstreffer oder Spielende durch Matt).

**[KSV-03] Ebene-2-Bausteine nicht in Laufzeitsicht aufgelöst** 🔵

- **Beschreibung:** S6 beschreibt sich als Subsystem-Ebene, bricht aber die Engine in ihre internen Bestandteile auf, ohne Ebene-2-Terminologie zu verwenden.

**[KSV-04] Verteilungssicht ohne explizites Baustein-zu-Artefakt-Mapping** 🔵

- **Beschreibung:** S7 verweist nur pauschal auf „sämtliche Module" im JAR. Kein Mapping zu Subsystemen oder Java-Paketen.

**[KSV-06] Fehlende Deployment-Szenarien für andere Plattformen** 🔵

- **Beschreibung:** Nur Windows-Deployment dokumentiert, obwohl DokChess plattformunabhängig ist.

---

### 6. Konzept-Entscheidungs-Abgrenzung (S8 ↔ S9)

#### Zuordnungsanalyse

| Element | Sektion | Korrekt? |
|---|---|---|
| Abhängigkeiten (DI-Pattern) | S8 ✅ | ⚠️ Enthält eingebettete Entscheidung „kein DI-Framework" |
| Domänenmodell | S8 ✅ | ✅ Verweist sauber auf ADR-02 |
| Benutzungsoberfläche | S8 ✅ | ✅ Verweist sauber auf ADR-01 |
| Validierung | S8 ✅ | ✅ Reines Konzept |
| Fehlerbehandlung | S8 ✅ | ⚠️ Enthält implizite Entscheidung „nur Runtime Exceptions" |
| Logging | S8 ✅ | ⚠️ Enthält eingebettete Entscheidungen „kein Framework", „kein Tracing" |
| Testbarkeit | S8 ✅ | ✅ Reines Konzept |
| Frontend-Anbindung (XBoard) | S9 ✅ | ✅ Sauberes ADR |
| Stellungsobjekte (immutable) | S9 ✅ | ✅ Sauberes ADR |

#### Konflikte

**[KKE-01] Entscheidung „Kein DI-Framework" in Konzept-Sektion eingebettet** 🟡

- **Betroffene Dateien:** [08-01-Abhaengigkeiten.md](src/08-Konzepte/08-01-Abhaengigkeiten.md)
- **Beschreibung:** „DokChess verzichtet auf die Verwendung eines speziellen DI Frameworks" ist eine bewusste Architekturentscheidung mit klar existierenden Alternativen (Spring, CDI werden sogar genannt).
- **Empfehlung:** Neue Entscheidung `09-03-DI-Framework.md` erstellen.

**[KKE-02] Entscheidung „Kein Logging-Framework / Kein Tracing" in Konzept-Sektion eingebettet** 🟡

- **Betroffene Dateien:** [08-06-Logging.md](src/08-Konzepte/08-06-Logging.md)
- **Beschreibung:** Enthält zwei eingebettete Entscheidungen gegen log4j und eigenes Tracing. Hat direkte Auswirkungen auf Analysierbarkeit (Qualitätsziel Nr. 1).
- **Empfehlung:** Neue Entscheidung `09-04-Logging-Strategie.md` erstellen.

**[KKE-03] „Nur Runtime Exceptions" ohne formale Entscheidungsgrundlage** 🔵

- **Beschreibung:** Das gesamte Fehlerhandling basiert auf dieser Festlegung. In Java verbreitet, daher geringe Schwere.

**[KKE-04] DI als Architekturansatz ohne eigenständige Entscheidung** 🔵

- **Beschreibung:** Die Grundsatzentscheidung *für* DI (statt Service Locator, Factory etc.) wird nirgends formal dokumentiert. Durch S4 implizit abgedeckt.

**[KKE-05] JUnit 4 ohne Entscheidungsgrundlage** 🔵

- **Beschreibung:** Konkrete Technologiefestlegung, aber trivial und nicht architekturrelevant genug für einen ADR.

#### Positive Befunde

- Querverweise S8 → S9 funktionieren sauber (08-02 → 09-02, 08-03 → 09-01)
- Keine inhaltlichen Widersprüche (K1) zwischen Konzepten und Entscheidungen
- S9 enthält keine Konzepte — saubere Trennung in dieser Richtung

---

### 7. Risiko-Qualitäts-Abdeckung (S11 ↔ S1/S10)

#### Zuordnungsmatrix

| # | Qualitätsziel (S1.2) | Priorität | Bedrohende Risiken | Status |
|---|---|---|---|---|
| Q1 | Analysierbarkeit | 1 (höchste) | — | ⚠️ Kein Risiko |
| Q2 | Änderbarkeit | 2 | — | ⚠️ Kein Risiko |
| Q3 | Interoperabilität | 3 | R11.1 (Frontend) | ✅ Abgedeckt |
| Q4 | Funktionale Eignung | 4 | R11.3 (Spielstärke), R11.2 (Aufwand) | ✅ Abgedeckt |
| Q5 | Effizienz | 5 | R11.3 (erwähnt) | ⚠️ Teilweise |

#### Konflikte

**[KRQ-01] Analysierbarkeit ohne Risikobetrachtung** 🟡

- **Beschreibung:** Das **höchstpriorisierte** Qualitätsziel hat kein einziges zugeordnetes Risiko. Die Komplexität der Schachalgorithmen könnte die Verständlichkeit gefährden.
- **Empfehlung:** Risiko ergänzen (z. B. „Domänenkomplexität gefährdet Analysierbarkeit").

**[KRQ-02] Änderbarkeit ohne Risikobetrachtung** 🟡

- **Beschreibung:** Zweitwichtigstes Qualitätsziel ohne Risiko. R11.3 erkennt das Spannungsfeld Einfachheit vs. Leistung an, ohne daraus ein explizites Risiko abzuleiten.
- **Empfehlung:** Spannungsfeld als Risiko formulieren.

**[KRQ-03] Effizienz-Risiko ohne spezifische Maßnahme** 🟡

- **Betroffene Dateien:** [11-03-Spielstaerke.md](src/11-Risiken/11-03-Spielstaerke.md)
- **Beschreibung:** R11.3 benennt „zu lange Wartezeiten" als mögliche Manifestation. Die Maßnahmen fokussieren nur auf Spielstärke, nicht auf die konkreten Effizienz-Szenarien E01/E02 (≤ 5 bzw. 10 Sekunden).
- **Empfehlung:** Spezifische Effizienz-Maßnahme ergänzen (z. B. zeitlich begrenzte Zugsuche, Performance-Benchmarks).

**[KRQ-07] Priorisierungsinkonsistenz: Niedrigprioritäre Ziele besser abgesichert** 🟡

- **Beschreibung:** Qualitätsziele mit Priorität 3–5 (Interoperabilität, Spielstärke, Effizienz) haben Risikobetrachtungen. Die höchstpriorisierten Ziele (Analysierbarkeit, Änderbarkeit) haben keine einzige. Dies invertiert faktisch die Prioritäten.
- **Empfehlung:** Für Analysierbarkeit und Änderbarkeit mindestens je ein Risiko dokumentieren oder explizit begründen, warum diese als risikofrei gelten.

**[KRQ-04] Aufwandrisiko-Maßnahme bedroht implizit Funktionale Eignung** 🔵

- **Beschreibung:** R11.2 deprioritisiert Eröffnungsbibliotheken. Diese bieten aber Spielstärke-Vorteil und schnelle Antwortzeiten. Folgenabschätzung fehlt.

**[KRQ-05] Zuverlässigkeits-Szenarien Z01/Z02 ohne Risikoabdeckung** 🔵

- **Beschreibung:** Szenarien für ungültige Eingaben implizieren Zuverlässigkeitsrisiko, das in S11 nicht dokumentiert ist.

**[KRQ-06] Protokoll-Erweiterbarkeit als implizites Risiko** 🔵

- **Beschreibung:** Szenario P01 fordert Erweiterbarkeit für neue Protokolle. R11.1 adressiert nur bestehende Protokolle.

---

## Kritische Konflikte (Sofortmaßnahmen erforderlich)

Keine kritischen Konflikte (🔴) gefunden. Die Dokumentation weist keine fundamentalen Widersprüche auf.

---

## Konfliktkarte

| Sektion | Involviert in Konflikten |
|---|---|
| S1 — Einführung und Ziele | 7 (KQS-01, KQS-02, KQS-03, KRQ-01, KRQ-02, KRQ-03, KRQ-07) |
| S2 — Randbedingungen | 5 (KRC-01, KRC-02, KRC-03, KRC-04, KRC-05) |
| S3 — Kontextabgrenzung | 4 (KKB-01, KKB-02, KKB-03, KKB-04) |
| S4 — Lösungsstrategie | 11 (KQS-01, KQS-04, KSE-01..06, KRC-04) |
| S5 — Bausteinsicht | 8 (KKB-01..04, KSV-01..04) |
| S6 — Laufzeitsicht | 4 (KSV-01, KSV-03, KSV-05, KSV-06) |
| S7 — Verteilungssicht | 4 (KSV-02, KSV-04, KSV-05, KSV-06) |
| S8 — Konzepte | 4 (KKE-01, KKE-02, KKE-03, KRC-04) |
| S9 — Entscheidungen | 10 (KSE-01..06, KRC-01, KRC-02, KKE-01, KKE-02) |
| S10 — Qualitätsanforderungen | 5 (KQS-02, KQS-03, KQS-05, KRQ-03, KRQ-05) |
| S11 — Risiken | 7 (KRQ-01..07) |
| S12 — Glossar | 0 |

---

## Empfohlene Reihenfolge der Behebung

1. **S9 — Formale Bereinigung** (KRC-01, KRC-02): Umlaute und deutsche Überschriften in den ADRs — geringster Aufwand, höchste Sichtbarkeit
2. **S1/S4 — Namensangleichung Spielstärke** (KQS-01): „Attraktive Spielstärke (Attraktivität)" → „Akzeptable Spielstärke (Funktionale Eignung)" in S4.1
3. **S3 — Kontextbereinigung** (KKB-01, KKB-04): Endspiele und Remisangebote als nicht realisiert kennzeichnen
4. **S11 — Risikoabdeckung ergänzen** (KRQ-01, KRQ-02, KRQ-07): Risiken für Analysierbarkeit und Änderbarkeit aufnehmen
5. **S9 — Fehlende ADRs erstellen** (KSE-01, KSE-02, KKE-01, KKE-02): Minimax/Alpha-Beta, Reactive Extensions, DI-Framework-Verzicht, Logging-Strategie
6. **S6/S7 — Szenarien ergänzen** (KSV-02, KSV-05): Weiteres Laufzeitszenario, Deployment mit Eröffnungsbibliothek
7. **S1/S10 — Verwaiste Szenarien zuordnen** (KQS-02): Z01/Z02 einem Qualitätsziel zuordnen
8. **Hinweise adressieren** (alle 🔵): Bei Gelegenheit, kein dringender Handlungsbedarf