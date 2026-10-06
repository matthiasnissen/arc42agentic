# arc42 Dokumentations-Review

**Dokumentation:** [arc-doc/](arc-doc/) (DokChess, Layout: Multi-Folder, Sektionen 0–12)
**Review-Modus:** Vollständiges Review
**Analyse-Modus:** GRAPH-MODUS
**Wissensgraph:** [.arc42-graph_demo_results/FullReviewRunOpus55/arc-doc.graphml](.arc42-graph_demo_results/FullReviewRunOpus55/arc-doc.graphml) mit Manifest [.arc42-graph_demo_results/FullReviewRunOpus55/arc-doc.manifest.json](.arc42-graph_demo_results/FullReviewRunOpus55/arc-doc.manifest.json). Der Graph wurde neu aufgebaut, weil vorher kein Graph existierte. Er umfasst 164 Knoten und 614 Kanten, einschließlich 13 Sektions- und 7 Konfliktdimensions-Communities. `build_graph.py` lief mit 0 Fehlern, 0 Warnungen und 12 Hinweisen durch. Die Hinweise betreffen Knoten ohne semantische Kante, z. B. Stakeholder.
**Diagrammauswertung beim Graphaufbau:** Qualitätsbaum (10.1), Kontextdiagramme (3.1/3.2), Bausteinsicht Ebene 1 und 2 (5.1/5.6), Sequenzdiagramm (6.1), Verteilungsdiagramm (7.1), Überblicksbild (4.1)

## Gesamtübersicht

| Sektion | Status | Befunde |
|---------|--------|---------|
| 1. Einführung und Ziele | 🟡 | Mehrere Punkte sind unklar: Die FIDE-Anforderung hat keine Referenz, und das Spielstärkeziel ist nicht operationalisiert. In der Stakeholderliste fehlen Spieler und Vorführbetrieb, außerdem ist die Entscheidungszuständigkeit offen. |
| 2. Randbedingungen | 🟡 | Hardware- und Java-/Plattform-Baseline sind unbestimmt, Lizenzfolgen unklar. Historische und geltende Vorgaben sind vermischt, Kodierrichtlinien und Formatstandards nicht konkretisiert. |
| 3. Kontextabgrenzung | 🔴 | Remisangebote und „jedes XBoard-Frontend“ werden zugesichert, obwohl 5.2 sie ausschließt. Datenflüsse, Computergegner und der Status der Endspielanbindung sind unklar. |
| 4. Lösungsstrategie | 🟡 | Das Spielstärkeziel ist abweichend benannt („Attraktive Spielstärke (Attraktivität)“). Der Zielkonflikt zwischen Effizienz und Verständlichkeit ist im Überblick nicht eingeordnet, und eine organisatorische Strategie fehlt. |
| 5. Bausteinsicht | 🟡 | Der Protokollumfang widerspricht 3.1. Die Zerlegungsbegründung fehlt auf Ebene 1 und 2, und der Übergang von Engine zu Suche ist implizit. |
| 6. Laufzeitsicht | 🟡 | Es gibt nur das Gutfall-Szenario. Abbruch-, Fehler- und Bibliothekstreffer-Pfade fehlen, und Zugsuche bzw. Stellungsbewertung bleiben implizit. |
| 7. Verteilungssicht | 🟡 | Die Begründung fehlt, Umgebungen und Hardwareprofil sind nicht beschrieben. Die Startvoraussetzungen (`javaw.exe`, relativer Pfad) sind problematisch, und die Variante mit Buchdatei fehlt. |
| 8. Querschnittliche Konzepte | 🟡 | Regeln für Nebenläufigkeit und Fortsetzung nach Fehlern fehlen. Der Protokollkanal ist nicht gegen Diagnoseausgaben geschützt, und asynchrone Testverträge sind nicht beschrieben. |
| 9. Architekturentscheidungen | 🟡 | ADR 9.1 stützt sich auf den Stand 2011, ist aber 2026 akzeptiert. Der 30-%-Messwert in ADR 9.2 ist nicht reproduzierbar, und Zukunftsfolge und Ist-Stand der Parallelisierung sind vermischt. |
| 10. Qualitätsanforderungen | 🔴 | Die Geltungsbereiche von E01 und E02 sind widersprüchlich bzw. unklar, und die Messbedingungen fehlen. Das Spielstärkeziel ist nur durch taktische Einzelszenarien belegt. Mehreren Szenarien fehlen messbare Kriterien. |
| 11. Risiken und technische Schulden | 🔴 | Das Korrektheitsrisiko durch fehlende Validierung ist nicht erfasst, und der Verzicht auf die Remisregeln wird als „keine Konsequenz bzgl. Korrektheit“ verharmlost. Bewertung und aktueller Status fehlen. |
| 12. Glossar | 🟡 | Homonyme (Engine, Eröffnung, XBoard) sind nicht aufgelöst. Stellung, Zug, Bitboard, Material und UCI fehlen. Mehrere Regeldefinitionen sind ungenau, dazu kommen redaktionelle Fehler. |

## Sektions-Reviews

### Sektion 1: Einführung und Ziele

*Prüfumfang: 17 Knoten der Community `c-s01`, dazu Szenario- und Referenzkanten. Alle drei Unterabschnitte sind vorhanden. Alle fünf Qualitätsziele haben explizit zugeordnete Szenarien, und der Verweis auf Sektion 10 ist gültig.*

#### [S01-01] FIDE-Anforderung ohne verbindliche Referenz

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/01-Einfuehrung-und-Ziele/01-01-Aufgabenstellung.md](arc-doc/01-Einfuehrung-und-Ziele/01-01-Aufgabenstellung.md#L14)
**Kriterium:** 1.1 – Referenzierung und eindeutige Beschreibung wesentlicher Anforderungen
**Zitat:** „Vollständige Implementierung der FIDE-Schachregeln“

**Befund:** Es wird weder eine Regelfassung noch ein Anforderungsdokument referenziert. „Vollständig“ lässt offen, welche spielbezogenen Regeln die Engine verantwortet und welche turnierbezogenen Regeln beim Frontend liegen.

**Änderungsvorschlag:** Nach der Feature-Liste ergänzen:
> **Anforderungsreferenz und offene Abgrenzung:** Maßgebliche externe Referenz sind die FIDE Laws of Chess im FIDE Handbook (https://handbook.fide.com/). Die für DokChess verbindliche Regelfassung und die Abgrenzung zwischen Engine, Frontend und Turnierorganisation sind noch festzulegen. Bis dahin ist die Aussage „vollständige Implementierung“ als Ziel, nicht als nachgewiesene Konformitätszusage zu verstehen.

#### [S01-02] Allgemeine Spielstärke nicht ausreichend operationalisiert

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md](arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md#L12)
**Kriterium:** 1.2 – Konkrete, überprüfbare Qualitätsziele
**Zitat:** „DokChess spielt stark genug, um schwache Gegner sicher zu schlagen und Gelegenheitsspieler zumindest zu fordern.“

**Befund:** F02–F04 prüfen taktische Fähigkeiten, aber keine Gewinnquote gegen definierte Gegner. Die Begriffe „schwache Gegner“, „sicher“ und „fordern“ bleiben unbestimmt.

**Änderungsvorschlag:** Die Erläuterung auf den vorhandenen Szenarioumfang begrenzen. Alternativ wird ein Partieszenario ergänzt, siehe S10-02 und KQS-03.
> DokChess zeigt grundlegende taktische Fähigkeiten: Es schlägt eine ohne taktische Kompensation eingestellte Figur (F02), nutzt eine gewinnbringende Springergabel (F03) und findet ein Matt in zwei Zügen (F04). Diese Fähigkeiten werden anhand der Qualitätsszenarien in Abschnitt 10.2 bewertet; eine allgemeine Gewinnquote gegen menschliche Gegner wird damit nicht zugesichert.

#### [S01-03] Spieler und Demonstrationsbetrieb fehlen als Stakeholder

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/01-Einfuehrung-und-Ziele/01-03-Stakeholder.md](arc-doc/01-Einfuehrung-und-Ziele/01-03-Stakeholder.md#L7)
**Kriterium:** 1.3 – Abdeckung relevanter Nutzer- und Betriebsrollen
**Zitat:** „Die folgende Tabelle stellt die Stakeholder von DokChess und ihre jeweilige Intention dar.“

**Befund:** Menschliche Spieler und Personen, die die Engine für Seminare installieren und betreiben, fehlen. Beide Nutzungen sind in 3.1 bzw. 7.1 dokumentiert.

**Änderungsvorschlag:** Zwei Tabellenzeilen ergänzen:
> | Gelegenheitsspielerinnen und -spieler | Erwarten regelkonforme Partien, nachvollziehbare Fehlermeldungen bei unzulässigen Eingaben und zeitnahe Antworten über ein unterstütztes Schach-Frontend. |
> | Vorführende und Verantwortliche für den Demonstrationsbetrieb | Erwarten eine reproduzierbare Installation und Frontend-Konfiguration, einen verlässlichen Start sowie verständliche Hinweise zur Fehlerdiagnose auf dem Vorführ-Notebook. Diese Rolle kann mit der Autoren- oder Schulungsrolle zusammenfallen. |

#### [S01-04] Organisationserwartungen und Entscheidungszuständigkeit bleiben offen

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/01-Einfuehrung-und-Ziele/01-03-Stakeholder.md](arc-doc/01-Einfuehrung-und-Ziele/01-03-Stakeholder.md#L12)
**Kriterium:** 1.3 – Rollenbeschreibung, Architekturerwartungen und Entscheidungsverantwortung
**Zitat:** „Schulungsunternehmen, Arbeitgeber von Stefan Zörner zum Zeitpunkt der Konzeption von DokChess“

**Befund:** Der Eintrag beschreibt den Bezug von oose, aber keine Erwartungen an Architektur oder Dokumentation. Offen bleibt auch, wer Architekturentscheidungen verantwortet.

**Änderungsvorschlag:**
> | oose Innovative Informatik | Schulungsunternehmen und Arbeitgeber von Stefan Zörner zum Zeitpunkt der Konzeption. Erwartet ein didaktisch geeignetes, verständlich dokumentiertes und in Seminaren zuverlässig demonstrierbares Architekturbeispiel. |
>
> **Entscheidungsverantwortung:** Die Zuständigkeit für Architekturentscheidungen und die Freigabe von Änderungen ist noch zu benennen.

---

### Sektion 2: Randbedingungen

*Prüfumfang: 15 Randbedingungen der Community `c-s02`. Abschnitte, Erklärungstabellen und die drei Kategorien sind vorhanden.*

#### [S02-01] Hardwaregrenze bleibt unbestimmt

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/02-Randbedingungen/02-01-Technisch.md](arc-doc/02-Randbedingungen/02-01-Technisch.md#L7)
**Kriterium:** Technische Einschränkungen und Konsequenzen eindeutig dokumentieren
**Zitat:** „Betrieb der Lösung auf einem marktüblichen Standard-Notebook“

**Befund:** Ohne Referenzprofil bleibt offen, welche Ressourcen die Architektur voraussetzen darf. Siehe auch KRC-01 und S07-03.

**Änderungsvorschlag:**
> Für Vorführungen ist ein Standard-Notebook ohne zusätzliche Spezialhardware vorgesehen. Das Referenzprofil mit Prozessor, Arbeitsspeicher und zulässigem Ressourcenbedarf ist noch festzulegen. Bis dahin ist „moderate Hardwareausstattung“ keine quantitativ überprüfbare Grenze.

#### [S02-02] Verbindliche Plattform- und Java-Baseline fehlt

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/02-Randbedingungen/02-01-Technisch.md](arc-doc/02-Randbedingungen/02-01-Technisch.md#L8)
**Kriterium:** Plattformvorgaben und architektonische Freiheitsgrade klar abgrenzen
**Zitat:** „zum Zeitpunkt der Konzeption“; „später Java SE 7 und Java SE 11“; „soll auch auf neueren Java-Versionen […] laufen“

**Befund:** Die historischen Entwicklungsstände ordnen den Releases keine unterstützten Windows- und Java-Versionen zu. Die Zukunftskompatibilität bleibt ein unbestimmter Anspruch.

**Änderungsvorschlag:**
> Windows-Unterstützung ist verpflichtend; Linux und macOS sind optional. Je DokChess-Release werden Windows-Version, Build-JDK und minimale Java-Laufzeit in einer Kompatibilitätstabelle dokumentiert. Neuere Java-Versionen gelten erst nach erfolgreicher Kompatibilitätsprüfung als unterstützt.

#### [S02-03] Kostenfreiheit und Lizenzfolgen nicht abgegrenzt

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/02-Randbedingungen/02-01-Technisch.md](arc-doc/02-Randbedingungen/02-01-Technisch.md#L10), [arc-doc/02-Randbedingungen/02-02-Organisatorisch.md](arc-doc/02-Randbedingungen/02-02-Organisatorisch.md#L13)
**Kriterium:** Verbindlichkeit und Konsequenzen technischer und rechtlicher Randbedingungen
**Zitat:** „sollte diese idealerweise frei verfügbar und kostenlos sein“; „Die Quelltexte der Lösung oder zumindest Teile […] GPLv3“

**Befund:** Die Kostenfreiheit ist als Präferenz formuliert, steht aber unter den Randbedingungen. Offen bleiben der Veröffentlichungsumfang und die Lizenzverträglichkeit eingebundener Fremdsoftware.

**Änderungsvorschlag:**
> Kostenlos verfügbare Fremdsoftware wird bevorzugt; Kostenfreiheit ist keine Muss-Vorgabe. Für jede eingebundene oder mitgelieferte Komponente sind Nutzungs- und Weitergaberechte sowie die Verträglichkeit mit der GPLv3-Veröffentlichung zu prüfen. Separat betriebene Frontends sind gesondert zu betrachten. Welche Quelltextteile unter GPLv3 veröffentlicht werden, ist ausdrücklich festzulegen.

#### [S02-04] Historie und geltende organisatorische Vorgaben vermischt

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/02-Randbedingungen/02-02-Organisatorisch.md](arc-doc/02-Randbedingungen/02-02-Organisatorisch.md#L8)
**Kriterium:** Geltungsbereich organisatorischer Einschränkungen kenntlich machen
**Zitat:** „Fertigstellung Version 1.0: Februar 2012“; „Zu Beginn (Version 1.0) Subversion bei SourceForge, später Git bei GitHub“

**Befund:** Die Tabelle trennt historische Rahmenbedingungen nicht von weiterhin bindenden Vorgaben. Außerdem enthält sie den Tippfehler „Schulungsunternehmenin“.

**Änderungsvorschlag:**
> Die Termine von Dezember 2010 bis Februar 2012 gelten ausschließlich für die Entwicklung von Version 1.0 (Abendvortrag beim Schulungsunternehmen in Hamburg). Subversion bei SourceForge beschreibt den ursprünglichen, Git bei GitHub den aktuellen Stand. Für nachfolgende Releases sind verbindliche Termine und der geltende Werkzeugstand separat auszuweisen.

#### [S02-05] Technische Build-Vorgabe unter Organisation eingeordnet

**Schwere:** 🟢 Hinweis
**Datei:** [arc-doc/02-Randbedingungen/02-02-Organisatorisch.md](arc-doc/02-Randbedingungen/02-02-Organisatorisch.md#L10)
**Kriterium:** Kategorien von Randbedingungen klar differenzieren
**Zitat:** „Die Software muss jedoch auch, allein mit Gradle, also ohne IDE baubar sein.“

**Befund:** Die Werkzeugzeile vermischt organisatorische Arbeitsmittel mit einer technischen Build-Einschränkung. Siehe auch KRC-02.

**Änderungsvorschlag:** In 2.1 ergänzen:
> **IDE-unabhängiger Build:** Die Software muss allein mit Gradle baubar sein. IDE-spezifische Einstellungen dürfen keine Voraussetzung für den Build sein.

#### [S02-06] Kodierrichtlinien nicht reproduzierbar konkretisiert

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/02-Randbedingungen/02-03-Konventionen.md](arc-doc/02-Randbedingungen/02-03-Konventionen.md#L8)
**Kriterium:** Programmier- und Namenskonventionen eindeutig dokumentieren
**Zitat:** „Java Coding Conventions von Sun/Oracle, geprüft mit Hilfe von CheckStyle“

**Befund:** Regelstand, Checkstyle-Konfiguration und projektspezifische Ausnahmen fehlen, insbesondere die Ausnahme für deutsche Bezeichner.

**Änderungsvorschlag:**
> Grundlage sind die Java Coding Conventions von Sun/Oracle. Der verbindliche Regelstand wird durch eine versionierte Checkstyle-Konfiguration festgelegt. Regelwerksreferenz, Checkstyle-Version und Konfigurationspfad sind noch zu dokumentieren. Projektspezifische Ausnahmen, insbesondere für deutsche Bezeichner, werden ausdrücklich in dieser Konfiguration festgehalten.

#### [S02-07] Austauschformate ohne konkrete Standardzuordnung

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/02-Randbedingungen/02-03-Konventionen.md](arc-doc/02-Randbedingungen/02-03-Konventionen.md#L10)
**Kriterium:** Konventionen und verbleibende Freiheitsgrade nachvollziehbar festlegen
**Zitat:** „Themen: Züge, Stellungen, Partien, Eröffnungen, … Keinesfalls sind eigene Formate zu entwickeln.“

**Befund:** Das Verbot eigener Formate ist eindeutig. Welche Standards zulässig sind (z. B. XBoard, Polyglot, FEN) und wofür sie gelten, ist dagegen nicht festgelegt.

**Änderungsvorschlag:**
> | Thema | Standard | Verwendung in DokChess |
> | --- | --- | --- |
> | Kommunikation/Züge | XBoard-Protokoll (Koordinatennotation, z. B. e2e4) | Frontend-Anbindung (5.2) |
> | Stellungen | Forsyth-Edwards-Notation (FEN) | Tests, Stellungs-Konstruktor (8.7) |
> | Eröffnungen | Polyglot Opening Book | Eröffnungsbibliothek (5.5) |
>
> Eigene Austauschformate sind ausgeschlossen; interne Datenstrukturen sind davon nicht betroffen.

---

### Sektion 3: Kontextabgrenzung

*Prüfumfang: 6 externe Partner der Community `c-s03`, `communicates_with`-Kanten und Kontextdiagramme. Die Black-Box-Abgrenzung sowie die XBoard- und Polyglot-Anbindung sind grundsätzlich konsistent.*

#### [S03-01] Nicht unterstützte Kommunikation wird zugesichert

**Schwere:** 🔴 Kritisch
**Datei:** [arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md#L9), [arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md](arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md#L9)
**Kriterium:** Konsistenz der externen Schnittstellen mit der Bausteinsicht
**Zitat:** „beispielsweise über ihre Züge, oder über Remisangebote“; „jedes grafische Frontend […] welches das sogenannte XBoard-Protokoll unterstützt“

**Befund:** Sektion 3 unterscheidet nicht zwischen fachlich gewünschtem und implementiertem Austausch. [5.2](arc-doc/05-Bausteinsicht/05-02-XBoard-Protokoll.md#L35) schließt Remisangebote, gegnerische Aufgabe, Zeitkontrolle, Permanent Brain und Schachvarianten ausdrücklich aus. Damit ist die uneingeschränkte Frontend-Zusage nicht gedeckt. Siehe auch S05-01 und KKB-01.

**Änderungsvorschlag:**
> Fachlich tauschen die Gegner insbesondere Züge und gegebenenfalls Remisangebote aus. Die aktuelle Implementierung unterstützt jedoch keine Remisangebote, keine Aufgabe der Gegenseite, keine Zeitkontrolle, kein Permanent Brain und keine Schachvarianten (siehe Abschnitt 5.2). Ein XBoard-Frontend ist verwendbar, soweit es mit diesem eingeschränkten Funktionsumfang zusammenarbeitet.

#### [S03-02] Fachliche Datenflüsse bleiben unbestimmt

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md#L5)
**Kriterium:** Kommunikationspartner mit gerichteten fachlichen Ein- und Ausgaben beschreiben
**Zitat:** „Die Anforderungen bezüglich des Informationsaustausches sind die selben.“

**Befund:** Die Verbindungen im Diagramm sind unbeschriftet. Flussrichtungen und Ein-/Ausgaben werden nicht systematisch angegeben.

**Änderungsvorschlag:**
> Fachliche Datenflüsse: Gegner → DokChess: gegnerische Züge; DokChess → Gegner: eigene Züge. Dies gilt alternativ für menschliche und computergesteuerte Gegner. Beim optionalen Eröffnungszugriff verwendet DokChess die aktuelle Stellung als Suchkriterium und erhält einen bekannten Zug oder keinen passenden Eintrag. Die Verbindungen im Kontextdiagramm sind entsprechend mit Richtung und Dateninhalt zu beschriften.

#### [S03-03] Technische Zuordnung der Gegner ist unvollständig

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md](arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md#L9)
**Kriterium:** Fachliche Partner technischen Kanälen zuordnen
**Zitat:** „Die ‘Anbindung’ menschlicher Spieler erfolgt über ein grafisches Frontend“

**Befund:** Computergegner und die direkte Kommandozeilenbedienung fehlen, obwohl [8.3](arc-doc/08-Konzepte/08-03-Benutzungsoberflaeche.md#L7) beide beschreibt. Auch der Transport über stdin/stdout wird nicht genannt. Siehe auch KKB-03.

**Änderungsvorschlag:**
> Menschliche Gegner kommunizieren typischerweise über ein externes grafisches Frontend mit DokChess. Alternativ können sie XBoard-Kommandos direkt in einer Kommandozeile eingeben. Auch Partien gegen andere Engines werden über das Frontend vermittelt; eine direkte Engine-zu-Engine-Schnittstelle ist nicht vorgesehen. DokChess empfängt zeilenweise XBoard-Kommandos über stdin und sendet Antworten über stdout. Diesen Systemzugang realisiert das Subsystem XBoard-Protokoll (Abschnitt 5.2).

#### [S03-04] Endspielanbindung erscheint als bestehende Option

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md#L28)
**Kriterium:** Aktuelle Systemgrenze von vorgesehenen Erweiterungen unterscheiden
**Zitat:** „Stattdessen kann (optional) eine angebunden werden“

**Befund:** Das fachliche Diagramm stellt Endspiele genauso dar wie die realisierten Partner. Erst 3.2 erklärt, dass die Anbindung nicht implementiert ist. Siehe auch KKB-02.

**Änderungsvorschlag:**
> Endspieldatenbanken sind eine vorgesehene Erweiterungsmöglichkeit, keine aktuell verfügbare optionale Anbindung. Aus Aufwandsgründen wurde kein entsprechender Adapter implementiert (siehe Abschnitt 3.2 und Risiko 11.2). Im fachlichen Kontextdiagramm sind Partner und Verbindung gestrichelt und mit „nicht implementiert; Erweiterungsoption“ zu kennzeichnen.

#### [S03-05] Frontend-Risiko fehlt im Kontext

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md](arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md#L9)
**Kriterium:** Risiken externer Abhängigkeiten im Kontext aufzeigen
**Zitat:** „dessen Entwicklung nicht Teil von DokChess ist“

**Befund:** Die Abhängigkeit vom Frontend wird benannt, das zugehörige Integrationsrisiko (11.1) aber nicht verlinkt. Der vorhandene Risikoverweis betrifft nur Endspiele.

**Änderungsvorschlag:**
> Schnittstellenrisiko: Die grafische Nutzung hängt von einer funktionierenden Integration mit einem externen XBoard-Frontend ab. Risiko 11.1 beschreibt die frühzeitige Absicherung durch einen Proof of Concept; der unterstützte Protokollumfang ist in Abschnitt 5.2 dokumentiert.

#### [S03-06] Qualitätsanforderungen sind nicht den Schnittstellen zugeordnet

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md](arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md#L9)
**Kriterium:** Qualitätsanforderungen an externen Schnittstellen berücksichtigen
**Zitat:** „Der Zugriff erfolgt ausschließlich lesend.“

**Befund:** Für Polyglot ist eine Zugriffseigenschaft angegeben. Für Frontend-Integration und Antwortzeit fehlen solche Angaben, K01 und E01 sind nicht zugeordnet.

**Änderungsvorschlag:**
> Für die Frontend-Anbindung gilt Qualitätsszenario K01 aus Abschnitt 10.2: Ein kompatibles Frontend soll ohne Programmieraufwand innerhalb von zehn Minuten konfiguriert und getestet werden können. Für den Austausch von Spielzügen gilt E01. Diese Antwortzeit ist eine Qualitätsanforderung und keine Unterstützung der nicht implementierten XBoard-Zeitkontrolle.

---

### Sektion 4: Lösungsstrategie

*Prüfumfang: 28 Lösungsansätze der Community `c-s04` und ihre `addresses`-Kanten. Die Sektion ist kompakt, beschreibt Technologien und Top-Level-Zerlegung und verweist auf S5/S8. Alle Qualitätsziele sind abgedeckt.*

#### [S04-01] Qualitätsziel zur Spielstärke abweichend bezeichnet

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/04-Loesungsstrategie/04-01-Einstieg.md](arc-doc/04-Loesungsstrategie/04-01-Einstieg.md#L12)
**Kriterium:** Konsistente Zuordnung zu den Qualitätszielen aus 1.2
**Zitat:** „Attraktive Spielstärke (Attraktivität)“

**Befund:** Sektion 1.2 nennt dieses Ziel „Akzeptable Spielstärke (Funktionale Eignung)“. Die Strategie verwendet also einen anderen Namen und eine andere Qualitätskategorie.

**Änderungsvorschlag:** Erste Spalte ersetzen durch:
> Akzeptable Spielstärke (Funktionale Eignung)

#### [S04-02] Effizienzansatz ohne Einordnung des Zielkonflikts

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/04-Loesungsstrategie/04-01-Einstieg.md](arc-doc/04-Loesungsstrategie/04-01-Einstieg.md#L13), [arc-doc/04-Loesungsstrategie/04-02-Aufbau.md](arc-doc/04-Loesungsstrategie/04-02-Aufbau.md#L16)
**Kriterium:** Konsistente Lösungsansätze im Kontext priorisierter Qualitätsziele
**Zitat:** „Effiziente Implementierung des Domänenmodells“ vs. „Hier wurde bewusst eine bessere Verständlichkeit angestrebt, auf Kosten von Effizienz.“

**Befund:** Die Spannung, die im Graphen nur inferiert war, wurde im Quelltext bestätigt. Die Tabelle lässt offen, welche Effizienzoptimierung trotz des Vorrangs der Verständlichkeit gemeint ist.

**Änderungsvorschlag:** Tabellenpunkt ersetzen durch:
> Verständliches Domänenmodell mit bewusst akzeptierten Effizienznachteilen zugunsten der Analysierbarkeit (siehe Abschnitt 4.2); Absicherung ausreichender Antwortzeiten durch Integrationstests mit den Zeitvorgaben aus Abschnitt 10.2.

#### [S04-03] Organisatorische Strategie nicht zusammengefasst

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/04-Loesungsstrategie/04-01-Einstieg.md](arc-doc/04-Loesungsstrategie/04-01-Einstieg.md#L16)
**Kriterium:** Relevante organisatorische Entscheidungen
**Zitat:** „Der restliche Abschnitt 4 führt in wesentliche Architekturaspekte ein und verweist auf weitere Informationen.“

**Befund:** Das in [2.2](arc-doc/02-Randbedingungen/02-02-Organisatorisch.md) beschriebene Vorgehen „risikogetrieben, iterativ und inkrementell“ wird in der Strategie nicht aufgegriffen.

**Änderungsvorschlag:**
> Organisatorisch erfolgt die Entwicklung risikogetrieben, iterativ und inkrementell gemäß Abschnitt 2.2. Automatisierte Tests dienen als Sicherheitsnetz für den schrittweisen Austausch von Algorithmen und Komponenten (Abschnitt 8.7).

---

### Sektion 5: Bausteinsicht

*Prüfumfang: 14 Knoten der Community `c-s05` (8 Bausteine, 6 Schnittstellen) sowie Diagramme Ebene 1 und 2. Verantwortlichkeiten, Java-Schnittstellen und Pakete sind für alle Blackboxes beschrieben, und die Engine-Verfeinerung ist hierarchisch konsistent.*

#### [S05-01] Protokollumfang widerspricht dem fachlichen Kontext

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/05-Bausteinsicht/05-02-XBoard-Protokoll.md](arc-doc/05-Bausteinsicht/05-02-XBoard-Protokoll.md#L34)
**Kriterium:** Konsistenz externer Schnittstellen mit Sektion 3
**Zitat:** „Sie reicht aber für die an DokChess gestellten Anforderungen aus.“ Ausgeschlossen: „Remis-Angebote und Aufgabe der anderen Seite“

**Befund:** [3.1](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md#L9) nennt den Austausch „über Remisangebote“ ausdrücklich. Die pauschale Aussage, die Unterstützung reiche aus, verdeckt diese Abweichung. Siehe auch S03-01 und KKB-01.

**Änderungsvorschlag:**
> Die Implementierung unterstützt den grundlegenden Spielbetrieb, jedoch nicht sämtliche im fachlichen Kontext beschriebenen Interaktionen. Insbesondere werden Remisangebote entgegen der Beschreibung in Abschnitt 3.1 derzeit nicht unterstützt. Diese Abweichung gilt für menschliche Gegner und Computergegner.

#### [S05-02] Zerlegungsbegründung auf Ebene 1 fehlt

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/05-Bausteinsicht/05-01-Ebene-1.md](arc-doc/05-Bausteinsicht/05-01-Ebene-1.md#L3)
**Kriterium:** Begründung der Zerlegung
**Zitat:** „DokChess zerfällt wie in Bild unten dargestellt in vier Subsysteme.“

**Befund:** Diagramm und Tabelle beschreiben die Zerlegung, begründen aber nicht, warum die Grenzen so gezogen wurden.

**Änderungsvorschlag:**
> Die Zerlegung trennt die externe Protokollkommunikation, die Prüfung der Schachregeln, die Zugermittlung und den Zugriff auf Eröffnungswissen. Dadurch bleiben Kommunikationsformat und Bibliotheksformat von der eigentlichen Zugermittlung getrennt (vgl. Abschnitt 4.2). Die Schnittstellen erlauben es, Implementierungen unabhängig von ihren Nutzern auszutauschen; die Eröffnungsbibliothek bleibt optional.

#### [S05-03] Auswahl und Begründung der Engine-Verfeinerung fehlen

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/05-Bausteinsicht/05-06-Ebene-2-Engine.md](arc-doc/05-Bausteinsicht/05-06-Ebene-2-Engine.md#L3)
**Kriterium:** Relevanz der Verfeinerung und Begründung der internen Zerlegung
**Zitat:** „Die Engine zerfällt wie in der folgenden Abbildung dargestellt in Zugsuche und Stellungsbewertung.“

**Befund:** Es wird nicht erklärt, warum gerade die Engine vertieft wird und welchen Nutzen die Trennung bringt.

**Änderungsvorschlag:**
> Die Engine wird vertieft, weil Suchverfahren und Bewertungsfunktion zentrale Ansatzpunkte für Experimente mit der Spielstärke sind. Die Zugsuche verantwortet die Exploration des Spielbaums, die Stellungsbewertung den Vergleich der untersuchten Stellungen. Diese Trennung ermöglicht Änderungen an der Bewertungsfunktion unabhängig vom Suchalgorithmus (Szenario W04). Die übrigen Subsysteme werden nicht weiter verfeinert.

#### [S05-04] Interner Übergang von Engine zu Suche bleibt implizit

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/05-Bausteinsicht/05-06-Ebene-2-Engine.md](arc-doc/05-Bausteinsicht/05-06-Ebene-2-Engine.md#L5)
**Kriterium:** Beschreibung wichtiger interner Schnittstellen
**Zitat:** „Nur wenn diese keinen Rat weiß, kommt die Zugsuche zum Einsatz.“

**Befund:** `Engine.ermittleDeinenZug` liefert ein `Observable`, `Suche.zugSuchen` erwartet einen Observer. Wie beides zusammenhängt, wird nicht erklärt, die Graphkante ist nur inferiert. Auch die in 4.3 genannte Alpha-Beta-Suche taucht in 5.7 nicht als Klasse auf.

**Änderungsvorschlag:**
> Die Engine nutzt die Zugsuche über die Schnittstelle `de.dokchess.engine.suche.Suche`. Liefert die optionale Eröffnungsbibliothek keinen Zug, wird die aktuelle Stellung an `zugSuchen` übergeben. Die Suche meldet Zugkandidaten und ihren Abschluss an einen Observer; die Engine stellt die Zugkandidaten ihrem Aufrufer über das von `ermittleDeinenZug` zurückgegebene Observable bereit. Die Zugsuche nutzt ihrerseits `Spielregeln` und `Bewertung`.

---

### Sektion 6: Laufzeitsicht

*Prüfumfang: 1 Szenario der Community `c-s06` mit Sequenzdiagramm. Das Szenario ist geeignet und auf Ebene 1 konsistent mit S5.*

#### [S06-01] Unterbrechung der asynchronen Zugermittlung fehlt

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/06-Laufzeitsicht/06-01-Zugermittlung.md](arc-doc/06-Laufzeitsicht/06-01-Zugermittlung.md#L14)
**Kriterium:** Architekturrelevante Ausnahmeabläufe beschreiben
**Zitat:** „DokChess aber weiter auf Eingaben reagieren können soll, erfolgt der Aufruf asynchron.“

**Befund:** Es fehlt eine Eingabe während der laufenden Suche. Laut [5.4](arc-doc/05-Bausteinsicht/05-04-Engine.md#L17) brechen `ziehen` und `figurenAufbauen` eine laufende Zugermittlung ab. Offen bleibt, wie verspätete Kandidaten behandelt werden.

**Änderungsvorschlag:**
> ### Unterbrechung einer laufenden Zugermittlung
> 1. Während der asynchronen Suche nimmt das XBoard-Protokoll-Subsystem weitere Eingaben entgegen.
> 2. Erfordert eine Eingabe einen Aufruf von `ziehen` oder `figurenAufbauen`, bricht die Engine die bisherige Zugermittlung ab und übernimmt die Zustandsänderung.
> 3. Offener Punkt: Die Behandlung bereits empfangener und verspäteter Kandidaten der abgebrochenen Suche ist noch zu dokumentieren.

#### [S06-02] Fehlerpfade an der externen Schnittstelle fehlen

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/06-Laufzeitsicht/06-01-Zugermittlung.md](arc-doc/06-Laufzeitsicht/06-01-Zugermittlung.md#L11)
**Kriterium:** Relevante Fehler- und Ausnahmeszenarien darstellen
**Zitat:** „Der Zug wird im Beispiel als zulässig erkannt“

**Befund:** Beschrieben ist nur der Erfolgsfall. Die Fehlerwege aus 8.4 und 8.5 (`Illegal move`, `onError` → `tellusererror`) werden nicht gezeigt.

**Änderungsvorschlag:**
> ### Fehlerpfade der Zugermittlung
> 1. Erkennt das XBoard-Protokoll-Subsystem mithilfe der Spielregeln einen unzulässigen Zug, meldet es dem Client `Illegal move`. Der Zug wird nicht auf der Engine ausgeführt.
> 2. Meldet die Engine während der asynchronen Zugermittlung einen Fehler über `onError`, kommuniziert das XBoard-Protokoll-Subsystem diesen mit `tellusererror` an den Client.
> 3. DokChess arbeitet anschließend weiter; der Anwender entscheidet, ob ein Fortfahren sinnvoll ist (Abschnitte 8.4 und 8.5).

#### [S06-03] Zusammenarbeit der Engine-Bausteine bleibt implizit

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/06-Laufzeitsicht/06-01-Zugermittlung.md](arc-doc/06-Laufzeitsicht/06-01-Zugermittlung.md#L19)
**Kriterium:** Laufzeitinteraktionen der Bausteine aus S5 nachvollziehbar machen
**Zitat:** „Anschließend untersucht und bewertet es diese“

**Befund:** Zugsuche und Stellungsbewertung erscheinen weder als Lebenslinien noch im Text, ihre `involves`-Kanten sind nur inferiert. Grammatik: „es“ statt „sie“.

**Änderungsvorschlag:**
> ### Verfeinerung innerhalb der Engine
> Ohne passenden Bibliothekszug übernimmt der Baustein Zugsuche die Berechnung. Die `MinimaxParalleleSuche` untersucht mehrere Teilbäume parallel; der Minimax-Algorithmus verwendet die Spielregeln zur Ermittlung gültiger Züge und die Stellungsbewertung bei maximaler Suchtiefe. Verbesserte Zugkandidaten werden über `onNext`, der Abschluss über `onComplete` gemeldet.

#### [S06-04] Alternative mit Bibliothekszug fehlt

**Schwere:** 🟢 Hinweis
**Datei:** [arc-doc/06-Laufzeitsicht/06-01-Zugermittlung.md](arc-doc/06-Laufzeitsicht/06-01-Zugermittlung.md#L17)
**Kriterium:** Architekturrelevante Alternativen beschreiben
**Zitat:** „Zunächst prüft die Engine, ob die Eröffnungsbibliothek etwas hergibt. Im Beispiel ist das nicht der Fall.“

**Befund:** Der Pfad mit Bibliothekstreffer und der Fall ohne konfigurierte Bibliothek werden nicht erläutert. Siehe auch KSV-01.

**Änderungsvorschlag:**
> **Alternative Eröffnungsbibliothek:** Ist eine Eröffnungsbibliothek eingebunden und liefert sie einen Zug, verwendet die Engine diesen bevorzugt; die Zugsuche wird nicht gestartet. Ohne eingebundene Bibliothek oder bei Rückgabe von `null` erfolgt die Berechnung durch die Zugsuche.

---

### Sektion 7: Verteilungssicht

*Prüfumfang: 5 Infrastrukturknoten der Community `c-s07` mit Deployment-Diagramm. Alle vier Subsysteme sind über `DokChess.jar` zugeordnet. Eine geografische Verteilung oder weitere Ebenen sind für ein Single-PC-System nicht nötig.*

#### [S07-01] Motivation der Deployment-Struktur fehlt

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md](arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md#L5)
**Kriterium:** Deployment-Struktur begründen
**Zitat:** „Das Verteilungsdiagramm […] zeigt den Einsatz von DokChess unter Windows ohne Eröffnungsbibliothek.“

**Befund:** Nicht begründet sind die gemeinsame Platzierung von Frontend und Engine sowie die Bündelung als Über-JAR.

**Änderungsvorschlag:**
> Die lokale Single-PC-Struktur hält Installation und Betrieb einfach: Arena und DokChess kommunizieren über Standardein- und -ausgabe; ein separater Server oder eine Netzwerkverbindung ist nicht erforderlich. Das Über-JAR bündelt sämtliche DokChess-Module und ihre Abhängigkeiten und vermeidet deren separate Installation.

#### [S07-02] Entwicklungs-, Test- und Einsatzumgebungen bleiben unbestimmt

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md](arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md#L10)
**Kriterium:** Relevante Umgebungen dokumentieren
**Zitat:** „Software-Voraussetzungen auf dem PC:“

**Befund:** Nur der Einsatz mit Arena ist beschrieben. Entwicklung, Test und Plattformen außer Windows (2.1 nennt Linux und Mac OS X als wünschenswert) fehlen.

**Änderungsvorschlag:**
> **Umgebungen:** Das Diagramm beschreibt die lokale Einsatzumgebung zum Spielen und Demonstrieren mit Arena unter Windows. Für Linux/Mac OS X erfolgt der Einsatz analog mit XBoard bzw. einem anderen XBoard-fähigen Frontend und einem Shell-Startskript. Nachzutragen sind die benötigte JDK-Version, Build- und Testwerkzeuge sowie Unterschiede zur Einsatzumgebung.

#### [S07-03] Hardware- und Performance-Eigenschaften fehlen

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md](arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md#L10)
**Kriterium:** Qualitäts- und Performance-Merkmale der Infrastruktur
**Zitat:** „Java Runtime Environment SE 11 (oder höher)“

**Befund:** Es gibt keine Referenzkonfiguration (CPU, RAM, JVM-Parameter) für die Zeitszenarien E01 und E02. Siehe auch S02-01 und KRC-01.

**Änderungsvorschlag:**
> **Hardware und Performance:** CPU- und RAM-Mindestanforderungen sind noch nicht festgelegt. Für die Überprüfung der Qualitätsszenarien aus Sektion 10 sind Windows- und Java-Version, CPU-Modell, Anzahl verfügbarer Kerne, Arbeitsspeicher, JVM-Speicherparameter und verwendeter Suchalgorithmus zu dokumentieren.

#### [S07-04] Startvoraussetzungen sichern den Kommunikationskanal nicht ausreichend ab

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md](arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md#L13)
**Kriterium:** Betriebsrelevante Voraussetzungen und Kommunikationskanäle eindeutig beschreiben
**Zitat:** „Die JVM (javaw.exe) muss im Pfad liegen“; „[…] da dokchess.bat die jar-Datei relativ anspricht.“

**Befund:** Das Diagramm setzt `stdin/stdout` voraus. Ob der GUI-Launcher `javaw.exe` diese Kanäle bereitstellt, wird nicht geklärt. Zudem hängt die relative Auflösung vom Arbeitsverzeichnis ab, nicht vom gemeinsamen Ablageort.

**Änderungsvorschlag:**
> Das Startskript soll `java.exe` verwenden und Standardeingabe sowie Standardausgabe für das XBoard-Protokoll unverändert durchreichen. `DokChess.jar` ist relativ zum Verzeichnis des Skripts aufzulösen (`%~dp0DokChess.jar`), nicht zum Arbeitsverzeichnis des Frontends. Pfade sind in Anführungszeichen zu setzen.

#### [S07-05] Deployment mit optionaler Buchdatei bleibt offen

**Schwere:** 🟢 Hinweis
**Datei:** [arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md](arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md#L5)
**Kriterium:** Deployment-Varianten und externe Laufzeitartefakte abgrenzen
**Zitat:** „[…] unter Windows ohne Eröffnungsbibliothek.“

**Befund:** Die Einschränkung ist dokumentiert. Die Variante mit Polyglot-Buchdatei (Ablage, Konfiguration) wird jedoch nicht beschrieben.

**Änderungsvorschlag:**
> „Ohne Eröffnungsbibliothek“ bedeutet hier ohne konfigurierte Polyglot-Buchdatei; das Subsystem „Eröffnung“ aus 5.5 ist weiterhin im Über-JAR enthalten. Für die Variante mit Buchdatei sind Ablageort, Pfadkonfiguration und erforderliche Leserechte zu ergänzen.

---

### Sektion 8: Querschnittliche Konzepte

*Prüfumfang: 13 Knoten der Community `c-s08` (7 Konzepte, 6 Domänenmodell-Elemente). Die Sektion ist angemessen gegliedert und hat explizite Bezüge zu Bausteinen und Entscheidungen.*

#### [S08-01] Nebenläufigkeitsregeln fehlen

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/08-Konzepte/08-02-Domaenenmodell.md](arc-doc/08-Konzepte/08-02-Domaenenmodell.md#L33)
**Kriterium:** Konzepte erklären das WIE und sichern bausteinübergreifende Konsistenz
**Zitat:** „Die Klasse *Stellung* ist ebenfalls unveränderlich, die Methode *fuehreZugAus()* liefert eine neue Stellung“

**Befund:** Für die zustandsbehaftete Engine und die parallele Zugsuche fehlen gemeinsame Regeln zu Zustandszugriff, Callback-Verarbeitung und Abbruch.

**Änderungsvorschlag:**
> **Nebenläufigkeit:** Parallele Suchläufe verwenden unveränderliche Stellungsobjekte. Änderungen am Partiezustand und die Verarbeitung von Suchergebnissen werden serialisiert. Ergebnisse werden dem auslösenden Suchauftrag zugeordnet; Ergebnisse abgebrochener oder überholter Aufträge dürfen den Partiezustand nicht verändern.

#### [S08-02] Fortsetzung nach Fehlern ist nicht ausreichend definiert

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/08-Konzepte/08-05-Fehlerbehandlung.md](arc-doc/08-Konzepte/08-05-Fehlerbehandlung.md#L7)
**Kriterium:** Fehlerbehandlung beschreibt Mechanismus, Zuständigkeit und Auswirkungen
**Zitat:** „bei asynchroner Zugermittlung zusätzlich Fehlernachrichten (*onError*)“; „DokChess arbeitet dann ‘normal’ weiter“

**Befund:** Offen ist, welchen Zustand Engine und Suchauftrag nach einem Fehler haben. Der Weiterbetrieb ohne Eröffnungsbibliothek ist nicht dasselbe wie der Weiterbetrieb bei ungültiger Stellung, was auch Z02 widerspricht (siehe KRQ-01). Im GitHub-Link fehlt außerdem die schließende Klammer.

**Änderungsvorschlag:**
> Nach einer Fehlermeldung kann die Protokollverarbeitung fortgesetzt werden; daraus folgt keine Zusicherung eines gültigen Engine-Zustands. Ohne Eröffnungsbibliothek ist Weiterbetrieb vorgesehen. Für Fehler einer asynchronen Zugermittlung sind die Weiterleitung von `onError` an das XBoard-Subsystem, die Beendigung des betroffenen Suchauftrags und die Voraussetzungen eines erneuten Suchstarts verbindlich festzulegen. Bei ungültiger Stellung darf eine erfolgreiche Zugermittlung nicht vorausgesetzt werden.

#### [S08-03] Diagnosekonzept schützt den Protokollkanal nicht ausdrücklich

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/08-Konzepte/08-06-Logging.md](arc-doc/08-Konzepte/08-06-Logging.md#L11)
**Kriterium:** Querschnittliche Regeln sichern konsistentes Verhalten
**Zitat:** „Innerhalb von DokChess gibt es daher keine feinkörnigen Logging-Ausgaben“

**Befund:** Für Erweiterungen fehlt eine Regel, die Diagnoseausgaben vom textbasierten Protokollkanal (stdout) trennt.

**Änderungsvorschlag:**
> **Regel für Erweiterungen:** Die Standardausgabe bleibt ausschließlich XBoard-Protokollnachrichten vorbehalten. Zusätzliche Diagnoseausgaben dürfen diesen Kanal nicht verwenden. Zur Untersuchung von Kommunikationsfehlern werden die Protokollzeilen über das Frontend aufgezeichnet.

#### [S08-04] Testkonzept bleibt bei asynchronen Verträgen zu allgemein

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/08-Konzepte/08-07-Testbarkeit.md](arc-doc/08-Konzepte/08-07-Testbarkeit.md#L11)
**Kriterium:** Konzepte werden mit Bausteinen und konkreten Tests verknüpft
**Zitat:** „Darüber hinaus gibt es Tests, die das Zusammenspiel von Modulen prüfen“; „Dies erfolgt mit der *@Test*-Annotation und deren Timeout-Parameter“

**Befund:** Es fehlen Nachweise für asynchrone Ergebnisfolgen, Fehlerweiterleitung und Suchabbruch. Ein Timeout allein prüft diese Verträge nicht.

**Änderungsvorschlag:**
> **Ergänzende Testanforderungen:** Integrationstests für [Engine](../05-Bausteinsicht/05-04-Engine.md), [Zugsuche](../05-Bausteinsicht/05-07-Zugsuche.md) und [XBoard-Protokoll](../05-Bausteinsicht/05-02-XBoard-Protokoll.md) prüfen Ergebniszustellung, Abschluss, Fehlerweiterleitung und Abbruch. Sie synchronisieren auf beobachtbare Ereignisse statt auf feste Wartezeiten. Repräsentative Testklassen sind hier direkt zu verlinken.

#### [S08-05] Protokollspezifikation ist nicht eindeutig referenziert

**Schwere:** 🟢 Hinweis
**Datei:** [arc-doc/08-Konzepte/08-03-Benutzungsoberflaeche.md](arc-doc/08-Konzepte/08-03-Benutzungsoberflaeche.md#L22)
**Kriterium:** Nachvollziehbare weiterführende Referenzen
**Zitat:** „Das Protokoll selbst ist in [Mann+2009] detailliert beschrieben“

**Befund:** Der Kurzverweis lässt sich nicht auflösen, weil es kein Literaturverzeichnis gibt. Redaktionell fallen außerdem „teileweise“, „inder Regel“, „die Protokollbefehl“ und eine überzählige Klammer auf.

**Änderungsvorschlag:**
> Das XBoard-Protokoll ist in der [Chess Engine Communication Protocol Specification](https://www.gnu.org/software/xboard/engine-intf.html) beschrieben. Den von DokChess implementierten Umfang und bekannte Einschränkungen dokumentiert die [Bausteinsicht 5.2](../05-Bausteinsicht/05-02-XBoard-Protokoll.md).

---

### Sektion 9: Architekturentscheidungen

*Prüfumfang: 2 ADRs der Community `c-s09`. Beide enthalten Titel, Status, Datum, Context, Decision und Consequences mit Alternativen. Gegenüber S4 gibt es keinen sachlichen Widerspruch.*

#### [S09-01] Aktualität der Frontend-Auswahl nicht belegt

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/09-Entscheidungen/09-01-Anbindung.md](arc-doc/09-Entscheidungen/09-01-Anbindung.md#L5)
**Kriterium:** Kontext, Entscheidungskriterien und Nachvollziehbarkeit
**Zitat:** „Accepted (2026-03-10)“; „Untersuchte Frontends (Stand 2011)“; „Die Untersuchung weniger verfuegbarer Frontends fuehrt zu allen relevanten Integrationsoptionen.“

**Befund:** Die 2026 akzeptierte Entscheidung stützt sich auf eine Untersuchung von 2011. Eine erneute Bewertung ist nicht dokumentiert, und die kleine Stichprobe belegt nicht die behauptete Vollständigkeit.

**Änderungsvorschlag:**
> Die betrachteten Frontends bilden eine begrenzte Stichprobe mit Untersuchungsstand 2011. Daraus wird keine Vollständigkeit der Integrationsoptionen abgeleitet. Die Entscheidung wurde 2011 getroffen und am 2026-03-10 in dieses ADR-Format übertragen; eine erneute Bewertung ist nicht erfolgt. Vor einer Erweiterung der unterstützten Frontends ist die Protokollwahl anhand konkreter Frontend-Versionen zu überprüfen.

#### [S09-02] Leistungsbegründung nicht reproduzierbar

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md](arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md#L50)
**Kriterium:** Entscheidungskriterien und Nachvollziehbarkeit
**Zitat:** „In einem Prototypvergleich (Mattsuche, Minimax, Matt in 3) lag die unveraenderliche Variante bei ca. 30 Prozent laengerer Laufzeit, aber weiterhin innerhalb der geforderten Grenzen.“

**Befund:** Absolute Laufzeiten, Hardware, JVM und Messverfahren fehlen, ebenso die geprüften Grenzen. Ein relativer Unterschied belegt nicht, dass E01 eingehalten wird.

**Änderungsvorschlag:**
> Der Prototypvergleich für Mattsuche mit Minimax („Matt in 3“) ergab ungefähr 30 Prozent längere Laufzeiten für unveränderliche Stellungen. Für einen belastbaren Nachweis sind Teststellungen, Suchtiefe, Code-Version, Hardware, JVM-Konfiguration, Messverfahren und absolute Laufzeiten beider Varianten zu dokumentieren und den Szenarien E01/E02 aus Abschnitt 10.2 zuzuordnen.

#### [S09-03] Parallelisierung als Zukunftsfolge und vorhandene Umsetzung vermischt

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md](arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md#L68)
**Kriterium:** Konsequenzen und zeitliche Nachvollziehbarkeit
**Zitat:** „Performance-Optimierungen bleiben relevant (effizientes Kopieren, spaeter Parallelisierung).“; „mit DokChess 2.0 durch einen parallelen Minimax bereits teilweise adressiert.“

**Befund:** Die Parallelisierung erscheint zugleich als künftige Maßnahme und als vorhandene Umsetzung. Dass sie den Laufzeitnachteil kompensiert, ist nicht belegt.

**Änderungsvorschlag:**
> - Effizientes Kopieren und weitere Performance-Optimierungen bleiben relevant.
> - Seit DokChess 2.0 ist ein paralleler Minimax als Beispiel vorhanden (siehe Abschnitt 4.3). Er demonstriert die Nutzung unveränderlicher Stellungen in nebenläufigen Algorithmen.
> - Eine quantitative Kompensation des gemessenen Laufzeitnachteils durch Parallelisierung ist nicht nachgewiesen.

---

### Sektion 10: Qualitätsanforderungen

*Prüfumfang: 15 Szenarien der Community `c-s10` mit `concretizes`-Kanten aus dem ausgewerteten Qualitätsbaum. Baum, Kategorien und Nutzungs-, Änderungs- und Fehlerszenarien sind vorhanden. Alle fünf Ziele sind zugeordnet. F01, Z01 und Z02 hängen an keinem Hauptziel.*

#### [S10-01] Unklare Performance-Grenzen und Messbedingungen

**Schwere:** 🔴 Kritisch
**Datei:** [arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L22)
**Kriterium:** Eindeutige, reproduzierbar messbare Performance-Szenarien
**Zitat:** E01: „innerhalb von fünf Sekunden“; E02: „maximal zehn Sekunden mit ihrem ersten Zug“

**Befund:** Der erste Gegenzug fällt unter beide Szenarien, und eine Ausnahme ist nicht festgelegt. Referenzkonfiguration und Messgrenzen fehlen. Siehe auch KQS-02.

**Änderungsvorschlag:**
> E01 gilt ab dem zweiten Engine-Zug: Zwischen vollständigem Eingang eines legalen Gegenzugs und vollständiger Ausgabe eines legalen Antwortzugs dürfen höchstens fünf Sekunden liegen. E02 regelt ausschließlich den ersten Engine-Zug nach Partiebeginn: höchstens zehn Sekunden bis zur Zugausgabe und, sofern noch kein Zug vorliegt, höchstens fünf Sekunden bis zur sichtbaren Denk-Rückmeldung im Frontend. Hardware, Betriebssystem, JVM, Engine- und Frontend-Version, Suchparameter und Eröffnungsbuch werden vor der Messung festgelegt und dokumentiert.

#### [S10-02] Spielstärkeziel nur teilweise konkretisiert

**Schwere:** 🔴 Kritisch
**Datei:** [arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L19)
**Kriterium:** Vollständige Konkretisierung der Qualitätsziele aus 1.2
**Zitat:** F02: „nimmt die ‚eingestellte‘ Figur“; 1.2: „schwache Gegner sicher zu schlagen und Gelegenheitsspieler zumindest zu fordern“

**Befund:** F02–F04 messen taktische Einzelfähigkeiten. Daraus folgt keine ausreichende Spielstärke über ganze Partien gegen die genannten Gegnergruppen. Siehe auch S01-02 und KQS-03.

**Änderungsvorschlag:**
> F05 – Spielstärke: DokChess spielt jeweils 40 Partien gegen zwei versionierte Referenzgegner, die einen schwachen Spieler beziehungsweise einen Gelegenheitsspieler repräsentieren. Bei gleichen Zeitbudgets, wechselnden Farben und festgelegten Eröffnungen gewinnt DokChess mindestens 80 Prozent der Partien gegen den schwachen Gegner und erreicht mindestens 25 Prozent der möglichen Punkte gegen den Gelegenheitsspieler.

#### [S10-03] Analysierbarkeit nicht objektiv prüfbar

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L12)
**Kriterium:** Konkrete Metriken und beobachtbare Akzeptanzkriterien
**Zitat:** W01: „erschließen sich […] innerhalb von 15 Minuten“; W02: „unverzüglich“; W03: „ohne Umwege“

**Befund:** W01 nennt eine Zeitgrenze, definiert aber keinen Verständniserfolg. W02 und W03 haben keine Zeitgrenze. Siehe auch KQS-04.

**Änderungsvorschlag:**
> W01: Eine Person mit UML- und Schachgrundkenntnissen, aber ohne DokChess-Vorkenntnisse, benennt nach höchstens 15 Minuten Lektüre die zentralen Bausteine, deren Verantwortlichkeiten und den Ablauf der Zugermittlung korrekt anhand einer vorab festgelegten Prüfliste. W02: Ein arc42-kundiger Architekt findet ausgehend vom Dokumentationsüberblick innerhalb von 60 Sekunden einen Beispielinhalt zu jedem vorgegebenen Kapitel. W03: Eine erfahrene Java-Entwicklerin findet für jedes vorgegebene Modul innerhalb von zwei Minuten die zugehörige Implementierung ohne fremde Hilfe.

#### [S10-04] Änderungsaufwand und Abschlusskriterien fehlen

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L15)
**Kriterium:** Änderungsszenarien mit Aufwand als Metrik
**Zitat:** W04: „ohne Änderung und ohne Übersetzung vorhandenen Codes“; W05: „maximal eine Woche“; P01: „ohne Änderung am bestehenden Code“

**Befund:** W04 und P01 begrenzen nur die Eingriffsfläche, nicht den Aufwand. W05 unterscheidet nicht zwischen Kalenderdauer und Personenaufwand.

**Änderungsvorschlag:**
> Für W04, W05 und P01 wird eine mit Java und den dokumentierten Schnittstellen vertraute Person vorausgesetzt. W04 einschließlich Integration und Tests benötigt höchstens zwei Personentage, P01 höchstens fünf Personentage. W05 einschließlich Austausch und Regressionstests benötigt höchstens fünf Personentage. Abgeschlossen ist die Änderung erst, wenn die neuen Akzeptanztests und alle bestehenden Regressionstests erfolgreich sind.

#### [S10-05] Funktionale Szenarien benötigen eindeutige Testfälle

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L18)
**Kriterium:** Szenarien als reproduzierbare Akzeptanzkriterien
**Zitat:** F02: „ungedeckt und frei von Sinn“; F03: „gewinnt Dame (bzw. Turm) gegen Springer“; F04: „zieht sicher zum Sieg“

**Befund:** Ausgangsstellungen, zulässige Lösungsvarianten und eine gemeinsame Suchkonfiguration fehlen.

**Änderungsvorschlag:**
> F01–F04 werden mit einer vorab versionierten Sammlung von FEN-Stellungen, erwarteten Ergebnissen und festgelegten Suchparametern geprüft; alle Fälle müssen bestehen. F04 verlangt ein Matt spätestens mit dem zweiten eigenen Zug gegen jede legale gegnerische Verteidigung.

#### [S10-06] Fehlerreaktionen nicht ausreichend beobachtbar

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L24)
**Kriterium:** Fehlerszenarien mit konkreten Reaktionen
**Zitat:** Z01: „spielt fehlerfrei weiter“; Z02: „erkennt die Situation und beendet das Spiel“

**Befund:** Offen bleiben Zustandsintegrität, beobachtbare Fehlermeldung und die Abgrenzung zwischen Partieende und Prozessabbruch. Z02 widerspricht 8.4, wonach die Zulässigkeit einer Position nicht geprüft wird (siehe KRQ-01).

**Änderungsvorschlag:**
> Z01: Nach einem unzulässigen Gegenzug meldet die Engine „Illegal move“; Brettstellung, Zugrecht und Zugzähler bleiben unverändert. Ein anschließend eingegebener legaler Gegenzug wird akzeptiert und mit einem legalen Zug beantwortet. Z02: Bei einer unzulässigen Anfangsstellung meldet die Engine den Fehler, startet keine Zugsuche und beendet ausschließlich die betroffene Partie. Der Prozess bleibt ansprechbar.

#### [S10-07] W05 belegt Analysierbarkeit nicht eigenständig

**Schwere:** 🟢 Hinweis
**Datei:** [arc-doc/10-Qualitaetsanforderungen/10-01-Qualitaetsbaum.md](arc-doc/10-Qualitaetsanforderungen/10-01-Qualitaetsbaum.md#L6)
**Kriterium:** Nachvollziehbare Zuordnung zwischen Qualitätsmerkmal und Szenario
**Zitat:** Diagramm: „Analysierbarkeit“ → „W05“

**Befund:** W05 misst den gesamten Änderungsaufwand und isoliert keinen Analyseerfolg.

**Änderungsvorschlag:**
> W05 konkretisiert primär Änderbarkeit. Sein begrenzter Gesamtaufwand liefert lediglich einen indirekten Hinweis auf Analysierbarkeit. Der direkte Nachweis des Qualitätsziels „Zugängliches Beispiel“ erfolgt durch W01–W03.

---

### Sektion 11: Risiken und technische Schulden

*Prüfumfang: 3 Risiken der Community `c-s11`. Alle Risiken haben `priority = nicht angegeben`. Es gibt eine gegliederte Risikoaufstellung mit Eventualfallplanung und Maßnahmen.*

#### [S11-01] Fehlende Validierung nicht als Risiko erfasst

**Schwere:** 🔴 Kritisch
**Datei:** [arc-doc/11-Risiken/11-03-Spielstaerke.md](arc-doc/11-Risiken/11-03-Spielstaerke.md); Beleg: [arc-doc/08-Konzepte/08-04-Validierung.md](arc-doc/08-Konzepte/08-04-Validierung.md#L17)
**Kriterium:** Bekannte technische Risiken aus anderen Sektionen aufnehmen
**Zitat:** „Im Extremfall antwortet die Engine mit einem ungültigen Zug.“

**Befund:** Ungeprüfte Ausgangsstellungen und Bibliothekszüge können zu Fehlern oder regelwidrigen Antworten führen. Dieses Korrektheitsrisiko fehlt in Sektion 11. Siehe auch KRQ-01.

**Änderungsvorschlag:** Neue Datei `11-04-Validierung.md`:
> ## 11.4 Risiko: Ungeprüfte Eingabedaten gefährden die Spielkorrektheit
> Gemäß 8.4 werden Ausgangsstellungen und Eröffnungsbibliotheken nicht inhaltlich validiert. Maßnahmen: Ausgangsstellungen vor der Zugermittlung auf Zulässigkeit prüfen; Bibliothekszüge gegen die gültigen Züge der aktuellen Stellung prüfen und unzulässige Kandidaten verwerfen. Regressionstests decken fehlende Könige und unzulässige Bibliothekszüge ab. Abschlusskriterium: Z02 wird erfüllt und Bibliotheksdaten führen nicht zu regelwidrigen Antworten gemäß F01.

#### [S11-02] Regelverzicht verharmlost technische Schulden

**Schwere:** 🔴 Kritisch
**Datei:** [arc-doc/11-Risiken/11-02-Aufwand.md](arc-doc/11-Risiken/11-02-Aufwand.md#L29)
**Kriterium:** Konsequenzen von Maßnahmen und technische Schulden korrekt dokumentieren
**Zitat:** „Das Fehlen hat geringe Konsequenzen bezüglich der Spielstärke, und keine bezüglich der Korrektheit des Spiels der Engine.“

**Befund:** Legale Einzelzüge bedeuten noch keine vollständige Regelkonformität. Die fehlende Remiserkennung widerspricht der Anforderung „Vollständige Implementierung der FIDE-Schachregeln“ (1.1) und ist in 5.3 als offener Punkt dokumentiert.

**Änderungsvorschlag:**
> Das Weglassen der 50-Züge-Regel und der Stellungswiederholung reduziert den Implementierungsaufwand, hinterlässt aber technische Schulden: Die Engine kann diese Remisfälle nicht selbst erkennen und erfüllt die geforderte vollständige Umsetzung der Spielregeln (Abschnitt 1.1) insoweit nicht. Maßnahmen: erforderliche Partiehistorie und Zähler ergänzen sowie Grenzfalltests für beide Regeln erstellen. Bis dahin ist die Einschränkung bei Demonstrationen und Nutzung ausdrücklich auszuweisen.

#### [S11-03] Keine bewertete Priorisierung

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/11-Risiken/11-01-Frontend.md](arc-doc/11-Risiken/11-01-Frontend.md), [arc-doc/11-Risiken/11-02-Aufwand.md](arc-doc/11-Risiken/11-02-Aufwand.md), [arc-doc/11-Risiken/11-03-Spielstaerke.md](arc-doc/11-Risiken/11-03-Spielstaerke.md)
**Kriterium:** Risiken nach Priorität ordnen
**Zitat:** „Falls es uns nicht gelingt, eine funktionierende Anbindung zu realisieren, können wir die Lösung nicht mit bestehenden Frontends verwenden.“

**Befund:** Kein Risiko ist nach Eintrittswahrscheinlichkeit und Auswirkung bewertet. Verantwortliche und Prüftermine fehlen.

**Änderungsvorschlag:**
> **Bewertung und Steuerung:** Für jedes Risiko dokumentieren wir Eintrittswahrscheinlichkeit, Auswirkung, begründete Priorität, verantwortliche Person, Maßnahmenstatus und nächsten Prüftermin. Noch ausstehende Bewertungen kennzeichnen wir als „offen“. Die Übersicht wird nach Priorität sortiert.

#### [S11-04] Historische Ausgangslage ohne aktuellen Status

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/11-Risiken/11-01-Frontend.md](arc-doc/11-Risiken/11-01-Frontend.md#L5), [arc-doc/11-Risiken/11-02-Aufwand.md](arc-doc/11-Risiken/11-02-Aufwand.md#L18)
**Kriterium:** Aktuelle von historischen Risiken unterscheiden
**Zitat:** „Über Kommunikationsprotokolle ist überhaupt nichts bekannt.“; „Falls zu den Vorträgen in März und Mai 2011 keine lauffähige Fassung vorliegt […]“

**Befund:** Die Ausgangslage von 2011 ist nicht als historisch gekennzeichnet, obwohl XBoard-Anbindung (ADR 9.1) und Deployment inzwischen dokumentiert sind.

**Änderungsvorschlag:**
> **Zeitlicher Bezug:** Die Risikobeschreibung bezieht sich auf die Konzeption und Vorträge 2011. **Status (aktuell):** Die XBoard-Anbindung ist umgesetzt (ADR 9.1, Abschnitt 5.2); das Risiko gilt als weitgehend gemindert. Restrisiken: unvollständiger Protokollumfang (5.2) und Frontends, die nur *.exe einbinden (7.1).

#### [S11-05] Frontend-Maßnahme ohne Nachweis und Restumfang

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/11-Risiken/11-01-Frontend.md](arc-doc/11-Risiken/11-01-Frontend.md#L20)
**Kriterium:** Maßnahmen konkretisieren
**Zitat:** „Durch einen Proof of concept erreichen wir hier frühestmöglich Sicherheit.“

**Befund:** Umfang, Erfolgskriterium und Ergebnis des PoC fehlen. Siehe auch KRQ-04.

**Änderungsvorschlag:**
> Der Integrationsnachweis dokumentiert Frontend-, Betriebssystem- und Java-Version sowie Start, Protokollinitialisierung, Zugwechsel und Beenden. Erfolgskriterium ist K01: Einbindung ohne Programmieraufwand innerhalb von zehn Minuten. Für Frontends mit EXE-Zwang wird ein getesteter Wrapper bereitgestellt oder die fehlende Unterstützung ausgewiesen.

#### [S11-06] Spielstärketests erkennen Probleme, lösen sie aber nicht

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/11-Risiken/11-03-Spielstaerke.md](arc-doc/11-Risiken/11-03-Spielstaerke.md#L19)
**Kriterium:** Umsetzbare Risikoreduktion
**Zitat:** „So können wir zumindest früh ermitteln, wo die Engine steht.“

**Befund:** Es fehlen Reaktionen auf fehlgeschlagene Tests sowie der Bezug zu den Speicher- und GC-Nachteilen aus ADR 9.2.

**Änderungsvorschlag:**
> Als Mindestnachweis verwenden wir F02–F04 und E01 aus 10.2 mit dokumentierten Teststellungen, Suchkonfiguration und Referenzhardware. Bei Fehlschlägen verbessern wir gezielt Suche oder Stellungsbewertung (z. B. Alpha-Beta, Abschnitt 4.3). Das Restrisiko unveränderlicher Stellungsobjekte umfasst erhöhten Speicherbedarf und GC-Last gemäß ADR 9.2.

#### [S11-07] Breite der Risikoermittlung nicht nachvollziehbar

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/11-Risiken/11-02-Aufwand.md](arc-doc/11-Risiken/11-02-Aufwand.md#L5)
**Kriterium:** Stakeholder-, Schnittstellen-, Prozess- und Datenperspektiven berücksichtigen
**Zitat:** „Es liegt keinerlei Erfahrung mit der Schachprogrammierung vor.“

**Befund:** Nicht dokumentiert ist, welche Stakeholder beteiligt waren und welche Prüfungen der Risikoliste zugrunde liegen.

**Änderungsvorschlag:**
> **Ermittlung der Risiken:** Beim nächsten Risikoreview beteiligen wir Architektur-/Entwicklungsverantwortliche und die für Vorträge verantwortliche Person. Wir prüfen Frontend-Schnittstellen, Demonstrationsabläufe sowie Ausgangsstellungen, Partiehistorie und Bibliotheksdaten. Datum, Beteiligte und neue bzw. akzeptierte Risiken werden protokolliert.

---

### Sektion 12: Glossar

*Prüfumfang: 24 Glossarbegriffe der Community `c-s12` sowie eine sektionsübergreifende Begriffsprüfung. Das Glossar ist kompakt und tabellarisch.*

#### [S12-01] Mehrdeutige Fachbegriffe und Bausteinnamen

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/12-Glossar/12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md#L9)
**Kriterium:** Homonyme auflösen
**Zitat:** „Engine […] Bezeichnung für den Teil des Schachprogramms, der die Züge berechnet.“

**Befund:** Mehrere Begriffe sind doppelt belegt: „Engine“ steht für DokChess insgesamt und für das Subsystem 5.4. „Eröffnung“ ist Partiephase und Baustein, „XBoard-Protokoll“ ist Standard und Subsystem.

**Änderungsvorschlag:**
> | Engine | Auch Schach-Engine: Schachprogramm zur Zugermittlung, typischerweise ohne eigene grafische Oberfläche. DokChess ist insgesamt eine Schach-Engine. Innerhalb seiner Architektur bezeichnet „Subsystem Engine“ den zustandsbehafteten Baustein zur Zugermittlung aus Abschnitt 5.4. |
> | Eröffnung | Erste Phase einer Schachpartie. Davon zu unterscheiden ist das DokChess-Subsystem „Eröffnung“ aus Abschnitt 5.5. |
> | XBoard-Protokoll | Textbasiertes Kommunikationsprotokoll zwischen Schach-Frontends und Engines; auch WinBoard-Protokoll oder Chess Engine Communication Protocol (CECP). Das gleichnamige DokChess-Subsystem aus Abschnitt 5.2 implementiert dieses Protokoll. |

#### [S12-02] Stellung und Zug nicht ausreichend abgegrenzt

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/12-Glossar/12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md#L14)
**Kriterium:** Zentrale Domänenbegriffe definieren; Konsistenz mit S8
**Zitat:** „Halbzug […] Im Gegensatz zur Folge von weißem und schwarzem Zug, die z.B. beim Nummerieren als Zug gezählt wird.“

**Befund:** Im [Domänenmodell](arc-doc/08-Konzepte/08-02-Domaenenmodell.md#L25) bezeichnet `Zug` die Aktion eines einzelnen Spielers. „Stellung“ fehlt im Glossar ganz.

**Änderungsvorschlag:**
> | Stellung | Spielsituation aus Figurenanordnung, Zugrecht, Rochaderechten und gegebenenfalls einer En-passant-Möglichkeit. In DokChess durch die unveränderliche Klasse Stellung repräsentiert; siehe Abschnitt 8.2. |
> | Zug | Im DokChess-Domänenmodell die Aktion eines einzelnen Spielers (Halbzug), beschrieben durch Ausgangs- und Zielfeld sowie gegebenenfalls die Umwandlungsfigur. Bei der Partienummerierung bezeichnet ein Zug dagegen einen weißen und einen schwarzen Halbzug. |

#### [S12-03] Relevante Computerschachbegriffe fehlen

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/12-Glossar/12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md)
**Kriterium:** Wichtige technische und domänenspezifische Begriffe auswählen
**Zitat:** „figurenzentrierte Bitboard-Repräsentation“ (W05); „ausschließlich […] Material“ (4.3); „UCI Protocol (Universal Chess Interface)“ (ADR 09-01)

**Befund:** Diese Begriffe sind für Repräsentation, Bewertung und Protokollentscheidung relevant, werden im Glossar aber nicht erklärt.

**Änderungsvorschlag:**
> | Bitboard | Darstellung einer Menge von Schachbrettfeldern durch 64 Bits, eines je Feld. Mehrere Bitboards können beispielsweise die Positionen bestimmter Figurenarten und Farben abbilden. |
> | Material | Vorhandene Figuren eines Spielers und ihre relativen Werte. Eine reine Materialbewertung vergleicht diese Werte, ohne die Positionen der Figuren zu berücksichtigen. |
> | UCI | Universal Chess Interface. Textbasiertes Kommunikationsprotokoll zwischen Schach-Frontend und Engine; Alternative zum XBoard-Protokoll. In DokChess laut ADR 09-01 nicht implementiert. |

#### [S12-04] Regeldefinitionen lassen entscheidende Bedingungen offen

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/12-Glossar/12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md#L4)
**Kriterium:** Fachlich eindeutige Definitionen
**Zitat:** „wenn 50 Züge lang […]“; „darf dieser en passant schlagen“; „wenn dieselbe Stellung mindestens zum dritten Mal auftritt“

**Befund:** Es fehlen die Zähleinheit der 50-Züge-Regel, das Zeitfenster für en passant und eine Definition, wann Stellungen als gleich gelten.

**Änderungsvorschlag:**
> | 50-Züge-Regel | Ein Spieler am Zug kann Remis reklamieren, wenn beide Spieler jeweils 50 aufeinanderfolgende Züge (insgesamt 100 Halbzüge) ohne Bauernzug und ohne Schlagen ausgeführt haben. |
> | en passant | Besonderes Schlagen eines Bauern unmittelbar nach dessen Doppelschritt aus der Ausgangsstellung. Ein gegnerischer Bauer auf einer benachbarten Linie schlägt ihn auf dem übersprungenen Feld. Dieses Recht besteht nur im unmittelbar folgenden Halbzug. |
> | Stellungswiederholung | Ein Spieler am Zug kann Remis reklamieren, wenn dieselbe Stellung zum dritten Mal vorliegt. Gleichheit erfordert dieselbe Figurenanordnung, denselben Spieler am Zug und dieselben Rochade- und En-passant-Möglichkeiten. Die Wiederholungen müssen nicht unmittelbar aufeinanderfolgen. |

#### [S12-05] Endspiel wird über Figurenarten statt Figurenbestand erklärt

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/12-Glossar/12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md#L8)
**Kriterium:** Fachlich zutreffende Definition
**Zitat:** „nur noch wenige Figurenarten auf dem Brett“

**Befund:** Wenige Figurenarten sind kein hinreichendes Merkmal eines Endspiels, entscheidend ist der reduzierte Figurenbestand.

**Änderungsvorschlag:**
> | Endspiel | Späte Phase einer Schachpartie mit typischerweise deutlich reduziertem Figurenbestand. Der Übergang vom Mittelspiel zum Endspiel ist nicht eindeutig festgelegt. |

#### [S12-06] Minimax und Alpha-Beta versprechen zu uneingeschränkte Ergebnisse

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/12-Glossar/12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md#L16)
**Kriterium:** Verständliche Algorithmusdefinitionen; Konsistenz mit Lösungsstrategie
**Zitat:** „Ermittlung des besten Zuges […] aller Optionen beider Spieler“; „ohne dabei zu einem anderen Ergebnis zu kommen“

**Befund:** Die Minimax-Definition nennt weder das Max-/Min-Prinzip noch die feste Suchtiefe aus [4.3](arc-doc/04-Loesungsstrategie/04-03-Spielstrategie.md#L7). Alpha-Beta erhält zwar den Bewertungswert, liefert aber nicht zwingend denselben Zug.

**Änderungsvorschlag:**
> | Minimax-Algorithmus | Suchverfahren für Zwei-Personen-Nullsummenspiele: Der eigene Spieler maximiert, der Gegner minimiert den Bewertungswert. DokChess durchsucht den Spielbaum bis zu einer festen Suchtiefe und bewertet die Endstellungen. |
> | Alpha-Beta-Suche | Optimierung von Minimax, die Teilbäume auslässt, sobald sie den Minimax-Wert nicht mehr beeinflussen können. Bei gleicher Suchtiefe und Bewertung bleibt dieser Wert erhalten; bei gleichwertigen Zügen kann die Zugauswahl variieren. |

#### [S12-07] Einstellen wird zu eng beschrieben

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/12-Glossar/12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md#L7)
**Kriterium:** Fachlich vollständige Definition
**Zitat:** „Anfängerfehler […] wenn sie auf ein vom Gegner angegriffenes Feld gezogen wird“

**Befund:** Eine Figur kann auch eingestellt werden, indem die Deckung weggezogen oder eine Drohung übersehen wird.

**Änderungsvorschlag:**
> | Einstellen | Unbeabsichtigtes Ermöglichen eines Materialverlusts durch einen fehlerhaften Zug oder eine übersehene Drohung, beispielsweise indem eine Figur ungedeckt angegriffen bleibt oder ihre Deckung weggezogen wird. |

#### [S12-08] Spieß nicht ausreichend von Fesselung abgegrenzt

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/12-Glossar/12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md#L23)
**Kriterium:** Eindeutige Definition verwandter taktischer Motive
**Zitat:** „die vordere der beiden zum Wegziehen zwingt“

**Befund:** Die Definition erklärt nicht, dass nach dem Ausweichen die dahinterstehende Figur angreifbar wird.

**Änderungsvorschlag:**
> | Spieß | Taktikmotiv, bei dem Läufer, Turm oder Dame eine vordere gegnerische Figur angreifen und hinter ihr eine weitere Figur auf derselben Reihe, Linie oder Diagonalen steht. Weicht die vordere, typischerweise wertvollere Figur aus, kann die dahinterstehende geschlagen werden. |

#### [S12-09] Redaktionelle Fehler und Sortierung

**Schwere:** 🟢 Hinweis
**Datei:** [arc-doc/12-Glossar/12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md#L22)
**Kriterium:** Verständlichkeit und alphabetische Ordnung
**Zitat:** „Schachvariante, bei die Anfangsstellung […]“; Reihenfolge „Endspiel“, „Engine“, „en passant“

**Befund:** Der Eintrag enthält einen Grammatikfehler, „en passant“ ist falsch einsortiert, und [00-00-Overview.md](arc-doc/00-Ueberblick/00-00-Overview.md#L5) schreibt „Fisher“ statt „Fischer“.

**Änderungsvorschlag:**
> | Schach960 | Eine von Bobby Fischer entwickelte Schachvariante, bei der die Anfangsstellung aus 960 möglichen Aufstellungen ausgewählt wird. Auch als Fischer-Random-Chess bekannt. |

Zusätzlich „en passant“ vor „Endspiel“ einordnen und im Überblick „Robert (“Bobby”) Fischer“ schreiben.

---

## Sektionsübergreifende Konflikte

| Konfliktdimension | Status | Befunde |
|---|---|---|
| Qualitätsstrang (S1 ↔ S4 ↔ S10) | 🟡 | Strategische Absicherung von Z01/Z02 fehlt. Zeitgrenzen E01/E02 sind ohne Durchsetzungsmechanismus, und die Spielstärke ist nur taktisch belegt. W02/W03 sind nicht prüfbar. |
| Strategie ↔ Entscheidungen (S4 ↔ S9) | 🟡 | Modularchitektur/DI, Reactive Extensions sowie Such- und Formatwahl haben keine ADR. Die allgemeine Unveränderlichkeitsregel ist nur teilweise durch ADR 9.2 gedeckt. |
| Constraint-Compliance (S2 ↔ S4/S8/S9) | 🟡 | Es gibt keine belegte Verletzung. Nachweise fehlen für die Notebook-Eignung, den IDE-freien Gradle-Build und die CheckStyle-Prüfung. |
| Kontext ↔ Bausteine (S3 ↔ S5) | 🟡 | Remisangebote werden zugesagt, aber nicht unterstützt. Die Endspieloption ist nicht gekennzeichnet, und die Vermittlung des Computergegners ist nur inferierbar. |
| Sichten-Konsistenz (S5 ↔ S6 ↔ S7) | 🟢 | Die Bibliotheksabfrage in S6 ist keiner Deployment-Variante zugeordnet (S7 „ohne Eröffnungsbibliothek“). |
| Konzepte ↔ Entscheidungen (S8 ↔ S9) | 🟡 | DI-Framework-Verzicht, Logging- und Tracing-Verzicht und der Fehlervertrag sind nur im Konzept entschieden, eine ADR fehlt jeweils. |
| Risiken ↔ Qualität (S11 ↔ S1/S10) | 🔴 | Fehler- und Legalitätsrisiken (F01/Z02 vs. 8.4) fehlen in S11. Änderbarkeit hat keine Risikobetrachtung, Verständlichkeit und K01 sind nicht abgesichert. |

### 1. Qualitätsstrang (S1 ↔ S4 ↔ S10)

**Zuordnungsmatrix**

| Qualitätsziel (S1.2), Rang | Strategieansatz (S4) | Szenario (S10) | Status |
|---|---|---|---|
| Analysierbarkeit, 1 | arc42-Gliederung, Domänenmodell, deutsche Namen, Javadoc; Verständlichkeit vor Effizienz¹ | W01, W02, W03, W05 | ⚠️ Teilweise unscharfe Akzeptanzkriterien |
| Änderbarkeit, 2 | Java, Kerninterfaces, unveränderliche Objekte, DI, Testabdeckung; Zerlegung, Algorithmusaustausch¹ | W04, W05, P01 | ✅ |
| Interoperabilität, 3 | XBoard, portables Java | K01 | ✅ |
| Akzeptable Spielstärke, 4 | Eröffnungsbibliotheken, Minimax, Stellungsbewertung, taktische Integrationstests | F02, F03, F04 | ⚠️ Kein Nachweis des Gegnerbezugs |
| Effizienz, 5 | Reactive Extensions, Alpha-Beta, effizientes Domänenmodell, Zeittests; reaktive Anbindung¹ | E01, E02 | ⚠️ Zeitvertrag unvollständig |
| – | Schachregelimplementierung (4.2) | F01 | ✅ Basisanforderung aus 1.1 |
| – | Keine Validierungs-/Wiederherstellungsstrategie | Z01, Z02 | ⚠️ |

¹ `evidence=inferred`

#### [KQS-01] Fehlerfallzusagen ohne strategische Absicherung

**Konflikttyp:** K4
**Schwere:** 🟡 Warnung
**Beteiligte Sektionen:** S4 ↔ S10 (S1.1)
**Betroffene Dateien:**
- [arc-doc/04-Loesungsstrategie/04-02-Aufbau.md](arc-doc/04-Loesungsstrategie/04-02-Aufbau.md#L7) — „eine Implementierung der Schachregeln“
- [arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L26) — Z01 „spielt fehlerfrei weiter“; Z02 „erkennt die Situation und beendet das Spiel“

**Beschreibung:** Dass es ein Regelmodul gibt, erklärt nicht, wie unzulässige Eingaben erkannt und Zustandsänderungen verhindert werden.

**Lösungsvorschlag:** In S4.2 ergänzen:
> Zur Erfüllung von Z01 und Z02 werden gegnerische Züge und Anfangsstellungen vor ihrer Übernahme durch die Schachregelkomponente validiert. Bei einem unzulässigen Gegenzug bleibt der Spielzustand unverändert; die Protokollanbindung meldet den Fehler und nimmt einen neuen Zug entgegen. Bei einer unzulässigen Anfangsstellung wird keine Zugberechnung gestartet und das Spiel mit einer Fehlermeldung beendet.

#### [KQS-02] Zeitgrenzen ohne eindeutigen Geltungsbereich und Durchsetzungsmechanismus

**Konflikttyp:** K4/K5
**Schwere:** 🟡 Warnung
**Beteiligte Sektionen:** S1 ↔ S4 ↔ S10
**Betroffene Dateien:**
- [arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md](arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md#L13) — „erfolgt die Berechnung der Spielzüge rasch“
- [arc-doc/04-Loesungsstrategie/04-03-Spielstrategie.md](arc-doc/04-Loesungsstrategie/04-03-Spielstrategie.md#L7) — „mit fester Suchtiefe“
- [arc-doc/04-Loesungsstrategie/04-04-Anbindung.md](arc-doc/04-Loesungsstrategie/04-04-Anbindung.md#L13) — „ein Benutzer kann zum Beispiel ein sofortiges Ziehen erzwingen“
- [arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L24) — E01 fünf Sekunden, E02 zehn Sekunden für den ersten Zug

**Beschreibung:** Eine feste Suchtiefe begrenzt die Laufzeit nicht. Das manuelle Erzwingen eines Zugs garantiert keine automatische Fristeinhaltung. Zudem ist unklar, ob E02 eine Ausnahme von E01 sein soll.

**Lösungsvorschlag:** In S10 (siehe S10-01) und als Ansatz in S4.4 aufnehmen:
> Die Engine überwacht das jeweilige Zeitbudget (E01/E02) automatisch, hält einen regelkonformen Ersatz-Zug bereit und beendet die Suche rechtzeitig vor Ablauf der Ausgabefrist.

#### [KQS-03] Taktische Einzelszenarien belegen das Spielstärkeziel nicht

**Konflikttyp:** K5
**Schwere:** 🟡 Warnung
**Beteiligte Sektionen:** S1 ↔ S4 ↔ S10
**Betroffene Dateien:**
- [arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md](arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md#L12) — „schwache Gegner sicher zu schlagen und Gelegenheitsspieler zumindest zu fordern“
- [arc-doc/04-Loesungsstrategie/04-02-Aufbau.md](arc-doc/04-Loesungsstrategie/04-02-Aufbau.md#L17) — „erreicht DokChess eine akzeptable Spielstärke, wie ein Durchspielen der entsprechenden Szenarien zeigt“
- [arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L21) — F02–F04

**Beschreibung:** Die Erreichungsbehauptung in S4.2 geht über den beschriebenen Nachweis hinaus.

**Lösungsvorschlag:** S4.2 anpassen und F05 gemäß S10-02 ergänzen:
> F02–F04 prüfen taktische Mindestfähigkeiten; das gegnerbezogene Spielstärkeziel wird zusätzlich durch Szenario F05 (Partien gegen Referenzgegner) bewertet.

#### [KQS-04] Auffindbarkeitszusagen nicht reproduzierbar prüfbar

**Konflikttyp:** K5
**Schwere:** 🟡 Warnung
**Beteiligte Sektionen:** S1 ↔ S4 ↔ S10
**Betroffene Dateien:**
- [arc-doc/04-Loesungsstrategie/04-01-Einstieg.md](arc-doc/04-Loesungsstrategie/04-01-Einstieg.md#L9) — „Architekturüberblick gegliedert nach arc42“; „Modul-, Klassen- und Methodennamen in Deutsch“
- [arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L14) — W02 „unverzüglich“; W03 „ohne Umwege oder fremde Hilfe“

**Beschreibung:** Mit „unverzüglich“ und „ohne Umwege“ lässt sich nicht reproduzierbar abnehmen, ob die Strategieansätze wirken.

**Lösungsvorschlag:** W02/W03 präzisieren wie in S10-03 (60 Sekunden je Kapitel; zwei Minuten je Modul der Ebene 1).

---

### 2. Strategie ↔ Entscheidungen (S4 ↔ S9)

**Zuordnungsmatrix**

| Strategische Festlegung (S4) | Entscheidung (S9) | Status |
|---|---|---|
| XBoard-Protokoll; stdin/stdout statt eigener GUI | ADR 09-01 | ✅ |
| Unveränderliche Stellung | ADR 09-02 | ✅ |
| Unveränderlichkeit aller fachlichen Klassen | ADR 09-02 nur für `Stellung` | 🔲 KSE-04 |
| Paralleler Minimax | ADR 09-02 (Weiterentwicklung) | ✅ |
| Kernabstraktionen, Zerlegung, Dependency Injection | – | 🔲 KSE-01 |
| Reactive Extensions, reaktive Anbindung | – | 🔲 KSE-02 |
| Polyglot; Minimax, Materialbewertung, Alpha-Beta | – | 🔲 KSE-03 |

#### [KSE-01] Austauschbare Modularchitektur ohne dokumentierte Entscheidung

**Konflikttyp:** K4 – Strategie ohne Entscheidungsgrundlage
**Schwere:** 🟡 Warnung
**Beteiligte Sektionen:** S4 ↔ S9
**Betroffene Dateien:**
- [arc-doc/04-Loesungsstrategie/04-02-Aufbau.md](arc-doc/04-Loesungsstrategie/04-02-Aufbau.md#L12) — „Alle Teile sind durch Schnittstellen abstrahiert, die Implementierungen werden per Dependency Injection zusammengesteckt“
- [arc-doc/09-Entscheidungen/09-01-Anbindung.md](arc-doc/09-Entscheidungen/09-01-Anbindung.md#L55) — „ohne die Engine selbst zu veraendern“

**Beschreibung:** ADR 09-01 setzt Austauschbarkeit voraus, entscheidet aber nur über das Protokoll.

**Lösungsvorschlag:** ADR-Entwurf in S9 ergänzen und aus S4.2 verlinken:
> **Status: Proposed. Kontext:** Protokolle, Eröffnungsformate und Schachalgorithmen sollen unabhängig austauschbar und testbar sein. **Entscheidung:** Die vier Hauptteile werden über Schnittstellen gekoppelt und per Dependency Injection zusammengesetzt. **Konsequenzen:** Austausch und isolierte Tests werden erleichtert; zusätzliche Schnittstellen und eine explizite Verdrahtung sind erforderlich.

#### [KSE-02] Reaktive Anbindung ohne eigene Entscheidungsgrundlage

**Konflikttyp:** K4
**Schwere:** 🟡 Warnung
**Beteiligte Sektionen:** S4 ↔ S9
**Betroffene Dateien:**
- [arc-doc/04-Loesungsstrategie/04-04-Anbindung.md](arc-doc/04-Loesungsstrategie/04-04-Anbindung.md#L11) — „über einen reaktiven Ansatz („Reactive Extensions“) angebunden“
- [arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md](arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md#L50) — „Bessere Eignung fuer nebenlaeufige Ausfuehrung.“

**Beschreibung:** Unveränderlichkeit unterstützt Nebenläufigkeit, begründet aber nicht die Wahl von Reactive Extensions.

**Lösungsvorschlag:**
> **Status: Proposed. Kontext:** Während der Zugermittlung müssen Frontend-Kommandos bearbeitbar bleiben. **Entscheidung:** Die Engine wird über Reactive Extensions angebunden; neu gefundene bessere Züge werden als Ereignisse gemeldet. Eine blockierende Anbindung wird nicht gewählt. **Konsequenzen:** Ereignisreihenfolge, Suchabbruch und Fehlerweitergabe benötigen explizite Regeln (siehe S08-01, S08-02).

#### [KSE-03] Spielstrategie ohne nachvollziehbare Auswahlentscheidungen

**Konflikttyp:** K4
**Schwere:** 🟡 Warnung
**Beteiligte Sektionen:** S4 ↔ S9
**Betroffene Dateien:**
- [arc-doc/04-Loesungsstrategie/04-03-Spielstrategie.md](arc-doc/04-Loesungsstrategie/04-03-Spielstrategie.md#L5) — „Polyglot Opening Book“; „Minimax-Algorithmus mit fester Suchtiefe“; Bewertung „ausschließlich auf dem Material“
- [arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md](arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md#L44) — entschieden wird nur die Unveränderlichkeit

**Beschreibung:** Format-, Such- und Bewertungswahl werden nicht als Entscheidungen begründet.

**Lösungsvorschlag:**
> **Suchstrategie – Status: Proposed:** Als verständliche Referenz dienen sequenzieller Minimax mit fester Suchtiefe und reine Materialbewertung; Alpha-Beta und paralleler Minimax dienen als austauschbare Erweiterungsbeispiele.
> **Eröffnungsformat – Status: Proposed:** Eröffnungswissen wird über einen austauschbaren Polyglot-Adapter eingebunden, da Polyglot das einzige geläufige nicht-proprietäre Format ist (5.5, Konvention 2.3).

#### [KSE-04] Allgemeine Unveränderlichkeitsregel nur teilweise durch ADR gedeckt

**Konflikttyp:** K4 – Unvollständige Entscheidungsgrundlage
**Schwere:** 🟢 Hinweis
**Beteiligte Sektionen:** S4 ↔ S9
**Betroffene Dateien:**
- [arc-doc/04-Loesungsstrategie/04-02-Aufbau.md](arc-doc/04-Loesungsstrategie/04-02-Aufbau.md#L23) — „Wie alle anderen fachlichen Klassen ist auch sie unveränderlich“
- [arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md](arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md#L44) — „fuer `Stellung` die unveraenderliche Variante“

**Beschreibung:** Hier liegt kein Widerspruch vor, aber eine Reichweitenlücke. Zusätzlich lautet der Linktitel in 4.2/4.4 anders als die ADR-Titel („Sind Stellungsobjekte veränderlich oder nicht?“ bzw. „Wie kommuniziert die Engine mit der Außenwelt?“ statt „09-02 Stellungsobjekte …“ bzw. „09-01 Frontend-Anbindung“).

**Lösungsvorschlag:**
> Die Stellung ist unveränderlich; Entscheidung 9.2 dokumentiert diese Wahl und ihre Konsequenzen. Auch die übrigen fachlichen Klassen sind unveränderlich; diese weitergehende Entwurfsregel ist in Abschnitt 8.2 beschrieben.

---

### 3. Constraint-Compliance (S2 ↔ S4/S8/S9)

**Ergebnis:** Es gibt keine belegte Constraint-Verletzung, aber drei Nachweislücken. FEN-Zeichen und XBoard-Kommandos sind standardisierte Austauschsyntax und verletzen die deutsche Benennungsregel nicht. Auch englische ADR-Rubriken und transliterierte Umlaute in den ADRs verletzen die Benennungsregel nicht.

| Constraint (S2) | S4 | S8 | S9 | Status |
|---|---|---|---|---|
| Moderate Hardwareausstattung | ❓ | ❓ | ❓ | 🟡 KRC-01 |
| Windows-Desktop-Betrieb | ✅ | ✅ | ✅ | ✅ |
| Implementierung in Java | ✅ | ✅ | ✅ | ✅ |
| Fremdsoftware frei verfügbar | ✅ | ✅ | ✅ | ✅ |
| IDE-freier Gradle-Build | ❓ | ❓ | — | 🟡 KRC-02 |
| JUnit im Annotationsstil | ✅ | ✅ | — | ✅ |
| arc42-Template 6.0, deutsche Bezeichner, offene Schachformate | ✅ | ✅ | ✅ | ✅ |
| Java Coding Conventions / CheckStyle | — | ❓ | — | 🟡 KRC-03 |

#### [KRC-01] Notebook-Eignung trotz Effizienznachteilen nicht nachvollziehbar abgesichert

**Konflikttyp:** K4 – Verdachtsfall einer impliziten Verletzung
**Schwere:** 🟡 Warnung
**Beteiligte Sektionen:** S2 ↔ S4 / S8 / S9
**Betroffene Dateien:**
- [arc-doc/02-Randbedingungen/02-01-Technisch.md](arc-doc/02-Randbedingungen/02-01-Technisch.md#L7) — „Betrieb der Lösung auf einem marktüblichen Standard-Notebook“
- [arc-doc/04-Loesungsstrategie/04-02-Aufbau.md](arc-doc/04-Loesungsstrategie/04-02-Aufbau.md#L16) — „auf Kosten von Effizienz“
- [arc-doc/08-Konzepte/08-07-Testbarkeit.md](arc-doc/08-Konzepte/08-07-Testbarkeit.md#L39) — „Der Erfolg dieser Tests hängt von der eingesetzten Hardware ab.“
- [arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md](arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md#L50) — „ca. 30 Prozent laengerer Laufzeit“; „Hoeherer Speicherbedarf“

**Beschreibung:** Aus relativen Laufzeitangaben ohne Referenzhardware lässt sich die Einhaltung nicht prüfen.

**Lösungsvorschlag:** In S8.7 ergänzen und in ADR 9.2 referenzieren:
> Die Einhaltung von S2.1 wird auf einem dokumentierten marktüblichen Standard-Notebook geprüft. Der Nachweis nennt CPU, RAM, Windows- und JVM-Version, JVM-Speichergrenze, Suchalgorithmus und Suchtiefe sowie die gemessenen Antwortzeiten und den maximalen Speicherbedarf einschließlich des Frontends.

#### [KRC-02] Verbindlicher IDE-freier Gradle-Build ohne Umsetzungskonzept

**Konflikttyp:** K4
**Schwere:** 🟡 Warnung
**Beteiligte Sektionen:** S2 ↔ S4 / S8
**Betroffene Dateien:**
- [arc-doc/02-Randbedingungen/02-02-Organisatorisch.md](arc-doc/02-Randbedingungen/02-02-Organisatorisch.md#L10) — „Die Software muss jedoch auch, allein mit Gradle, also ohne IDE baubar sein.“
- [arc-doc/08-Konzepte/08-07-Testbarkeit.md](arc-doc/08-Konzepte/08-07-Testbarkeit.md#L14) — Integrationstests unter „src/integTest“

**Beschreibung:** S4, S8 und S9 nennen keine Gradle-Aufgaben, Voraussetzungen oder die Einbindung der Integrationstests.

**Lösungsvorschlag:** In S8.7 ergänzen:
> Gemäß S2.2 muss DokChess aus einem frischen Checkout ohne Eclipse oder IntelliJ allein mit Gradle baubar sein. Die Build-Dokumentation benennt die erforderlichen JDK- und Gradle-Versionen sowie die Befehle für Kompilierung, Paketierung, Unit-Tests und Integrationstests aus src/integTest.

#### [KRC-03] Vorgeschriebene CheckStyle-Prüfung nicht im Prüfkonzept verankert

**Konflikttyp:** K3 – ungeprüfte Konventions-Einhaltung
**Schwere:** 🟡 Warnung
**Beteiligte Sektionen:** S2 ↔ S8
**Betroffene Dateien:**
- [arc-doc/02-Randbedingungen/02-03-Konventionen.md](arc-doc/02-Randbedingungen/02-03-Konventionen.md#L8) — „geprüft mit Hilfe von CheckStyle“
- [arc-doc/08-Konzepte/08-07-Testbarkeit.md](arc-doc/08-Konzepte/08-07-Testbarkeit.md#L9) — nur JUnit-Tests beschrieben

**Beschreibung:** JUnit ersetzt CheckStyle nicht.

**Lösungsvorschlag:** In S8.7 ergänzen:
> Zusätzlich zu den JUnit-Tests prüft CheckStyle die Java-Quelltexte gemäß S2.3. Regelkonfiguration, Werkzeugversion und Gradle-Aufruf werden versioniert dokumentiert; Regelverstöße lassen den Prüfschritt fehlschlagen.

---

### 4. Kontext ↔ Bausteine (S3 ↔ S5)

| Externer Partner | S3 | S5 | Status |
|---|---|---|---|
| Menschlicher Gegner | Züge und Remisangebote | XBoard-Protokoll (inferred) | 🟡 Remisangebote nicht unterstützt |
| Computergegner | Alternative zum Menschen | XBoard-Protokoll (inferred) | 🟡 Vermittlung nicht beschrieben |
| Eröffnungen | Optionaler Wissenslieferant | Eröffnung (inferred) | ✅ |
| Endspiele | Fachlich optional, technisch nicht implementiert | – | 🟡 |
| XBoard Client | Externes Frontend | XBoard-Protokoll (explicit) | ✅ |
| Polyglot Opening Book | Optionale Datei, lesend | Eröffnung (explicit) | ✅ |

#### [KKB-01] Remisangebote zugesagt, aber nicht unterstützt

**Konflikttyp:** K1 – Kontextschnittstelle teilweise ohne Umsetzung
**Schwere:** 🟡 Warnung
**Beteiligte Sektionen:** S3 ↔ S5
**Betroffene Dateien:**
- [arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md#L13) — „über ihre Züge, oder über Remisangebote“
- [arc-doc/05-Bausteinsicht/05-02-XBoard-Protokoll.md](arc-doc/05-Bausteinsicht/05-02-XBoard-Protokoll.md#L35) — nicht unterstützt: „Remis-Angebote und Aufgabe der anderen Seite“

**Beschreibung:** Der zuständige Baustein deckt den in S3 genannten Austausch ausdrücklich nicht ab. Siehe auch S03-01.

**Lösungsvorschlag:**
> DokChess und der Gegner tauschen insbesondere ihre Züge aus. Remisangebote gehören zum fachlichen Kommunikationsbedarf, werden vom aktuellen Implementierungsstand jedoch nicht unterstützt (siehe Abschnitt 5.2, „Offene Punkte“). Diese Einschränkung gilt auch für Computergegner.

#### [KKB-02] Endspielpartner ohne Kennzeichnung als Zukunftsoption

**Konflikttyp:** K1 – Kontextpartner ohne Bausteinzuordnung
**Schwere:** 🟡 Warnung
**Beteiligte Sektionen:** S3 ↔ S5
**Betroffene Dateien:**
- [arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md#L33) — „Stattdessen kann (optional) eine angebunden werden“
- [arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md](arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md#L21) — „aus Aufwandsgründen Abstand genommen“
- [arc-doc/05-Bausteinsicht/05-01-Ebene-1.md](arc-doc/05-Bausteinsicht/05-01-Ebene-1.md#L5) — vier Subsysteme, kein Endspieladapter

**Beschreibung:** Die Darstellung ist unstimmig, ein Implementierungsfehler liegt nicht vor. Siehe auch S03-04.

**Lösungsvorschlag:**
> Endspieldatenbanken sind ausschließlich eine zukünftige Erweiterungsoption. Der aktuelle Stand besitzt weder eine technische Anbindung noch einen zugeordneten Baustein oder Außenport in Ebene 1.

#### [KKB-03] Technische Vermittlung des Computergegners nur inferierbar

**Konflikttyp:** K1 – unvollständige explizite Schnittstellenzuordnung
**Schwere:** 🟡 Warnung
**Beteiligte Sektionen:** S3 ↔ S5
**Betroffene Dateien:**
- [arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md#L17) — „auch gegen eine andere Engine antreten“
- [arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md](arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md#L11) — nur „Anbindung menschlicher Spieler“
- [arc-doc/05-Bausteinsicht/05-02-XBoard-Protokoll.md](arc-doc/05-Bausteinsicht/05-02-XBoard-Protokoll.md#L7) — „Kommunikation mit einem Client“

**Beschreibung:** Nur 8.3 bestätigt die Vermittlung über ein Frontend. In S3 und S5 fehlt die Zuordnung. Siehe auch S03-03.

**Lösungsvorschlag:** In S3.2 und S5.2 ergänzen:
> Bei Partien gegen eine andere Schach-Engine vermittelt ein externes Schachfrontend die Kommunikation. Aus Sicht von DokChess bleibt dieses Frontend der XBoard-Client; eine separate direkte Schnittstelle zum Computergegner ist nicht vorgesehen.

---

### 5. Sichten-Konsistenz (S5 ↔ S6 ↔ S7)

| Baustein | S5 | S6 | S7 | Status |
|---|---|---|---|---|
| XBoard-Protokoll | 5.2 | explizit | DokChess.jar | ✅ |
| Spielregeln | 5.3 | explizit | DokChess.jar | ✅ |
| Engine | 5.4 | explizit | DokChess.jar | ✅ |
| Eröffnung | 5.5 | explizit (liefereZug : null) | im JAR; Betrieb ohne Bibliothek | 🟢 KSV-01 |
| Zugsuche / Stellungsbewertung | 5.7 / 5.8 | inferred, hinter Engine | über Engine/JAR | ✅ Verfeinerung |

K1–K3, K5 und K6 sind ohne Befund: Es gibt keine unbekannten oder verwaisten Bausteine, und Verantwortlichkeiten und Abstraktionsebenen sind konsistent.

#### [KSV-01] Optionale Bibliotheksabfrage keiner Deployment-Variante zugeordnet

**Konflikttyp:** K4 – fehlende Nutzungsbedingung
**Schwere:** 🟢 Hinweis
**Beteiligte Sektionen:** S5 ↔ S6 ↔ S7
**Betroffene Dateien:**
- [arc-doc/05-Bausteinsicht/05-04-Engine.md](arc-doc/05-Bausteinsicht/05-04-Engine.md#L7) — „die Eröffnungsbibliothek hingegen ist optional“
- [arc-doc/06-Laufzeitsicht/06-01-Zugermittlung.md](arc-doc/06-Laufzeitsicht/06-01-Zugermittlung.md#L17) — „Im Beispiel ist das nicht der Fall.“
- [arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md](arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md#L5) — „ohne Eröffnungsbibliothek“

**Beschreibung:** S6 zeigt eine konfigurierte Bibliothek ohne Treffer, S7 den Betrieb ohne Bibliothek. Beides sind zulässige Konfigurationen, aber sie sind nicht als solche gekennzeichnet.

**Lösungsvorschlag:** In S6 ersetzen:
> Der Walkthrough zeigt die Variante mit konfigurierter Eröffnungsbibliothek. Die Engine fragt diese zunächst über `liefereZug` ab; im Beispiel liefert sie `null`, anschließend beginnt die Zugsuche. Im Windows-Deployment aus Abschnitt 7.1 ist keine Eröffnungsbibliothek konfiguriert; dort entfällt die Abfrage.

Im Sequenzdiagramm die Abfrage als `opt [Eröffnungsbibliothek konfiguriert]` kennzeichnen.

---

### 6. Konzepte ↔ Entscheidungen (S8 ↔ S9)

| Element | Sektion | Korrekte Zuordnung? | Ergebnis |
|---|---|---|---|
| Abhängigkeiten | S8.1 | Teilweise | Framework-Verzicht ist eine Entscheidung (KKE-01) |
| Domänenmodell | S8.2 | Ja | `based_on` ADR 9.2 explizit |
| Benutzungsoberfläche | S8.3 | Ja | `based_on` ADR 9.1 explizit |
| Validierung | S8.4 | Ja | Passt zu ADR 9.1 |
| Fehlerbehandlung | S8.5 | Ja, Entscheidungsgrundlage fehlt | KKE-03 |
| Logging/Tracing | S8.6 | Teilweise | Bewusster Verzicht ist Entscheidung (KKE-02) |
| Testbarkeit | S8.7 | Ja | – |

#### [KKE-01] Framework-Verzicht wird ausschließlich im Konzept entschieden

**Konflikttyp:** K2 – Falsche Zuordnung
**Schwere:** 🟡 Warnung
**Beteiligte Sektionen:** S8 ↔ S9
**Betroffene Dateien:**
- [arc-doc/08-Konzepte/08-01-Abhaengigkeiten.md](arc-doc/08-Konzepte/08-01-Abhaengigkeiten.md#L12) — „DokChess verzichtet auf die Verwendung eines speziellen DI Frameworks.“; „keine annotationsgetriebene Konfiguration“

**Beschreibung:** Der systemweite Verzicht auf ein Framework ist eine Wahl zwischen Alternativen. Eine ADR dazu fehlt.

**Lösungsvorschlag:**
> **Titel:** Framework-unabhängige Modulverdrahtung. **Status:** Proposed. **Kontext:** DokChess soll alternative Modulimplementierungen und frei wählbare DI-Lösungen ermöglichen. **Alternativen:** Manuelle Verdrahtung oder verbindliche Integration eines DI-Frameworks. **Entscheidung:** Setter-Injection ohne verpflichtendes DI-Framework und ohne frameworkgebundene Annotationen; Verdrahtung ausschließlich in Glue-Code und Tests. **Konsequenzen:** Spring oder CDI können ergänzt werden; die Standardverdrahtung muss manuell gepflegt werden. Umsetzung: Abschnitt 8.1.

#### [KKE-02] Verzicht auf internes Logging und Tracing steht in der Konzeptsektion

**Konflikttyp:** K2 – Falsche Zuordnung
**Schwere:** 🟡 Warnung
**Beteiligte Sektionen:** S8 ↔ S9
**Betroffene Dateien:**
- [arc-doc/08-Konzepte/08-06-Logging.md](arc-doc/08-Konzepte/08-06-Logging.md#L10) — „keine feinkörnigen Logging-Ausgaben; Lösungen wie log4j kommen nicht zum Einsatz“; „auf die Implementierung eines Kommunikationsprotokoll-Tracings … verzichtet“

**Beschreibung:** Hier stehen zwei bewusst begründete Architekturfestlegungen ohne ADR.

**Lösungsvorschlag:**
> **Titel:** Diagnose ohne internes Logging und Protokoll-Tracing. **Status:** Proposed. **Entscheidung:** DokChess implementiert weder feinkörniges internes Logging noch eigenes Kommunikationsprotokoll-Tracing und bindet keine Logging-Bibliothek ein. **Konsequenzen:** Keine zusätzlichen Abhängigkeiten; interne Abläufe sind bei Laufzeitfehlern weniger sichtbar; Kommunikationsdiagnosen benötigen ein Frontend. Abschnitt 8.6 beschreibt das Diagnosevorgehen.

#### [KKE-03] Modulübergreifender Fehlervertrag ohne Entscheidungsgrundlage

**Konflikttyp:** K4 – Fehlende Entscheidung
**Schwere:** 🟡 Warnung
**Beteiligte Sektionen:** S8 ↔ S9
**Betroffene Dateien:**
- [arc-doc/08-Konzepte/08-05-Fehlerbehandlung.md](arc-doc/08-Konzepte/08-05-Fehlerbehandlung.md#L7) — „Runtime Exceptions“, „onError“; Checked Exceptions „sind geeignet zu verpacken“
- [arc-doc/09-Entscheidungen/09-01-Anbindung.md](arc-doc/09-Entscheidungen/09-01-Anbindung.md#L50) — nur Protokollwahl

**Beschreibung:** Der Fehlervertrag gilt auch für Erweiterungen und bestimmt damit modulübergreifende Schnittstellen.

**Lösungsvorschlag:**
> **Titel:** Einheitlicher Fehlervertrag für Subsysteme. **Status:** Proposed. **Alternativen:** Checked Exceptions, Ergebnisobjekte oder Runtime Exceptions mit asynchronem Fehlerkanal. **Entscheidung:** Synchrone Aufrufe melden Fehler über Runtime Exceptions; Checked Exceptions werden verpackt. Asynchrone Zugermittlung meldet zusätzlich über onError. Das XBoard-Subsystem übersetzt Fehler in tellusererror. **Konsequenzen:** Erweiterungen müssen diesen Vertrag einhalten; die Fehleranzeige garantiert keinen weiterhin gültigen Spielzustand.

---

### 7. Risiken ↔ Qualität (S11 ↔ S1/S10)

| Qualitätsziel, Rang | Bedrohende Risiken | Maßnahmen | Status |
|---|---|---|---|
| Analysierbarkeit, 1 | 11.1¹, 11.3 | PoC; Schachaufgaben | ⚠️ Verständlichkeit nicht gezielt abgesichert |
| Änderbarkeit, 2 | – | – | ⚠️ Blinder Fleck |
| Interoperabilität, 3 | 11.1¹ | PoC¹ | ⚠️ Nachweis K01 fehlt |
| Funktionale Eignung, 4 | 11.2¹, 11.3 | Umfangsreduktion; F02–F04-Tests¹ | ⚠️ Legalitätsrisiken fehlen |
| Effizienz, 5 | 11.3 | Szenarien/Tests¹ | ⚠️ Teilweise |

¹ `evidence=inferred`

#### [KRQ-01] Fehler- und Legalitätsrisiken fehlen trotz dokumentierter Einschränkungen

**Konflikttyp:** K4 – Implizites Risiko nicht dokumentiert
**Schwere:** 🔴 Kritisch
**Beteiligte Sektionen:** S10 ↔ S11 (S8 als Beleg)
**Betroffene Dateien:**
- [arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L19) — F01 „antwortet mit einem dieser Züge“; Z02 „erkennt die Situation und beendet das Spiel“
- [arc-doc/08-Konzepte/08-04-Validierung.md](arc-doc/08-Konzepte/08-04-Validierung.md#L12) — „nicht aber, ob die Position zulässig ist“; „Im Extremfall antwortet die Engine mit einem ungültigen Zug.“
- [arc-doc/08-Konzepte/08-05-Fehlerbehandlung.md](arc-doc/08-Konzepte/08-05-Fehlerbehandlung.md#L17) — „DokChess arbeitet dann “normal” weiter“
- [arc-doc/11-Risiken/11-02-Aufwand.md](arc-doc/11-Risiken/11-02-Aufwand.md#L3) — betrachtet nur den Implementierungsumfang

**Beschreibung:** Die Architektur dokumentiert selbst, dass F01 und Z02 gefährdet sind, behandelt das aber in S11 nicht als Risiko. Z02 („beendet das Spiel“) widerspricht direkt 8.4 (keine Prüfung der Zulässigkeit) und 8.5 (Weiterarbeiten). Siehe auch S11-01.

**Lösungsvorschlag:** In S11 ergänzen (siehe S11-01) und Z02 bis zur Umsetzung als „nicht erfüllt“ kennzeichnen:
> **Risiko: Ungültige Eingaben oder Bibliothekszüge verletzen F01/Z01/Z02.** Maßnahmen: Stellung vor Suchbeginn validieren, jeden Bibliothekszug auf Legalität prüfen und Z01/Z02 durch Integrationstests einschließlich Zustandsprüfung absichern. Bis zur Umsetzung bleibt insbesondere Z02 nicht erfüllt.

#### [KRQ-02] Hochpriorisierte Änderbarkeit ohne Risikobetrachtung

**Konflikttyp:** K1 – Blinder Fleck
**Schwere:** 🟡 Warnung
**Beteiligte Sektionen:** S1 ↔ S10 ↔ S11
**Betroffene Dateien:**
- [arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md](arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md#L10) — „können leicht implementiert und in die Lösung integriert werden“
- [arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L16) — W04, W05 „maximal eine Woche“

**Beschreibung:** Das zweitwichtigste Ziel hat keine Risikozuordnung. Dabei hängen laut ADR 9.2 „saemtliche Module“ von der Schnittstelle der Stellung ab, was W05 gefährdet.

**Lösungsvorschlag:**
> **Risiko: Erweiterungen erfordern Änderungen am bestehenden Code oder überschreiten W05.** Betroffen sind Änderbarkeit sowie W04, W05 und P01. Maßnahmen: eine alternative Bewertung und einen zusätzlichen Protokolladapter integrieren, ohne bestehenden Code zu ändern; den Bitboard-Austausch als zeitlich begrenzten Versuch durchführen und den Aufwand protokollieren.

#### [KRQ-03] Spielstärketests schützen das wichtigste Qualitätsziel nicht ausreichend

**Konflikttyp:** K2 – Teilweise unmitigiertes Qualitätsrisiko
**Schwere:** 🟡 Warnung
**Beteiligte Sektionen:** S1 ↔ S10 ↔ S11
**Betroffene Dateien:**
- [arc-doc/11-Risiken/11-03-Spielstaerke.md](arc-doc/11-Risiken/11-03-Spielstaerke.md#L5) — „konkurrierenden Ziele“; Maßnahme nur Spielstärke-Testfälle
- [arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L12) — W01 „innerhalb von 15 Minuten“

**Beschreibung:** Risiko 11.3 bedroht ausdrücklich auch die Zugänglichkeit. Die Maßnahmen prüfen jedoch nur die Spielstärke.

**Lösungsvorschlag:** In 11.3 ergänzen:
> Verständlichkeit wird unabhängig von der Spielstärke geprüft: Personen der vorgesehenen Zielgruppe bearbeiten W01–W03 ohne Hilfestellung. Spielstärkeoptimierungen werden nur übernommen, wenn die Verständlichkeitsprüfung weiterhin bestanden wird.

#### [KRQ-04] Anbindungs-PoC sichert die Zehn-Minuten-Zusage nicht nachweisbar ab

**Konflikttyp:** K4
**Schwere:** 🟡 Warnung
**Beteiligte Sektionen:** S10 ↔ S11
**Betroffene Dateien:**
- [arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L18) — K01 „innerhalb von zehn Minuten durchgeführt und getestet“
- [arc-doc/11-Risiken/11-01-Frontend.md](arc-doc/11-Risiken/11-01-Frontend.md#L20) — „Durch einen Proof of concept erreichen wir hier frühestmöglich Sicherheit.“

**Beschreibung:** PoC-Ergebnis und Restrisiko für K01 fehlen. Siehe auch S11-05.

**Lösungsvorschlag:** In 11.1 ergänzen:
> **Restrisiko:** Trotz funktionierender Protokollanbindung kann die Einrichtung K01 verfehlen. Der PoC wird um einen Einrichtungstest mit einem repräsentativen Frontend erweitert; Frontend-Version, Zeitbedarf und Ergebnis werden dokumentiert.

---

## Konfliktkarte

| Sektion | Involviert in Konflikten |
|---|---|
| S4 — Lösungsstrategie | 10 |
| S9 — Architekturentscheidungen | 8 |
| S10 — Qualitätsanforderungen | 8 |
| S8 — Querschnittliche Konzepte | 7 |
| S1 — Einführung/Ziele | 6 |
| S5 — Bausteinsicht | 4 |
| S11 — Risiken | 4 |
| S2 — Randbedingungen | 3 |
| S3 — Kontextabgrenzung | 3 |
| S6 — Laufzeitsicht | 1 |
| S7 — Verteilungssicht | 1 |

## Zusammenfassung

| Kategorie | Anzahl |
|---|---|
| 🔴 Kritische Befunde | 6 |
| 🟡 Warnungen / Empfehlungen | 72 |
| 🟢 Hinweise | 8 |

Aufteilung: In den Sektions-Reviews sind es 5 🔴, 53 🟡 und 6 🟢, insgesamt 64 Befunde. Die Konfliktanalyse ergab 1 🔴, 19 🟡 und 2 🟢, insgesamt 22 Konflikte. Mehrere Befunde beschreiben denselben Sachverhalt aus verschiedenen Blickwinkeln und sind über Querverweise verknüpft:
- Remisangebote: S03-01, S05-01, KKB-01
- Zeitgrenzen: S10-01, KQS-02
- Spielstärke: S01-02, S10-02, KQS-03
- Validierung: S11-01, KRQ-01, S10-06

### Handlungsempfehlungen

1. **Validierungsrisiko aufnehmen und Z02 auflösen** (S11-01, KRQ-01, S10-06, S08-02): Neues Risiko 11.4 „Ungeprüfte Eingabedaten“ anlegen. Den Widerspruch zwischen Z02 („erkennt … beendet das Spiel“) und 8.4/8.5 („nicht aber, ob die Position zulässig ist“, „arbeitet … weiter“) auflösen. Dafür entweder die Validierung umsetzen und in 8.4 dokumentieren oder Z02 ausdrücklich als nicht erfüllt kennzeichnen.
2. **Technische Schuld der Remisregeln korrekt ausweisen** (S11-02, S01-01): Die Aussage „keine [Konsequenzen] bezüglich der Korrektheit“ in 11.2 ersetzen. Den Widerspruch zu „Vollständige Implementierung der FIDE-Schachregeln“ (1.1) offenlegen.
3. **Kontextzusagen an den Implementierungsumfang anpassen** (S03-01, S05-01, KKB-01..03): In 3.1/3.2 Remisangebote, Aufgabe, Zeitkontrolle und Schachvarianten als nicht unterstützt kennzeichnen. Endspiele als reine Zukunftsoption markieren und die Vermittlung von Computergegnern über ein Frontend beschreiben.
4. **Zeitvertrag E01/E02 eindeutig festlegen** (S10-01, KQS-02, S07-03, KRC-01, S09-02): Geltungsbereich (erster Zug vs. Folgezüge), Messpunkte und Referenzhardware definieren. Einen automatischen Zeitbudget-Mechanismus in S4 beschreiben.
5. **Spielstärke über Partien operationalisieren** (S10-02, KQS-03, S01-02): F05 mit Referenzgegnern und Gewinnquote ergänzen und die Erreichungsbehauptung in 4.2 entsprechend relativieren.
6. **Fehlende ADRs nachziehen** (KSE-01..03, KKE-01..03): Für Modularchitektur/DI, Reactive Extensions, Such- und Bewertungsstrategie, Polyglot-Format, DI-Framework-Verzicht, Logging-Verzicht und Fehlervertrag kurze Nygard-ADRs erstellen. Bei ADR 9.1 Entscheidungsjahr 2011 und Übertragungsdatum 2026 trennen (S09-01).
7. **Bezeichnungen vereinheitlichen** (S04-01, S12-01, S12-02): Die Zeile „Attraktive Spielstärke (Attraktivität)“ in 4.1 an 1.2 angleichen. Homonyme im Glossar auflösen und „Stellung“ sowie „Zug“ ergänzen.
8. **Laufzeit- und Konzeptlücken schließen** (S06-01..03, S08-01, S08-03): Abbruch-, Fehler- und Bibliothekstreffer-Szenario ergänzen, Nebenläufigkeitsregeln festlegen und stdout für das Protokoll reservieren.
9. **Risikomanagement aktualisieren** (S11-03..07, KRQ-02..04): Risiken bewerten, ihren Status gegenüber 2011 kennzeichnen und ein Änderbarkeitsrisiko (W04/W05/P01) sowie das K01-Restrisiko ergänzen.
10. **Nachweise für Randbedingungen dokumentieren** (KRC-02, KRC-03, S02-06, S07-04): Gradle-Build ohne IDE, CheckStyle-Konfiguration, Startskript mit `java.exe` und skriptrelativem JAR-Pfad.
