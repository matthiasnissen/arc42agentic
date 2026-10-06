# arc42 Dokumentations-Review

**Dokumentation:** `arc-doc/` (Multi-Folder-Struktur, Sektionen 1–12 vollständig vorhanden, zusätzlich `00-Ueberblick`)
**Analyse-Modus:** DATEI-MODUS (rohe Markdown-Dateien, kein Wissensgraph)
**Review-Modus:** Vollständiges Review (12 Sektions-Reviews + 7 Konfliktdimensionen)

## Gesamtübersicht

| Sektion | Status | Befunde |
|---------|--------|---------|
| 1. Einführung und Ziele | 🟡 | Endnutzer/Demo-Rollen fehlen in Stakeholdern, Spielstärke-Zusage überdehnt, Szenario-Zuordnung nur indirekt |
| 2. Randbedingungen | 🟡 | Verbindlichkeit und Konsequenzen unklar; Java-Version, Hardware/Windows, GPLv3-Umfang und Schachformate unbestimmt |
| 3. Kontextabgrenzung | 🟡 | Datenflüsse nicht gerichtet, Remisangebote und Endspielanbindung vs. Umsetzungsstand, Computergegner-Kanal, Qualitätsbezug fehlen |
| 4. Lösungsstrategie | 🟡 | Spielstärke-Zielbezeichnung weicht von S1 ab, organisatorischer Ansatz unvollständig |
| 5. Bausteinsicht | 🟡 | Begründung der Zerlegung fehlt, Abbruch-/Randfallvertrag der Zugermittlung offen |
| 6. Laufzeitsicht | 🟡 | Nur ein Normalszenario; Abbruch, Fehlerpfade, Suche ohne Zugkandidaten und Engine-Interna fehlen |
| 7. Verteilungssicht | 🟡 | Motivation, Umgebungsabgrenzung und Hardware-/Performance-Rahmen fehlen |
| 8. Querschnittliche Konzepte | 🟡 | Asynchrone Fehlerbehandlung, Eingabevalidierung, Verlinkung und Testregeln unpräzise |
| 9. Architekturentscheidungen | 🟡 | Historische Bewertungsgrundlage (2011) bei Datum 2026; Performance-Abwägung ohne Messnachweis |
| 10. Qualitätsanforderungen | 🔴 | Akzeptable Spielstärke nicht ausreichend operationalisiert; mehrere Szenarien ohne Messbedingungen |
| 11. Risiken und technische Schulden | 🔴 | Bekannte Fehlerfolgen aus 8.4 fehlen; keine Priorisierung, historische Risiken nicht eingeordnet |
| 12. Glossar | 🟡 | Mehrere Definitionen unpräzise oder mehrdeutig, zentrale Begriffe fehlen |

## Sektions-Reviews

### Sektion 1: Einführung und Ziele

**Prüfmodus:** Vollständiger Review, DATEI-MODUS, ausschließlich lesend.

Alle drei Unterabschnitte sind vorhanden. Die Aufgabenstellung beschreibt den fachlichen Umfang und den didaktischen Zweck kompakt. Die fünf Qualitätsziele sind Architekturqualitäten; ihre Reihenfolge kennzeichnet die Priorität. Der Querverweis auf Sektion 10 funktioniert und erschließt konkrete, teilweise messbare Szenarien. Es wurden keine kritischen Mängel festgestellt.

#### [S01-01] Endnutzer und Verantwortliche für Demonstrationen fehlen

**Schwere:** 🟡 Empfehlung  
**Datei/Stelle:** [arc-doc/01-Einfuehrung-und-Ziele/01-03-Stakeholder.md](arc-doc/01-Einfuehrung-und-Ziele/01-03-Stakeholder.md#L7), Stakeholder-Tabelle  
**Kriterium:** 1.3 – Vollständigkeit relevanter Stakeholder-Gruppen

**Befund:** Menschliche Schachspieler werden in der Aufgabenstellung ausdrücklich als Nutzer genannt, fehlen aber in der Tabelle. Auch die Einrichtung und Durchführung von Live-Demonstrationen ist keiner Rolle ausdrücklich zugeordnet. Ein separater Produktionsbetrieb muss für dieses Fallbeispiel nicht unterstellt werden.

**Änderungsvorschlag:**
> Ergänze die Tabellenzeilen:  
> | Schachspielerinnen und Schachspieler | Nutzen DokChess über ein grafisches Schach-Frontend; erwarten regelkonformes Spiel, nachvollziehbare Fehlermeldungen und kurze Antwortzeiten. |  
> | Workshop- und Vortragsdurchführende | Richten Engine und Frontend für Demonstrationen ein; benötigen dokumentierte Voraussetzungen, Konfigurationsschritte und Hinweise zur Fehlerdiagnose. |

#### [S01-02] Erwartungen und Entscheidungsverantwortung bleiben unklar

**Schwere:** 🟡 Empfehlung  
**Datei/Stelle:** [arc-doc/01-Einfuehrung-und-Ziele/01-03-Stakeholder.md](arc-doc/01-Einfuehrung-und-Ziele/01-03-Stakeholder.md#L9), bestehende Stakeholder-Zeilen  
**Kriterium:** 1.3 – Erwartungen an Architektur und Dokumentation; Rollenbeschreibung

**Befund:** Die Tabelle beschreibt überwiegend Interessen und Motivation. Insbesondere bei Entwicklung, Stefan Zörner und oose bleiben konkrete Dokumentationserwartungen sowie Zuständigkeiten für Architekturentscheidungen offen. Sektion 2 nennt Stefan Zörner als zentralen Beteiligten des Entwicklungsteams, ohne die Entscheidungsverantwortung eindeutig festzulegen.

**Änderungsvorschlag:**
> Ergänze bei „Entwicklerinnen und Entwickler“: „Benötigen nachvollziehbare Modulgrenzen, Schnittstellen und Erweiterungspunkte sowie die Begründung zentraler Architekturentscheidungen.“  
> Ergänze bei „Stefan Zörner“: „Autor und Mitglied des Entwicklungsteams; benötigt ein konsistentes, nachvollziehbares Architekturbeispiel für Buch, Workshops und Vorträge.“  
> Ergänze bei „oose Innovative Informatik“: „Erwartet didaktisch geeignete und für Schulungen reproduzierbare Beispiele.“  
> Ergänze unterhalb der Tabelle: „Offen: Wer Architekturentscheidungen trifft und Änderungen an der Dokumentation freigibt, ist noch festzulegen.“

#### [S01-03] Spielstärkezusage geht über die referenzierten Szenarien hinaus

**Schwere:** 🟡 Empfehlung  
**Datei/Stelle:** [arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md](arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md#L12), „Akzeptable Spielstärke“  
**Kriterium:** 1.2 – Konkrete, messbare Qualitätsziele und passende Szenarien

**Befund:** „Schwache Gegner sicher zu schlagen“ verspricht einen Partieerfolg gegen eine nicht definierte Gegnerklasse. Die referenzierten Szenarien F02–F04 konkretisieren dagegen einzelne taktische Leistungen, nicht eine Gewinnquote oder Spielstärkeklasse. Sie operationalisieren diese Zusage daher nicht vollständig.

**Änderungsvorschlag:**
> Ersetze die Erläuterung durch: „DokChess nutzt typische taktische Gewinnmöglichkeiten: Es schlägt ungedeckte angegriffene Figuren, nutzt Springergabeln zum Materialgewinn und findet ein vorhandenes Matt in zwei Zügen. Maßgeblich sind die Szenarien F02–F04 in Abschnitt 10.2; eine garantierte Gewinnquote gegen bestimmte Gegner wird nicht zugesagt.“

#### [S01-04] Zuordnung der Qualitätsziele zu Szenarien ist nur indirekt sichtbar

**Schwere:** 🟢 Hinweis  
**Datei/Stelle:** [arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md](arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md#L15), Verweis auf Abschnitt 10  
**Kriterium:** 1.2 – Szenarien und überprüfbare Konkretisierung der Qualitätsziele

**Befund:** Szenarien fehlen nicht: Sie sind in Sektion 10 vorhanden, und der Qualitätsbaum beschreibt ihre Zuordnung. In Sektion 1 bleibt diese Zuordnung jedoch unspezifisch; Formulierungen wie „rasch“ und „angemessener Aufwand“ erhalten erst beim Nachschlagen überprüfbare Bedeutung.

**Änderungsvorschlag:**
> Ergänze: „Zur Konkretisierung dienen insbesondere W01–W03 für Analysierbarkeit, W04–W05 für Änderbarkeit, K01 für Interoperabilität, F02–F04 für Spielstärke und E01–E02 für Antwortzeiten. Beispiele für Zielwerte sind 15 Minuten für den Architektureinstieg, zehn Minuten für die Frontend-Konfiguration und fünf Sekunden für die Zugantwort gemäß E01.“

#### [S01-05] Anforderungsgrundlagen sind nicht referenziert

**Schwere:** 🟢 Hinweis  
**Datei/Stelle:** [arc-doc/01-Einfuehrung-und-Ziele/01-01-Aufgabenstellung.md](arc-doc/01-Einfuehrung-und-Ziele/01-01-Aufgabenstellung.md#L14), „Wesentliche Features“  
**Kriterium:** 1.1 – Verweise auf Anforderungsdokumente und fachliche Grundlagen

**Befund:** Der kompakte Feature-Überblick enthält keine Quellenverweise. Insbesondere bleibt bei „vollständiger Implementierung der FIDE-Schachregeln“ die maßgebliche Regelversion offen. Ein separates Anforderungsdokument wurde im gelesenen Kontext nicht nachgewiesen; dessen Existenz wird daher nicht vorausgesetzt.

**Änderungsvorschlag:**
> Ergänze: „Die wesentlichen funktionalen Anforderungen sind in dieser Aufgabenstellung zusammengefasst. Fachliche Grundlage sind die [FIDE Laws of Chess](https://handbook.fide.com/chapter/E012023); die für DokChess maßgebliche Fassung und ihr Gültigkeitsdatum sind noch festzulegen. Überprüfbare Qualitätsanforderungen beschreibt [Abschnitt 10.2](../10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md).“

**Befundanzahl:** 🔴 Kritisch: **0** · 🟡 Empfehlung: **3** · 🟢 Hinweis: **2** · Gesamt: **5**  
**Ampelstatus:** 🟡 **Gelb** – wesentliche Inhalte vorhanden; Konkretisierung und Ergänzung empfohlen.

### Sektion 2: Randbedingungen

**Prüfmodus:** Vollständiger Review im DATEI-MODUS. Die drei Sektionsdateien wurden vollständig gelesen; der Architekturüberblick wurde ergänzend berücksichtigt. Keine Dateien wurden verändert.

**Formales Ergebnis:** Sektion 2 ist vorhanden. Technische und organisatorische Randbedingungen sowie Konventionen sind klar getrennt und jeweils als Tabelle mit Erläuterungen dargestellt. Die wesentlichen Themen sind abgedeckt. Die folgenden Befunde betreffen die Präzisierung der Vorgaben und ihrer Konsequenzen.

#### [S02-01] Konsequenzen und Freiheitsgrade nicht durchgängig erläutert

**Schwere:** 🟡 Empfehlung  
**Datei/Stelle:** Alle drei Tabellen, insbesondere [Technisch](arc-doc/02-Randbedingungen/02-01-Technisch.md#L5), [Organisatorisch](arc-doc/02-Randbedingungen/02-02-Organisatorisch.md#L5) und [Konventionen](arc-doc/02-Randbedingungen/02-03-Konventionen.md#L5)  
**Kriterium:** Konsequenzen erläutern; verbindliche Vorgaben und architektonische Freiheitsgrade erkennbar machen.

**Befund:** Die Tabellen erklären überwiegend Motivation und Hintergrund. Architekturfolgen sind teilweise ableitbar, aber nicht systematisch benannt. Harte Vorgaben, Wünsche und frei wählbare Lösungen werden nicht durchgängig explizit unterschieden.

**Änderungsvorschlag:**
> Ergänzung unter den Tabellen: „Verbindlich sind die Implementierung in Java, der Betrieb unter Windows, der IDE-unabhängige Build mit Gradle und die Verwendung etablierter Schachformate. Unterstützung weiterer Betriebssysteme und kostenlose Fremdsoftware sind wünschenswert. Frei wählbar bleiben insbesondere die interne Komponentenzerlegung und die Such- und Bewertungsalgorithmen, soweit sie die übrigen Anforderungen erfüllen.“

#### [S02-02] Historische Java-Versionen ersetzen keine gültige Kompatibilitätsvorgabe

**Schwere:** 🟡 Empfehlung  
**Datei/Stelle:** [arc-doc/02-Randbedingungen/02-01-Technisch.md](arc-doc/02-Randbedingungen/02-01-Technisch.md#L9), Zeile „Implementierung in Java“  
**Kriterium:** Technische Einschränkungen und ihr Geltungsbereich eindeutig dokumentieren.

**Befund:** Java SE 6, 7 und 11 werden als Entwicklungshistorie aufgeführt. Welche Version für den dokumentierten Stand zum Bauen und Ausführen erforderlich ist, bleibt offen. „Auf neueren Java-Versionen“ ist zudem eine unbegrenzte Kompatibilitätsabsicht ohne definierten Nachweis.

**Änderungsvorschlag:**
> „Die Angaben zu Java SE 6, 7 und 11 beschreiben historische Entwicklungsstände. Für den hier dokumentierten Stand sind Mindestlaufzeit, Build-JDK und geprüfte Java-Versionen noch festzulegen. Kompatibilität mit künftigen Java-Versionen ist ein Ziel, aber keine bereits nachgewiesene Eigenschaft.“

#### [S02-03] Hardware- und Windows-Vorgaben bleiben unbestimmt

**Schwere:** 🟡 Empfehlung  
**Datei/Stelle:** [arc-doc/02-Randbedingungen/02-01-Technisch.md](arc-doc/02-Randbedingungen/02-01-Technisch.md#L7), Zeilen „Moderate Hardwareausstattung“ und „Betrieb auf Windows Desktop Betriebssystemen“  
**Kriterium:** Plattform- und Hardwareeinschränkungen so beschreiben, dass ihre Bedeutung für den Entwurf erkennbar ist.

**Befund:** „Marktübliches Standard-Notebook“ ist zeitabhängig; unterstützte Windows-Versionen und Architekturen fehlen. Damit lässt sich insbesondere die zulässige Ressourcenannahme für die Engine nicht eindeutig bestimmen.

**Änderungsvorschlag:**
> „Der Notebook-Betrieb ist verbindlich; eine konkrete Referenzkonfiguration ist noch festzulegen. Diese muss CPU, Arbeitsspeicher, Prozessorarchitektur, Windows-Version und Java-Laufzeit benennen. Bis dahin sind ‚Standard-Notebook‘ und ‚Windows Desktop‘ Zielbeschreibungen, keine überprüfbaren Mindestanforderungen.“

#### [S02-04] Umfang der GPLv3-Veröffentlichung bleibt offen

**Schwere:** 🟡 Empfehlung  
**Datei/Stelle:** [arc-doc/02-Randbedingungen/02-02-Organisatorisch.md](arc-doc/02-Randbedingungen/02-02-Organisatorisch.md#L13), Zeile „Veröffentlichung als Open Source“  
**Kriterium:** Organisatorische und rechtliche Vorgaben einschließlich ihrer Konsequenzen eindeutig erfassen.

**Befund:** Die Lizenz wird konkret genannt, der Veröffentlichungsumfang jedoch durch „oder zumindest Teile“ offengelassen. Es ist nicht erkennbar, welche eigenen Komponenten der Vorgabe unterliegen und wie separat bezogene Fremdsoftware abgegrenzt wird.

**Änderungsvorschlag:**
> „Die Veröffentlichung eigener Quelltexte unter GPLv3 ist vorgesehen. Der verbindliche Umfang ist noch offen und muss durch eine Liste der veröffentlichten Komponenten und gegebenenfalls ausgeschlossenen Teile konkretisiert werden. Separat bezogene Fremdsoftware ist mit ihrer jeweiligen Lizenz und Integrationsform gesondert auszuweisen.“

#### [S02-05] Vorgeschriebene Schachformate sind nicht benannt oder referenziert

**Schwere:** 🟡 Empfehlung  
**Datei/Stelle:** [arc-doc/02-Randbedingungen/02-03-Konventionen.md](arc-doc/02-Randbedingungen/02-03-Konventionen.md#L10), Zeile „Schach-Spezifische Datenformate“  
**Kriterium:** Relevante Konventionen konkret und eindeutig dokumentieren.

**Befund:** Das Verbot eigener Formate ist klar. Für Züge, Stellungen, Partien und Eröffnungen wird jedoch weder ein konkreter Standard noch ein Verweis auf dessen Festlegung angegeben. „Etablierte Standards“ allein legt die zulässigen Formate nicht fest.

**Änderungsvorschlag:**
> „Für jede verwendete Notation und jedes Austauschformat ist der gewählte Standard mit Spezifikationsreferenz und unterstütztem Umfang zu dokumentieren. Die Zuordnung zu Zügen, Stellungen, Partien und Eröffnungsdaten ist noch offen. Eigene Ersatzformate sind ausgeschlossen; offene Standards werden gegenüber proprietären bevorzugt.“

**Gesamtergebnis:** 🔴 Kritisch: **0** · 🟡 Empfehlung: **5** · 🟢 Hinweis: **0**  
**Ampelstatus:** 🟡 **Gelb**. Die Sektion ist strukturell vollständig und verständlich; mehrere Vorgaben benötigen Präzisierung, damit ihre Verbindlichkeit und Architekturfolgen eindeutig sind.

### Sektion 3: Kontextabgrenzung

**Prüfumfang:** Vollständiger Review im DATEI-MODUS, einschließlich beider Kontextdiagramme und Konsistenzabgleich mit Sektion 5. Keine Dateien wurden verändert.

Systemgrenze, fachlicher und technischer Kontext sowie Beschreibungen der Kommunikationspartner sind vorhanden. Die realisierten Außenanschlüsse stimmen grundsätzlich mit der Bausteinsicht überein: Standard-Ein-/Ausgabe und Eröffnungsbuchdatei. Folgende Abweichungen bleiben:

#### [S03-01] Fachliche Datenflüsse fehlen im Kontextdiagramm

**Schwere:** 🟡 Empfehlung  
**Datei:** [arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md#L5), Kontextdiagramm und Partnerbeschreibungen  
**Kriterium:** Kommunikationspartner mit fachlichen Ein-/Ausgaben spezifizieren; Datenflüsse statt bloßer Abhängigkeiten darstellen.

**Befund:** Die Diagrammkanten sind ungerichtet und unbeschriftet. Der Begleittext nennt Beispiele für den Austausch, beschreibt aber nicht systematisch dessen Richtung und Inhalt. Auch der Informationsfluss zu den Eröffnungsbibliotheken bleibt implizit.

**Änderungsvorschlag:**
> Die Beziehungen im Diagramm werden als gerichtete, beschriftete Informationsflüsse dargestellt: Gegner → DokChess: gegnerische Züge; DokChess → Gegner: eigene Züge. Eröffnungswissen → DokChess: Buchdaten zur Auswahl bekannter Eröffnungszüge. Für die nur geplante Endspielanbindung: Stellung als Anfrage; Bewertung und gegebenenfalls nächster Zug als Antwort. Die letzten beiden Flüsse kennzeichnen einen zukünftigen Ausbau, keine vorhandene Schnittstelle.

#### [S03-02] Remisangebote widersprechen dem implementierten Umfang

**Schwere:** 🟡 Empfehlung  
**Datei:** [arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md#L13), „Menschlicher Gegner“  
**Kriterium:** Konsistenz der externen Schnittstellen mit der Bausteinsicht.

**Befund:** Remisangebote werden als Beispiel des Austauschs genannt, ohne ihren Status einzuschränken. Die [XBoard-Blackbox](arc-doc/05-Bausteinsicht/05-02-XBoard-Protokoll.md#L40) schließt Remisangebote und die Aufgabe der anderen Seite ausdrücklich aus. Fachlicher Bedarf und realisierte Funktion sind nicht getrennt.

**Änderungsvorschlag:**
> DokChess und sein Gegner tauschen insbesondere ihre Züge aus. Zum allgemeinen fachlichen Austausch einer Schachpartie gehören auch Remisangebote und die Aufgabe eines Gegners; diese beiden Funktionen werden von der aktuellen XBoard-Implementierung jedoch nicht unterstützt (siehe Abschnitt 5.2).

#### [S03-03] Endspielanbindung ist fachlich nicht als Zukunftsumfang markiert

**Schwere:** 🟡 Empfehlung  
**Datei:** [arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md#L29), „Endspiele“ und Kontextdiagramm  
**Kriterium:** Eindeutige Systemabgrenzung; Konsistenz zwischen fachlichem Kontext, technischem Kontext und Bausteinsicht.

**Befund:** Die fachliche Grafik stellt Endspiele gleichrangig mit vorhandenen Partnern dar. „Kann (optional) eine angebunden werden“ unterscheidet nicht zwischen vorhandener Option und Erweiterungsmöglichkeit. Technisch wurde die Anbindung dagegen ausdrücklich nicht implementiert; entsprechend fehlt sie in Sektion 5.

**Änderungsvorschlag:**
> Endspieldatenbanken sind eine mögliche zukünftige Erweiterung. Die aktuelle Version von DokChess besitzt keine entsprechende Anbindung. Im fachlichen Kontextdiagramm wird diese Beziehung gestrichelt und mit „geplant, nicht implementiert“ gekennzeichnet.

#### [S03-04] Zuordnung der Gegner zum technischen Kanal bleibt unvollständig

**Schwere:** 🟡 Empfehlung  
**Datei:** [arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md](arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md#L9), „XBoard Client“ und technisches Kontextdiagramm  
**Kriterium:** Fachliche Kommunikationspartner auf technische Kanäle abbilden; Übertragungsmedien beschreiben.

**Befund:** Der Text erläutert nur die Anbindung menschlicher Spieler. Wie der Computergegner technisch vermittelt wird, bleibt offen. Das Diagramm nennt XBoard, aber nicht die in Sektion 5 dokumentierten Kanäle `stdin` und `stdout`. Das Eröffnungsbuchformat und der ausschließlich lesende Zugriff sind dagegen beschrieben.

**Änderungsvorschlag:**
> Der XBoard-Client ist der direkte technische Kommunikationspartner von DokChess. Befehle einschließlich gegnerischer Züge gelangen über die Standardeingabe (`stdin`) zur Engine; Antworten einschließlich eigener Züge werden über die Standardausgabe (`stdout`) zurückgegeben. Menschliche Spieler bedienen den Client. Für Engine-gegen-Engine-Partien ist die Vermittlung durch einen geeigneten Client zu beschreiben; eine direkte Engine-zu-Engine-Schnittstelle ist hier nicht dokumentiert.

#### [S03-05] Kompatibilitätsaussage ist zu weitgehend; Kontextrisiko fehlt

**Schwere:** 🟡 Empfehlung  
**Datei:** [arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md](arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md#L11), „XBoard Client“  
**Kriterium:** Schnittstellenumfang korrekt abgrenzen und Risiken an externen Abhängigkeiten explizit aufzeigen.

**Befund:** „Jedes grafische Frontend“ mit XBoard-Unterstützung suggeriert uneingeschränkte Kompatibilität. Sektion 5 dokumentiert jedoch nur eine Teilimplementierung. Das ausdrücklich dokumentierte [Frontend-Anbindungsrisiko](arc-doc/11-Risiken/11-01-Frontend.md#L3) wird im Kontext nicht aufgegriffen; die genannten Frontends werden nicht nach Kompatibilitätsnachweis unterschieden.

**Änderungsvorschlag:**
> Als Frontends kommen XBoard/WinBoard, Arena und Aquarium grundsätzlich infrage. Voraussetzung ist die Kompatibilität mit dem von DokChess implementierten XBoard-Teilumfang; die Protokollunterstützung allein ist kein Nachweis. Nicht unterstützt werden Zeitkontrolle, Permanent Brain, Remisangebote, Aufgabe der anderen Seite und Schachvarianten (Abschnitt 5.2). Risiko: Ein Client kann zusätzliche Funktionen voraussetzen. Die Anbindung ist deshalb durch einen Proof of Concept abzusichern (Abschnitt 11.1); getestete Frontends und Versionen sind gesondert auszuweisen.

#### [S03-06] Qualitätsanforderungen sind nicht den Außenanschlüssen zugeordnet

**Schwere:** 🟡 Empfehlung  
**Datei:** [arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md](arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md#L9), technische Schnittstellenbeschreibungen  
**Kriterium:** Qualitätsanforderungen an externen Schnittstellen berücksichtigen.

**Befund:** Es fehlt die Zuordnung der vorhandenen Qualitätsszenarien zur Client-Schnittstelle. Insbesondere Konfigurierbarkeit, Antwortzeiten, Rückmeldung und der Umgang mit ungültigen Eingaben bleiben im technischen Kontext unreferenziert, obwohl sie in Sektion 10 konkretisiert sind.

**Änderungsvorschlag:**
> Für die XBoard-Client-Schnittstelle gelten die Qualitätsszenarien aus Abschnitt 10.2: K01 verlangt Einbindung ohne Programmierung innerhalb von zehn Minuten; E01 eine Zugantwort innerhalb von fünf Sekunden. E02 verlangt beim ersten Zug als Schwarz eine Antwort innerhalb von zehn Sekunden und eine Denk-Rückmeldung spätestens nach fünf Sekunden. Z01 verlangt die Ablehnung ungültiger Gegenzüge bei fortsetzbarer Partie; Z02 die Erkennung einer ungültigen Anfangsstellung mit anschließendem Spielende.

**Befunde je Schwere:** 🔴 Kritisch: **0** · 🟡 Empfehlung: **6** · 🟢 Hinweis: **0**  
**Ampelstatus:** 🟡 **Gelb**. Die Kontextabgrenzung ist vorhanden und grundsätzlich konsistent; Datenflüsse, Funktionsumfang und technische Schnittstellenbedingungen müssen präzisiert werden.

### Sektion 4: Lösungsstrategie

**Prüfmodus:** Vollständiger Review im DATEI-MODUS. Alle vier Sektionsdateien wurden vollständig gelesen; ergänzend wurden Sektion 1.2, die technischen und organisatorischen Randbedingungen sowie Konzept 8.1 herangezogen.

Die Lösungsstrategie ist vorhanden und angemessen kompakt. Grundlegende Technologien, Top-Level-Zerlegung und Architekturansätze für alle fünf Qualitätsziele werden beschrieben. Austauschbarkeit, Testbarkeit und der Vorrang der Verständlichkeit werden begründet. Verweise auf Sektion 5, Sektion 8 sowie weitere Detailsektionen sind vorhanden. Es bestehen folgende Abweichungen beziehungsweise Präzisierungsbedarfe:

#### [S04-01] Spielstärkeziel weicht von Sektion 1.2 ab

**Schwere:** 🟡 Empfehlung  
**Datei:** [arc-doc/04-Loesungsstrategie/04-01-Einstieg.md](arc-doc/04-Loesungsstrategie/04-01-Einstieg.md#L12), Tabellenzeile zur Spielstärke  
**Kriterium:** Konsistente Zuordnung der Lösungsansätze zu den Qualitätszielen aus Sektion 1.2

**Befund:** Die Tabelle bezeichnet das Ziel als „Attraktive Spielstärke (Attraktivität)“. Sektion 1.2 definiert hingegen „Akzeptable Spielstärke (Funktionale Eignung)“. Damit ändern sich sowohl die Zielbezeichnung als auch die Qualitätskategorie. Die zugeordneten Ansätze passen grundsätzlich zum ursprünglichen Ziel; dessen unveränderte Übernahme würde die Rückverfolgbarkeit herstellen.

**Änderungsvorschlag:**
> Ersetze in der ersten Spalte „Attraktive Spielstärke (Attraktivität)“ durch „Akzeptable Spielstärke (Funktionale Eignung)“.

#### [S04-02] Organisatorischer Lösungsansatz bleibt unvollständig

**Schwere:** 🟡 Empfehlung  
**Datei:** [arc-doc/04-Loesungsstrategie/04-01-Einstieg.md](arc-doc/04-Loesungsstrategie/04-01-Einstieg.md#L9), Ansätze für Analysierbarkeit und Änderbarkeit  
**Kriterium:** Relevante organisatorische Entscheidungen und deren Beitrag zu den Qualitätszielen

**Befund:** Die Strategie nennt arc42-Dokumentation und Tests, greift aber das in Sektion 2.2 dokumentierte risikogetriebene, iterative und inkrementelle Vorgehen nicht auf. Auch die Open-Source-Veröffentlichung als organisatorischer Beitrag zur Experimentierplattform bleibt unerwähnt. Ein kurzer Verweis mit Zielbezug genügt; eine Wiederholung der gesamten Randbedingungen ist nicht erforderlich.

**Änderungsvorschlag:**
> Organisatorisch wird DokChess risikogetrieben, iterativ und inkrementell entwickelt. Die arc42-Dokumentation ist ein zentrales Projektergebnis und unterstützt die Analysierbarkeit. Die Veröffentlichung der Quelltexte als Open Source unter GPLv3 ermöglicht Interessierten eigene Experimente und Erweiterungen. Vorgehensmodell, Testprozesse und Veröffentlichung sind in [Abschnitt 2.2](../02-Randbedingungen/02-02-Organisatorisch.md) beschrieben.

#### [S04-03] Nebenläufige Anbindung und parallele Suche deutlicher unterscheiden

**Schwere:** 🟢 Hinweis  
**Datei:** [arc-doc/04-Loesungsstrategie/04-01-Einstieg.md](arc-doc/04-Loesungsstrategie/04-01-Einstieg.md#L13), Tabellenzeile „Schnelles Antworten auf Züge“  
**Kriterium:** Präzise Beschreibung und Begründung der Qualitätsziel-Ansätze

**Befund:** „Reactive Extensions für nebenläufige Berechnung“ lässt offen, ob die Anbindung der Suche oder der Suchalgorithmus selbst nebenläufig ist. Abschnitt 4.3 beschreibt die Basisimplementierung ausdrücklich als nicht nebenläufig; Abschnitt 4.4 begründet den reaktiven Ansatz mit der Ansprechbarkeit während der Zugermittlung. Das ist kein nachgewiesener Widerspruch, sollte aber bereits in der Übersicht unterschieden werden.

**Änderungsvorschlag:**
> Ersetze den entsprechenden Tabellenpunkt durch: „Reaktive Anbindung der Zugermittlung mit Reactive Extensions: Die Engine bleibt während der Suche ansprechbar; neu gefundene bessere Züge werden als Ereignisse bereitgestellt → **(f)**. Die Basisimplementierung der Minimax-Suche selbst ist nicht nebenläufig (siehe Abschnitt 4.3).“

**Zusammenfassung:** 🔴 Kritisch: **0** · 🟡 Empfehlung: **2** · 🟢 Hinweis: **1**  
**Ampelstatus:** 🟡 **Gelb**. Die Lösungsstrategie erfüllt die wesentlichen Anforderungen; Zielbezeichnung und organisatorischer Strategieanteil sollten nachgeschärft werden.

### Sektion 5: Bausteinsicht

**Prüfmodus:** Vollständiger Review im DATEI-MODUS, ausschließlich lesend.
**Prüfumfang:** Alle acht Dateien einschließlich ihrer Diagramme. Kontextabgleich mit Sektion 3; ergänzend Überblick, Laufzeitszenario 6.1 und Konzepte 8.4/8.5.

Die verpflichtende Bausteinsicht einschließlich Level 1 ist vorhanden. Alle vier Subsysteme sowie die beiden Engine-Module besitzen Verantwortlichkeits- und Schnittstellenbeschreibungen. Die Verfeinerung ist hierarchisch konsistent und auf die Engine begrenzt. XBoard über Standardein-/ausgabe und die optionale Polyglot-Dateianbindung entsprechen dem technischen Kontext. Die nicht implementierte Endspieldatenbankanbindung wird dort ausdrücklich abgegrenzt. Das Source-Code-Mapping ist durch qualifizierte Klassen-, Interface- und Paketnamen vorhanden.

#### [S05-01] Begründung der Zerlegung fehlt

**Schwere:** 🟡 Empfehlung  
**Datei:** [arc-doc/05-Bausteinsicht/05-01-Ebene-1.md](arc-doc/05-Bausteinsicht/05-01-Ebene-1.md), Abschnitt „5.1 Ebene 1“; ergänzend [arc-doc/05-Bausteinsicht/05-06-Ebene-2-Engine.md](arc-doc/05-Bausteinsicht/05-06-Ebene-2-Engine.md), Abschnitt „5.6 Ebene 2: Engine“.  
**Kriterium:** Whitebox-Beschreibungen begründen die gewählte Zerlegung.

**Befund:** Beide Ebenen beschreiben die enthaltenen Bausteine und deren Zusammenspiel, erläutern aber nicht ausdrücklich, warum diese Verantwortlichkeitsgrenzen gewählt wurden. Insbesondere bleibt die Trennung von Zugsuche und Stellungsbewertung als Entwurfsentscheidung unbegründet.

**Änderungsvorschlag:** In Ebene 1 ergänzen:
> ### Begründung der Zerlegung
> Die Zerlegung trennt Clientkommunikation, Schachregeln, Zugermittlung und Eröffnungswissen. Änderungen am XBoard-Protokoll bleiben damit von der Zugermittlung getrennt. Spielregeln werden von Protokoll und Engine gemeinsam genutzt. Eröffnungsbibliotheken werden über eine eigene Schnittstelle optional angebunden.

In Ebene 2 ergänzen:
> ### Begründung der Verfeinerung
> Die Engine wird verfeinert, weil hier Suchverfahren und Bewertungsfunktion zusammenwirken. Ihre Trennung ermöglicht es, die Stellungsbewertung unabhängig vom Suchverfahren auszutauschen. Die Zugsuche steuert die Exploration; die Stellungsbewertung liefert die Vergleichswerte.

#### [S05-02] Abbruch- und Randfallvertrag der Zugermittlung bleibt offen

**Schwere:** 🟡 Empfehlung  
**Datei:** [arc-doc/05-Bausteinsicht/05-04-Engine.md](arc-doc/05-Bausteinsicht/05-04-Engine.md), Tabelle „Methoden der Schnittstelle Engine“; [arc-doc/05-Bausteinsicht/05-07-Zugsuche.md](arc-doc/05-Bausteinsicht/05-07-Zugsuche.md), Beschreibung von `zugSuchen` und `sucheAbbrechen`.  
**Kriterium:** Wichtige interne Schnittstellen sind minimal, aber ausreichend beschrieben.

**Befund:** Kandidatenmeldungen, regulärer Abschluss und Abbruchoperationen sind dokumentiert. Abschnitt 6.1 erklärt die Auswahl des letzten Kandidaten; Konzept 8.5 beschreibt `onError`. Nicht festgelegt ist jedoch, ob ein Abbruch ein Abschlussereignis auslöst und ob anschließend noch Kandidaten eintreffen können. Ebenso fehlt das Ereignisverhalten bei einer Stellung ohne legale Züge. Dadurch bleibt für den Aufrufer unklar, wann ein Kandidat noch zum aktuellen Engine-Zustand gehört.

**Änderungsvorschlag:** Als ausdrücklich offenen Vertrag ergänzen und nach Abgleich mit Implementierung beziehungsweise Tests verbindlich ausfüllen:
> ### Ereignisvertrag der Zugermittlung
> Zugkandidaten werden asynchron gemeldet. Beim regulären Abschluss verwendet das XBoard-Subsystem den zuletzt gemeldeten Kandidaten gemäß Abschnitt 6.1. Fehler werden gemäß Konzept 8.5 über `onError` signalisiert.
>
> Noch festzulegen sind das Abschlussverhalten bei Abbruch, der Umgang mit nachlaufenden Kandidaten einer abgebrochenen Suche und das Ergebnis einer Suche ohne legale Züge. Diese Regeln gelten auch für Abbrüche durch `figurenAufbauen`, `ziehen` und `schliessen` und müssen zwischen Engine und Zugsuche abgestimmt werden.

#### [S05-03] Blackbox-Diagramme zeigen geschützte Implementierungsdetails

**Schwere:** 🟢 Hinweis  
**Datei:** [arc-doc/05-Bausteinsicht/05-07-Zugsuche.md](arc-doc/05-Bausteinsicht/05-07-Zugsuche.md), Schnittstellendiagramm; [arc-doc/05-Bausteinsicht/05-08-Stellungsbewertung.md](arc-doc/05-Bausteinsicht/05-08-Stellungsbewertung.md), Schnittstellendiagramm.  
**Kriterium:** Blackbox-Beschreibungen verbergen innere Implementierungsdetails.

**Befund:** Die Diagramme enthalten die geschützten Methoden `bewerteStellungRekursiv(Stellung, Farbe)` und `figurenWert(Figur)`. Diese gehören nicht zum öffentlichen Nutzungsvertrag der Module. Ob sie als Erweiterungspunkte relevant sind, wird nicht erläutert.

**Änderungsvorschlag:**
> Die Blackbox-Diagramme zeigen öffentliche Schnittstellen, Konfigurationsmethoden und Implementierungszuordnungen. Die geschützten Methoden `bewerteStellungRekursiv` und `figurenWert` werden daraus entfernt. Falls sie vorgesehene Erweiterungspunkte sind, werden sie separat mit ihrem Erweiterungsvertrag dokumentiert.

**Zusammenfassung:** 🔴 Kritisch: **0** · 🟡 Empfehlung: **2** · 🟢 Hinweis: **1** · Gesamt: **3**  
**Ampelstatus:** 🟡 **Gelb**. Die Bausteinsicht erfüllt die grundlegenden Anforderungen. Ergänzungsbedarf besteht bei den Zerlegungsgründen und dem asynchronen Schnittstellenvertrag.

### Sektion 6: Laufzeitsicht

**Prüfumfang:** Vollständiger Review im DATEI-MODUS, einschließlich Sequenzdiagramm und Konsistenzprüfung gegen Sektion 5.

Ein verständliches, architekturrelevantes Szenario ist vorhanden. Text und Sequenzdiagramm stimmen überein; alle dargestellten Subsysteme sind in Sektion 5 definiert. Die Szenarioanzahl ist überschaubar. Ergänzungsbedarf besteht bei Nebenläufigkeit, Ausnahmeabläufen und dem Zusammenspiel innerhalb der Engine.

#### [S06-01] Abbruch und Zustandswechsel während der Zugermittlung fehlen

**Schwere:** 🟡 Empfehlung  
**Datei:** [arc-doc/06-Laufzeitsicht/06-01-Zugermittlung.md](arc-doc/06-Laufzeitsicht/06-01-Zugermittlung.md#L14), Absatz zum asynchronen Aufruf  
**Kriterium:** Architekturrelevante Interaktionen und bemerkenswerte Aspekte der Laufzeit beschreiben.

**Befund:** Die weitere Verarbeitung von Eingaben wird als Grund für Asynchronität genannt, aber nicht gezeigt. Laut Sektion 5.4 brechen `ziehen` und `figurenAufbauen` eine laufende Zugermittlung ab. Unklar bleibt, wie Suchabbruch, Zustandswechsel und möglicherweise noch eintreffende Rückmeldungen zusammenwirken.

**Änderungsvorschlag:**
> Ergänzendes Szenario „Zustandswechsel während der Suche“: Während einer Zugermittlung fordert das XBoard-Protokoll-Subsystem eine neue Stellung über `figurenAufbauen` an. Die Engine bricht die bisherige Zugermittlung ab und übernimmt die neue Stellung. Zugkandidaten der abgebrochenen Suche dürfen anschließend weder ausgeführt noch als Antwort für die neue Stellung ausgegeben werden. Der Mechanismus zur Zuordnung und Unterdrückung veralteter Rückmeldungen ist im Ablauf zu benennen.

#### [S06-02] Fehlerpfade an der Protokollgrenze fehlen

**Schwere:** 🟡 Empfehlung  
**Datei:** [arc-doc/06-Laufzeitsicht/06-01-Zugermittlung.md](arc-doc/06-Laufzeitsicht/06-01-Zugermittlung.md#L11), Validierung und anschließende Zugermittlung  
**Kriterium:** Fehler- und Ausnahmeszenarien sowie kritische externe Schnittstellen beschreiben.

**Befund:** Gezeigt wird ausschließlich ein zulässiger Zug mit erfolgreicher Suche. Die bereits in Sektion 8.4 und 8.5 beschriebenen Fehlerwege fehlen: `Illegal move` bei unzulässigen Zügen sowie `onError` und die Ausgabe von `tellusererror` bei asynchronen Engine-Fehlern. Insbesondere der zweite Weg ist für die Observer-basierte Zusammenarbeit wesentlich.

**Änderungsvorschlag:**
> Fehleralternativen: Erkennt die Validierung einen unzulässigen Zug, antwortet das XBoard-Protokoll-Subsystem mit `Illegal move`; der Zug wird nicht ausgeführt. Meldet die asynchrone Zugermittlung einen Fehler über `onError`, kommuniziert das XBoard-Protokoll-Subsystem diesen mit `tellusererror` an den Client. DokChess verarbeitet anschließend weitere Eingaben; der Anwender entscheidet, ob ein Fortfahren sinnvoll ist.

#### [S06-03] Suchabschluss ohne Zugkandidaten ist nicht beschrieben

**Schwere:** 🟡 Empfehlung  
**Datei:** [arc-doc/06-Laufzeitsicht/06-01-Zugermittlung.md](arc-doc/06-Laufzeitsicht/06-01-Zugermittlung.md#L23), Abschluss und Ausführung des letzten Zuges  
**Kriterium:** Relevante Ausnahme- und Grenzszenarien nachvollziehbar darstellen.

**Befund:** Die Abschlussbeschreibung setzt einen zuvor gelieferten Zug voraus. Sektion 5.3 definiert jedoch eine leere Menge gültiger Züge bei Matt oder Patt. Für diesen regulären Endzustand bleibt offen, wie die Suche endet und wie das XBoard-Protokoll-Subsystem ohne „letzten Zug“ reagiert.

**Änderungsvorschlag:**
> Ergänzendes Szenario „Keine gültigen Züge“: Die Spielregeln liefern für die aktuelle Stellung eine leere Zugmenge. Über `aufMattPruefen` beziehungsweise `aufPattPruefen` wird der Endzustand bestimmt. Ohne Zugkandidaten darf das XBoard-Protokoll-Subsystem keinen letzten Zug ausführen und keine `move`-Antwort erzeugen. Zu ergänzen sind das tatsächlich verwendete Abschlusssignal der Engine und die konkrete Protokollausgabe für Matt beziehungsweise Patt.

#### [S06-04] Zugsuche und Stellungsbewertung bleiben verborgen

**Schwere:** 🟡 Empfehlung  
**Datei:** [arc-doc/06-Laufzeitsicht/06-01-Zugermittlung.md](arc-doc/06-Laufzeitsicht/06-01-Zugermittlung.md#L19), Untersuchung und Bewertung der Kandidaten  
**Kriterium:** Bausteine unterschiedlicher Granularität einsetzen und ihre Zusammenarbeit erklären.

**Befund:** Das Szenario verwendet ausschließlich die Subsystemebene. Die in Sektion 5.6–5.8 definierten Module Zugsuche und Stellungsbewertung werden nicht benannt. Damit bleiben die parallele Untersuchung von Teilbäumen und die Rolle der Bewertungsfunktion hinter der pauschalen Aussage verborgen, die Engine untersuche und bewerte Kandidaten. Ein Widerspruch zur Bausteinsicht besteht nicht, aber eine relevante Erklärungslücke.

**Änderungsvorschlag:**
> Bleibt die Eröffnungsabfrage ohne Ergebnis, übernimmt innerhalb der Engine das Modul Zugsuche. `MinimaxParalleleSuche` untersucht mehrere Teilbäume parallel. Der Minimax-Algorithmus verwendet die Spielregeln zur Erzeugung gültiger Züge und die Stellungsbewertung zur Bewertung der Stellungen an der vorgegebenen Suchtiefe. Verbesserte Zugkandidaten werden über `onNext`, der Suchabschluss über `onComplete` signalisiert und durch die Engine an das XBoard-Protokoll-Subsystem weitergegeben.

**Zusammenfassung:** 🔴 Kritisch: **0** · 🟡 Empfehlung: **4** · 🟢 Hinweis: **0**  
**Ampelstatus:** 🟡 **Gelb**. Der Normalablauf ist nachvollziehbar und bausteinkonsistent; wesentliche Nebenläufigkeits- und Ausnahmeabläufe fehlen.

### Sektion 7: Verteilungssicht

**Prüfmodus:** Vollständiger Review, DATEI-MODUS. Abgleich mit Sektion 5; keine Dateien geändert.

Das Deployment-Diagramm zeigt Windows-PC, Arena, Java-Laufzeit, JAR und Startskript einschließlich der Kommunikation über `stdin/stdout`. Installationsschritte und Software-Voraussetzungen sind beschrieben. Das gemeinsame JAR ist mit der Bausteinsicht vereinbar; der Betrieb ohne Eröffnungsbibliothek entspricht deren optionaler Nutzung. Für dieses lokale Single-PC-System sind weder zusätzliche Standorte noch eine zweite Infrastrukturebene erforderlich.

#### [S07-01] Motivation der Deployment-Struktur fehlt

**Schwere:** 🟡 Empfehlung  
**Datei/Stelle:** [arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md](arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md#L5), Einleitung und Deployment-Diagramm  
**Kriterium:** Motivation der Deployment-Struktur und Begründung von Infrastrukturentscheidungen.

**Befund:** Die Struktur wird dargestellt, aber ihre Wahl nicht begründet. Der Verweis auf Entscheidung 9.1 betrifft die Frontend-Anbindung; die Gründe für den gemeinsamen Rechner und die Bündelung als Über-JAR bleiben hier offen.

**Änderungsvorschlag:**
> DokChess und das Frontend werden auf demselben Windows-PC betrieben. Die Kommunikation über stdin/stdout benötigt damit keine Netzwerkverbindung zwischen diesen Komponenten. Das Über-JAR bündelt die Module und ihre Abhängigkeiten in einem Artefakt; zusammen mit dem Startskript vereinfacht dies die lokale Installation. Arena dient als exemplarisches Frontend, nicht als Bestandteil von DokChess.

#### [S07-02] Geltungsbereich der Betriebsumgebung bleibt offen

**Schwere:** 🟡 Empfehlung  
**Datei/Stelle:** [arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md](arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md#L3), „7.1 Infrastruktur Windows“  
**Kriterium:** Dokumentation der relevanten Umgebungen, insbesondere Entwicklung, Test und produktiver Einsatz.

**Befund:** Beschrieben ist eine Windows-Installation zur Nutzung mit Arena. Es bleibt unklar, ob diese Darstellung auch für Entwicklung und Tests gilt. Separate Serverumgebungen sind für die Desktop-Engine nicht notwendig, eine Abgrenzung der betrachteten Umgebung hingegen schon.

**Änderungsvorschlag:**
> Die folgende Verteilungssicht beschreibt den lokalen Einsatz von DokChess mit einem Windows-Frontend. Entwicklungs- und Testumgebungen sind hier nicht beschrieben. Ihre Betriebssysteme, Java-Versionen und gegebenenfalls abweichenden Startwege sind noch zu dokumentieren; eine Übereinstimmung mit der dargestellten Umgebung wird nicht vorausgesetzt.

#### [S07-03] Hardware- und Performance-Rahmen fehlen

**Schwere:** 🟡 Empfehlung  
**Datei/Stelle:** [arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md](arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md#L10), „Software-Voraussetzungen auf dem PC“  
**Kriterium:** Beschreibung der Infrastruktur sowie ihrer Qualitäts- und Performance-Merkmale.

**Befund:** Java-Version und Frontend sind genannt, aber CPU-, Speicher- und Laufzeitkonfiguration fehlen. Für eine lokal rechnende Schach-Engine erschwert dies die Einordnung ihrer Leistungsfähigkeit und die Reproduktion von Messungen. Eine detaillierte Netzwerktopologie ist dagegen nicht erforderlich.

**Änderungsvorschlag:**
> Hardware- und Performance-Rahmen: Mindestwerte für CPU und Arbeitsspeicher sowie erforderliche JVM-Speicherparameter sind bislang nicht festgelegt. Leistungsangaben müssen deshalb zusammen mit CPU-Modell, verfügbarem Arbeitsspeicher, Windows-Version, Java-Version und JVM-Startparametern dokumentiert werden. Eine vermessene Referenzkonfiguration ist noch zu ergänzen.

#### [S07-04] Baustein-Mapping kann expliziter dargestellt werden

**Schwere:** 🟢 Hinweis  
**Datei/Stelle:** [arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md](arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md#L16), Beschreibung von DokChess.jar  
**Kriterium:** Nachvollziehbares Mapping der Bausteine aus Sektion 5 auf Infrastruktur-Elemente.

**Befund:** „Sämtliche Module“ im gemeinsamen JAR liefert bereits ein grundsätzlich ausreichendes Mapping. Eine ausdrückliche Nennung der vier Subsysteme würde jedoch deutlicher zwischen enthaltenem Eröffnungsmodul und der hier nicht verwendeten externen Buchdatei unterscheiden. Ein Widerspruch zu Sektion 5 liegt nicht vor.

**Änderungsvorschlag:**
> Die Subsysteme XBoard-Protokoll, Spielregeln, Engine und Eröffnung aus Sektion 5 sind in DokChess.jar enthalten und werden innerhalb der Java-Laufzeit auf dem Windows-PC ausgeführt. Arena läuft als separates Frontend auf demselben Rechner. In der dargestellten Konfiguration wird keine externe Polyglot-Buchdatei eingebunden; die Engine arbeitet ohne konfigurierte Eröffnungsbibliothek.

**Befunde je Schwere:** 🔴 Kritisch: **0** · 🟡 Empfehlung: **3** · 🟢 Hinweis: **1**  
**Ampelstatus:** 🟡 **Gelb**. Die lokale Deployment-Struktur ist nachvollziehbar; Motivation, Umgebungsabgrenzung und Hardware-/Performance-Rahmen sollten ergänzt werden.

### Sektion 8: Querschnittliche Konzepte

**Prüfmodus:** Vollständiger Review im DATEI-MODUS. Alle sieben Konzeptdateien einschließlich der Domänenmodelldiagramme sowie die Bausteinsicht 5.1–5.8 wurden geprüft. Keine Dateien wurden geändert.

Die Konzepte sind als Unterabschnitte 8.1–8.7 angemessen strukturiert und auf relevante Themen beschränkt. Fachliches und technisches Datenmodell sind vorhanden. Dependency Injection und gemeinsame Datentypen unterstützen die konzeptuelle Integrität; die Bausteinsicht enthält hierzu funktionierende Querverweise. Folgende Abweichungen verbleiben:

#### [S08-01] Asynchrone Fehlerbehandlung und Fortsetzungszustand unbestimmt

**Schwere:** 🟡 Empfehlung  
**Datei/Stelle:** [arc-doc/08-Konzepte/08-05-Fehlerbehandlung.md](arc-doc/08-Konzepte/08-05-Fehlerbehandlung.md#L7), Absätze zu `onError`, Exception-Behandlung und Fortsetzung  
**Kriterium:** Konzepte erklären das WIE und definieren bausteinübergreifende Regeln.

**Befund:** Die Engine meldet asynchrone Fehler über `onError`; zugleich soll XBoard „sämtliche Exceptions“ fangen. Der Übergang zwischen diesen Mechanismen bleibt offen. „Normal“ weiterarbeiten definiert außerdem nicht, ob eine fehlgeschlagene Suche beendet ist und ob der Engine-Zustand weiterhin verwendbar bleibt.

**Änderungsvorschlag:**
> Synchrone Runtime Exceptions werden an der XBoard-Verarbeitungsgrenze behandelt; asynchrone Suchfehler werden im `onError`-Handler entgegengenommen und ebenfalls als `tellusererror` ausgegeben. Nach einem Suchfehler gilt die betroffene Suche als beendet. Vor einer erneuten Suche muss eine gültige Stellung vorliegen. Bei Fehlern beim Laden einer optionalen Eröffnungsbibliothek kann die Engine ohne diese Bibliothek weiterarbeiten. Diese Fortsetzungsregeln gelten auch für alternative Implementierungen.

#### [S08-02] Behandlung syntaktisch fehlerhafter Eingaben bleibt offen

**Schwere:** 🟡 Empfehlung  
**Datei/Stelle:** [arc-doc/08-Konzepte/08-04-Validierung.md](arc-doc/08-Konzepte/08-04-Validierung.md#L7), Verarbeitung von XBoard-Kommandos  
**Kriterium:** Validierung beschreibt Prüfgrenzen, Zuständigkeiten und Fehlerreaktionen.

**Befund:** Unbekannte Kommandos und regelwidrige Züge sind beschrieben. Für bekannte Kommandos mit fehlenden oder ungültigen Parametern fehlt jedoch die Regel. Ebenso bleibt offen, ob eine abgewiesene Eingabe den bisherigen Spielzustand unverändert lässt. Die ausdrücklich dokumentierte fehlende fachliche Prüfung von Stellungen und Bibliotheken ist dagegen keine unbelegte Konzeptlücke.

**Änderungsvorschlag:**
> Das XBoard-Subsystem prüft vor der Weitergabe eines Kommandos dessen Syntax und erforderliche Parameter. Syntaktisch fehlerhafte Kommandos werden mit einer protokollgerechten `Error`-Antwort zurückgewiesen; regelwidrige Züge mit `Illegal move`. Abgewiesene Eingaben verändern den bisherigen Spielzustand nicht. Syntaktisch gültige Stellungsbeschreibungen werden weiterhin ohne vollständige Prüfung ihrer schachlichen Zulässigkeit übernommen.

#### [S08-03] Verantwortlichkeiten für Validierung und Fehlerbehandlung nicht verlinkt

**Schwere:** 🟡 Empfehlung  
**Datei/Stelle:** [arc-doc/08-Konzepte/08-04-Validierung.md](arc-doc/08-Konzepte/08-04-Validierung.md#L5) und [arc-doc/08-Konzepte/08-05-Fehlerbehandlung.md](arc-doc/08-Konzepte/08-05-Fehlerbehandlung.md#L7), genannte Subsysteme  
**Kriterium:** Konzepte sind mit den betroffenen Bausteinen aus Sektion 5 verknüpft.

**Befund:** Die Subsysteme werden namentlich genannt, aber ihre Schnittstellenbeschreibungen nicht verlinkt. Anders als bei 8.1 und 8.2 fehlt damit für diese Konzepte die direkte Navigation zu den verantwortlichen Bausteinen.

**Änderungsvorschlag:**
> In 8.4 ergänzen: „Die Verantwortlichkeiten verteilen sich auf [XBoard-Protokoll](../05-Bausteinsicht/05-02-XBoard-Protokoll.md), [Spielregeln](../05-Bausteinsicht/05-03-Spielregeln.md) und [Eröffnung](../05-Bausteinsicht/05-05-Eroeffnung.md).“
> In 8.5 ergänzen: „Die Fehlerbehandlung verbindet [Engine](../05-Bausteinsicht/05-04-Engine.md), [Zugsuche](../05-Bausteinsicht/05-07-Zugsuche.md) und [XBoard-Protokoll](../05-Bausteinsicht/05-02-XBoard-Protokoll.md).“

#### [S08-04] Testkonzept erklärt Ablage, aber nicht gezielte Isolation und Fehlerprüfung

**Schwere:** 🟡 Empfehlung  
**Datei/Stelle:** [arc-doc/08-Konzepte/08-07-Testbarkeit.md](arc-doc/08-Konzepte/08-07-Testbarkeit.md#L7), Testorganisation und Zusammenspieltests  
**Kriterium:** Testbarkeit erklärt konkrete Mechanismen und ihre bausteinübergreifende Anwendung.

**Befund:** Verzeichnisse, JUnit, FEN und Zeitlimits sind nachvollziehbar beschrieben. Wie austauschbare Abhängigkeiten zur Isolation eingesetzt werden und wie asynchrone Fehler sowie Protokollreaktionen geprüft werden sollen, bleibt offen. Gerade diese Schnittstellen benötigen mehr als den allgemeinen Hinweis auf umfangreiche Tests.

**Änderungsvorschlag:**
> Für isolierte Modultests werden Abhängigkeiten gemäß [Konzept 8.1](08-01-Abhaengigkeiten.md) durch kontrollierbare Testimplementierungen ersetzt. XBoard-Tests verwenden injizierte Ein- und Ausgabeströme und prüfen Antworten auf unbekannte Kommandos, fehlerhafte Parameter und unzulässige Züge. Tests der asynchronen Zugermittlung prüfen Zugereignisse, regulären Abschluss, Fehlerbenachrichtigung und Abbruch. Dabei wird insbesondere geprüft, dass fehlgeschlagene oder abgebrochene Suchen keine weiteren Zugereignisse liefern.

#### [S08-05] Logging-Konzept vermischt Betriebsregel und Entscheidungsbegründung

**Schwere:** 🟢 Hinweis  
**Datei/Stelle:** [arc-doc/08-Konzepte/08-06-Logging.md](arc-doc/08-Konzepte/08-06-Logging.md#L10), Verzicht auf Logging und internes Tracing  
**Kriterium:** Konzepte beschreiben das WIE; Entscheidungen und ihre Begründungen bleiben davon unterscheidbar.

**Befund:** Externes Protokoll-Tracing ist konkret erläutert. Die Aussagen zum Verzicht auf Logging-Bibliotheken und internes Tracing sind überwiegend Entscheidungsbegründungen. Eine klar erkennbare Regel für Erweiterungen fehlt insbesondere hinsichtlich der protokollführenden Standardausgabe.

**Änderungsvorschlag:**
> **Regel für Implementierungen und Erweiterungen:** Die Standardausgabe bleibt ausschließlich XBoard-Protokollnachrichten vorbehalten. Zusätzliche Diagnoseausgaben dürfen den Protokollstrom nicht verändern. Die Kommunikationsanalyse erfolgt über das Protokoll-Tracing des Clients.  
> **Entscheidungsbegründung:** Auf internes Kommunikations-Tracing und eine Logging-Bibliothek wird verzichtet, um zusätzliche Abhängigkeiten und Diagnosecode zu vermeiden.

**Zusammenfassung:** 🔴 Kritisch: **0** · 🟡 Empfehlungen: **4** · 🟢 Hinweise: **1**  
**Ampelstatus:** 🟡 **Gelb**. Die wesentlichen Konzepte sind vorhanden; Präzisierungen bei Fehlerübergängen, Validierung und Testregeln sind erforderlich.

### Sektion 9: Architekturentscheidungen

**Prüfumfang:** DATEI-MODUS, vollständiger Review der beiden Entscheidungsdokumente. Sektion 4, Architekturüberblick und Qualitätsszenarien wurden ergänzend gelesen. Keine Dateien wurden verändert.

Beide ADRs enthalten aussagekräftige Titel sowie **Status, Context, Decision und Consequences**. Der Status „Accepted“ ist semantisch zulässig; beide Entscheidungen sind datiert. Architekturrelevanz, Einflussfaktoren, Alternativen, Auswahlgründe sowie positive und negative Konsequenzen sind dokumentiert. Neutrale beziehungsweise weiterführende Folgen werden ebenfalls behandelt. Die Entscheidungen sind mit Sektion 4 konsistent. Die dortige strategische Zusammenfassung mit ADR-Verweisen stellt keine problematische Redundanz dar. Fehlende Nygard-Pflichtabschnitte oder kritische Abweichungen wurden nicht festgestellt.

#### [S09-01] Historische Bewertungsgrundlage bei aktuellem Entscheidungsdatum

**Schwere:** 🟡 Empfehlung  
**Datei:** [arc-doc/09-Entscheidungen/09-01-Anbindung.md](arc-doc/09-Entscheidungen/09-01-Anbindung.md#L35), „Untersuchte Frontends (Stand 2011)“; Status und Decision  
**Kriterium:** Aktualität und Nachvollziehbarkeit der Entscheidungsgrundlage

**Befund:** Die Entscheidung ist auf den 10.03.2026 datiert, ihre Frontend-Bewertung stammt jedoch ausdrücklich aus 2011. Es bleibt offen, ob das Datum eine erneute fachliche Bestätigung oder die nachträgliche Dokumentation einer historischen Entscheidung bezeichnet. Die Begründung für plattformübergreifende Interoperabilität ist anhand der damaligen Tabelle nachvollziehbar, für den Entscheidungsstand 2026 aber nicht belegt. Dies weist keine falsche Protokollwahl nach, begrenzt jedoch die Aussagekraft der Begründung.

**Änderungsvorschlag:**
> **Zeitliche Einordnung der Bewertungsgrundlage:** Die Frontend-Auswahl und die Protokollvergleichstabelle dokumentieren den Untersuchungsstand von 2011. Eine erneute Prüfung der aktuellen Frontend-Versionen und ihrer Protokollunterstützung zum Statusdatum 10.03.2026 ist hier nicht nachgewiesen. Die Aussage zur plattformübergreifenden Interoperabilität bezieht sich daher auf die damals untersuchten Frontends. Vor einer Übertragung auf heutige Einsatzumgebungen sind deren Betriebssystem- und Protokollunterstützung erneut zu prüfen.

Zusätzlich beim Status ausdrücklich kennzeichnen, ob das Datum die ursprüngliche Annahme, eine erneute Bestätigung oder die nachträgliche Erfassung bezeichnet.

#### [S09-02] Performance-Abwägung ohne überprüfbaren Grenzwertnachweis

**Schwere:** 🟡 Empfehlung  
**Datei:** [arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md](arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md#L52), „Decision“, Begründung zum Prototypvergleich  
**Kriterium:** Nachvollziehbarkeit der Entscheidungskriterien und Konsequenzen

**Befund:** Der relative Laufzeitnachteil von etwa 30 Prozent wird mit der Aussage verbunden, die unveränderliche Variante liege „weiterhin innerhalb der geforderten Grenzen“. Absolute Laufzeiten, Hardware, JVM, konkrete Teststellungen und ein Messnachweis fehlen. Auch der Bezug zu den Anforderungen ist nicht benannt: E01 verlangt eine Zugantwort innerhalb von fünf Sekunden; E02 definiert zusätzliche Grenzen für den ersten Zug und die Rückmeldung. Ein isolierter Mattsuche-Prototyp belegt deren Einhaltung im integrierten Betrieb nicht automatisch. Der höhere Speicherbedarf wird zutreffend als Nachteil genannt, seine Größenordnung bleibt jedoch unbewertet.

**Änderungsvorschlag:**
> Im Prototypvergleich mit Minimax und einer Matt-in-3-Aufgabe benötigte die unveränderliche Variante etwa 30 Prozent mehr Laufzeit als die veränderliche Variante. Absolute Laufzeiten, Teststellungen, Hardware, JVM-Konfiguration und Speicherverbrauch sind in diesem ADR bislang nicht dokumentiert. Das Ergebnis beschreibt daher einen relativen Laufzeitnachteil, belegt für sich allein aber nicht die Einhaltung der Qualitätsszenarien E01 und E02 aus Sektion 10.2. Für den Grenzwertnachweis sind reproduzierbare Messungen der integrierten Engine unter den vorgesehenen Betriebsbedingungen erforderlich.

Den vorhandenen Messnachweis ergänzen oder verlinken, sofern verfügbar, und die Aussage zur Grenzwerteinhaltung erst damit konkret begründen.

**Befunde:** 🔴 Kritisch: **0** · 🟡 Empfehlung: **2** · 🟢 Hinweis: **0**  
**Ampelstatus:** 🟡 **Gelb**

### Sektion 10: Qualitätsanforderungen

**Prüfumfang:** Vollständiger Review im DATEI-MODUS. Beide Sektionsdateien einschließlich des eingebundenen Qualitätsbaums wurden geprüft; Sektion 1.2 und der Architekturüberblick dienten als Kontext. Keine Dateien wurden verändert.

Die Qualitätsübersicht ist als kategorisierter Baum vorhanden und umfasst auch Anforderungen jenseits der fünf zentralen Qualitätsziele. Nutzungs-, Änderungs- und Fehlerszenarien sind dokumentiert. Alle Qualitätsziele aus Sektion 1.2 werden referenziert, allerdings nicht durchgehend ausreichend messbar konkretisiert.

Die nachfolgend vorgeschlagenen zusätzlichen Grenzwerte sind Abstimmungsvorschläge, keine bereits belegten Anforderungen.

#### [S10-01] Akzeptable Spielstärke nicht ausreichend operationalisiert

**Schwere:** 🔴 Kritisch  
**Datei:** [arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md), F02–F04; Bezug zu [Sektion 1.2](arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md), „Akzeptable Spielstärke“  
**Kriterium:** Alle zentralen Qualitätsziele müssen durch belastbare Akzeptanzszenarien konkretisiert werden.

**Befund:** Einzelne taktische Fähigkeiten belegen nicht, dass DokChess schwache Gegner sicher schlägt und Gelegenheitsspieler fordert. Dafür fehlt ein Spielszenario mit definierter Gegnerstärke und Erfolgsschwelle. Auch die taktischen Szenarien sind nicht eindeutig reproduzierbar: Eine angegriffene Figur zu nehmen oder eine Springergabel auszuführen kann beispielsweise wegen eigener Mattgefährdung falsch sein.

**Änderungsvorschlag:**
> F02–F04 werden anhand eines versionierten Testkorpus mit FEN-Stellungen, Zugrecht und zulässigen Lösungszügen geprüft. F02 enthält ausschließlich Stellungen, in denen der Figurengewinn taktisch korrekt ist; F03 enthält gewinnbringende Springergabeln; F04 enthält erzwingbare Mattführungen in zwei Zügen gegen jede legale Verteidigung. Alle Fälle müssen unter den für E01 festgelegten Bedingungen bestanden werden.
>
> F05: DokChess spielt gegen zwei versionierte Referenzgegner, deren Einstufung als schwach beziehungsweise als Gelegenheitsspieler dokumentiert ist. Bei identischen Ressourcen und Zeitkontrollen werden je Gegner 100 Partien mit ausgeglichener Farbverteilung und festgelegten Eröffnungen gespielt. DokChess erreicht gegen den schwachen Gegner mindestens 80 Prozent und gegen den Gelegenheitsspieler mindestens 40 Prozent der möglichen Punkte; ein Remis zählt als halber Punkt.

#### [S10-02] Zeitgrenzen ohne eindeutige Messbedingungen

**Schwere:** 🟡 Empfehlung  
**Datei:** [arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md), E01 und E02  
**Kriterium:** Performance-Szenarien benötigen definierten Kontext, Messgrenzen und überprüfbare Akzeptanzkriterien.

**Befund:** Die Zeitgrenzen sind numerisch festgelegt, jedoch fehlen Referenzumgebung, Lastbedingungen und Messbeginn beziehungsweise Messende. E02 lässt für den ersten Zug zehn Sekunden zu, während E01 allgemein fünf Sekunden fordert. Ob dies eine gewollte Ausnahme ist, bleibt offen. Außerdem ist nicht festgelegt, ob die Rückmeldung durch Engine oder Frontend erfolgen muss.

**Änderungsvorschlag:**
> Für E01 und E02 werden Hardware, Betriebssystem, JVM-Version, Engine-Konfiguration, Frontend-Version und parallele Last in einem versionierten Messprofil festgehalten. Die Testfälle werden einschließlich Engine-Startzustand reproduzierbar dokumentiert.
>
> E01: Ab dem zweiten Engine-Zug vergehen zwischen dem vollständigen Empfang eines legalen Gegenzugs und der vollständigen Ausgabe des Antwortzugs höchstens fünf Sekunden.
>
> E02: Für den ersten Engine-Zug gilt ab dem vollständigen Empfang des eröffnenden Gegenzugs abweichend eine Grenze von zehn Sekunden. Innerhalb von fünf Sekunden zeigt das Frontend einen sichtbaren Berechnungsstatus an. Beide Zeitgrenzen müssen in jedem festgelegten Testfall eingehalten werden.

#### [S10-03] Auffindbarkeit in W02 und W03 nicht messbar

**Schwere:** 🟡 Empfehlung  
**Datei:** [arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md), W02 und W03  
**Kriterium:** Szenarien müssen spezifische, überprüfbare Metriken enthalten.

**Befund:** „Unverzüglich“ und „ohne Umwege“ erlauben keine eindeutige Bewertung. W01 besitzt dagegen bereits eine Zeitgrenze. Für W02 und W03 fehlen vergleichbare Kriterien sowie ein ausreichend definierter Ausgangspunkt.

**Änderungsvorschlag:**
> W02: Ein mit arc42 vertrauter Architekt ohne vorherige Kenntnis der DokChess-Dokumentation findet, ausgehend vom Architekturüberblick, zu jedem arc42-Hauptkapitel innerhalb von höchstens zwei Minuten einen konkreten Beispielinhalt, ohne Unterstützung anderer Personen.
>
> W03: Eine erfahrene Java-Entwicklerin ohne vorherige Kenntnis des DokChess-Quelltexts findet, ausgehend von der Beschreibung eines implementierten Moduls, innerhalb von höchstens fünf Minuten dessen implementierende Klassen. Sie darf Dokumentation und IDE-Suche verwenden, benötigt aber keine fremde Hilfe. Die Prüfung erfolgt anhand einer vorab festgelegten Modulauswahl.

#### [S10-04] Änderungsaufwand für zentrale Erweiterungen bleibt offen

**Schwere:** 🟡 Empfehlung  
**Datei:** [arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md), W04, W05 und P01  
**Kriterium:** Änderungsszenarien sollen Aufwand oder Dauer und den gewünschten Änderungserfolg messbar beschreiben.

**Befund:** W04 und P01 begrenzen Eingriffe in bestehenden Code, nicht aber den Aufwand. Damit wird die in Sektion 1.2 geforderte leichte Erweiterbarkeit nur teilweise konkretisiert. W05 nennt eine Woche, unterscheidet jedoch nicht zwischen Arbeitsaufwand und Kalenderdauer; die notwendige Regression bleibt unbestimmt.

**Änderungsvorschlag:**
> W04: Eine erfahrene Java-Entwicklerin integriert eine vorab spezifizierte neue Stellungsbewertung einschließlich automatisierter Tests innerhalb von höchstens zwei Personentagen. Vorhandener Code wird weder geändert noch neu übersetzt; alle bestehenden Regressionstests bestehen.
>
> W05: Implementierung, Austausch der Repräsentation und Regressionstests erfordern höchstens fünf Personentage einer erfahrenen Java-Entwicklerin. Alle bestehenden Tests zur Regelkonformität bestehen anschließend.
>
> P01: Eine erfahrene Java-Programmiererin implementiert und integriert ein vorab spezifiziertes zusätzliches Frontend-Protokoll einschließlich Integrationstests innerhalb von höchstens fünf Personentagen. Bestehender Code bleibt unverändert; die bisherigen Protokolltests bestehen weiterhin. Ein Personentag entspricht acht Arbeitsstunden.

#### [S10-05] Fehlerszenarien lassen Zustand und Reaktion unbestimmt

**Schwere:** 🟡 Empfehlung  
**Datei:** [arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md), Z01 und Z02  
**Kriterium:** Fehlerszenarien müssen beobachtbare Reaktionen und überprüfbare Akzeptanzkriterien festlegen.

**Befund:** Z01 definiert weder die Ablehnungsreaktion noch die Erhaltung des Spielzustands. „Fehlerfrei weiter“ ist kein konkretes Prüfkriterium. Z02 lässt offen, welche unzulässigen Stellungen erkannt werden und ob „beendet das Spiel“ auch den Engine-Prozess beendet. Beide Szenarien besitzen keine Reaktionsfrist.

**Änderungsvorschlag:**
> Z01: Bei einem regelwidrigen Gegenzug meldet die Engine innerhalb einer Sekunde die Ablehnung gemäß dem verwendeten Protokoll. Brettstellung, Zugrecht und Spielhistorie bleiben unverändert. Ein anschließend übermittelter legaler Zug wird akzeptiert; die Antwort erfüllt F01 und E01.
>
> Z02: Ein versionierter Testkorpus definiert unzulässige Anfangsstellungen und die jeweils erwartete Fehlerreaktion. Die Engine erkennt jeden Fall innerhalb einer Sekunde, meldet den Fehler gemäß dem verwendeten Protokoll und beendet die betroffene Partie ohne Zugausgabe. Der Engine-Prozess bleibt verfügbar und kann anschließend eine neue Partie mit gültiger Stellung beginnen.

#### [S10-06] Frontend-Kompatibilität ohne festgelegte Abnahmekonfiguration

**Schwere:** 🟡 Empfehlung  
**Datei:** [arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md), K01  
**Kriterium:** Interoperabilitätsszenarien benötigen einen definierten Anwendungskontext und eindeutige Erfolgskriterien.

**Befund:** K01 enthält mit zehn Minuten und ohne Programmieraufwand brauchbare Grenzen. „Durchgeführt und getestet“ legt aber keinen Testumfang fest. Protokollunterstützung allein garantiert außerdem nicht die Kompatibilität beliebiger Frontend-Versionen und Konfigurationen.

**Änderungsvorschlag:**
> K01: Für jedes als unterstützt ausgewiesene Frontend werden Version, Betriebssystem und verwendetes Protokoll in einer Kompatibilitätsmatrix dokumentiert. Ein Benutzer mit Grundkenntnissen des Frontends bindet die bereitgestellte Engine anhand der Installationsanleitung ohne Programmierung innerhalb von zehn Minuten ein. Innerhalb dieser Zeit startet er eine Partie, übermittelt einen legalen Zug und erhält einen im Frontend korrekt dargestellten legalen Antwortzug.

**Befunde:** 🔴 Kritisch: **1** · 🟡 Empfehlung: **5** · 🟢 Hinweis: **0**  
**Ampelstatus:** 🔴 **Rot**. Die grundlegende Struktur und Szenarioabdeckung sind vorhanden. Kritisch bleibt die fehlende belastbare Abnahme des zentralen Qualitätsziels „Akzeptable Spielstärke“; weitere Szenarien benötigen präzisere Mess- und Testbedingungen.

### Sektion 11: Risiken und technische Schulden

Vollständiger Review im DATEI-MODUS. Die drei Risikodateien wurden vollständig geprüft; ergänzend wurden Architekturüberblick, Qualitätsszenarien, Validierung und XBoard-Bausteinbeschreibung gelesen. Keine Dateien wurden verändert.

#### [S11-01] Bekannte Fehlerfolgen fehlen im Risikoverzeichnis

**Schwere:** 🔴 Kritisch  
**Datei/Stelle:** Sektion 11 insgesamt; Gegenbeleg: [08-04-Validierung.md](arc-doc/08-Konzepte/08-04-Validierung.md#L12)  
**Kriterium:** Bekannte Probleme und Risiken aus anderen Sektionen werden aufgegriffen.

**Befund:** Sektion 8.4 dokumentiert mögliche Engine-Fehler durch unzulässige Ausgangsstellungen sowie ungültige Engine-Züge durch fehlerhafte Eröffnungsbibliotheken. Beide Risiken fehlen in Sektion 11. Sie betreffen unmittelbar die Funktionsfähigkeit und regelkonformes Spiel, nicht lediglich die Spielstärke.

**Änderungsvorschlag:**
> **Risiko: Unzureichend validierte Eingabedaten.** Unzulässige Ausgangsstellungen können Engine-Fehler auslösen; fehlerhafte Eröffnungsbibliotheken können zu ungültigen Engine-Zügen führen (siehe Sektion 8.4). Maßnahmen: Ausgangsstellungen vor der Verarbeitung fachlich validieren und Bibliothekszüge vor ihrer Verwendung auf Regelkonformität prüfen. Negativtests müssen beide Fehlerklassen abdecken. Bis dahin werden für Demonstrationen ausschließlich geprüfte Stellungen und Bibliotheken verwendet.

#### [S11-02] Priorisierung und Managementübersicht fehlen

**Schwere:** 🟡 Empfehlung  
**Datei/Stelle:** Risikoüberschriften in [11-01-Frontend.md](arc-doc/11-Risiken/11-01-Frontend.md#L3), [11-02-Aufwand.md](arc-doc/11-Risiken/11-02-Aufwand.md#L3) und [11-03-Spielstaerke.md](arc-doc/11-Risiken/11-03-Spielstaerke.md#L3)  
**Kriterium:** Risiken sind nach Priorität geordnet und für die Gesamtrisikoanalyse nutzbar.

**Befund:** Die drei Einzelbeschreibungen bilden eine erkennbare Risikoliste. Ihre Nummerierung belegt jedoch keine Priorisierung. Eintrittswahrscheinlichkeit, Schadensbewertung und Verantwortlichkeit fehlen; dadurch können Management-Stakeholder Maßnahmen und Ressourcen nicht nachvollziehbar gewichten.

**Änderungsvorschlag:**
> **Priorisierte Risikoübersicht:** Vorläufige Reihenfolge zur Abstimmung: 1. unzureichende Eingabevalidierung, 2. fehlgeschlagene Frontend-Anbindung, 3. Implementierungsaufwand, 4. unzureichende Spielstärke. Für jeden Eintrag werden Eintrittswahrscheinlichkeit und Auswirkung mit niedrig/mittel/hoch bewertet sowie eine verantwortliche Person und ein nächster Prüftermin benannt. Die Reihenfolge wird anhand dieser Bewertung bestätigt oder angepasst.

#### [S11-03] Historische Risiken sind nicht vom aktuellen Stand abgegrenzt

**Schwere:** 🟡 Empfehlung  
**Datei/Stelle:** [11-01-Frontend.md](arc-doc/11-Risiken/11-01-Frontend.md#L5) und [11-02-Aufwand.md](arc-doc/11-Risiken/11-02-Aufwand.md#L18)  
**Kriterium:** Die Risikoliste bildet den nachvollziehbaren Bearbeitungsstand ab.

**Befund:** Fehlendes Protokollwissen und bevorstehende Vorträge im März/Mai 2011 werden ohne zeitliche Einordnung beschrieben. Demgegenüber bezeichnet der Überblick DokChess als voll funktionsfähig, und Sektion 5.2 beschreibt eine implementierte XBoard-Anbindung. Ob die Risiken historisch, eingetreten, reduziert oder weiterhin offen sind, bleibt unklar.

**Änderungsvorschlag:**
> **Zeitliche Einordnung:** Die Risiken 11.1 bis 11.3 beschreiben die ursprüngliche Planungssituation vor den Vorträgen im März und Mai 2011. Ihr heutiger Status ist hier noch nicht nachgewiesen. Für jedes Risiko werden letzter Bewertungszeitpunkt, Maßnahmenresultat und verbleibendes Restrisiko ergänzt. Die implementierte XBoard-Anbindung wird bei der Neubewertung von Risiko 11.1 berücksichtigt.

#### [S11-04] Bewusste Regeldefizite werden nicht als technische Schulden bewertet

**Schwere:** 🟡 Empfehlung  
**Datei/Stelle:** [11-02-Aufwand.md](arc-doc/11-Risiken/11-02-Aufwand.md#L23)  
**Kriterium:** Technische Schulden und ihre Konsequenzen werden identifiziert.

**Befund:** Das Weglassen von 50-Züge-Regel und Stellungswiederholung ist eine bewusste Einschränkung, aber weder als technische Schuld noch mit einem Abbaukriterium dokumentiert. „Keine [Konsequenzen] bezüglich der Korrektheit“ ist zu pauschal: Legalität einzelner Züge und korrekte Behandlung von Remis beziehungsweise Partieende sind zu unterscheiden.

**Änderungsvorschlag:**
> **Technische Schuld: Unvollständige Remisbehandlung.** 50-Züge-Regel und Stellungswiederholung werden zunächst nicht implementiert. Dies betrifft die Erkennung beziehungsweise Behandlung von Remis, auch wenn einzelne Engine-Züge legal bleiben. Vor einer Zusage vollständiger Regelunterstützung werden die Zuständigkeit zwischen Frontend und Engine geklärt, die fehlenden Regeln ergänzt und durch Tests abgesichert.

#### [S11-05] Risikominderung bleibt ohne überprüfbare Abschlusskriterien

**Schwere:** 🟡 Empfehlung  
**Datei/Stelle:** „Risikominderung“ in [11-01-Frontend.md](arc-doc/11-Risiken/11-01-Frontend.md#L18) und [11-03-Spielstaerke.md](arc-doc/11-Risiken/11-03-Spielstaerke.md#L20)  
**Kriterium:** Maßnahmen sind konkret, umsetzbar und überprüfbar.

**Befund:** Proof of Concept und Schachaufgaben sind geeignete Ansätze. Es fehlen jedoch konkrete Erfolgskriterien und Ergebnisse. Die bereits vorhandenen Szenarien K01, F02–F04 und E01–E02 werden nicht ausdrücklich zugeordnet. Der Verzicht auf Live-Demonstrationen reduziert Präsentationsfolgen, nicht das technische Restrisiko.

**Änderungsvorschlag:**
> **Maßnahmenprüfung:** Der Frontend-Proof-of-Concept gilt als erfolgreich, wenn ein benanntes Referenzfrontend gemäß K01 innerhalb von zehn Minuten eingebunden und getestet werden kann. Für die Spielstärke werden reproduzierbare Teststellungen zu F02–F04 festgelegt; Antwortzeiten werden gemäß E01–E02 auf dokumentierter Referenzhardware geprüft. Testumfang, Ergebnisse und verbleibende Abweichungen werden am jeweiligen Risiko festgehalten.

#### [S11-06] Perspektiven und Abdeckung der Risikoermittlung sind nicht nachvollziehbar

**Schwere:** 🟡 Empfehlung  
**Datei/Stelle:** Sektion 11 insgesamt, insbesondere [11-02-Aufwand.md](arc-doc/11-Risiken/11-02-Aufwand.md#L5)  
**Kriterium:** Stakeholder, externe Schnittstellen, Prozesse, Datenstrukturen und gegebenenfalls Quellcode werden als Risikoquellen berücksichtigt.

**Befund:** Erfahrungsdefizite, Frontend-Anbindung und Freizeitentwicklung werden betrachtet. Eine systematische Risikoermittlung mit verschiedenen Stakeholdern sowie eine Prüfung von Datenstrukturen und Quellcode ist nicht dokumentiert. Auch die in Sektion 5.2 genannten Protokolleinschränkungen werden nicht auf verbleibende Integrationsrisiken bewertet. Daraus folgt keine nachgewiesene Durchführungslücke, aber eine fehlende Nachvollziehbarkeit.

**Änderungsvorschlag:**
> **Abdeckung der Risikoermittlung:** Die Risikoliste wird mit Entwicklung, Frontend-Anwendern und Vortragsverantwortlichen überprüft. Prüfgegenstände sind XBoard einschließlich nicht unterstützter Funktionen, Zeit- und Freigabeplanung, Stellungsdaten und Eröffnungsbibliotheken sowie risikorelevante Implementierungsstellen. Datum, Beteiligte, Ergebnisse und bewusst ausgeschlossene Prüfbereiche werden dokumentiert.

**Befundanzahl:** 🔴 Kritisch: **1** · 🟡 Empfehlung: **5** · 🟢 Hinweis: **0** · Gesamt: **6**  
**Ampelstatus:** 🔴 **Rot**. Die Sektion ist vorhanden und enthält sinnvolle Gegenmaßnahmen; bekannte Fehlerfolgen mit unmittelbarer Auswirkung auf die Funktionsfähigkeit fehlen jedoch.

### Sektion 12: Glossar

**Prüfumfang:** Vollständiger Review im DATEI-MODUS, einschließlich Begriffskonsistenz in Sektionen 1–11 und Abgleich mit dem Domänenmodell. Keine Dateien verändert; kein Wissensgraph verwendet.

Das Glossar ist vorhanden, kompakt und weitgehend alphabetisch geordnet. Die folgenden Abweichungen betreffen vor allem Definitionspräzision, Begriffsvollständigkeit und Mehrdeutigkeiten.

#### [S12-01] Zug und Halbzug nicht eindeutig abgegrenzt

**Schwere:** 🟡 Empfehlung  
**Datei/Stelle:** [12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md#L15), „Halbzug“  
**Kriterium:** Konsistenz mit dem Domänenmodell.

**Befund:** Das Glossar grenzt den Halbzug von „Zug“ als Zugpaar ab. Die Klasse `Zug` in [08-02-Domaenenmodell.md](arc-doc/08-Konzepte/08-02-Domaenenmodell.md#L23) bezeichnet dagegen eine einzelne Spieleraktion. Ohne ausdrückliche Unterscheidung bleiben Schnittstellen und Suchtiefen missverständlich.

**Änderungsvorschlag:**
> **Halbzug:** Einzelne regelkonforme Aktion eines Spielers. Suchtiefen werden in DokChess in Halbzügen angegeben. **Zug:** Im Domänenmodell und in den Schnittstellen eine einzelne Spieleraktion, also ein Halbzug. Bei der Zugnummerierung einer Partie bezeichnet eine Zugnummer dagegen das Zugpaar aus weißem und schwarzem Zug.

#### [S12-02] Engine bezeichnet Gesamtsystem und Subsystem

**Schwere:** 🟡 Empfehlung  
**Datei/Stelle:** [12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md#L9), „Engine“  
**Kriterium:** Auflösung von Homonymen.

**Befund:** Die Definition beschreibt nur den zugberechnenden Programmteil. Im [Architekturüberblick](arc-doc/00-Ueberblick/00-00-Overview.md#L9) heißt jedoch auch das gesamte DokChess-System „Schach-Engine“, während die Bausteinsicht ein eigenes Engine-Subsystem ausweist.

**Änderungsvorschlag:**
> **Engine / Schach-Engine:** Schachsoftware, die eigene Züge ermittelt und typischerweise über ein externes Frontend bedient wird. DokChess als Gesamtsystem ist eine Schach-Engine. Das innerhalb von DokChess „Engine“ genannte Subsystem verwaltet die aktuelle Stellung und koordiniert die Zugermittlung; Protokollanbindung, Spielregeln und Eröffnungsbibliothek sind separate Subsysteme.

#### [S12-03] XBoard und WinBoard als Programme und Protokoll vermischt

**Schwere:** 🟡 Empfehlung  
**Datei/Stelle:** [12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md#L27), „WinBoard-Protokoll“ und „XBoard-Protokoll“  
**Kriterium:** Eindeutige technische Begriffe und Synonyme.

**Befund:** Die Definition nennt „Winboard“ als Protokollsynonym, ohne die gleichnamigen Frontends abzugrenzen. In [03-02-Technischer-Kontext.md](arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md#L11) stehen XBoard und WinBoard für Programme.

**Änderungsvorschlag:**
> **XBoard-Protokoll:** Textbasiertes Kommunikationsprotokoll zwischen Schach-Frontend und Engine, auch WinBoard-Protokoll oder Chess Engine Communication Protocol (CECP) genannt. Davon zu unterscheiden sind die grafischen Frontends XBoard und WinBoard. Das DokChess-Subsystem „XBoard-Protokoll“ implementiert die Protokollanbindung.

#### [S12-04] Entscheidende Bedingungen bei Spezialregeln fehlen

**Schwere:** 🟡 Empfehlung  
**Datei/Stelle:** [12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md#L5), „50-Züge-Regel“, [„en passant“](arc-doc/12-Glossar/12-02-Begriffe.md#L10) und [„Stellungswiederholung“](arc-doc/12-Glossar/12-02-Begriffe.md#L25)  
**Kriterium:** Klare, fachlich präzise Definitionen.

**Befund:** Bei en passant fehlt die Beschränkung auf den unmittelbar folgenden Zug. Bei Stellungswiederholung bleiben Zugrecht und Zugmöglichkeiten unberücksichtigt; die 50-Züge-Regel nennt die Zählung je Spieler nicht ausdrücklich. Dadurch sind falsche Regelinterpretationen möglich. Sektion 5.3 kennzeichnet die beiden Remisregeln zudem als nicht implementiert.

**Änderungsvorschlag:**
> **en passant:** Ein Bauer darf einen gegnerischen Bauern, der unmittelbar zuvor aus seiner Ausgangsstellung zwei Felder vorgerückt ist, so schlagen, als wäre dieser nur ein Feld vorgerückt. Das Schlagen ist ausschließlich im unmittelbar folgenden Zug zulässig. **50-Züge-Regel:** Remis kann vom Spieler am Zug reklamiert werden, wenn beide Spieler jeweils 50 aufeinanderfolgende Züge ohne Bauernzug und ohne Schlagen ausgeführt haben oder diese Bedingung mit seinem angekündigten Zug erfüllt wird. **Stellungswiederholung:** Remis kann vom Spieler am Zug reklamiert werden, wenn dieselbe Stellung mindestens zum dritten Mal vorliegt oder durch seinen angekündigten Zug entsteht. Gleichheit setzt gleiche Figuren auf gleichen Feldern, denselben Spieler am Zug und gleiche Zugmöglichkeiten einschließlich Rochade- und en-passant-Rechten voraus. Beide Remisregeln sind in DokChess gemäß Abschnitt 5.3 nicht implementiert.

#### [S12-05] Endspiel über Figurenarten statt Figurenbestand definiert

**Schwere:** 🟡 Empfehlung  
**Datei/Stelle:** [12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md#L8), „Endspiel“  
**Kriterium:** Fachliche Definitionsqualität.

**Befund:** „Nur noch wenige Figurenarten“ ist kein geeignetes Kennzeichen: Eine Stellung kann wenige Figurenarten, aber zahlreiche Figuren enthalten. Der fachliche Kontext beschreibt Endspiele dagegen über wenige verbleibende Figuren.

**Änderungsvorschlag:**
> **Endspiel:** Späte Phase einer Schachpartie mit meist deutlich reduziertem Figurenbestand. Typisch sind die aktive Rolle des Königs und die Bedeutung der Bauernumwandlung; eine starre Grenze zur vorhergehenden Partiephase gibt es nicht.

#### [S12-06] Minimax suggeriert uneingeschränkte Optimalität

**Schwere:** 🟡 Empfehlung  
**Datei/Stelle:** [12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md#L17), „Minimax-Algorithmus“  
**Kriterium:** Konsistenz mit Lösungsstrategie und Zugsuche.

**Befund:** „Unter Berücksichtigung aller Optionen“ verschweigt die begrenzte Suchtiefe und die Bewertungsfunktion. In [05-07-Zugsuche.md](arc-doc/05-Bausteinsicht/05-07-Zugsuche.md#L9) wird ausdrücklich nur ein begrenzter Spielbaum untersucht; der gefundene Zug ist nicht zwingend objektiv optimal.

**Änderungsvorschlag:**
> **Minimax-Algorithmus:** Suchverfahren für Spiele mit gegensätzlichen Spielerinteressen. Es wählt den Zug mit der besten Bewertung unter der Annahme optimaler gegnerischer Antworten. DokChess untersucht den Spielbaum bis zu einer festen Suchtiefe und bewertet die dort erreichten Stellungen; „bester Zug“ gilt daher relativ zu Suchtiefe und Bewertungsfunktion.

#### [S12-07] Zentrale Fach- und Computerschachbegriffe fehlen

**Schwere:** 🟡 Empfehlung  
**Datei/Stelle:** [12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md)  
**Kriterium:** Abdeckung wichtiger Begriffe und Zusammenspiel mit Sektion 8.

**Befund:** Nicht definiert sind insbesondere „Stellung“ aus dem Domänenmodell, „Material“ aus der Stellungsbewertung, „Bitboard“ aus Qualitätsszenario W05 sowie Eröffnungsbibliothek, Endspieldatenbank und UCI aus Kontext und Architekturentscheidungen. Das vorhandene Domänenmodell ergänzt das Glossar bereits sinnvoll, ist dort aber nicht verknüpft.

**Änderungsvorschlag:**
> Alphabetisch ergänzen: **Bitboard:** Darstellung einer Menge von Schachbrettfeldern durch 64 Bits, ein Bit je Feld; figurenzentrierte Darstellungen verwenden solche Bitmengen für Figurenarten und Farben. **Endspieldatenbank / Tablebase:** Vorberechnete Ergebnisse für Stellungen mit begrenztem Figurenbestand; in DokChess nicht angebunden. **Eröffnungsbibliothek / Opening Book:** Sammlung bekannter Eröffnungsstellungen und zugehöriger Züge, aus der DokChess optional einen Zug statt eigener Suche übernimmt. **Material:** Vorhandene Figuren und ihr relativer Wert; Grundlage der reinen Materialbewertung. **Stellung / Position:** Figurenbelegung des Bretts einschließlich Spieler am Zug, Rochaderechten und en-passant-Möglichkeit; siehe Domänenmodell in Abschnitt 8.2. **UCI:** Universal Chess Interface, alternatives textbasiertes Frontend-Engine-Protokoll; von DokChess derzeit nicht nativ implementiert.

#### [S12-08] Englische Bildbeschriftungen ohne deutsche Zuordnung

**Schwere:** 🟡 Empfehlung  
**Datei/Stelle:** [12-01-Einstieg.md](arc-doc/12-Glossar/12-01-Einstieg.md#L11), Figuren- und Geometrieabbildungen  
**Kriterium:** Übersetzungen und gemeinsames Begriffsverständnis.

**Befund:** Die Bilder verwenden ausschließlich englische Namen. Das widerspricht dem Ziel aus Sektion 2.3, englische Schachbegriffe für die nicht schacherfahrene Zielgruppe nicht zur zusätzlichen Barriere zu machen; zugleich benötigt Sektion 8.7 diese Namen für FEN.

**Änderungsvorschlag:**
> Unter den Abbildungen ergänzen: „Figurenbezeichnungen Deutsch/Englisch (FEN-Kürzel): Bauer/Pawn (P), Läufer/Bishop (B), Springer/Knight (N), Turm/Rook (R), Dame/Queen (Q), König/King (K). In FEN stehen Großbuchstaben für weiße und Kleinbuchstaben für schwarze Figuren. Brettbegriffe: Feld/Square, Reihe/Rank (1–8), Linie/File (a–h).“

#### [S12-09] Definitionsspalte abweichend benannt

**Schwere:** 🟢 Hinweis  
**Datei/Stelle:** [12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md#L3), Tabellenkopf  
**Kriterium:** Tabelle mit den Spalten „Begriff“ und „Definition“.

**Befund:** Die zweite Spalte heißt „Erklärung“. Inhaltlich erfüllt sie die Definitionsfunktion; formal weicht die Bezeichnung vom vorgegebenen Prüfkriterium ab.

**Änderungsvorschlag:**
> Tabellenkopf ersetzen durch: `| Begriff | Definition |`

**Zusammenfassung:** 🔴 Kritisch: **0** · 🟡 Empfehlung: **8** · 🟢 Hinweis: **1**  
**Ampelstatus:** 🟡 **Gelb**. Das Glossar ist nutzbar, benötigt jedoch präzisere Definitionen und eine gezielte Ergänzung zentraler Begriffe.

## Sektionsübergreifende Konflikte

| Konfliktdimension | Status | Befunde |
|---|---|---|
| Qualitätsstrang (S1 ↔ S4 ↔ S10) | 🟡 | Uneindeutige Antwortzeit E01/E02, nicht objektiv abnehmbare Analysierbarkeit (W02/W03), Fehlertoleranz ohne Strategie, Spielstärke-Szenarien ohne Partiebezug |
| Strategie ↔ Entscheidungen (S4 ↔ S9) | 🟡 | Keine ADRs für DI/reaktive Anbindung und für Suchverfahren/Eröffnungsformat; Unveränderlichkeit in S4 weiter gefasst als ADR 9.2 |
| Constraint-Compliance (S2 ↔ S4/S8/S9) | 🟡 | Englische ADR-Strukturbegriffe; Gradle/CheckStyle- und Lizenz-Nachweislücken |
| Kontext ↔ Bausteine (S3 ↔ S5) | 🟡 | Remisangebote im Kontext vs. Ausschluss in 5.2; Computergegner ohne dokumentierte Schnittstellenzuordnung |
| Sichten-Konsistenz (S5 ↔ S6 ↔ S7) | 🟢 | Keine Konflikte |
| Konzepte ↔ Entscheidungen (S8 ↔ S9) | 🟡 | DI-Framework-Verzicht und Logging-Verzicht stehen als Entscheidungen im Konzept; Fehlervertrag ohne ADR |
| Risiken ↔ Qualität (S11 ↔ S1/S10) | 🟡 | Aufwandsminderung schränkt Regelumfang ein; Risiken für Experimentierbarkeit, Antwortzeit, Eingabevalidierung und Verständlichkeit fehlen |

### 1. Qualitätsstrang (S1 ↔ S4 ↔ S10)

**Prüfumfang:** DATEI-MODUS, vollständige Prüfung der neun vorgegebenen Dateien einschließlich des eingebundenen Qualitätsbaums.

#### Zuordnungsmatrix

| Qualitätsziel (S1.2, grobe Priorität) | Strategieansatz (S4) | Szenarien (S10) | Status |
|---|---|---|---|
| 1. Zugängliches Beispiel | arc42-Dokumentation, Domänenmodell, deutsche Bezeichner, Javadoc | W01–W03; im Qualitätsbaum zusätzlich W05 | ⚠️ Teilweise unbestimmte Akzeptanzkriterien |
| 2. Einladende Experimentierplattform | Schnittstellen, Dependency Injection, unveränderliche Objekte, Testabdeckung | W04, W05, P01 | ✅ Strategisch adressiert und konkretisiert |
| 3. Bestehende Frontends nutzen | XBoard, Java, Einbindung über Startskript | K01 | ✅ Strategisch adressiert und konkretisiert |
| 4. Akzeptable Spielstärke | Eröffnungsbibliothek, Minimax, Stellungsbewertung, taktische Integrationstests | F02–F04 | ⚠️ Taktische Fähigkeiten prüfbar, Erfolg gegen Gegner nicht operationalisiert |
| 5. Schnelles Antworten auf Züge | Reaktive Anbindung, Alpha-Beta-Suche, Zeitvorgaben in Tests | E01, E02 | ⚠️ Überlappende Zeitvorgaben ohne Abgrenzung |
| Ergänzende Anforderungen: Regelkorrektheit und Fehlertoleranz | Schachregelkomponente; keine explizite Strategie für ungültige Eingaben | F01, Z01, Z02 | ⚠️ F01 fachlich gedeckt; strategische Grundlage für Z01/Z02 fehlt |

#### [KQS-01] Antwortzeit für den ersten Gegenzug ist uneindeutig

**Konflikttyp:** K5  
**Schwere:** 🟡 Warnung  
**Betroffene Dateien:**
- S1.2: [arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md](arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md), Ziel „Schnelles Antworten auf Züge“.
- S4.1: [arc-doc/04-Loesungsstrategie/04-01-Einstieg.md](arc-doc/04-Loesungsstrategie/04-01-Einstieg.md), Effizienzansätze und Integrationstests mit Zeitvorgaben.
- S10.2: [arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md), E01 und E02.

**Beschreibung:** E01 verlangt eine Zugantwort innerhalb von fünf Sekunden während einer Partie. E02 erlaubt für die erste Antwort der schwarzen Engine zehn Sekunden. Dieser Fall fällt ohne ausdrücklich genannte Ausnahme auch unter E01. Eine Antwort nach acht Sekunden besteht somit E02, verletzt aber E01. Die Anforderungen sind gleichzeitig erfüllbar, liefern jedoch unterschiedliche Abnahmegrenzen.

**Lösungsvorschlag:** E01 ergänzen: „Ab der zweiten Zugantwort der Engine erfolgt jede Antwort innerhalb von fünf Sekunden nach Eingang des gegnerischen Zugs. Für die erste Zugantwort gilt E02.“ E02 ergänzen: „Die Fristen beginnen mit Eingang des ersten gegnerischen Zugs bei der gestarteten Engine.“

#### [KQS-02] Analysierbarkeit ist teilweise nicht objektiv abnehmbar

**Konflikttyp:** K5  
**Schwere:** 🟡 Warnung  
**Betroffene Dateien:**
- S1.2: [arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md](arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md), höchstpriorisiertes Ziel „Zugängliches Beispiel“.
- S4.1: [arc-doc/04-Loesungsstrategie/04-01-Einstieg.md](arc-doc/04-Loesungsstrategie/04-01-Einstieg.md), Dokumentations- und Benennungsansätze.
- S10.2: [arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md), W01–W03.

**Beschreibung:** W01 bietet mit 15 Minuten eine Zeitgrenze. Die ergänzenden Szenarien W02 und W03 verwenden dagegen „unverzüglich“ und „ohne Umwege“ ohne objektive Grenze. Damit ist gerade die Auffindbarkeit von Dokumentationsinhalten und Implementierungen nicht reproduzierbar bewertbar; W01 ersetzt diese spezifischen Prüfungen nicht.

**Lösungsvorschlag:** W02 konkretisieren: „Eine mit arc42 vertraute Person findet für jedes von drei vorab ausgewählten Kapiteln innerhalb von jeweils zwei Minuten den zugehörigen Beispielinhalt.“ W03 konkretisieren: „Eine erfahrene Java-Entwicklerin findet ohne fremde Hilfe für jedes von drei vorab ausgewählten Modulen innerhalb von jeweils fünf Minuten die zugehörige Implementierung.“

#### [KQS-03] Fehlertoleranzszenarien haben keine explizite strategische Antwort

**Konflikttyp:** K4  
**Schwere:** 🟡 Warnung  
**Betroffene Dateien:**
- S1.1: [arc-doc/01-Einfuehrung-und-Ziele/01-01-Aufgabenstellung.md](arc-doc/01-Einfuehrung-und-Ziele/01-01-Aufgabenstellung.md), vollständige Implementierung der Schachregeln.
- S4.2/S4.4: [arc-doc/04-Loesungsstrategie/04-02-Aufbau.md](arc-doc/04-Loesungsstrategie/04-02-Aufbau.md) und [arc-doc/04-Loesungsstrategie/04-04-Anbindung.md](arc-doc/04-Loesungsstrategie/04-04-Anbindung.md), Regelkomponente und Protokollanbindung.
- S10.1/S10.2: [arc-doc/10-Qualitaetsanforderungen/10-01-Qualitaetsbaum.md](arc-doc/10-Qualitaetsanforderungen/10-01-Qualitaetsbaum.md) und [arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md), Fehlertoleranz sowie Z01/Z02.

**Beschreibung:** Z01/Z02 verlangen zustandserhaltende Ablehnung unzulässiger Züge beziehungsweise Spielbeendigung bei einer unzulässigen Anfangsstellung. Der Qualitätsbaum ordnet sie zusätzlichen Qualitätsmerkmalen zu, nicht einem der fünf Hauptziele. Zusätzliche Anforderungen sind zulässig; die bloße Existenz einer Regelkomponente erklärt aber weder Validierungszeitpunkt noch Zustands- und Fehlerbehandlung.

**Lösungsvorschlag:** S4.4 ergänzen: „Als ergänzende Qualitätsanforderung wird Fehlertoleranz adressiert: Eingaben werden vor ihrer Übernahme in den Spielzustand durch die Schachregelkomponente geprüft. Unzulässige Gegenzüge werden ohne Zustandsänderung zurückgewiesen; die Engine bleibt eingabebereit (Z01). Eine unzulässige Anfangsstellung führt zur kontrollierten Beendigung des Spiels (Z02).“

#### [KQS-04] Taktische Szenarien belegen nicht die zugesagte Spielstärke gegen Gegner

**Konflikttyp:** K5  
**Schwere:** 🟡 Warnung  
**Betroffene Dateien:**
- S1.2: [arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md](arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md), „schwache Gegner sicher zu schlagen“ und Gelegenheitsspieler zu fordern.
- S4.2/S4.3: [arc-doc/04-Loesungsstrategie/04-02-Aufbau.md](arc-doc/04-Loesungsstrategie/04-02-Aufbau.md) und [arc-doc/04-Loesungsstrategie/04-03-Spielstrategie.md](arc-doc/04-Loesungsstrategie/04-03-Spielstrategie.md), Erfüllungsbehauptungen mit Verweis auf die Qualitätsszenarien.
- S10.2: [arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md), F02–F04.

**Beschreibung:** Materialgewinn, Springergabel und Matt in zwei Zügen sind überprüfbare Einzelfähigkeiten. Sie operationalisieren jedoch weder „schwache Gegner“ noch den Erfolg über vollständige Partien. Die behauptete akzeptable Spielstärke ist durch diese Szenarien deshalb nur teilweise belegt.

**Lösungsvorschlag:** Bei unverändertem Prüfbestand S1.2 präzisieren: „Akzeptable Spielstärke bedeutet hier das zuverlässige Lösen der taktischen Situationen F02–F04; eine bestimmte Gewinnquote gegen menschliche Gegner wird nicht zugesichert.“ S4.2 entsprechend ändern: „Die Szenarien F02–F04 prüfen ausgewählte taktische Fähigkeiten, nicht die allgemeine Spielstärke über vollständige Partien.“

**Anzahl:** 🔴 Kritisch: **0** · 🟡 Warnung: **4** · 🟢 Hinweis: **0**  
**Ampelstatus:** 🟡 **Gelb**. Alle fünf Hauptziele sind strategisch adressiert. Signifikante Lücken bestehen bei Abnahmegrenzen und der strategischen Einordnung zusätzlicher Anforderungen. Kein zusätzlicher K1-, K2- oder K3-Befund: Verständlichkeit vor Effizienz ist ausdrücklich als Trade-off dokumentiert.

### 2. Strategie ↔ Entscheidungen (S4 ↔ S9)

**Prüfumfang:** Vollständige Prüfung von K1–K5 anhand der sechs vorgegebenen Dateien. Beide ADRs haben den Status „Accepted (2026-03-10)“. Beide ADRs stimmen in ihren Kernaussagen mit S4 überein; direkte Widersprüche oder unbeabsichtigte Redundanzen sind nicht erkennbar.

#### Zuordnungsmatrix

| Strategische Festlegung (S4) | Zugehörige Entscheidung(en) (S9) | Status |
|---|---|---|
| XBoard über Standardein-/ausgabe; Nutzung bestehender Frontends | 09-01, Accepted | ✅ Aligned |
| Austauschbare Protokollanbindung ohne Änderung der Engine | 09-01, Accepted | ✅ Aligned |
| Unveränderliche Stellungsobjekte; Verständlichkeit vor maximaler Effizienz | 09-02, Accepted | ✅ Aligned |
| Unveränderlichkeit aller fachlichen Klassen | 09-02 begründet ausdrücklich nur `Stellung` | 🔲 Begründungslücke, KSE-03 |
| Allgemeine Schnittstellenabstraktion und Dependency Injection | Keine entsprechende Entscheidung; 09-01 behandelt nur die Protokollerweiterbarkeit | 🔲 Lücke, KSE-01 |
| Reaktive Engine-Anbindung für Ansprechbarkeit während der Suche | Keine entsprechende Entscheidung | 🔲 Lücke, KSE-01 |
| Minimax, Alpha-Beta und paralleler Minimax | 09-02 unterstützt Nebenläufigkeit, entscheidet aber nicht über Suchverfahren | 🔲 Lücke, KSE-02 |
| Polyglot als Eröffnungsbibliotheksformat | Keine entsprechende Entscheidung | 🔲 Lücke, KSE-02 |
| Java, verständliches Domänenmodell, Dokumentations- und Testansätze | Keine eigene Entscheidung in den geprüften S9-Dateien | Kein eigenständiger Konflikt nachweisbar |

#### [KSE-01] Austauschbarkeit und reaktive Anbindung ohne dokumentierte Entscheidungsgrundlage

**Konflikttyp:** K4 – Strategie ohne Entscheidungsgrundlage  
**Schwere:** 🟡 Warnung  
**Betroffene Dateien:**
- S4: [arc-doc/04-Loesungsstrategie/04-02-Aufbau.md](arc-doc/04-Loesungsstrategie/04-02-Aufbau.md#L12) – Schnittstellenabstraktion aller Teile und Zusammensetzen per Dependency Injection.
- S4: [arc-doc/04-Loesungsstrategie/04-04-Anbindung.md](arc-doc/04-Loesungsstrategie/04-04-Anbindung.md#L11) – Reactive Extensions zur Ansprechbarkeit während der Zugermittlung.
- S9: [arc-doc/09-Entscheidungen/09-01-Anbindung.md](arc-doc/09-Entscheidungen/09-01-Anbindung.md) – „Decision“ beschreibt Protokollerweiterbarkeit, nicht die allgemeinen Integrationsmechanismen.

**Beschreibung:** Zwei grundlegende Architekturmechanismen sind strategisch festgelegt, aber durch keinen der beiden ADRs nachvollziehbar entschieden. Die XBoard-Entscheidung deckt weder die allgemeine Wahl von Dependency Injection noch die reaktive Engine-Anbindung ab. Für diese querschnittlich wirksamen Festlegungen fehlen dokumentierte Alternativen, Abwägungen und Konsequenzen.

**Lösungsvorschlag:** Zwei ADRs ergänzen und aus S4 verlinken. Als Entscheidungskerne übernehmen:
> **Austauschbarkeit:** Die zentralen Bestandteile werden über Schnittstellen abstrahiert und per Dependency Injection zusammengesetzt. Dadurch können Implementierungen insbesondere für Spielregeln, Stellungsbewertung, Protokollanbindung und Eröffnungsbibliotheken ausgetauscht und getrennt getestet werden.
>
> **Reaktive Anbindung:** Die Engine wird über Reactive Extensions angebunden. Verbesserte Zugvorschläge werden als Ereignisse bereitgestellt; die Kommunikationsanbindung bleibt während der Zugermittlung ansprechbar und kann ein sofortiges Ziehen anfordern.

Die tatsächlich betrachteten Alternativen, Konsequenzen und den Beschlussstatus ergänzen; nicht nachträglich erfinden.

#### [KSE-02] Suchverfahren und Eröffnungsformat bleiben ohne Auswahlbegründung in S9

**Konflikttyp:** K4 – Strategie ohne Entscheidungsgrundlage  
**Schwere:** 🟡 Warnung  
**Betroffene Dateien:**
- S4: [arc-doc/04-Loesungsstrategie/04-03-Spielstrategie.md](arc-doc/04-Loesungsstrategie/04-03-Spielstrategie.md) – Absätze zu Polyglot, Minimax mit fester Suchtiefe sowie Alpha-Beta und parallelem Minimax.
- S9: [arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md](arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md) – „Decision“ und „Consequences“ begründen Unveränderlichkeit und erwähnen parallelen Minimax, entscheiden jedoch nicht über die Spielstrategie.

**Beschreibung:** S4 benennt konkrete, für Spielstärke und Erweiterbarkeit wesentliche Technologie- und Algorithmusentscheidungen. S9 erläutert weder die Auswahl des Polyglot-Formats noch die Wahl und Rollenverteilung der Suchverfahren. Die Erwähnung parallelen Minimax als Weiterentwicklung in 09-02 ersetzt diese Entscheidungen nicht.

**Lösungsvorschlag:** Entscheidungen zu Eröffnungsformat und Suchstrategie ergänzen und S4 darauf verweisen lassen. Als Entscheidungskerne übernehmen:
> **Eröffnungsformat:** DokChess integriert Eröffnungswissen über einen austauschbaren Adapter für das Polyglot-Opening-Book-Format.
>
> **Suchstrategie:** Die Basisimplementierung verwendet Minimax mit fester Suchtiefe und materialbasierter Bewertung. Alpha-Beta und paralleler Minimax werden als alternative Implementierungen bereitgestellt, um Austauschbarkeit sowie Verbesserungen von Spielstärke beziehungsweise Effizienz zu demonstrieren.

Jeweils die tatsächliche Auswahlbegründung, Alternativen und Konsequenzen dokumentieren.

#### [KSE-03] Allgemeine Unveränderlichkeitsstrategie reicht über den ADR-Geltungsbereich hinaus

**Konflikttyp:** K4 – Strategie ohne vollständige Entscheidungsgrundlage  
**Schwere:** 🟢 Hinweis  
**Betroffene Dateien:**
- S4: [arc-doc/04-Loesungsstrategie/04-02-Aufbau.md](arc-doc/04-Loesungsstrategie/04-02-Aufbau.md#L21) – Unveränderlichkeit der Stellung „wie alle anderen fachlichen Klassen“ mit Verweis auf Entscheidung 9.2.
- S9: [arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md](arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md) – „Context“ und „Decision“ beschränken die Entscheidung ausdrücklich auf `Stellung`.

**Beschreibung:** Die Aussagen widersprechen sich nicht. Der ADR begründet aber nur einen Teil der weiter gefassten strategischen Festlegung; sein Verweis kann als Begründung für sämtliche fachlichen Klassen missverstanden werden.

**Lösungsvorschlag:** In 09-02 einen Absatz „Geltungsbereich“ ergänzen:
> Die konkrete Variantenabwägung und der Prototypvergleich betreffen ausschließlich `Stellung`. Darüber hinaus gilt Unveränderlichkeit als Entwurfsleitlinie für die fachlichen Klassen: Sie erleichtert den Austausch von Werten zwischen Algorithmen und die Implementierung nebenläufiger Verfahren. Die Messwerte für `Stellung` sind nicht auf andere Klassen übertragbar.

**Anzahl:** 🔴 Kritisch: **0** · 🟡 Warnung: **2** · 🟢 Hinweis: **1**  
**Ampelstatus:** 🟡 **Gelb**. Keine direkten Widersprüche, aber fehlende beziehungsweise unvollständige Entscheidungsgrundlagen. K1: kein Widerspruch; K2: keine unbeabsichtigte Redundanz; K3: keine belegte Strategielücke; K5: keine als „superseded“ gekennzeichneten Entscheidungen.

### 3. Constraint-Compliance (S2 ↔ S4/S8/S9)

**Prüfmodus:** DATEI-MODUS, vollständige Analyse aller 16 angegebenen Dateien aus S2, S4, S8 und S9.

**Legende:** ✅ Vereinbare Aussagen, keine Verletzung erkennbar; 🟡 dokumentierte Abweichung; ❔ Einhaltung nicht ausreichend belegt; — keine einschlägige Aussage. ✅ ist kein Implementierungsnachweis.

| Constraint (S2) | Kategorie | S4 Strategie | S8 Konzepte | S9 Entscheidungen | Gesamtstatus |
|---|---|---|---|---|---|
| Moderate Hardwareausstattung | Technisch | ✅ Einfache Suche, Alpha-Beta | ✅ Hardwareabhängige Zeittests | ✅ Prototyp innerhalb Zeitgrenzen | Vereinbar; Referenzhardware nicht konkretisiert |
| Windows-Desktop-Betriebssysteme | Technisch | ✅ Windows-Batchdatei | ✅ Arena unter Windows | ✅ Windows ausdrücklich berücksichtigt | Vereinbar |
| Implementierung in Java | Technisch | ✅ Java-Programm | ✅ Java-Schnittstellen, POJOs, JUnit | ✅ Java als Einflussfaktor | Vereinbar; neuere Java-Versionen nicht nachgewiesen |
| Fremdsoftware frei verfügbar | Technisch, Präferenz | ✅ Bestehende Frontends | ✅ Arena als Beispiel | ✅ Arena und WinBoard/XBoard | Vereinbar; keine Open-Source-only-Vorgabe |
| Team | Organisatorisch | — | — | ✅ Geringerer Implementierungsaufwand | Kein Widerspruch; Personalbedarf nicht quantifiziert |
| Zeitplan | Organisatorisch | — | — | — | Historische Meilensteine; keine widersprechende Terminplanung |
| Vorgehensmodell und arc42 als Projektergebnis | Organisatorisch | ✅ arc42, austauschbare Algorithmen | ✅ Erweiterbarkeit und Tests | ✅ Prototypvergleich | Vereinbar; Prozessdurchführung nicht nachgewiesen |
| Entwicklungswerkzeuge, insbesondere IDE-unabhängiger Gradle-Build | Organisatorisch | — | ❔ Teststruktur ohne Build-Anbindung | — | Nachweislücke, KRC-02 |
| Konfigurations- und Versionsverwaltung | Organisatorisch | — | ✅ GitHub-Verweis | — | Kein Widerspruch zur dokumentierten Migration |
| JUnit für Funktion, Integration und Effizienz | Organisatorisch | ✅ Integrations- und Zeittests | ✅ JUnit 4, Integrationstests, Annotation mit Timeout | — | Vereinbar |
| Open-Source-Veröffentlichung unter GPLv3 | Organisatorisch | ❔ Reactive Extensions ohne Lizenzangaben | ❔ JUnit ohne Lizenzbetrachtung | — | Nachweislücke, KRC-03 |
| Deutsches arc42-Template 6.0: Terminologie und Gliederung | Konvention | ✅ Deutsche Abschnittsstruktur | ✅ Deutsche Abschnittsstruktur | 🟡 Englische ADR-Strukturbegriffe | Abweichung, KRC-01 |
| Java Coding Conventions, geprüft mit CheckStyle | Konvention | — | ❔ Prüfmechanismus nicht beschrieben | — | Nachweislücke, KRC-02 |
| Deutsche Komponenten-, Schnittstellen- und Codebezeichner | Konvention | ✅ Explizite Festlegung | ✅ Figur, Feld, Zug, Stellung | ✅ Deutsche fachliche Bezeichner | Vereinbar |
| Etablierte Schachformate, keine Eigenformate | Konvention | ✅ XBoard, Polyglot | ✅ XBoard, FEN | ✅ XBoard statt Eigenprotokoll | Vereinbar |

#### [KRC-01] Englische ADR-Strukturbegriffe ohne dokumentierte Ausnahme

**Konflikttyp:** K3 – Konventions-Verletzung  
**Schwere:** 🟡 Warnung  
**Betroffene Sektionen/Dateien/Stellen:**
- S2: [02-03-Konventionen.md](arc-doc/02-Randbedingungen/02-03-Konventionen.md#L7) — Terminologie und Gliederung nach dem deutschen arc42-Template.
- S9: [09-01-Anbindung.md](arc-doc/09-Entscheidungen/09-01-Anbindung.md#L7) und [09-02-Stellungsobjekte.md](arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md#L7) — Überschriften „Context“, „Decision“, „Consequences“; Status jeweils „Accepted“.

**Beschreibung:** Die Entscheidungen sind inhaltlich deutsch, verwenden aber englische Struktur- und Statusbegriffe. Das weicht von der festgelegten deutschen Dokumentationsterminologie ab; eine Ausnahme für ADRs ist nicht dokumentiert. Das ADR-Format selbst widerspricht arc42 nicht. Englische Protokollkommandos, Java-API-Namen und FEN-Symbole sind dagegen keine Verletzung der deutschen fachlichen Benennung.

**Lösungsvorschlag:** In beiden ADRs „Context“ durch „Kontext“, „Decision“ durch „Entscheidung“, „Consequences“ durch „Konsequenzen“ und „Accepted (2026-03-10)“ durch „Akzeptiert (2026-03-10)“ ersetzen.

#### [KRC-02] Gradle-Build und CheckStyle-Prüfung bleiben ohne Einhaltungsnachweis

**Konflikttyp:** K2/K3 – Verdachtsfall für ungeprüfte organisatorische Randbedingung und Konvention  
**Schwere:** 🟢 Hinweis  
**Betroffene Sektionen/Dateien/Stellen:**
- S2: [02-02-Organisatorisch.md](arc-doc/02-Randbedingungen/02-02-Organisatorisch.md#L10) — zwingender Build allein mit Gradle; [02-03-Konventionen.md](arc-doc/02-Randbedingungen/02-03-Konventionen.md#L8) — Prüfung der Kodierrichtlinien mit CheckStyle.
- S8: [08-07-Testbarkeit.md](arc-doc/08-Konzepte/08-07-Testbarkeit.md#L9) — JUnit 4; eigener Integrationstestordner und zeitbeschränkte Tests, jedoch keine Gradle- oder CheckStyle-Anbindung.

**Beschreibung:** Die Testkonzeption ist mit S2 vereinbar. Offen bleibt jedoch, wie ein IDE-unabhängiger Build einschließlich der getrennten Integrationstests und der CheckStyle-Prüfung ausgeführt wird. Das belegt weder einen Gradle-Verstoß noch eine unterlassene CheckStyle-Prüfung; es ist eine Nachweislücke.

**Lösungsvorschlag:** S8.7 um folgenden Solltext ergänzen und anschließend die tatsächlich verwendeten Gradle-Tasks dokumentieren:
> Der Build muss ohne IDE allein mit Gradle ausführbar sein. Die Build-Konfiguration bindet Unit-Tests, Integrationstests aus src/integTest und die CheckStyle-Prüfung nach den Java Coding Conventions von Sun/Oracle ein. Die erforderliche JDK-Version und die konkreten Aufrufbefehle werden hier dokumentiert.

#### [KRC-03] Lizenzverträglichkeit eingebundener Bibliotheken nicht nachvollziehbar

**Konflikttyp:** K2 – Verdachtsfall für ungeprüfte organisatorische Lizenzrandbedingung  
**Schwere:** 🟢 Hinweis  
**Betroffene Sektionen/Dateien/Stellen:**
- S2: [02-02-Organisatorisch.md](arc-doc/02-Randbedingungen/02-02-Organisatorisch.md#L13) — Veröffentlichung der Quelltexte oder zumindest von Teilen unter GPLv3.
- S4: [04-04-Anbindung.md](arc-doc/04-Loesungsstrategie/04-04-Anbindung.md#L11) — Reactive Extensions ohne Angabe der konkreten Implementierung, Version oder Lizenz.
- S8: [08-07-Testbarkeit.md](arc-doc/08-Konzepte/08-07-Testbarkeit.md#L9) — JUnit 4 ohne dokumentierte Lizenzbewertung.

**Beschreibung:** Die geprüften Abschnitte lassen nicht erkennen, welche Bibliotheken tatsächlich eingebunden oder mitgeliefert werden und wie deren Lizenzbedingungen berücksichtigt sind. Eine GPLv3-Unverträglichkeit ist nicht belegt. Die bloße Untersuchung des kommerziellen Frontends Fritz for Fun ist kein Verstoß: S2 formuliert kostenlose Fremdsoftware als Präferenz, und S9 entscheidet sich für frei verfügbare Frontends.

**Lösungsvorschlag:** S8.1 um folgende Regel und eine ausgefüllte Abhängigkeitstabelle ergänzen:
> Für tatsächlich eingebundene oder mitgelieferte Fremdbibliotheken werden Implementierung, Version, Lizenz, Verwendungsart und erforderliche Lizenzhinweise dokumentiert. Vor der Veröffentlichung wird die Zulässigkeit der vorgesehenen Verwendung mit den unter GPLv3 veröffentlichten DokChess-Teilen geprüft. Separat gestartete Frontends werden von eingebundenen Bibliotheken unterschieden.

**Anzahl:** 🔴 Kritisch: **0** · 🟡 Warnung: **1** · 🟢 Hinweis: **2**  
**Ampelstatus:** 🟡 **Gelb**. Keine belegte technische, organisatorische oder implizite Constraint-Verletzung nach K1, K2 oder K4. Die Warnung betrifft die Dokumentationsterminologie; die zwei Hinweise sind Nachweislücken, keine nachgewiesenen Constraint-Verletzungen.

### 4. Kontext ↔ Bausteine (S3 ↔ S5)

**Analysemodus:** DATEI-MODUS, vollständige Prüfung aller zwei S3- und acht S5-Dateien einschließlich der Kontext- und Whitebox-Diagramme.

#### Schnittstellenvergleich

| Externer Partner / Schnittstelle | In Kontext (S3) | In Bausteinsicht (S5) | Status |
|---|---|---|---|
| Menschlicher Gegner | Kommunikation über Züge und Remisangebote; Anbindung über grafischen XBoard-Client | Subsystem XBoard-Protokoll; Befehle über stdin, Antworten über stdout; Remisangebote ausgeschlossen | 🟡 Funktionsumfang widersprüchlich |
| Computergegner | Andere Engine als alternativer Gegner; gleicher Informationsaustausch | XBoard-Protokoll als allgemeine Clientschnittstelle; Computergegner nicht ausdrücklich zugeordnet | 🟡 Zuordnungslücke |
| XBoard-Client | Externes Frontend mit XBoard-Protokoll | Externer Interaktionspunkt Standard-Ein-/Ausgabe am Subsystem XBoard-Protokoll | ✅ Konsistent |
| Eröffnungen / Polyglot Opening Book | Optionale externe Buchdatei; ausschließlich lesender Zugriff | Subsystem Eröffnung mit internem Adapter PolyglotOpeningBook; liest Binärdatei; Nutzung durch Engine optional | ✅ Konsistent |
| Endspiele / Endspieldatenbanken | Fachliche Erweiterungsmöglichkeit; technische Anbindung ausdrücklich nicht implementiert | Keine Endspielschnittstelle und kein entsprechender Adapter beschrieben | ✅ Konsistent mit dem dokumentierten Implementierungsumfang |

#### [KKB-01] Remisangebote im Kontext vorgesehen, in der Bausteinsicht ausgeschlossen

**Konflikttyp:** K4 – Datenfluss-Inkonsistenz hinsichtlich des unterstützten Informationsaustauschs  
**Schwere:** 🟡 Warnung  
**Beteiligte Sektionen:** S3 – Kontextabgrenzung; S5 – Bausteinsicht  
**Betroffene Dateien und Stellen:**
- [arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md#L13) — „Menschlicher Gegner“ nennt Züge und Remisangebote als auszutauschende Informationen; „Computergegner“ übernimmt dieselben Anforderungen.
- [arc-doc/05-Bausteinsicht/05-02-XBoard-Protokoll.md](arc-doc/05-Bausteinsicht/05-02-XBoard-Protokoll.md#L42) — „Offene Punkte“ schließt Remisangebote ausdrücklich aus.

**Beschreibung:** S3 beschreibt Remisangebote ohne Einschränkung als Teil der Kommunikation mit Gegnern. Das hierfür zuständige Subsystem in S5 unterstützt diesen Nachrichtentyp ausdrücklich nicht. Damit stimmen fachlich dargestellter und tatsächlich unterstützter Schnittstellenumfang nicht überein. Ein Widerspruch der Übertragungsrichtung liegt nicht vor.

**Lösungsvorschlag:** Den letzten Satz unter „Menschlicher Gegner“ in S3.1 ersetzen:
> Dazu tauschen die Gegner insbesondere ihre Züge aus. Remisangebote gehören grundsätzlich zur fachlichen Kommunikation einer Schachpartie, werden von der aktuellen DokChess-Implementierung jedoch nicht unterstützt (siehe Abschnitt 5.2). Diese Einschränkung gilt auch für Partien gegen einen Computergegner.

#### [KKB-02] Computergegner keiner technischen Schnittstelle ausdrücklich zugeordnet

**Konflikttyp:** K1 – Kontextpartner ohne explizite Zuordnung in der Bausteinsicht  
**Schwere:** 🟡 Warnung  
**Beteiligte Sektionen:** S3 – Kontextabgrenzung; S5 – Bausteinsicht  
**Betroffene Dateien und Stellen:**
- [arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md#L15) — „Computergegner“ definiert eine andere Engine als externen Kommunikationspartner.
- [arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md](arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md#L9) — „XBoard Client“ erläutert ausschließlich die Anbindung menschlicher Spieler.
- [arc-doc/05-Bausteinsicht/05-01-Ebene-1.md](arc-doc/05-Bausteinsicht/05-01-Ebene-1.md#L8) — Ebene-1-Diagramm zeigt Standard-Ein-/Ausgabe, aber keine Zuordnung zum Computergegner.
- [arc-doc/05-Bausteinsicht/05-02-XBoard-Protokoll.md](arc-doc/05-Bausteinsicht/05-02-XBoard-Protokoll.md#L7) — „Zweck/Verantwortlichkeit“ beschreibt einen allgemeinen Client, ohne die Vermittlung einer Partie gegen eine andere Engine zu erklären.

**Beschreibung:** Für den Computergegner aus S3.1 bleibt offen, wie dessen Kommunikation die Systemgrenze erreicht und welcher Ebene-1-Baustein sie bedient. Eine Vermittlung über einen XBoard-Client ist plausibel, aber nicht ausdrücklich dokumentiert. Der Befund betrifft die Nachvollziehbarkeit der Zuordnung, nicht eine nachgewiesene fehlende Implementierung.

**Lösungsvorschlag:** Sofern die Vermittlung über den XBoard-Client vorgesehen ist, in S3.2 unter „XBoard Client“ ergänzen:
> Bei Partien gegen einen Computergegner vermittelt der externe XBoard-Client den Austausch mit der anderen Engine. DokChess kommuniziert ausschließlich mit diesem Client; eine direkte Schnittstelle zur gegnerischen Engine besteht nicht.

In S5.2 unter „Zweck/Verantwortlichkeit“ ergänzen:
> Das Subsystem bedient über stdin und stdout den externen XBoard-Client sowohl für Partien gegen menschliche Gegner als auch für durch den Client vermittelte Partien gegen Computergegner.

**Anzahl:** 🔴 Kritisch: **0** · 🟡 Warnung: **2** · 🟢 Hinweis: **0**  
**Ampelstatus:** 🟡 **Gelb**. Keine zusätzlichen undokumentierten externen Schnittstellen (K2), belastbaren Terminologie-Konflikte (K3) oder Systemgrenz-Verschiebungen (K5) festgestellt. Die fehlende Endspielanbindung ist durch S3.2 ausdrücklich begründet und deshalb kein zusätzlicher K1-Befund.

### 5. Sichten-Konsistenz (S5 ↔ S6 ↔ S7)

**Analysemodus:** DATEI-MODUS, vollständige Prüfung aller zehn angegebenen Markdown-Dateien einschließlich ihrer eingebetteten Diagramme.

#### Baustein-Kreuzreferenz

| Baustein | Bausteinsicht (S5) | Laufzeitsicht (S6) | Verteilungssicht (S7) | Status |
|---|---|---|---|---|
| XBoard-Protokoll | In [5.2](arc-doc/05-Bausteinsicht/05-02-XBoard-Protokoll.md#L5) definiert | Validiert Eingaben, steuert Engine und gibt den gewählten Zug aus | Im DokChess.jar enthalten; Kommunikation über stdin/stdout | ✅ Konsistent |
| Spielregeln | In [5.3](arc-doc/05-Bausteinsicht/05-03-Spielregeln.md#L5) definiert | Liefert gültige Züge für Validierung und Zugermittlung | Über die Aussage „sämtlicher Module“ dem DokChess.jar zugeordnet | ✅ Konsistent |
| Engine | In [5.4](arc-doc/05-Bausteinsicht/05-04-Engine.md#L5) definiert | Verwaltet Stellung und liefert Zugkandidaten asynchron | Im DokChess.jar innerhalb der Java-Laufzeitumgebung | ✅ Konsistent |
| Eröffnung / Eröffnungsbibliothek | In [5.5](arc-doc/05-Bausteinsicht/05-05-Eroeffnung.md#L5) definiert; laut 5.4 optional | Wird angefragt und liefert im Beispiel keinen Zug | Modulcode vom gemeinsamen JAR umfasst; gezeigte Betriebsvariante ausdrücklich ohne Eröffnungsbibliothek | ✅ Zulässige Variante |
| Zugsuche | In [5.7](arc-doc/05-Bausteinsicht/05-07-Zugsuche.md#L5) als Engine-Modul definiert | Auf Subsystem-Ebene durch die Engine repräsentiert; Suche und fortlaufende Kandidaten beschrieben | Als internes Modul im gemeinsamen JAR enthalten | ✅ Konsistente Aggregation |
| Stellungsbewertung | In [5.8](arc-doc/05-Bausteinsicht/05-08-Stellungsbewertung.md#L5) als Engine-Modul definiert | Bewertung im Engine-Ablauf beschrieben; keine eigene Lebenslinie | Als internes Modul im gemeinsamen JAR enthalten | ✅ Konsistente Aggregation |

Arena beziehungsweise der XBoard-Client sind externe Kommunikationspartner, keine zusätzlich zu definierenden internen Bausteine. JVM, JAR und Startskript sind Ausführungsumgebung beziehungsweise Deployment-Artefakte.

#### Ergebnisse der Konfliktprüfungen

| Prüfung | Ergebnis | Begründung |
|---|---|---|
| K1: Undefinierter Baustein in Laufzeitsicht | Kein Konflikt | Alle internen Lebenslinien des Sequenzdiagramms entsprechen den vier Subsystemen aus S5. „Eröffnungsbibliothek“ bezeichnet die dokumentierte Schnittstelle des Subsystems „Eröffnung“. |
| K2: Undefinierter Baustein in Verteilungssicht | Kein Konflikt | S7 führt keine unbekannten internen Komponenten ein. DokChess.jar bündelt ausdrücklich sämtliche Module und benötigten Abhängigkeiten. |
| K3: Verwaister Baustein | Kein Konflikt | Alle vier Subsysteme erscheinen in S6. Zugsuche und Stellungsbewertung sind innerhalb der Engine eingeordnet und durch das gemeinsame Deployment erfasst. |
| K4: Inkonsistente Schnittstelle | Kein Konflikt | `liefereGueltigeZuege`, `ziehen`, `ermittleDeinenZug` und `liefereZug` entsprechen S5. Zugereignisse und Abschlussmeldung passen zur dokumentierten Observable-/Observer-Kommunikation; stdin/stdout stimmen zwischen S5 und S7 überein. |
| K5: Inkonsistente Abstraktionsebene | Kein Konflikt | S6 kennzeichnet die Darstellung ausdrücklich als Subsystem-Ebene. S7 aggregiert die Module nachvollziehbar zu einem Deployment-Artefakt. |
| K6: Verantwortlichkeits-Verletzung | Kein Konflikt | XBoard-Protokoll verantwortet Validierung und Protokollausgabe; Spielregeln liefern zulässige Züge; Eröffnung liefert Buchzüge; Engine koordiniert die Zugermittlung. |

**Gefundene Konflikte:** Keine.

**Anzahl:** 🔴 Kritisch: **0** · 🟡 Warnung: **0** · 🟢 Hinweis: **0**  
**Ampelstatus:** 🟢 **Grün**. Die geprüften Sichten sind auf ihren jeweils ausgewiesenen Abstraktionsebenen konsistent. Die Bewertung betrifft die Dokumentation; eine Übereinstimmung mit Implementierung oder tatsächlichem Deployment wurde nicht geprüft.

### 6. Konzepte ↔ Entscheidungen (S8 ↔ S9)

**Prüfumfang:** Vollständige Analyse der sieben S8-Dateien und beider S9-Dateien. Aussagen über fehlende Entscheidungen beziehen sich auf die geprüfte Sektion 9.

#### Zuordnungsanalyse

| Element | Sektion | Korrekte Zuordnung? | Bezug |
|---|---|---|---|
| Abhängigkeiten zwischen Modulen | S8, 8.1 | Teilweise: DI-Regeln sind ein Konzept; Framework-Verzicht ist eine Entscheidung | KKE-01 |
| Schach-Domänenmodell | S8, 8.2 | ✅ Korrekt: Datenmodell und Nutzungssemantik | Entscheidung 9.2 begründet unveränderliche Stellungsobjekte |
| Benutzungsoberfläche | S8, 8.3 | ✅ Korrekt: Umsetzung der Frontend-Anbindung | Entscheidung 9.1 begründet XBoard |
| Plausibilisierung und Validierung | S8, 8.4 | ✅ Korrekt: übergreifende Prüf- und Rückmelderegeln | Konzepte 8.3 und 8.5 |
| Ausnahme- und Fehlerbehandlung | S8, 8.5 | ✅ Konzept korrekt zugeordnet; Entscheidungsgrundlage fehlt | KKE-03 |
| Logging, Protokollierung, Tracing | S8, 8.6 | Teilweise: Diagnosekonzept und begründete Verzichtsentscheidungen vermischt | KKE-02 |
| Testbarkeit | S8, 8.7 | ✅ Korrekt: Testorganisation, Testdaten und Zeitprüfungen | Keine separate Entscheidung zwingend erforderlich |
| Frontend-Anbindung | S9, 9.1 | ✅ Korrekt: Alternativen, Wahl, Begründung und Konsequenzen | Umsetzung in S8, 8.3 |
| Unveränderliche Stellungsobjekte | S9, 9.2 | ✅ Korrekt: Alternativen, Wahl, Begründung und Konsequenzen | Umsetzung in S8, 8.2 |

#### [KKE-01] Entscheidung gegen ein DI-Framework steht im Konzept

**Konflikttyp:** K2 – Falsche Zuordnung  
**Schwere:** 🟡 Warnung  
**Betroffene Dateien:**
- S8: [08-01-Abhaengigkeiten.md](arc-doc/08-Konzepte/08-01-Abhaengigkeiten.md#L12), Absatz ab „DokChess verzichtet“: Framework-Verzicht, Verdrahtung im Quelltext und Ausschluss annotationsgetriebener Konfiguration.
- S9: [09-01-Anbindung.md](arc-doc/09-Entscheidungen/09-01-Anbindung.md) und [09-02-Stellungsobjekte.md](arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md): keine entsprechende Entscheidung.

**Beschreibung:** Setter-Injection, Java-Interfaces und die Trennung zwischen Modulen und Verdrahtung sind korrekt in S8 beschrieben. Der bewusst begründete Verzicht auf ein DI-Framework ist hingegen eine dokumentationswürdige Architekturentscheidung: Er betrifft Abhängigkeiten, Konfiguration und Erweiterbarkeit aller Module. Das WAS und WARUM stehen ausschließlich im Konzept.

**Lösungsvorschlag:** Die Grundsatzentscheidung samt Begründung nach S9 auslagern; die Umsetzungsregeln in S8 belassen. Direkt übernehmbarer Entscheidungstext:
> DokChess verwendet im Kern kein DI-Framework und keine annotationsgetriebene DI-Konfiguration. Die Module bleiben reine POJOs; ihre Abhängigkeiten werden in Unit-Tests und im Glue-Code über Setter injiziert. Dadurch bleibt die Wahl einer DI-Implementierung für Erweiterungen offen. Die Verdrahtung muss ohne Framework-Unterstützung im Quelltext gepflegt werden. Die Umsetzungsregeln beschreibt Konzept 8.1.

#### [KKE-02] Verzicht auf internes Logging und Tracing ist ausschließlich in S8 begründet

**Konflikttyp:** K2 – Falsche Zuordnung  
**Schwere:** 🟡 Warnung  
**Betroffene Dateien:**
- S8: [08-06-Logging.md](arc-doc/08-Konzepte/08-06-Logging.md#L10): kein feinkörniges Logging und keine Logging-Bibliothek; Begründung durch vermiedene Abhängigkeiten.
- S8: [08-06-Logging.md](arc-doc/08-Konzepte/08-06-Logging.md#L17): bewusster Verzicht auf internes Kommunikationstracing zugunsten vorhandener Frontend-Werkzeuge.
- S9: [09-01-Anbindung.md](arc-doc/09-Entscheidungen/09-01-Anbindung.md#L54): gute Debugging-Unterstützung durch Arena als Konsequenz, aber keine Entscheidung über den Verzicht auf interne Diagnoseinstrumentierung.

**Beschreibung:** S8 beschreibt nicht nur das Vorgehen zur Diagnose, sondern begründet zwei systemweite Verzichtsentscheidungen. Diese beeinflussen Abhängigkeiten und Beobachtbarkeit wesentlich und sind mehr als eine triviale Logging-Konvention. Die Entscheidung für XBoard begründet nicht automatisch den Verzicht auf interne Diagnosemöglichkeiten.

**Lösungsvorschlag:** Den Verzicht mit Begründung und Konsequenzen als Entscheidung in S9 dokumentieren; die praktische Nutzung von Frontend-Protokollierung in S8 belassen. Direkt übernehmbarer Entscheidungstext:
> DokChess verzichtet auf feinkörniges internes Logging, eine zusätzliche Logging-Bibliothek und eigenes XBoard-Kommunikationstracing. Für Funktionsdiagnosen werden Tests, für Kommunikationsdiagnosen die Protokollierungsfunktionen geeigneter Frontends verwendet. Damit werden zusätzliche Bibliotheksabhängigkeiten und Diagnosecode im Kern vermieden. Als Konsequenz sind interne Abläufe nicht feinkörnig protokolliert; Kommunikationstraces setzen ein geeignetes externes Werkzeug voraus. Das Diagnosevorgehen beschreibt Konzept 8.6.

#### [KKE-03] Subsystemübergreifender Fehlervertrag ohne dokumentierte Grundsatzentscheidung

**Konflikttyp:** K4 – Fehlende Entscheidung  
**Schwere:** 🟡 Warnung  
**Betroffene Dateien:**
- S8: [08-05-Fehlerbehandlung.md](arc-doc/08-Konzepte/08-05-Fehlerbehandlung.md#L7): Runtime Exceptions, zusätzliche `onError`-Nachrichten bei asynchroner Zugermittlung und verpflichtendes Verpacken von Checked Exceptions.
- S8: [08-05-Fehlerbehandlung.md](arc-doc/08-Konzepte/08-05-Fehlerbehandlung.md#L11): zentrale Übersetzung von Exceptions in `tellusererror`; Fortsetzen des Betriebs im abschließenden Absatz.
- S9: [09-01-Anbindung.md](arc-doc/09-Entscheidungen/09-01-Anbindung.md) und [09-02-Stellungsobjekte.md](arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md): keine Entscheidung zum Fehlervertrag.

**Beschreibung:** Das Konzept legt verbindliche Regeln für sämtliche Subsysteme und Erweiterungen fest. Insbesondere die Wahl zwischen Checked und Runtime Exceptions sowie zwischen synchroner und asynchroner Fehlermeldung prägt die öffentlichen Schnittstellen. Keine der geprüften Entscheidungen begründet diese Wahl. Das Konzept ist richtig zugeordnet; es fehlt die nachvollziehbare Grundsatzentscheidung, nicht seine Verschiebung nach S9.

**Lösungsvorschlag:** Eine Entscheidung zum Fehlervertrag ergänzen und mit Konzept 8.5 verknüpfen. Direkt übernehmbarer, vor Annahme fachlich zu bestätigender Entscheidungsentwurf:
> DokChess signalisiert synchrone Subsystemfehler über Runtime Exceptions; Checked Exceptions werden an den Subsystemgrenzen verpackt. Bei asynchroner Zugermittlung erfolgt die Fehlerbenachrichtigung zusätzlich über `onError`. Das XBoard-Subsystem übersetzt Fehler in `tellusererror`. Einheitliche Fehlersignalisierung soll die Integration austauschbarer Module erleichtern. Aufrufer müssen Laufzeitfehler behandeln; asynchrone Aufrufer müssen den Fehlerkanal berücksichtigen. Konzept 8.5 beschreibt die Umsetzung und muss festlegen, unter welchen Fehlerbedingungen ein sicherer Weiterbetrieb möglich ist.

**Anzahl:** 🔴 Kritisch: **0** · 🟡 Warnung: **3** · 🟢 Hinweis: **0**  
**Ampelstatus:** 🟡 **Gelb**. Keine direkten Widersprüche zwischen Konzepten und akzeptierten Entscheidungen (K1), keine falsch zugeordneten Konzepte in S9 (K3) und keine fehlende Konzeptumsetzung der beiden akzeptierten Entscheidungen (K5). Die Befunde betreffen zwei ausschließlich in S8 dokumentierte Grundsatzentscheidungen und eine fehlende Entscheidungsgrundlage für den übergreifenden Fehlervertrag.

### 7. Risiken ↔ Qualität (S11 ↔ S1/S10)

**Prüfmodus:** DATEI-MODUS, vollständige Analyse der acht angegebenen Dateien aus S1, S10 und S11 einschließlich des eingebetteten Qualitätsbaums.

#### Zuordnungsmatrix

| Qualitätsziel bzw. Qualitätsanforderung | Bedrohende Risiken (S11) | Dokumentierte Maßnahmen | Status |
|---|---|---|---|
| Zugängliches Beispiel; W01–W03, W05 | 11.3 nennt einfache Zugänglichkeit als konkurrierendes Ziel; 11.1 gefährdet die Glaubwürdigkeit als Fallbeispiel | Frontend-Prototyp; Tests zur Spielstärke, aber keine Überprüfung der Verständlichkeit | ⚠️ Teilweise abgedeckt |
| Einladende Experimentierplattform; W04, W05, P01 | Kein Risiko für erschwerten Komponenten- oder Protokollaustausch beschrieben | Keine zugeordnete Maßnahme | ⚠️ Lücke |
| Bestehende Frontends nutzen; K01 | 11.1: Anbindung scheitert | Früher Proof of Concept; eigenes UI als Ausweichlösung | ✅ Risiko und Minderung benannt; eigenes UI erfüllt K01 nicht |
| Akzeptable Spielstärke; F02–F04 | 11.3: Spielstärke scheitert | Konkretisierung durch Szenarien und Schachaufgaben als Tests | ✅ Risiko und Früherkennung benannt |
| Schnelles Antworten; E01, E02 | 11.3: zu lange Wartezeiten | Szenariokonkretisierung; ausdrücklich beschrieben sind anschließend Spielstärketests | ⚠️ Effizienzspezifische Maßnahme fehlt |
| Vollständige FIDE-Regeln; funktionale Eignung | 11.2: Implementierungsaufwand zu hoch | Vorläufiger Verzicht auf zwei Remisregeln | ❌ Maßnahme schränkt zugesagten Funktionsumfang ein |
| Fehlertoleranz; Z01, Z02 | Kein entsprechendes Risiko beschrieben | Keine zugeordnete Maßnahme | ⚠️ Lücke |

„Abgedeckt“ bedeutet hier, dass Risiko und Maßnahme dokumentiert sind, nicht dass ihre Wirksamkeit nachgewiesen ist.

#### [KRQ-01] Aufwandsminderung schränkt den zugesagten Regelumfang ein

**Konflikttyp:** K3 – Kontraproduktive Maßnahme  
**Schwere:** 🟡 Warnung  
**Betroffene Dateien:**
- S1: [Aufgabenstellung](arc-doc/01-Einfuehrung-und-Ziele/01-01-Aufgabenstellung.md#L12), „Wesentliche Features“: vollständige Implementierung der FIDE-Schachregeln.
- S11: [Aufwand](arc-doc/11-Risiken/11-02-Aufwand.md#L22), „Risikominderung“: zunächst keine 50-Züge-Regel und Stellungswiederholung; angeblich keine Konsequenzen für die Korrektheit.

**Beschreibung:** Die Maßnahme reduziert den ausdrücklich zugesagten Regelumfang. „Zunächst“ deutet eine Übergangslösung an, benennt aber weder deren Ende noch die verbleibende Einschränkung der Regelvollständigkeit. Das Auslassen von Remisregeln beweist nicht, dass einzelne ausgegebene Züge illegal sind; F01 ist deshalb kein unmittelbarer Gegenbeleg. Der belegbare Konflikt betrifft den vollständigen Regelumfang aus S1.

**Lösungsvorschlag:** In S11 die Aussage über folgenlose Korrektheit ersetzen:
> Der Verzicht auf die 50-Züge-Regel und Stellungswiederholung gilt ausschließlich für die erste Demonstrationsfassung. Diese erfüllt den in S1 zugesagten vollständigen FIDE-Regelumfang noch nicht. Vor der Freigabe als vollständig regelkonforme Engine werden beide Regeln implementiert und durch Tests zur Partiehistorie und Remisbehandlung abgesichert.

#### [KRQ-02] Experimentierbarkeit bleibt ohne eigene Risikobetrachtung

**Konflikttyp:** K1 – Blinder Fleck in der Risikoanalyse  
**Schwere:** 🟡 Warnung  
**Betroffene Dateien:**
- S1: [Qualitätsziele](arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md#L10), „Einladende Experimentierplattform“, zweites Ziel der groben Priorisierung.
- S10: [Qualitätsszenarien](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L16), W04, W05 und P01.
- S11: [Aufwand](arc-doc/11-Risiken/11-02-Aufwand.md) und [Spielstärke](arc-doc/11-Risiken/11-03-Spielstaerke.md): keine Betrachtung der Austauschbarkeit.

**Beschreibung:** Neue Bewertungen und Protokolle sollen ohne Änderungen bestehenden Codes integrierbar sein; eine neue Stellungsrepräsentation darf einschließlich Austausch maximal eine Woche beanspruchen. Die allgemeinen Risiken zu Aufwand und Spielstärke erfassen mögliche Kopplungshindernisse nicht. Eine vollständige Absicherung dieser anspruchsvollen Zusagen ist innerhalb der geprüften Sektionen nicht belegt.

**Lösungsvorschlag:** S11 um folgenden Risikoeintrag ergänzen:
> Risiko: Enge Kopplung verhindert die zugesagte Experimentierbarkeit. Betroffen sind W04, W05 und P01. Zur Minderung führen wir exemplarisch eine alternative Stellungsbewertung, eine alternative Stellungsrepräsentation und einen weiteren Protokolladapter ein. Wir prüfen die unveränderte Integration bestehenden Codes gemäß W04/P01 und erfassen für W05 den Gesamtaufwand einschließlich Austausch; dieser darf eine Woche nicht überschreiten.

#### [KRQ-03] Antwortzeitrisiko hat keine konkret zugeordnete Minderung

**Konflikttyp:** K2 – Unmitigiertes Qualitätsrisiko  
**Schwere:** 🟡 Warnung  
**Betroffene Dateien:**
- S1: [Qualitätsziele](arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md#L13), „Schnelles Antworten auf Züge“.
- S10: [Qualitätsszenarien](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L23), E01 und E02.
- S11: [Spielstärke](arc-doc/11-Risiken/11-03-Spielstaerke.md#L8), lange Wartezeiten; Abschnitt „Risikominderung“.

**Beschreibung:** Das Antwortzeitrisiko ist ausdrücklich erfasst. Die Maßnahme verweist allgemein auf Szenarien, konkretisiert die Tests anschließend jedoch ausschließlich hinsichtlich Spielstärke. Eine Maßnahme für die Fünf-Sekunden-Grenze von E01 sowie Erstzug und Denkrückmeldung aus E02 fehlt. Vorab gespielte Partien umgehen die Live-Situation, erfüllen aber die Antwortzeitanforderungen nicht.

**Lösungsvorschlag:** Die Risikominderung in 11.3 ergänzen:
> Für E01 und E02 messen wir Antwortzeiten auf einer dokumentierten Referenzumgebung und mit einem festgelegten Satz von Teststellungen. Die Zugberechnung erhält ein Zeitbudget und liefert bei dessen Ablauf den besten bisher gefundenen legalen Zug. Zusätzlich prüfen wir Erstzug und Denkrückmeldung im integrierten Frontend. Änderungen werden gemeinsam gegen E01/E02 und F02–F04 geprüft, damit Zeitbegrenzungen nicht unbemerkt die geforderte Spielstärke unterlaufen.

#### [KRQ-04] Ungültige Eingaben implizieren ein nicht dokumentiertes Risiko

**Konflikttyp:** K4 – Implizites Risiko nicht dokumentiert  
**Schwere:** 🟡 Warnung  
**Betroffene Dateien:**
- S10: [Qualitätsszenarien](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L25), Z01 und Z02; [Qualitätsbaum](arc-doc/10-Qualitaetsanforderungen/10-01-Qualitaetsbaum.md), Fehlertoleranz und Fehlervermeidung.
- S11: [Frontend-Anbindung](arc-doc/11-Risiken/11-01-Frontend.md) und [Aufwand](arc-doc/11-Risiken/11-02-Aufwand.md): keine Betrachtung fehlerhafter Eingaben und Zustandsbeschädigung.

**Beschreibung:** Z01 fordert Ablehnung eines unzulässigen Gegenzugs mit anschließend fehlerfreiem Weiterspielen; Z02 fordert Erkennung einer unzulässigen Anfangsstellung und Spielabbruch. Das Risiko unzureichender Validierung oder beschädigten Spielzustands wird weder durch das reine Anbindungsrisiko noch durch das allgemeine Implementierungsaufwandrisiko konkret erfasst.

**Lösungsvorschlag:** S11 ergänzen:
> Risiko: Ungültige Züge oder Anfangsstellungen werden akzeptiert oder verändern den Spielzustand unzulässig. Betroffen sind Z01 und Z02. Wir validieren Eingaben vor Zustandsänderungen. Integrationstests prüfen die Ablehnung ungültiger Züge, den unveränderten Zustand und die anschließende Fortsetzung mit einem gültigen Zug. Ungültige Anfangsstellungen müssen erkannt werden und zur Beendigung des Spiels führen.

#### [KRQ-05] Risiken für das höchstpriorisierte Anschauungsziel bleiben unkonkret

**Konflikttyp:** K4 – Implizites Risiko nicht dokumentiert  
**Schwere:** 🟡 Warnung  
**Betroffene Dateien:**
- S1: [Qualitätsziele](arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md#L9), „Zugängliches Beispiel“; [Stakeholder](arc-doc/01-Einfuehrung-und-Ziele/01-03-Stakeholder.md), Architektinnen und Architekten ohne tiefe Schachkenntnisse.
- S10: [Qualitätsszenarien](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L13), W01–W03.
- S11: [Spielstärke](arc-doc/11-Risiken/11-03-Spielstaerke.md#L5), einfache Zugänglichkeit als konkurrierendes Ziel; keine entsprechende Prüfmaßnahme.

**Beschreibung:** S11 erkennt den Zielkonflikt zwischen einfacher Lösung, Spielstärke und Effizienz, operationalisiert dessen Verständlichkeitsseite jedoch nicht. Risiken unverständlicher Dokumentation, fehlender arc42-Beispielinhalte oder einer nicht nachvollziehbaren Zuordnung zum Quelltext fehlen. Gerade W01–W03 und die Stakeholder ohne tiefe Schachkenntnisse machen diese Risiken relevant.

**Lösungsvorschlag:** Die Risikobeschreibung und Minderung in 11.3 ergänzen:
> Verbesserungen der Spielstärke und Effizienz können die Verständlichkeit des Fallbeispiels beeinträchtigen; veraltete Dokumentation kann außerdem die Zuordnung zum Quelltext erschweren. Wir prüfen W01 mit Personen mit UML- und Schachgrundkenntnissen anhand der 15-Minuten-Grenze. Für W02 prüfen wir die Auffindbarkeit von Beispielinhalten zu jedem arc42-Kapitel; für W03 die Zuordnung beschriebener Module zum Quelltext. Architekturänderungen werden gemeinsam mit ihrer Dokumentation überprüft.

**Anzahl:** 🔴 Kritisch: **0** · 🟡 Warnung: **5** · 🟢 Hinweis: **0** · Gesamt: **5**  
**Ampelstatus:** 🟡 **Gelb**. Risiken und Maßnahmen sind teilweise zugeordnet; es bestehen relevante Lücken und ein nicht ausreichend abgegrenzter Zielkonflikt beim Regelumfang. K5: Kein belastbarer Priorisierungswiderspruch feststellbar. Die Befunde betreffen die dokumentierte Konsistenz und belegen weder tatsächliche Implementierungsfehler noch das Fehlen von Absicherungen außerhalb der geprüften Sektionen.

## Konfliktkarte

| Sektion | Involviert in Konflikten |
|---|---|
| S1 — Einführung/Ziele | 8 |
| S4 — Lösungsstrategie | 8 |
| S10 — Qualitätsanforderungen | 8 |
| S9 — Entscheidungen | 7 |
| S8 — Konzepte | 5 |
| S11 — Risiken | 5 |
| S2 — Randbedingungen | 3 |
| S3 — Kontextabgrenzung | 2 |
| S5 — Bausteinsicht | 2 |

## Zusammenfassung

| Kategorie | Sektions-Reviews | Konfliktanalysen | Gesamt |
|---|---:|---:|---:|
| 🔴 Kritische Befunde | 2 | 0 | **2** |
| 🟡 Warnungen / Empfehlungen | 49 | 17 | **66** |
| 🟢 Hinweise | 7 | 3 | **10** |

Status: 10 von 12 Sektionen 🟡, 2 Sektionen 🔴 (S10, S11); 6 von 7 Konfliktdimensionen 🟡, 1 Dimension 🟢 (S5 ↔ S6 ↔ S7). Gesamtstatus: 🔴.

### Handlungsempfehlungen

1. **Spielstärke operationalisieren (S10-01, KQS-04, S01-03):** Taktische Szenarien F02–F04 über einen versionierten FEN-Testkorpus reproduzierbar machen und entweder ein Partieszenario mit Referenzgegnern und Erfolgsschwelle ergänzen oder die Zusage in S1/S4 auf die taktischen Fähigkeiten zurücknehmen.
2. **Fehlende Risiken aufnehmen (S11-01, KRQ-04, KRQ-02, KRQ-03, KRQ-05):** Unzureichend validierte Eingabedaten (Stellungen, Eröffnungsbibliotheken) aus 8.4 sowie Risiken für Experimentierbarkeit, Antwortzeit und Verständlichkeit in Sektion 11 ergänzen; Risiken priorisieren (S11-02) und historische Risiken zeitlich einordnen (S11-03).
3. **Regelumfang konsistent darstellen (KRQ-01, S11-04, S12-04, S03-02, KKB-01):** 50-Züge-Regel, Stellungswiederholung, Remisangebote und Aufgabe als bekannte Einschränkung beziehungsweise technische Schuld in S1, S3, S11 und Glossar einheitlich kennzeichnen.
4. **Fehlende ADRs ergänzen (KSE-01, KSE-02, KKE-01, KKE-02, KKE-03):** Dependency Injection ohne Framework, reaktive Anbindung, Suchverfahren, Polyglot-Format, Logging-Verzicht und Fehlervertrag als Entscheidungen in Sektion 9 dokumentieren; Konzepte in S8 auf das WIE beschränken.
5. **Asynchronen Ereignis- und Fehlervertrag festlegen (S05-02, S06-01 bis S06-03, S08-01, S08-02, S08-04):** Abbruch, nachlaufende Kandidaten, Suche ohne legale Züge und Fehlerpfade in S5, S6, S8 einheitlich beschreiben und durch Tests absichern.
6. **Messbarkeit der Qualitätsszenarien herstellen (S10-02 bis S10-06, KQS-01, KQS-02):** E01/E02 abgrenzen und Messprofil festlegen, W02–W05, Z01/Z02 und K01 mit Zeit-, Aufwands- und Zustandskriterien versehen.
7. **Historische Stände und Referenzumgebung klären (S09-01, S09-02, S02-02, S02-03, S07-02, S07-03):** Entscheidungsdatum vs. Bewertungsstand 2011, Java-/Windows-/Hardware-Referenz und Messnachweis zu Stellungsobjekten ergänzen.
8. **Konsistenz und Terminologie bereinigen (S04-01, KRC-01, S12-01 bis S12-08, S03-04, KKB-02):** Zielbezeichnung „Akzeptable Spielstärke“ übernehmen, ADR-Strukturbegriffe eindeutschen, Glossardefinitionen und fehlende Begriffe ergänzen, Computergegner-Anbindung über den XBoard-Client dokumentieren.
9. **Restliche Empfehlungen und Hinweise** (Stakeholder-Ergänzungen, Begründung der Zerlegung, Laufzeitszenarien, Nachweise zu Gradle/CheckStyle/Lizenzen) im Zuge der Überarbeitung der jeweiligen Sektionen umsetzen.
