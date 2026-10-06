# arc42 Dokumentations-Review

**Dokumentation:** [arc-doc](arc-doc/) · **System:** DokChess · **Reviewdatum:** 05.10.2026  
**Analysemodus:** DATEI-MODUS, vollständiges Review. Kein Wissensgraph, keine Graphskripte und keine früheren Reviewberichte wurden als Analysequelle verwendet.

## Prüfrahmen

Die Dokumentation hat ein Multi-Folder-Layout. Alle 38 Sektionsdateien wurden durch die zwölf zuständigen Sektionsagenten vollständig gelesen. Die sieben spezialisierten Konfliktagenten prüften zusätzlich sämtliche Dateien ihrer jeweiligen Sektionskombinationen. Referenzierte Diagramme und Screenshots wurden für die betreffenden Sektions- und Konfliktprüfungen einbezogen. Der [Architekturüberblick](arc-doc/00-Ueberblick/00-00-Overview.md) dient als Kontext: DokChess ist insbesondere ein didaktisches Architekturbeispiel. Die [Lizenzdatei](arc-doc/LICENSE.md) gehört nicht zu einer arc42-Sektion und wurde nicht rechtlich bewertet.

Es handelt sich um ein Dokumentationsreview, nicht um einen Quellcode-, Laufzeit-, Leistungs- oder Lizenzkonformitätsnachweis. Aussagen über Implementierung und Testergebnisse werden nur insoweit beurteilt, wie sie in der Dokumentation belegt sind. Unbekannte Konfigurationen, Grenzwerte und Verantwortlichkeiten werden nicht ergänzt oder als vorhandene Fakten ausgegeben.

Die Textvorschläge sind Vorschläge zur Änderung der Dokumentation. Wo sie eine neue Soll-Regel formulieren, muss deren Umsetzung beziehungsweise bewusste Aufnahme in den Soll-Umfang bestätigt werden. Angaben in eckigen Klammern müssen vor Übernahme fachlich ausgefüllt werden. Historische Projektangaben sind nicht allein wegen ihres Alters mangelhaft; unklare Vermischungen von historischem und aktuellem Stand werden dagegen benannt.

**Gesamtstatus: 🔴** Ein kritischer Konflikt betrifft das zugesagte vollständige FIDE-Regelwerk und die ausdrücklich ausgelassenen Remisregeln. Die übrigen Befunde sind Empfehlungen oder Hinweise, keine nachgewiesenen Implementierungsfehler.

## Gesamtübersicht

| Sektion | Status | Befunde |
|---------|--------|---------|
| 1. Einführung und Ziele | 🟡 | 3 Empfehlungen: Überprüfbarkeit der Ziele und vollständige Stakeholder-Erwartungen. |
| 2. Randbedingungen | 🟡 | 5 Empfehlungen: Java-Version, Hardwareprofil, Formate, Effizienzbezug und Veröffentlichungsumfang. |
| 3. Kontextabgrenzung | 🟡 | 3 Empfehlungen, 1 Hinweis: tatsächlicher Schnittstellenumfang, Datenflüsse und technische Zuordnung. |
| 4. Lösungsstrategie | 🟡 | 2 Empfehlungen: einheitliches Spielstärkeziel und Abgrenzung der Suchvarianten. |
| 5. Bausteinsicht | 🟡 | 2 Empfehlungen: Zerlegungsbegründung und eingeschränkter Regelumfang. |
| 6. Laufzeitsicht | 🟡 | 1 Empfehlung: weitere Eingabeverarbeitung während der Suche explizit darstellen. |
| 7. Verteilungssicht | 🟡 | 2 Empfehlungen, 1 Hinweis: Motivation, explizites Baustein-Mapping und Infrastrukturgrenzen. |
| 8. Konzepte | 🟡 | 2 Empfehlungen, 1 Hinweis: Fehlerfortsetzung, Querverweise und Grenzen von FEN. |
| 9. Entscheidungen | 🟡 | 2 Empfehlungen, 1 Hinweis: zeitliche Entscheidungsbasis, Benchmarknachweis und Nebenläufigkeit. |
| 10. Qualitätsanforderungen | 🟡 | 4 Empfehlungen: Spielstärkeabnahme, messbare Prüfschritte, Zeitmessung und Fehlerreaktionen. |
| 11. Risiken | 🟡 | 3 Empfehlungen: Priorisierung, Folgen ausgelassener Regeln und Erfolgskriterien. |
| 12. Glossar | 🟡 | 5 Empfehlungen: zentrale Begriffe und präzisere Schachregeldefinitionen. |

## Sektions-Reviews

### Sektion 1: Einführung und Ziele

**Stärken:** Der didaktische Zweck, die wesentlichen Funktionen und die Abgrenzung gegenüber maximaler Spielstärke sind klar. Fünf architekturrelevante Qualitätsziele sind grob priorisiert und mit Abschnitt 10 verknüpft. Drei Dateien wurden geprüft.

#### S01-01 Qualitätsziele mit prüfbaren Nachweisen verbinden

**Schwere:** 🟡 Empfehlung  
**Datei:** [01-02-Qualitaetsziele.md](arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md#L9)  
**Kriterium:** Konkretisierung der Qualitätsziele durch überprüfbare Szenarien.

**Befund:** Formulierungen wie „rasch“, „angemessener Aufwand“ und „stark genug“ sind als Überblick sinnvoll, benötigen aber nachvollziehbare Abnahmekriterien in S10. Dort gibt es bereits Zeitgrenzen; insbesondere die Spielstärkeabnahme bleibt offen. Siehe S10-01 bis S10-03.

**Änderungsvorschlag:**
> Die Qualitätsziele werden durch die Szenarien in Abschnitt 10 konkretisiert. Die dort angegebenen Zeit- und Aufwandsgrenzen gelten unter den jeweils dokumentierten Prüfbedingungen. Für die Spielstärke sind Referenzgegner, Testfälle und Abnahmekriterien noch festzulegen.

#### S01-02 Spielende als Stakeholder ergänzen

**Schwere:** 🟡 Empfehlung  
**Dateien:** [01-01-Aufgabenstellung.md](arc-doc/01-Einfuehrung-und-Ziele/01-01-Aufgabenstellung.md#L10), [01-03-Stakeholder.md](arc-doc/01-Einfuehrung-und-Ziele/01-03-Stakeholder.md#L9)  
**Kriterium:** Relevante Stakeholder und ihre Erwartungen.

**Befund:** Gelegenheitsspielende und menschliche Gegner werden als Zielgruppe und Spielpartner genannt, fehlen aber in der Stakeholder-Tabelle.

**Änderungsvorschlag:** Zusätzliche Tabellenzeile:
> | Menschliche Spielende, insbesondere Gelegenheitsspielende | Erwarten regelkonforme Partien, nachvollziehbare Rückmeldungen des Frontends und eine Spielstärke, die fordert, ohne den Beispielcharakter zu überlagern. Der konkrete Spielstärkeanspruch wird in Abschnitt 10 festgelegt. |

#### S01-03 Erwartung der Organisation klären

**Schwere:** 🟡 Empfehlung  
**Datei:** [01-03-Stakeholder.md](arc-doc/01-Einfuehrung-und-Ziele/01-03-Stakeholder.md#L12)  
**Kriterium:** Erwartungen statt bloßer Hintergrundinformationen dokumentieren.

**Befund:** Bei oose werden Schulungsangebot und Arbeitgeberbezug beschrieben, aber keine eigene Erwartung an DokChess. Eine Zuständigkeit für Pflege oder Entscheidungen ist daraus nicht ableitbar.

**Änderungsvorschlag:** Tabellenzeile präzisieren:
> | oose Innovative Informatik | Erwartung an DokChess als Schulungsbeispiel: [konkrete Erwartung bestätigen]. Eine Zuständigkeit für Pflege oder Architekturentscheidungen ist in dieser Dokumentation nicht festgelegt. |

### Sektion 2: Randbedingungen

**Stärken:** Technische und organisatorische Vorgaben sowie Konventionen sind getrennt und tabellarisch dargestellt. Build ohne IDE, Entwicklungswerkzeuge, Lizenz und Hosting werden konkret benannt. Drei Dateien wurden geprüft.

#### S02-01 Java-Zielversion eindeutig machen

**Schwere:** 🟡 Empfehlung  
**Datei:** [02-01-Technisch.md](arc-doc/02-Randbedingungen/02-01-Technisch.md#L9)  
**Kriterium:** Verbindliche technische Randbedingungen von Entwicklungsständen unterscheiden.

**Befund:** Java SE 6, 7 und 11 erscheinen als Entwicklungsstände; die verbindliche Mindest- oder Zielversion und die Zusicherung für spätere Versionen bleiben unklar.

**Änderungsvorschlag:**
> Die genannten Java-SE-Versionen beschreiben Entwicklungsstände von DokChess. Für die hier dokumentierte Fassung gilt Java SE [Mindestversion festlegen] als Mindestversion; geprüft wurde sie mit [JDK/JRE-Version ergänzen]. Spätere Java-Versionen sind erwünscht, aber ohne entsprechenden Test nicht zugesichert.

#### S02-02 Qualitative Hardwarevorgabe einordnen

**Schwere:** 🟡 Empfehlung  
**Datei:** [02-01-Technisch.md](arc-doc/02-Randbedingungen/02-01-Technisch.md#L7)  
**Kriterium:** Prüfbarkeit technischer Randbedingungen.

**Befund:** „Marktübliches Standard-Notebook“ erklärt den Vorführzweck, definiert aber kein reproduzierbares Hardwareprofil für Effizienzprüfungen.

**Änderungsvorschlag:**
> Die Ausführung auf einem marktüblichen Standard-Notebook ist eine qualitative Zielsetzung für Seminare und Konferenzen. Eine Mindestkonfiguration wird hier nicht zugesichert. Für die Zeitmessungen nach E01 und E02 wird dagegen eine dokumentierte Referenzplattform verwendet.

#### S02-03 Standards den Schach-Datenarten zuordnen

**Schwere:** 🟡 Empfehlung  
**Datei:** [02-03-Konventionen.md](arc-doc/02-Randbedingungen/02-03-Konventionen.md#L10)  
**Kriterium:** Konventionen operationalisieren.

**Befund:** Etablierte offene Standards sind vorgeschrieben, ohne hier die zuständigen Beschreibungen zu benennen. XBoard, Polyglot und FEN sind in anderen Sektionen bereits dokumentiert; es fehlt kein pauschal neues Format.

**Änderungsvorschlag:**
> Die Protokollkommunikation verwendet XBoard (Abschnitt 5.2), der optionale Eröffnungsbuchzugriff Polyglot (Abschnitt 5.5), und Teststellungen werden in FEN angegeben (Abschnitt 8.7). Für weitere tatsächlich verwendete Datenarten wird der ausgewählte Standard in der zuständigen Baustein- oder Konzeptbeschreibung benannt; eigene Austauschformate werden nicht eingeführt.

#### S02-04 Effizienztests mit Anforderungen verknüpfen

**Schwere:** 🟡 Empfehlung  
**Datei:** [02-02-Organisatorisch.md](arc-doc/02-Randbedingungen/02-02-Organisatorisch.md#L12)  
**Kriterium:** Anforderungen und Prüfmittel nachvollziehbar verbinden.

**Befund:** JUnit soll Effizienzvorgaben prüfen, deren konkreter Bezug aber an dieser Stelle fehlt.

**Änderungsvorschlag:**
> JUnit-Tests prüfen die Effizienzvorgaben E01 und E02 aus Abschnitt 10.2. Die betreffenden Tests dokumentieren die Referenzplattform, Suchkonfiguration und Messgrenzen und referenzieren die jeweilige Szenario-ID.

#### S02-05 Veröffentlichungsumfang präzisieren

**Schwere:** 🟡 Empfehlung  
**Datei:** [02-02-Organisatorisch.md](arc-doc/02-Randbedingungen/02-02-Organisatorisch.md#L13)  
**Kriterium:** Eindeutige organisatorische Vorgaben.

**Befund:** „Die Quelltexte der Lösung oder zumindest Teile“ lässt den zugesagten Veröffentlichungsumfang offen. Daraus folgt kein belegter Lizenzverstoß.

**Änderungsvorschlag:**
> Unter der GNU General Public License Version 3.0 werden [gesamter DokChess-Quelltext oder konkret benannte Teile ergänzen] veröffentlicht. Der Veröffentlichungsumfang und der Ablageort werden in der Projektbeschreibung angegeben.

### Sektion 3: Kontextabgrenzung

**Stärken:** Fachliche und technische Blackbox-Sicht unterscheiden Gegner, Client und Bibliotheken. XBoard, Polyglot und lesender Buchzugriff sind beschrieben. Zwei Dateien und beide Kontextdiagramme wurden geprüft.

#### S03-01 Remisangebote vom tatsächlich unterstützten Umfang abgrenzen

**Schwere:** 🟡 Empfehlung  
**Dateien:** [03-01-Fachlicher-Kontext.md](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md#L13), [05-02-XBoard-Protokoll.md](arc-doc/05-Bausteinsicht/05-02-XBoard-Protokoll.md#L42)  
**Kriterium:** Kontext darf keine nicht unterstützte Schnittstellenfähigkeit suggerieren.

**Befund:** Der Kontext nennt Remisangebote als Austausch zwischen Gegnern. S5 bezeichnet Remisangebote und die Aufgabe der Gegenseite dagegen als nicht unterstützte Features. Sektionsübergreifende Einordnung: KKB-01.

**Änderungsvorschlag:**
> DokChess tauscht mit dem Gegner Züge aus. Remisangebote und die Aufgabe der Gegenseite sind mögliche fachliche Interaktionen einer Schachpartie, werden von der hier dokumentierten XBoard-Implementierung jedoch nicht unterstützt.

#### S03-02 Endspieldatenbank sichtbar als Zukunftsoption kennzeichnen

**Schwere:** 🟡 Empfehlung  
**Dateien:** [03-01-Fachlicher-Kontext.md](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md#L28), [03-02-Technischer-Kontext.md](arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md#L21)  
**Kriterium:** Aktuellen Systemumfang und mögliche Erweiterung unterscheiden.

**Befund:** Fachlicher Text und Diagramm zeigen die optionale Endspielanbindung. Erst der technische Kontext erklärt ausdrücklich, dass sie nicht implementiert ist. Es fehlt keine aktuell zugesicherte Implementierung, wohl aber eine konsistente Kennzeichnung.

**Änderungsvorschlag:**
> Die Endspieldatenbank ist eine mögliche spätere Erweiterung und im aktuellen Stand nicht angebunden. Die entsprechende Verbindung im fachlichen Kontextdiagramm beschreibt keinen vorhandenen technischen Anschluss.

Im Diagramm die Verbindung zusätzlich als „zukünftig, nicht implementiert“ beschriften.

#### S03-03 Fachliche Datenflüsse ergänzen

**Schwere:** 🟡 Empfehlung  
**Datei:** [03-01-Fachlicher-Kontext.md](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md#L5)  
**Kriterium:** Ein-/Ausgaben und Richtung externer Beziehungen.

**Befund:** Das fachliche Diagramm zeigt Verbindungen ohne Datenflussbeschriftung. Der Text enthält Beispiele, aber keine kompakte vollständige Zuordnung.

**Änderungsvorschlag:** Tabelle im Kontext ergänzen:
> | Partner | Von außen an DokChess | Von DokChess nach außen | Technische Abbildung |
> | --- | --- | --- | --- |
> | Gegner, vermittelt über einen Client | Gegenzug und unterstützte Steuerkommandos | Engine-Zug und unterstützte Rückmeldungen | XBoard über Standard-Ein-/Ausgabe |
> | Optionales Eröffnungsbuch | Passender Buchzug oder kein Treffer | Stellung als Suchkriterium beim lokalen lesenden Zugriff | Polyglot-Datei |
> | Endspieldatenbank | Keine aktuelle Eingabe | Keine aktuelle Ausgabe | Noch nicht implementiert |

#### S03-04 Fachliche und technische Gegnerzuordnung erläutern

**Schwere:** 🟢 Hinweis  
**Dateien:** [03-01-Fachlicher-Kontext.md](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md#L11), [03-02-Technischer-Kontext.md](arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md#L9)  
**Kriterium:** Zuordnung fachlicher Partner zu technischen Gegenstellen.

**Befund:** Menschlicher Gegner und Computergegner sind fachlich unterschieden; technisch erscheint nur ein XBoard-Client. Eine direkte Engine-zu-Engine-Verbindung ist dadurch nicht belegt. Siehe KKB-02.

**Änderungsvorschlag:**
> Fachlich kann der Gegner ein Mensch oder eine andere Engine sein. Technisch kommuniziert DokChess mit einem XBoard-kompatiblen Client über Standard-Ein-/Ausgabe. Für Partien gegen eine andere Engine ist hier noch zu beschreiben, welcher Client die Partie vermittelt; eine direkte Engine-zu-Engine-Verbindung wird nicht zugesichert.

### Sektion 4: Lösungsstrategie

**Stärken:** Die Strategie verbindet Qualitätsziele mit Entwurfsansätzen und verweist auf Bausteine, Konzepte, Laufzeit und ADRs. Austauschbarkeit und der Vorrang von Verständlichkeit werden nachvollziehbar begründet. Vier Dateien wurden geprüft.

#### S04-01 Spielstärkeziel einheitlich benennen

**Schwere:** 🟡 Empfehlung  
**Dateien:** [04-01-Einstieg.md](arc-doc/04-Loesungsstrategie/04-01-Einstieg.md#L12), [01-02-Qualitaetsziele.md](arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md#L12)  
**Kriterium:** Rückverfolgbarkeit der Strategie zu Qualitätszielen.

**Befund:** S1 nennt „Akzeptable Spielstärke (Funktionale Eignung)“, S4 „Attraktive Spielstärke (Attraktivität)“. Der Qualitätsbaum erlaubt Mehrfachzuordnungen; die Zielbezeichnung sollte trotzdem stabil bleiben.

**Änderungsvorschlag:** Strategie-Tabellenzeile ersetzen:
> | Akzeptable Spielstärke (Funktionale Eignung; zusätzlich Attraktivität) | Integration von Eröffnungsbibliotheken; Minimax und geeignete Stellungsbewertung; Integrationstests mit taktischen Aufgaben und Mattsituationen gemäß F02–F04 |

#### S04-02 Algorithmus, Suchadapter und Standardkonfiguration trennen

**Schwere:** 🟡 Empfehlung  
**Dateien:** [04-03-Spielstrategie.md](arc-doc/04-Loesungsstrategie/04-03-Spielstrategie.md#L8), [05-07-Zugsuche.md](arc-doc/05-Bausteinsicht/05-07-Zugsuche.md#L16)  
**Kriterium:** Strategisches Nebenläufigkeitsmodell verständlich beschreiben.

**Befund:** S4 nennt einen nicht nebenläufigen Basis-Minimax und daneben parallele sowie reaktive Verarbeitung. S5 erklärt bereits einen blockierenden Algorithmus und einen parallelen Suchadapter. Diese Ebenen sind vereinbar; die konkret verwendete Standardkonfiguration bleibt aber unklar. Siehe KQS-02.

**Änderungsvorschlag:**
> `MinimaxAlgorithmus` berechnet einen Zug blockierend und deterministisch. `MinimaxParalleleSuche` implementiert die Suchschnittstelle, untersucht Teilbäume parallel und liefert Kandidaten über den Observer zurück. Die Standardkonfiguration der hier beschriebenen DokChess-Fassung verwendet [konkrete Suchimplementierung und Suchtiefe ergänzen]. Parallelität der Suche und Verarbeitung weiterer XBoard-Eingaben sind getrennte Eigenschaften.

### Sektion 5: Bausteinsicht

**Stärken:** Die Zerlegung von Ebene 1 bis zur Engine-Whitebox ist nachvollziehbar. Verantwortlichkeiten, Schnittstellen, Pakete und Einschränkungen sind überwiegend angegeben. Acht Dateien und acht referenzierte Diagramme wurden geprüft. Der Remisangebotsbefund wird unter S03-01 und KKB-01 geführt, nicht als zusätzlicher S5-Befund wiederholt.

#### S05-01 Zerlegung begründen

**Schwere:** 🟡 Empfehlung  
**Datei:** [05-01-Ebene-1.md](arc-doc/05-Bausteinsicht/05-01-Ebene-1.md#L5)  
**Kriterium:** Motivation der statischen Verantwortlichkeitsaufteilung.

**Befund:** Die vier Subsysteme werden gezeigt und beschrieben, aber die Zerlegung entlang dieser Verantwortlichkeiten wird nicht ausdrücklich begründet.

**Änderungsvorschlag:**
> Die Zerlegung trennt Protokollkommunikation, Schachregeln, Zugermittlung und Eröffnungswissen. Protokollverarbeitung und Eröffnungszugriff können so verändert werden, ohne die Spielregeln oder Suchstrategie mit ihren technischen Details zu vermischen.

#### S05-02 Regelumfang nicht als vollständig darstellen

**Schwere:** 🟡 Empfehlung  
**Datei:** [05-03-Spielregeln.md](arc-doc/05-Bausteinsicht/05-03-Spielregeln.md#L7)  
**Kriterium:** Zweck und Grenzen des Bausteins zutreffend beschreiben.

**Befund:** Die einleitende FIDE-Aussage klingt umfassend, während später eingeschränkte Remiserkennung dokumentiert wird. Der übergreifende Zusagekonflikt ist KRQ-01.

**Änderungsvorschlag:**
> Das Subsystem implementiert die von DokChess unterstützten Schachregeln. Es ermittelt gültige Züge und erkennt Schach, Matt und Patt. Die Remiserkennung ist eingeschränkt: Die 50-Züge-Regel und Stellungswiederholungen sind nicht implementiert. Damit wird keine vollständige Umsetzung sämtlicher FIDE-Regeln zugesichert.

### Sektion 6: Laufzeitsicht

**Stärken:** Das zentrale Szenario zeigt Validierung, Eröffnungsabfrage, asynchrone Zugkandidaten, Suchabschluss und Ausgabe. Es verwendet die Subsysteme aus S5 konsistent. Eine Datei und das Sequenzdiagramm wurden geprüft.

#### S06-01 Eingaben während der Suche im Szenario zeigen

**Schwere:** 🟡 Empfehlung  
**Datei:** [06-01-Zugermittlung.md](arc-doc/06-Laufzeitsicht/06-01-Zugermittlung.md#L14)  
**Kriterium:** Architekturrelevantes Laufzeitverhalten konkret darstellen.

**Befund:** Der Text fordert Reaktion auf weitere Eingaben während langer Berechnungen. Das Diagramm zeigt asynchrone Kandidaten, aber keine weitere Client-Eingabe. Kandidatenereignisse allein belegen keine weitere Protokollverarbeitung.

**Änderungsvorschlag:**
> Die Engine liefert Zugkandidaten asynchron zurück. Die Verarbeitung weiterer XBoard-Eingaben während einer laufenden Suche ist im dargestellten Ablauf nicht enthalten. Ein ergänzendes Szenario dokumentiert [unterstütztes Steuerkommando ergänzen], dessen Behandlung durch das Protokoll-Subsystem und die daraus folgende Aktion der Engine.

Das ergänzende Sequenzdiagramm erst nach Bestätigung des tatsächlichen Ablaufs hinzufügen; ein Abbruchpfad darf nicht allein aus der Asynchronität abgeleitet werden.

### Sektion 7: Verteilungssicht

**Stärken:** Die lokale Windows-Konfiguration nennt Arena, JRE, JAR, Batchdatei, Ablage und Standard-Ein-/Ausgabe. Die Variante ohne Eröffnungsbuch und das Wrapper-Thema sind sichtbar. Eine Datei und das Deployment-Diagramm wurden geprüft; Cloud-Infrastruktur ist nicht erforderlich.

#### S07-01 Zweck der Beispielkonfiguration erklären

**Schwere:** 🟡 Empfehlung  
**Datei:** [07-01-Infrastruktur-Windows.md](arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md#L5)  
**Kriterium:** Motivation der gezeigten Verteilung.

**Befund:** Windows und Arena werden als Beispiel genannt. Der didaktische Zweck und die Grenze dieser Variante sollten ausdrücklich von einer allgemeinen Plattformzusage getrennt werden.

**Änderungsvorschlag:**
> Diese Darstellung zeigt beispielhaft den lokalen Einsatz von DokChess unter Windows mit Arena auf einem PC. Sie erläutert die benötigten Laufzeit- und Startartefakte und ist keine vollständige Beschreibung aller unterstützten Frontends oder Betriebssysteme.

#### S07-02 Bausteine explizit auf das JAR abbilden

**Schwere:** 🟡 Empfehlung  
**Datei:** [07-01-Infrastruktur-Windows.md](arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md#L16)  
**Kriterium:** Mapping von Softwarebausteinen auf Infrastruktur.

**Befund:** „Sämtliche Module“ im JAR ist plausibel, aber nur implizit mit den vier Subsystemen aus S5 verbunden. Eine zusätzliche Deployment-Ebene ist dafür nicht nötig.

**Änderungsvorschlag:**
> DokChess.jar enthält die Subsysteme XBoard-Protokoll, Spielregeln, Engine und Eröffnung. Die Batchdatei startet das JAR in der Java Runtime Environment auf dem Windows-PC. In dieser Beispielvariante wird keine externe Eröffnungsbibliothek verwendet.

#### S07-03 Fehlende Infrastrukturkennzahlen transparent machen

**Schwere:** 🟢 Hinweis  
**Datei:** [07-01-Infrastruktur-Windows.md](arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md#L10)  
**Kriterium:** Reichweite der Infrastrukturvoraussetzungen.

**Befund:** CPU-, Speicher- und konkrete Versionsgrenzen sind nicht angegeben. Für ein Beispiel ist das kein kritischer Mangel; daraus darf aber kein Leistungsnachweis abgeleitet werden.

**Änderungsvorschlag:**
> Für diese Beispielkonfiguration sind keine konkreten CPU- oder Speichergrenzen spezifiziert. Die Umgebung für reproduzierbare Antwortzeitprüfungen wird bei E01 und E02 dokumentiert.

### Sektion 8: Querschnittliche Konzepte

**Stärken:** Abhängigkeiten, Domänenmodell, Oberfläche, Validierung, Fehlerbehandlung, Logging und Testbarkeit sind sinnvoll ausgewählt. Sieben Dateien und sieben zugehörige Bilder wurden geprüft. Keine pauschale Lücke für Cloud-, Security- oder Betriebskonzepte wird aus dem lokalen Beispiel abgeleitet.

#### S08-01 Fortsetzung nach unerwarteten Exceptions begrenzen

**Schwere:** 🟡 Empfehlung  
**Datei:** [08-05-Fehlerbehandlung.md](arc-doc/08-Konzepte/08-05-Fehlerbehandlung.md#L9)  
**Kriterium:** Fehlerklassen und Folgen nachvollziehbar behandeln.

**Befund:** Nicht erwartete Exceptions gelten als Programmierfehler, zugleich fängt XBoard sämtliche Exceptions ab und DokChess arbeitet „normal“ weiter. Es fehlt die Grenze, bis zu der ein konsistenter Spielzustand und sichere Fortsetzung angenommen werden dürfen.

**Änderungsvorschlag als zu bestätigende Soll-Regel:**
> Erwartete Laufzeitfehler werden dem Client mit `tellusererror` gemeldet. Bei unerwarteten Exceptions darf eine Fortsetzung nicht allein dem Anwenderurteil überlassen werden. Eine Partie wird nur fortgesetzt, wenn der Spielzustand nachweislich konsistent ist; andernfalls wird sie beendet oder neu initialisiert. Die konkrete Behandlung und Diagnose unerwarteter Exceptions ist noch festzulegen.

#### S08-02 Konzeptumsetzung mit Bausteinen verlinken

**Schwere:** 🟡 Empfehlung  
**Dateien:** [08-04-Validierung.md](arc-doc/08-Konzepte/08-04-Validierung.md#L5), [08-05-Fehlerbehandlung.md](arc-doc/08-Konzepte/08-05-Fehlerbehandlung.md#L11), [08-06-Logging.md](arc-doc/08-Konzepte/08-06-Logging.md#L13), [08-07-Testbarkeit.md](arc-doc/08-Konzepte/08-07-Testbarkeit.md#L12)  
**Kriterium:** Querschnittliche Regeln zu den betroffenen Bausteinen zurückverfolgen.

**Befund:** Die Konzepte benennen Subsysteme, verlinken deren Bausteinbeschreibungen aber weniger konsequent als S8.1 und S8.2.

**Änderungsvorschlag:** Jeweils als Querverweis einfügen:
> Validierung: siehe die Bausteine [XBoard-Protokoll](arc-doc/05-Bausteinsicht/05-02-XBoard-Protokoll.md), [Spielregeln](arc-doc/05-Bausteinsicht/05-03-Spielregeln.md) und [Eröffnung](arc-doc/05-Bausteinsicht/05-05-Eroeffnung.md). Fehlerbehandlung: siehe XBoard-Protokoll und [Engine](arc-doc/05-Bausteinsicht/05-04-Engine.md). Logging: siehe XBoard-Protokoll. Testbarkeit: siehe Spielregeln, Engine und [Zugsuche](arc-doc/05-Bausteinsicht/05-07-Zugsuche.md).

Bei Übernahme in S8 die Links relativ zum jeweiligen Sektionsordner setzen.

#### S08-03 FEN nicht mit vollständiger Partiehistorie gleichsetzen

**Schwere:** 🟢 Hinweis  
**Dateien:** [08-02-Domaenenmodell.md](arc-doc/08-Konzepte/08-02-Domaenenmodell.md#L27), [08-07-Testbarkeit.md](arc-doc/08-Konzepte/08-07-Testbarkeit.md#L16)  
**Kriterium:** Fachliche Daten und ihre Grenzen präzise definieren.

**Befund:** FEN wird als „komplette Spielsituation“ beschrieben. Es enthält die aktuelle Stellung samt Zählern, nicht den gesamten Partieverlauf. Welche FEN-Zähler das Domänenobjekt intern hält, bleibt offen.

**Änderungsvorschlag:**
> FEN beschreibt die aktuelle Stellung einschließlich der in der Notation enthaltenen Zugzähler, nicht den vollständigen Partieverlauf. Aus einer einzelnen FEN-Angabe lässt sich eine vorherige Stellungswiederholung nicht vollständig ermitteln. Welche FEN-Felder die Klasse `Stellung` intern abbildet, ist gesondert zu dokumentieren.

### Sektion 9: Architekturentscheidungen

**Stärken:** Beide Entscheidungen haben Status und Datum, nennen Alternativen, Einflussfaktoren und Folgen. Die Protokollwahl und die unveränderlichen Stellungsobjekte sind nachvollziehbar begründet. Zwei Dateien wurden geprüft; eine andere ADR-Gliederung als ein bestimmtes Schema wäre kein Mangel.

#### S09-01 Entscheidungsdatum und historische Evidenz unterscheiden

**Schwere:** 🟡 Empfehlung  
**Datei:** [09-01-Anbindung.md](arc-doc/09-Entscheidungen/09-01-Anbindung.md#L5)  
**Kriterium:** Zeitliche Gültigkeit und Belastbarkeit der Entscheidungsbasis.

**Befund:** Der Status ist auf 10.03.2026 datiert, die untersuchten Frontends auf 2011. Die Annahme, wenige untersuchte Frontends deckten alle relevanten Optionen ab, ist nicht belegt. Es bleibt unklar, ob 2026 eine erneute Entscheidung oder nur Dokumentationspflege bezeichnet.

**Änderungsvorschlag:**
> Die Vergleichsdaten der Frontends stammen aus der Bestandsaufnahme von 2011. Das Statusdatum 10.03.2026 bezeichnet [Entscheidungsbestätigung oder redaktionelle Überarbeitung klären]. Die Entscheidung gilt für den dokumentierten Anforderungskontext; heutige Frontend-Kompatibilität und vollständige Marktabdeckung werden damit nicht nachgewiesen.

#### S09-02 Prototypmessung nicht als unbelegten Grenzwertnachweis verwenden

**Schwere:** 🟡 Empfehlung  
**Datei:** [09-02-Stellungsobjekte.md](arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md#L50)  
**Kriterium:** Nachvollziehbare Abwägung des Effizienznachteils.

**Befund:** Mattsuche, Minimax und Matt in drei sind als Messkontext genannt. Für „ca. 30 Prozent“ und „innerhalb der geforderten Grenzen“ fehlen aber Referenzhardware, absolute Laufzeiten, konkrete Grenzwerte und ein reproduzierbarer Testfall.

**Änderungsvorschlag:**
> Im Prototypvergleich zur Mattsuche lag die unveränderliche Variante bei etwa 30 Prozent längerer Laufzeit. Die Messung ist ohne dokumentierte Teststellung, Plattform, absolute Zeiten und Abnahmegrenze nicht reproduzierbar und belegt daher nicht für sich die Einhaltung von E01 oder E02. Diese Angaben sind nachzutragen; bis dahin gilt sie als vorläufige Entscheidungsgrundlage.

#### S09-03 Nebenläufigkeitsvorteil nicht als Garantie darstellen

**Schwere:** 🟢 Hinweis  
**Datei:** [09-02-Stellungsobjekte.md](arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md#L49)  
**Kriterium:** Reichweite der Konsequenzen einer Entscheidung.

**Befund:** Unveränderliche Stellungen erleichtern parallele Verarbeitung; daraus folgt nicht, dass sämtliche gemeinsam verwendeten Ressourcen oder die zustandsbehaftete Engine threadsicher sind. Ein solcher Fehler ist nicht belegt.

**Änderungsvorschlag:**
> Die Unveränderlichkeit von `Stellung` erleichtert nebenläufige Suche, garantiert aber nicht die Threadsicherheit des Gesamtsystems. Die gemeinsam genutzten Ressourcen der konkreten Such- und Engine-Konfiguration sind gesondert zu betrachten.

### Sektion 10: Qualitätsanforderungen

**Stärken:** Qualitätsbaum und Tabelle decken alle fünf priorisierten Ziele ab. Szenario-IDs stimmen mit der Abbildung überein. Zeit- und einzelne Aufwandsgrenzen sind bereits konkret. Zwei Dateien und der Qualitätsbaum wurden geprüft; F04 ist ausdrücklich dem Spielstärkeziel zugeordnet.

#### S10-01 Taktische Tests von der Spielstärkeabnahme unterscheiden

**Schwere:** 🟡 Empfehlung  
**Dateien:** [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L19), [01-02-Qualitaetsziele.md](arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md#L12)  
**Kriterium:** Prüffähige Szenarien und Abdeckung des Qualitätsziels.

**Befund:** F02–F04 beschreiben nützliche taktische Situationen, aber keine festen Ausgangsstellungen und Abnahmeauswertung. Einzelne Taktiktests weisen zudem nicht nach, dass DokChess schwache Gegner sicher schlägt und Gelegenheitsspielende fordert. Das ist eine Nachweislücke, kein belegtes Scheitern der Engine und deshalb kein kritischer Befund.

**Änderungsvorschlag:**
> F02–F04 verwenden den festgelegten Positionssatz [FEN-Stellungen und erwartete Ergebnisse ergänzen] mit [Suchkonfiguration ergänzen]. Für F04 wird die Mattführung gegen alle relevanten Gegenantworten geprüft. Zusätzlich wird das allgemeine Spielstärkeziel anhand [Referenzgegner, Zeitkontrolle, Anzahl Partien und Erfolgsmaßstab festlegen] abgenommen. Taktiktests und Spielstärkeabnahme sind getrennte Nachweise.

#### S10-02 Erfolg der Verständlichkeits- und Erweiterungsszenarien definieren

**Schwere:** 🟡 Empfehlung  
**Datei:** [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L12)  
**Kriterium:** Erwartete Reaktion und Beobachtungskriterium konkretisieren.

**Befund:** W01 hat eine Zeitgrenze, aber keine beobachtbare Verständniskontrolle. „Unverzüglich“ und „ohne Umwege“ sind subjektiv. W04 und P01 enthalten bereits objektive Änderungsverbote; es fehlen vor allem Ausgangskonfiguration und Prüfschritte, nicht eine pauschale zusätzliche Zeitgrenze.

**Änderungsvorschlag:**
> W01 gilt als erfüllt, wenn die Testperson innerhalb von 15 Minuten die vier Subsysteme, ihre Verantwortlichkeiten und den Ablauf der Zugermittlung korrekt erläutern kann. Für W02 und W03 werden Aufgaben und zulässige Suchzeiten vor dem Test festgelegt. W04 und P01 werden mit einer dokumentierten Ausgangsversion geprüft; bestehende Quellen bleiben unverändert, und die neue Bewertung beziehungsweise das neue Protokoll wird in einem Integrationstest tatsächlich verwendet.

#### S10-03 Zeitgrenzen unter reproduzierbaren Bedingungen prüfen

**Schwere:** 🟡 Empfehlung  
**Datei:** [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L22)  
**Kriterium:** Reproduzierbare Effizienzszenarien und eindeutiger Messumfang.

**Befund:** E01 fordert fünf Sekunden, E02 zehn Sekunden für den ersten Zug und eine Rückmeldung spätestens nach fünf Sekunden. Plattform, Suchkonfiguration und Messbeginn fehlen. Außerdem ist zu klären, ob E02 eine Ausnahme von E01 oder ein Startfall mit zusätzlichen Initialisierungskosten ist.

**Änderungsvorschlag:**
> E01 und E02 werden auf [Hardware, Betriebssystem und JVM ergänzen] mit [Positionssatz und Suchkonfiguration ergänzen] geprüft. E01 misst von der Annahme eines Gegenzugs bis zur Ausgabe des Engine-Zugs und gilt für laufende Partien. E02 beschreibt den gesonderten Startfall mit [Umfang der Initialisierung klären]; hier gilt die Zehn-Sekunden-Grenze für den ersten Zug und die Fünf-Sekunden-Grenze für die Rückmeldung „denkt“.

Diese Abgrenzung nur übernehmen, wenn die Ausnahme fachlich gewollt ist; andernfalls E01 und E02 auf dieselbe Zugantwortgrenze vereinheitlichen.

#### S10-04 Fehlerreaktionen und Zustandsinvarianten festlegen

**Schwere:** 🟡 Empfehlung  
**Datei:** [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L24)  
**Kriterium:** Fehlerszenarien mit beobachtbarer Reaktion.

**Befund:** Z01 und Z02 nennen Ablehnung beziehungsweise Spielende, aber keine konkrete Außenreaktion und keinen Nachweis für „fehlerfrei weiter“. Testfälle für ungültige Züge und Stellungen sind nicht ausgewiesen.

**Änderungsvorschlag:**
> Z01 verwendet [ungültigen Zug und Ausgangsstellung ergänzen]. DokChess meldet [vorgesehene XBoard-Reaktion bestätigen], verändert die Stellung nicht und akzeptiert anschließend einen festgelegten gültigen Zug. Z02 verwendet [ungültige Startstellung ergänzen]; DokChess meldet [Fehlerreaktion bestätigen] und startet keine Zugermittlung. Der anschließende Protokoll- und Partiezustand wird ausdrücklich festgelegt und geprüft.

### Sektion 11: Risiken und technische Schulden

**Stärken:** Die drei Risiken nennen Ursachen, Auswirkungen, Gegenmaßnahmen und Eventualfallplanungen. Querverweise zu Anforderungen und Qualität sind vorhanden. Drei Dateien wurden geprüft.

#### S11-01 Risiken priorisieren

**Schwere:** 🟡 Empfehlung  
**Dateien:** [11-01-Frontend.md](arc-doc/11-Risiken/11-01-Frontend.md#L3), [11-02-Aufwand.md](arc-doc/11-Risiken/11-02-Aufwand.md#L3), [11-03-Spielstaerke.md](arc-doc/11-Risiken/11-03-Spielstaerke.md#L3)  
**Kriterium:** Handlungsleitende Risikobewertung.

**Befund:** Die Risiken sind beschrieben, aber nicht sichtbar bewertet oder nach Priorität geordnet. Für das Beispiel genügt eine qualitative Bewertung; erfundene Wahrscheinlichkeiten wären kein Gewinn.

**Änderungsvorschlag:**
> Für jedes Risiko werden Eintrittswahrscheinlichkeit, Auswirkung und daraus abgeleitete Priorität qualitativ bewertet. Bewertungsstand und Gültigkeitszeitraum werden angegeben. Die Übersicht wird nach Priorität geordnet; bislang fehlende Bewertungen sind als „noch nicht bewertet“ gekennzeichnet.

#### S11-02 Folgen der Regelreduktion sachlich richtig beschreiben

**Schwere:** 🟡 Empfehlung  
**Datei:** [11-02-Aufwand.md](arc-doc/11-Risiken/11-02-Aufwand.md#L23)  
**Kriterium:** Auswirkungen von Risikomaßnahmen zutreffend darstellen.

**Befund:** Das Weglassen der 50-Züge-Regel und Stellungswiederholung wird als ohne Konsequenz für die Korrektheit dargestellt. Die Legalität einzelner Züge kann erhalten bleiben, aber Remisansprüche und Partieenden sind nicht vollständig abgedeckt. Der Widerspruch zur Aufgabenstellung ist KRQ-01.

**Änderungsvorschlag:**
> Das vorläufige Weglassen der 50-Züge-Regel und Stellungswiederholung reduziert den Implementierungsaufwand, schränkt aber die Erkennung von Remisansprüchen ein. Damit ist die Partieabwicklung nicht vollständig FIDE-konform. Diese Einschränkung wird im Funktionsumfang ausdrücklich ausgewiesen.

#### S11-03 Maßnahmen mit Abnahme und Projektstand verbinden

**Schwere:** 🟡 Empfehlung  
**Dateien:** [11-01-Frontend.md](arc-doc/11-Risiken/11-01-Frontend.md#L19), [11-03-Spielstaerke.md](arc-doc/11-Risiken/11-03-Spielstaerke.md#L21)  
**Kriterium:** Maßnahmen prüfbar und nachverfolgbar formulieren.

**Befund:** PoC und Schachaufgaben sind geeignete Maßnahmen; Erfolgskriterien und Ergebnisse beziehungsweise offener Status fehlen. Angesichts historischer Termine muss klar sein, ob die Texte eine damalige Planung oder aktuelle offene Risiken beschreiben.

**Änderungsvorschlag:**
> Der Frontend-PoC wird anhand K01 und dokumentierter Integrationsschritte bewertet. Die Spielstärketests verwenden die in Abschnitt 10 festgelegten Testfälle und Abnahmekriterien. Für jede Maßnahme werden Prüfstand und Ergebnis oder „noch nicht durchgeführt“ angegeben. Historische Planungen werden als solche gekennzeichnet und nicht als aktuelle Maßnahmenliste ausgegeben.

### Sektion 12: Glossar

**Stärken:** Das Glossar ist tabellarisch aufgebaut, enthält 24 Einträge und deckt wichtige Schach- und Computerschachbegriffe ab. Zwei Dateien wurden geprüft. Übersetzungslisten sind ohne mehrsprachigen Nutzungskontext nicht erforderlich.

#### S12-01 Zentrale Architektur- und Suchbegriffe ergänzen

**Schwere:** 🟡 Empfehlung  
**Dateien:** [12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md), [08-02-Domaenenmodell.md](arc-doc/08-Konzepte/08-02-Domaenenmodell.md#L27), [05-07-Zugsuche.md](arc-doc/05-Bausteinsicht/05-07-Zugsuche.md#L34)  
**Kriterium:** Gemeinsames Verständnis zentraler Fachbegriffe.

**Befund:** Stellung, Stellungsbewertung und Suchtiefe prägen die Architektur, fehlen aber im Glossar.

**Änderungsvorschlag:**
> | Stellung | Aktuelle Spielsituation einschließlich Figurenbelegung, Spieler am Zug und relevanter Zugrechte. Welche weiteren Zustandsdaten DokChess speichert, beschreibt das Domänenmodell. |
> | Stellungsbewertung | Zahlenwert, der die Vorteilhaftigkeit einer Stellung aus einer festgelegten Spielerperspektive ausdrückt. |
> | Suchtiefe | Anzahl der Halbzüge, die eine Suche vorausschauend untersucht. |

#### S12-02 Endspiel nicht über Figurenarten definieren

**Schwere:** 🟡 Empfehlung  
**Datei:** [12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md#L8)  
**Kriterium:** Fachlich klare Definition.

**Befund:** „Wenige Figurenarten“ ist kein geeignetes allgemeines Kennzeichen; gemeint ist typischerweise reduziertes Material.

**Änderungsvorschlag:**
> | Endspiel | Späte Phase einer Schachpartie, in der typischerweise viele Figuren getauscht wurden und nur noch wenig Material auf dem Brett steht. |

#### S12-03 Zeitfenster für en passant nennen

**Schwere:** 🟡 Empfehlung  
**Datei:** [12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md#L10)  
**Kriterium:** Regelbegriffe eindeutig erklären.

**Befund:** Die Definition enthält nicht die Beschränkung auf den unmittelbar folgenden Zug.

**Änderungsvorschlag:**
> | en passant | Sonderregel für Bauern: Zieht ein gegnerischer Bauer von seiner Grundreihe zwei Felder vor und steht danach neben dem eigenen Bauern, darf dieser ihn unmittelbar im nächsten Zug so schlagen, als wäre der gegnerische Bauer nur ein Feld vorgerückt. |

#### S12-04 Zählweise der 50-Züge-Regel präzisieren

**Schwere:** 🟡 Empfehlung  
**Datei:** [12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md#L5)  
**Kriterium:** Vollzüge und Halbzüge unterscheiden.

**Befund:** „50 Züge lang“ lässt offen, ob Aktionen eines Spielers oder beider Spieler gemeint sind.

**Änderungsvorschlag:**
> | 50-Züge-Regel | Ein Spieler kann unter den vorgesehenen FIDE-Bedingungen Remis reklamieren, wenn während der jeweils letzten 50 Züge beider Spieler weder ein Bauer gezogen noch eine Figur geschlagen wurde; das entspricht 100 Halbzügen. |

#### S12-05 Identität wiederholter Stellungen definieren

**Schwere:** 🟡 Empfehlung  
**Datei:** [12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md#L25)  
**Kriterium:** Voraussetzungen der Regel präzisieren.

**Befund:** „Dieselbe Stellung“ wird nicht erläutert. Spieler am Zug und mögliche Züge, insbesondere Rochade- und en-passant-Rechte, sind relevant, nicht nur die Figurenbelegung.

**Änderungsvorschlag:**
> | Stellungswiederholung | Ein Spieler kann unter den vorgesehenen FIDE-Bedingungen Remis reklamieren, wenn dieselbe Stellung mindestens zum dritten Mal auftritt. Gleich sein müssen Figurenbelegung und Spieler am Zug; auch die möglichen Züge, insbesondere Rochade- und en-passant-Möglichkeiten, müssen übereinstimmen. |

## Sektionsübergreifende Konflikte

Die folgenden Matrizen unterscheiden Widersprüche von Zuordnungs-, Nachweis- und Strukturfragen. Eine Warnung bedeutet nicht automatisch einen implementierten Defekt. Wiederholte Sachverhalte aus Sektionsreviews werden über Befund-IDs verknüpft.

| Konfliktdimension | Status | Befunde |
|---|---|---|
| Qualitätsstrang (S1 ↔ S4 ↔ S10) | 🟡 | 3 Warnungen: Mattbewertung nicht erklärt, Standardkonfiguration offen, Zeitprüfung nicht reproduzierbar. |
| Strategie ↔ Entscheidungen (S4 ↔ S9) | 🟢 | Keine Konflikte; XBoard und unveränderliche Stellungen sind konsistent begründet. |
| Constraint-Compliance (S2 ↔ S4/S8/S9) | 🟢 | Keine belegten Verstöße; offene Effizienznachweise werden in S02-02, S09-02 und S10-03 behandelt. |
| Kontext ↔ Bausteine (S3 ↔ S5) | 🟡 | 2 Warnungen: Remisangebote und Zuordnung des Computergegners. |
| Sichten-Konsistenz (S5 ↔ S6 ↔ S7) | 🟢 | Keine Konflikte; optionaler Buchbetrieb und Beispiel ohne Buch sind vereinbar. |
| Konzepte ↔ Entscheidungen (S8 ↔ S9) | 🟢 | 1 Hinweis: DI-Framework-Verzicht kann als Entscheidung gezielter auffindbar gemacht werden. |
| Risiken ↔ Qualität (S11 ↔ S1/S10) | 🔴 | 1 kritischer Konflikt, 3 Warnungen: Regelvollständigkeit und teilweise offene Qualitätssicherung. |

### 1. Qualitätsstrang (S1 ↔ S4 ↔ S10)

| Qualitätsziel aus S1 | Strategie in S4 | Szenarien in S10 | Bewertung |
|---|---|---|---|
| Zugängliches Beispiel | arc42-Überblick, Domänenmodell, deutsche Namen | W01–W03, W05 | Inhaltlich abgedeckt; Erfolgskontrolle präzisieren, S10-02. |
| Experimentierplattform | Schnittstellen, DI, unveränderliche Objekte | W04, W05, P01 | Grundsätzlich konsistent. |
| Bestehende Frontends | XBoard und Java | K01 | Grundsätzlich konsistent. |
| Akzeptable Spielstärke | Eröffnungsbuch, Minimax, Materialbewertung | F02–F04 | Taktische Abnahme und terminale Bewertungen klären. |
| Schnelles Antworten | Suchvarianten, reaktive Anbindung, Zeitprüfungen | E01, E02 | Konfiguration, Messbedingungen und Startfall abgrenzen. |

#### KQS-01 Matt-in-zwei-Anforderung nicht mit der beschriebenen Bewertung erklärt

**Konflikttyp:** K2 – Strategie trägt Qualitätsanforderung nicht nachvollziehbar  
**Schwere:** 🟡 Warnung  
**Beteiligte Sektionen:** S4, S10  
**Betroffene Dateien:** [04-03-Spielstrategie.md](arc-doc/04-Loesungsstrategie/04-03-Spielstrategie.md#L8), [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L21)

**Beschreibung:** S4 beschreibt ausschließlich Materialbewertung an Terminalknoten und erklärt zugleich, die einfachen Implementierungen erfüllten die Szenarien. F04 fordert ein erzwungenes Matt in zwei. Eine Materialbewertung allein erklärt die Bevorzugung eines Matts nicht; eine gesonderte Behandlung terminaler Spielergebnisse ist möglich, aber hier nicht dokumentiert. Das Review belegt keinen Suchfehler. F04 ist im Qualitätsbaum korrekt zugeordnet.

**Lösungsvorschlag:** Nach Abgleich mit dem tatsächlichen Suchverhalten ergänzen:
> Für F04 ist die Behandlung terminaler Spielergebnisse ausdrücklich zu beschreiben. Falls Matt und Patt getrennt von der Materialheuristik bewertet werden, sind diese Werte und die Priorität eines Matts gegenüber Materialgewinnen anzugeben. Die Testkonfiguration für Matt in zwei untersucht die erforderlichen vier Halbzüge und prüft die Mattführung gegen die möglichen Gegenantworten.

### KQS-02 Nebenläufigkeit und Standardkonfiguration bleiben unklar

**Konflikttyp:** K2 – Strategiezuordnung unvollständig  
**Schwere:** 🟡 Warnung  
**Beteiligte Sektionen:** S4, S10  
**Betroffene Dateien:** [04-01-Einstieg.md](arc-doc/04-Loesungsstrategie/04-01-Einstieg.md#L13), [04-03-Spielstrategie.md](arc-doc/04-Loesungsstrategie/04-03-Spielstrategie.md#L8), [04-04-Anbindung.md](arc-doc/04-Loesungsstrategie/04-04-Anbindung.md#L11), [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L22)

**Beschreibung:** Übersicht und Anbindung nennen reaktive beziehungsweise nebenläufige Verarbeitung, während die Basisimplementierung nicht nebenläufig ist. S5 beschreibt kompatible Algorithmus- und Adapterebenen. Offen ist, welche konkrete Verdrahtung die Qualitätszusagen erfüllt. Das ist eine Nachvollziehbarkeitslücke, kein bewiesener Widerspruch zwischen synchronem Kern und asynchronem Adapter.

**Lösungsvorschlag:** Zusätzlich zu S04-02 aufnehmen:
> E01 und E02 werden mit der Standardkonfiguration [Suchimplementierung, Adapter, Suchtiefe und Parallelitätsgrad ergänzen] geprüft. Welche weiteren XBoard-Kommandos während der Suche verarbeitet werden, beschreibt das ergänzende Laufzeitszenario in Abschnitt 6.

### KQS-03 Effizienzziel und behauptete Erfüllung ohne reproduzierbaren Nachweis

**Konflikttyp:** K5 – Unzureichende Messbarkeit  
**Schwere:** 🟡 Warnung  
**Beteiligte Sektionen:** S1, S4, S10  
**Betroffene Dateien:** [01-02-Qualitaetsziele.md](arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md#L13), [04-03-Spielstrategie.md](arc-doc/04-Loesungsstrategie/04-03-Spielstrategie.md#L8), [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L22)

**Beschreibung:** Die Effizienzstrategie und die Aussage, die Basis erfülle die Szenarien, sind ohne Referenzplattform und Testkonfiguration nicht unabhängig überprüfbar. Zeitgrenzen existieren bereits und müssen nicht neu erfunden werden. Siehe S10-03.

**Lösungsvorschlag:**
> Die Aussage zur Erfüllung von E01 und E02 bezieht sich auf [dokumentierten Testlauf ergänzen] unter den in Abschnitt 10.2 angegebenen Bedingungen. Solange ein solcher Nachweis nicht dokumentiert ist, beschreibt die Strategie den vorgesehenen Ansatz, nicht eine nachgewiesene Erfüllung.

### 2. Strategie ↔ Entscheidungen (S4 ↔ S9)

| Strategie | Entscheidung | Ergebnis |
|---|---|---|
| XBoard als Kommunikationsprotokoll | ADR 9.1 wählt XBoard primär und erlaubt spätere Erweiterung | Konsistent. |
| Unveränderliche Stellung | ADR 9.2 wählt unveränderliche Stellungsobjekte und erläutert Folgen | Konsistent. |
| Austauschbare beziehungsweise parallele Suche | ADR 9.2 nennt die bessere Eignung für Nebenläufigkeit | Kein Widerspruch. |
| Polyglot und Reactive Extensions | Keine eigene ADR in S9 | Allein daraus folgt kein Konflikt. |

**Keine KSE-Befunde.** Strategischer Überblick und Entscheidungsbegründung ergänzen sich sinnvoll. Die historischen Grundlagen und Messbelege werden lokal unter S09-01 und S09-02 behandelt, nicht als Strategie-ADR-Widerspruch gezählt.

### 3. Constraint-Compliance (S2 ↔ S4/S8/S9)

| Randbedingung | Nachgelagerte Aussagen | Bewertung |
|---|---|---|
| Standard-Notebook | Effizienzansätze, Timeout-Tests und Prototypvergleich | Kein belegter Verstoß; Referenzplattform und Nachweis offen. |
| Windows und Java; weitere Betriebssysteme erwünscht | Java-Programm, XBoard, Windows-Batchstart | Vereinbar; weitere Systeme sind keine zwingende Zusage. |
| Freie/kostenlose Fremdsoftware bevorzugt | Freie Frontends betrachtet; keine verpflichtende DI-Framework-Abhängigkeit | Kein belegter Verstoß. |
| JUnit und Effizienztests | JUnit 4, Testbarkeit und Zeitvorgaben beschrieben | Dokumentatorisch konsistent. |
| Team, Zeitplan, Werkzeuge, Gradle, Versionsverwaltung | Keine widersprechende Festlegung in S4/S8/S9 | Kein Konflikt; Ausführung nicht geprüft. |
| GPLv3 und Veröffentlichung | Kein widersprechender Entscheid dokumentiert | Keine rechtliche Compliance-Aussage aus diesem Review. |
| arc42, deutsche Bezeichner, Java-/CheckStyle-Konventionen | arc42 und deutsche Domänenbegriffe aufgegriffen | Kein Konflikt; CheckStyle-Ausführung nicht geprüft. |
| Etablierte Schachformate | XBoard, Polyglot und FEN | Konsistent. |

**Keine KRC-Befunde.** Fehlende aktuelle Mess- oder Lizenznachweise sind nicht mit bewiesenen Constraint-Verletzungen gleichzusetzen. Die kombinierte Effizienzprüfung auf Zielhardware bleibt durch S02-02, S09-02 und S10-03 adressiert. Es wird ausdrücklich nicht behauptet, entsprechende Tests seien bereits erfolgreich durchgeführt worden.

### 4. Kontext ↔ Bausteine (S3 ↔ S5)

| Partner / Austausch | Kontext | Bausteinsicht | Bewertung |
|---|---|---|---|
| Mensch über grafischen Client | Menschlicher Gegner und XBoard-Client | XBoard-Protokoll mit Standard-Ein-/Ausgabe | Konsistent. |
| Computergegner | Andere Schachengine als Gegner | Allgemeiner Client-Anschluss | Technische Vermittlung klären. |
| Remisangebote | Als Informationsaustausch genannt | Nicht unterstütztes Protokollfeature | Umfang widersprüchlich beziehungsweise missverständlich. |
| Optionales Eröffnungsbuch | Polyglot, lesender Zugriff | Eröffnungsbaustein und Polyglot-Adapter | Konsistent. |
| Endspieldatenbank | Technisch ausdrücklich nicht implementiert | Kein entsprechender Baustein | Zukunftsoption, kein fehlender aktueller Baustein. |

#### KKB-01 Remisangebote erscheinen im Kontext als verfügbare Interaktion

**Konflikttyp:** K3 – Widersprüchliche Schnittstellenbeschreibung  
**Schwere:** 🟡 Warnung  
**Beteiligte Sektionen:** S3, S5  
**Betroffene Dateien:** [03-01-Fachlicher-Kontext.md](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md#L13), [05-02-XBoard-Protokoll.md](arc-doc/05-Bausteinsicht/05-02-XBoard-Protokoll.md#L42)

**Beschreibung:** Der allgemeine fachliche Austausch wird nicht vom implementierten DokChess-Umfang getrennt. Dadurch kann S3 eine Zusage suggerieren, die S5 ausdrücklich ausschließt. Siehe S03-01.

**Lösungsvorschlag:** Den Text aus S03-01 in S3 übernehmen und in S5 ergänzen:
> Der fachliche Kontext nennt mögliche Interaktionen einer Schachpartie. Der aktuelle technische Umfang umfasst jedoch weder Remisangebote noch die Aufgabe der Gegenseite über das Protokoll.

#### KKB-02 Computergegner keinem eindeutigen technischen Vermittlungsweg zugeordnet

**Konflikttyp:** K1 – Kontextpartner ohne eindeutige technische Zuordnung  
**Schwere:** 🟡 Warnung  
**Beteiligte Sektionen:** S3, S5  
**Betroffene Dateien:** [03-01-Fachlicher-Kontext.md](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md#L15), [03-02-Technischer-Kontext.md](arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md#L9), [05-02-XBoard-Protokoll.md](arc-doc/05-Bausteinsicht/05-02-XBoard-Protokoll.md#L7)

**Beschreibung:** Der fachliche Computergegner ist vorhanden, aber weder als direkter Protokollpartner noch als durch einen Client vermittelte Engine ausdrücklich eingeordnet. Ein eigener implementierter Anschluss darf nicht vorausgesetzt werden.

**Lösungsvorschlag:** In S3.2 und S5.2 ergänzen:
> Technischer Kommunikationspartner ist ein XBoard-kompatibler Client. Der Einsatz gegen eine andere Engine erfolgt über [vermittelnden Client und Ablauf bestätigen]. Eine separate direkte Engine-zu-Engine-Schnittstelle ist hier nicht beschrieben und wird deshalb nicht zugesichert.

### 5. Sichten-Konsistenz (S5 ↔ S6 ↔ S7)

| Baustein | Statische Sicht | Laufzeit | Deployment | Ergebnis |
|---|---|---|---|---|
| XBoard-Protokoll | Client-Kommunikation | Annahme und Ausgabe von Zügen | JAR, JVM und Frontend-Prozess | Konsistent. |
| Spielregeln | Gültige Züge und Regelprüfung | Validierung und Zugkandidaten | Im JAR enthalten | Konsistent. |
| Engine | Zustandsbehaftete Zugermittlung | Zugannahme und Kandidatenereignisse | Im JAR enthalten | Konsistent. |
| Eröffnung | Optionales Subsystem | Im Beispiel kein Treffer, danach Suche | Beispiel ohne externes Buch | Vereinbare Betriebsvarianten. |
| Zugsuche | Engine-Modul | Auf Engine-Ebene beschrieben | Im JAR enthalten | Keine eigene Lifeline erforderlich. |
| Stellungsbewertung | Engine-Modul | Bewertung auf Engine-Ebene beschrieben | Im JAR enthalten | Granularitätsunterschied, kein Widerspruch. |

**Keine KSV-Befunde.** Die Hierarchieebenen der Sichten dürfen unterschiedlich fein sein. Ein optionales Eröffnungsbuch in S5, ein leerer Buchtreffer in S6 und eine Deployment-Variante ohne externes Buch in S7 widersprechen sich nicht. Zehn Dateien und zehn zugehörige Diagramme wurden in dieser Dimension geprüft.

### 6. Konzepte ↔ Entscheidungen (S8 ↔ S9)

| Konzept | Bezug zu S9 | Ergebnis |
|---|---|---|
| Abhängigkeiten und DI | Keine eigene ADR zum Framework-Verzicht | Verständlich dokumentiert; Auffindbarkeit kann verbessert werden. |
| Domänenmodell und unveränderliche Stellung | ADR 9.2 direkt referenziert | Konsistent; keine unbeabsichtigte Redundanz. |
| Benutzeroberfläche und XBoard | ADR 9.1 | Konsistent mit primärem Protokoll und späterer Erweiterbarkeit. |
| Validierung, Fehlerbehandlung, Logging und Testbarkeit | Keine eigene ADR notwendig | Passende querschnittliche Konzepte. |

#### KKE-01 Framework-Verzicht als Entscheidung gezielt auffindbar machen

**Konflikttyp:** K2 – Struktur-/Zuordnungsfrage  
**Schwere:** 🟢 Hinweis  
**Beteiligte Sektionen:** S8, S9  
**Betroffene Datei:** [08-01-Abhaengigkeiten.md](arc-doc/08-Konzepte/08-01-Abhaengigkeiten.md#L12)

**Beschreibung:** S8 dokumentiert neben dem DI-Muster auch eine ausdrückliche Entscheidung gegen Framework und annotationsgetriebene Konfiguration, einschließlich Alternativen. Diese Festlegung ist bereits nachvollziehbar; eine separate ADR ist keine zwingende arc42-Pflicht. Bei Ausbau von S9 wäre die Entscheidung dort leichter auffindbar.

**Lösungsvorschlag:** Als kurze Entscheidung in S9 oder als verlinkten Entscheidungshinweis aufnehmen:
> **Entscheidung:** Das DokChess-Kernprojekt verwendet kein DI-Framework und keine annotationsgetriebene Konfiguration. Abhängigkeiten werden über Java-Interfaces deklariert; die Verdrahtung erfolgt im Glue-Code beziehungsweise in Tests. **Begründung:** Der Kern bleibt unabhängig von einer DI-Implementierung; Integratoren können die POJOs selbst konfigurieren. **Folge:** Die Komposition liegt bei der einbindenden Anwendung. Die Umsetzung beschreibt Abschnitt 8.1.

### 7. Risiken ↔ Qualität (S11 ↔ S1/S10)

| Ziel / Anforderung | Risiko und Maßnahme | Bewertung |
|---|---|---|
| Zugängliches Beispiel | Kein direkter Risikotreiber belegt | Nicht jedes Ziel muss als eigenes Risiko wiederholt werden. |
| Experimentierplattform | Keine spezifische Gefährdung belegt | Kein pauschaler Abdeckungsbefund. |
| Frontend-Integration, K01/P01 | Frontend-Risiko und PoC | K01 grundsätzlich adressiert; P01-Prüfumfang offen. |
| Spielstärke, F02–F04 | Spielstärkerisiko und taktische Tests | Allgemeines Ziel noch nicht objektiv abgenommen. |
| Antwortzeit, E01/E02 | Lange Wartezeiten als Risikoauswirkung | Zugehörige Maßnahme nicht ausdrücklich zugeordnet. |
| Vollständige FIDE-Regeln, F01 | Aufwandssenkung durch Weglassen zweier Regeln | Expliziter Zusagekonflikt. |

#### KRQ-01 Regelreduktion widerspricht dem zugesagten vollständigen FIDE-Regelwerk

**Konflikttyp:** K3 – Risikomaßnahme widerspricht Anforderung  
**Schwere:** 🔴 Kritisch  
**Beteiligte Sektionen:** S1, S10, S11  
**Betroffene Dateien:** [01-01-Aufgabenstellung.md](arc-doc/01-Einfuehrung-und-Ziele/01-01-Aufgabenstellung.md#L14), [11-02-Aufwand.md](arc-doc/11-Risiken/11-02-Aufwand.md#L23), [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L18)

**Beschreibung:** S1 fordert „Vollständige Implementierung der FIDE-Schachregeln“. S11 nimmt 50-Züge-Regel und Stellungswiederholung ausdrücklich aus und bezeichnet dies als ohne Konsequenzen für die Korrektheit. F01 prüft lediglich die Auswahl legaler Züge, nicht vollständige Remis- und Partieendbehandlung. Kritisch ist die unvereinbare Zusage, nicht eine bewusst reduzierte Beispielimplementierung an sich. S5 bestätigt den eingeschränkten Regelumfang.

**Lösungsvorschlag, passend zum dokumentierten Ist-Stand:** Feature in S1 ersetzen:
> DokChess implementiert die für das Architekturbeispiel beschriebenen Schachregeln einschließlich Zuglegalität, Schach, Matt und Patt. Die 50-Züge-Regel und Stellungswiederholung sind nicht implementiert; eine vollständige Umsetzung aller FIDE-Regeln wird für diesen Stand nicht zugesichert.

S11 mit S11-02 korrigieren und F01 ergänzen:
> F01 prüft die Legalität ausgegebener Züge innerhalb des ausdrücklich dokumentierten Regelumfangs. Es ist kein Nachweis vollständiger FIDE-Regelkonformität.

Falls vollständige FIDE-Regeln tatsächlich verbindlich bleiben sollen, ist stattdessen die Implementierung der ausgelassenen Regeln samt zusätzlicher Szenarien und Tests erforderlich. Ein Dokumentationstext allein schließt diese Umsetzungslücke nicht.

#### KRQ-02 Antwortzeitrisiko ohne ausdrücklich zugeordnete Maßnahme

**Konflikttyp:** K2 – Qualitätsrisiko teilweise unmitigiert  
**Schwere:** 🟡 Warnung  
**Beteiligte Sektionen:** S10, S11  
**Betroffene Dateien:** [11-03-Spielstaerke.md](arc-doc/11-Risiken/11-03-Spielstaerke.md#L9), [11-03-Spielstaerke.md](arc-doc/11-Risiken/11-03-Spielstaerke.md#L21), [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L22)

**Beschreibung:** Das Risiko nennt lange Wartezeiten, die Maßnahme konzentriert sich aber auf Spielstärketests. Zeitprüfungen sind anderswo vorgesehen; ihre Zuordnung zum konkreten Risiko bleibt offen. Daraus folgt nicht, dass solche Tests fehlen oder scheitern.

**Lösungsvorschlag:** In S11.3 ergänzen:
> Zur Minderung des Antwortzeitrisikos prüfen wir zusätzlich E01 und E02 auf der dokumentierten Referenzplattform. Die festgelegten Antwort- und Rückmeldegrenzen sind Abnahmekriterien. Prüfstand und Ergebnis werden zusammen mit den Spielstärketests ausgewiesen.

#### KRQ-03 Taktiktests decken die allgemeine Spielstärkezusage nur teilweise ab

**Konflikttyp:** K2 – Maßnahme deckt Qualitätsziel nur teilweise ab  
**Schwere:** 🟡 Warnung  
**Beteiligte Sektionen:** S1, S10, S11  
**Betroffene Dateien:** [01-02-Qualitaetsziele.md](arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md#L12), [11-03-Spielstaerke.md](arc-doc/11-Risiken/11-03-Spielstaerke.md#L12), [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L19)

**Beschreibung:** S11 erkennt die unklare Mindestspielstärke. F02–F04 konkretisieren Taktiken, aber nicht den Erfolg gegen schwache Gegner oder die angemessene Herausforderung von Gelegenheitsspielenden. Die Maßnahme adressiert das Risiko nur teilweise. Siehe S10-01.

**Lösungsvorschlag:**
> Vor der Abnahme legen wir Referenzgegner, Zeitkontrolle, Umfang der Testserie und ein akzeptiertes Ergebnis für das Spielstärkeziel fest. F02–F04 prüfen ergänzend taktische Fähigkeiten. Solange die Abnahmekriterien fehlen, gilt das Spielstärkerisiko nicht allein aufgrund bestandener Taktiktests als geschlossen.

#### KRQ-04 Prüfumfang des Frontend-PoC gegenüber P01 klären

**Konflikttyp:** K2 – Qualitätsszenario im Maßnahmenumfang nicht nachweisbar  
**Schwere:** 🟡 Warnung  
**Beteiligte Sektionen:** S10, S11  
**Betroffene Dateien:** [11-01-Frontend.md](arc-doc/11-Risiken/11-01-Frontend.md#L19), [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L17), [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L26)

**Beschreibung:** Der PoC ist eine geeignete Maßnahme gegen gescheiterte Integration und passt zu K01. Erfolgreiche Anbindung eines vorhandenen Protokolls beweist aber nicht P01, die Erweiterung um ein bisher nicht implementiertes Protokoll ohne Änderungen bestehender Quellen. Ein einzelner PoC muss nicht beide Ziele erfüllen; der getrennte Nachweis muss sichtbar sein.

**Lösungsvorschlag:**
> Der Frontend-PoC prüft die Integration über ein vorhandenes Protokoll nach K01. Die Erweiterbarkeit nach P01 wird [in einem zusätzlichen PoC oder einem gesonderten Integrationstest festlegen] geprüft. Ein erfolgreicher K01-PoC wird nicht als Nachweis für P01 gewertet.

## Konfliktkarte

Gezählt wird je detailliertem Konfliktbefund einmal pro ausdrücklich beteiligter Sektion, einschließlich des Strukturhinweises KKE-01. Konfliktfreie Dimensionen erzeugen keinen Eintrag; lokale Sektionsbefunde werden hier nicht erneut gezählt.

| Sektion | Involviert in Konflikten |
|---|---|
| S10 – Qualitätsanforderungen | 7 |
| S11 – Risiken | 4 |
| S4 – Lösungsstrategie | 3 |
| S1 – Einführung und Ziele | 3 |
| S3 – Kontextabgrenzung | 2 |
| S5 – Bausteinsicht | 2 |
| S8 – Konzepte | 1 |
| S9 – Entscheidungen | 1 |

## Zusammenfassung

| Kategorie | Anzahl |
|---|---|
| 🔴 Kritische Befunde | 1 |
| 🟡 Warnungen / Empfehlungen | 42 |
| 🟢 Hinweise | 5 |
| **Gesamt** | **48** |

Die Summe umfasst **38 Sektionsbefunde** (34 Empfehlungen, 4 Hinweise) und **10 Konfliktbefunde** (1 kritisch, 8 Warnungen, 1 Hinweis). Ein lokaler Befund und seine sektionsübergreifende Auswirkung können denselben Änderungsbedarf beschreiben; die Summe ist daher keine Zahl unabhängiger Defekte oder notwendiger Einzeländerungen. Die Verknüpfungen zwischen Befund-IDs machen solche Überschneidungen sichtbar. Die Ampel eines Abschnitts entspricht jeweils seiner höchsten Befundschwere; der Gesamtstatus ergibt sich entsprechend aus allen Befunden.

### Handlungsempfehlungen

1. **Regelumfang entscheiden und konsistent dokumentieren (KRQ-01).** Entweder das didaktische Beispiel ausdrücklich mit eingeschränkter Remiserkennung beschreiben oder die vollständige Regelumsetzung verbindlich nachziehen. S1, S5, S10 und S11 gemeinsam abgleichen; die Aussage zur folgenlosen Auslassung korrigieren.
2. **Prüfkonfiguration und Abnahme festlegen (S09-02, S10-01 bis S10-03, KQS-01 bis KQS-03).** Referenzplattform, Suchimplementierung, Suchtiefe, Teststellungen und Messumfang dokumentieren. Taktiktests, allgemeine Spielstärke und Antwortzeit getrennt nachweisen.
3. **Asynchronität und Fehlerfortsetzung konkretisieren (S04-02, S06-01, S08-01).** Algorithmus und Suchadapter unterscheiden, eine tatsächliche Eingabe während der Suche darstellen und Zustandskonsistenz nach unerwarteten Fehlern nicht pauschal zusichern.
4. **Externe Fähigkeiten sauber abgrenzen (S03-01 bis S03-04, KKB-01/KKB-02).** Remisangebote als nicht unterstützt, Endspieldatenbanken als Zukunftsoption und den technischen Weg zu Computergegnern explizit kennzeichnen.
5. **Historische Evidenz und Risikostand sichtbar machen (S09-01, S11-01/S11-03).** Entscheidungsdatum von Erhebungsstand unterscheiden sowie Maßnahmenstatus und qualitative Priorisierung ergänzen.
6. **Navigation und Fachdefinitionen verbessern (S02-03, S05-01, S07-02, S08-02, S12-01 bis S12-05).** Kleine Querverweise und präzise Definitionen schaffen hier mehr Nutzen als zusätzliche Diagramme oder pauschale neue Kapitel.

### Konsolidierungsentscheidungen

- Der kritische Regelkonflikt wird als KRQ-01 geführt. Seine lokalen Formulierungsprobleme in S5 und S11 bleiben Empfehlungen; damit wird nicht derselbe kritische Konflikt mehrfach gezählt.
- Der Spielstärkebefund aus der S10-Prüfung wurde von kritisch auf Empfehlung eingeordnet: fehlende Abnahmekriterien belegen keine unbrauchbare Engine und keinen falschen taktischen Zug.
- Ein vermuteter Zielgruppenwiderspruch wurde nicht übernommen: Grundkenntnisse in Schach und fehlende vertiefte Schachkenntnisse sind miteinander vereinbar.
- Ein vermutetes Fehlen der F04-Zuordnung wurde durch direkte Bildprüfung widerlegt. Die Klammer für „Akzeptable Spielstärke“ umfasst F02, F03 und F04.
- Nicht nebenläufiger Algorithmus und paralleler Adapter wurden nicht als bewiesener Widerspruch gewertet. Der verbleibende Befund betrifft die fehlende Zuordnung einer Standardkonfiguration.
- Kein eigenständiger Befund fordert zusätzliche organisatorische Strategieangaben, sämtliche Q42-Kategorien oder pauschale weitere Risikoperspektiven ohne belegte Relevanz für dieses Beispiel.
- Der DI-Framework-Verzicht ist bereits begründet. Eine separate ADR ist eine optionale Strukturverbesserung, deshalb KKE-01 nur als Hinweis.
- Der S5-Kontextbefund zu Remisangeboten wurde nicht als zusätzliche lokale Wiederholung gezählt; er ist unter S03-01 und KKB-01 enthalten.

## Anhang: Sektionszuordnung der geprüften Dateien

| Sektion | Quelldateien | Anzahl |
|---|---|---|
| S1 | [Aufgabenstellung](arc-doc/01-Einfuehrung-und-Ziele/01-01-Aufgabenstellung.md), [Qualitätsziele](arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md), [Stakeholder](arc-doc/01-Einfuehrung-und-Ziele/01-03-Stakeholder.md) | 3 |
| S2 | [Technisch](arc-doc/02-Randbedingungen/02-01-Technisch.md), [Organisatorisch](arc-doc/02-Randbedingungen/02-02-Organisatorisch.md), [Konventionen](arc-doc/02-Randbedingungen/02-03-Konventionen.md) | 3 |
| S3 | [Fachlicher Kontext](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md), [Technischer Kontext](arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md) | 2 |
| S4 | [Einstieg](arc-doc/04-Loesungsstrategie/04-01-Einstieg.md), [Aufbau](arc-doc/04-Loesungsstrategie/04-02-Aufbau.md), [Spielstrategie](arc-doc/04-Loesungsstrategie/04-03-Spielstrategie.md), [Anbindung](arc-doc/04-Loesungsstrategie/04-04-Anbindung.md) | 4 |
| S5 | [Ebene 1](arc-doc/05-Bausteinsicht/05-01-Ebene-1.md), [XBoard-Protokoll](arc-doc/05-Bausteinsicht/05-02-XBoard-Protokoll.md), [Spielregeln](arc-doc/05-Bausteinsicht/05-03-Spielregeln.md), [Engine](arc-doc/05-Bausteinsicht/05-04-Engine.md), [Eröffnung](arc-doc/05-Bausteinsicht/05-05-Eroeffnung.md), [Ebene 2 Engine](arc-doc/05-Bausteinsicht/05-06-Ebene-2-Engine.md), [Zugsuche](arc-doc/05-Bausteinsicht/05-07-Zugsuche.md), [Stellungsbewertung](arc-doc/05-Bausteinsicht/05-08-Stellungsbewertung.md) | 8 |
| S6 | [Zugermittlung](arc-doc/06-Laufzeitsicht/06-01-Zugermittlung.md) | 1 |
| S7 | [Infrastruktur Windows](arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md) | 1 |
| S8 | [Abhängigkeiten](arc-doc/08-Konzepte/08-01-Abhaengigkeiten.md), [Domänenmodell](arc-doc/08-Konzepte/08-02-Domaenenmodell.md), [Benutzungsoberfläche](arc-doc/08-Konzepte/08-03-Benutzungsoberflaeche.md), [Validierung](arc-doc/08-Konzepte/08-04-Validierung.md), [Fehlerbehandlung](arc-doc/08-Konzepte/08-05-Fehlerbehandlung.md), [Logging](arc-doc/08-Konzepte/08-06-Logging.md), [Testbarkeit](arc-doc/08-Konzepte/08-07-Testbarkeit.md) | 7 |
| S9 | [Anbindung](arc-doc/09-Entscheidungen/09-01-Anbindung.md), [Stellungsobjekte](arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md) | 2 |
| S10 | [Qualitätsbaum](arc-doc/10-Qualitaetsanforderungen/10-01-Qualitaetsbaum.md), [Qualitätsszenarien](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md) | 2 |
| S11 | [Frontend](arc-doc/11-Risiken/11-01-Frontend.md), [Aufwand](arc-doc/11-Risiken/11-02-Aufwand.md), [Spielstärke](arc-doc/11-Risiken/11-03-Spielstaerke.md) | 3 |
| S12 | [Einstieg](arc-doc/12-Glossar/12-01-Einstieg.md), [Begriffe](arc-doc/12-Glossar/12-02-Begriffe.md) | 2 |
| **Gesamt S1–S12** | Vollständig im DATEI-MODUS geprüft | **38** |