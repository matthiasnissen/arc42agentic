# arc42 Dokumentations-Review

## Prüfgrundlage

- **Datum:** 2026-10-06.
- **Umfang:** vollständiges Review aller zwölf arc42-Sektionen und aller sieben Konfliktdimensionen von [arc-doc](arc-doc/).
- **Analyse-Modus:** GRAPH-MODUS. Layout: Multi-Folder; 38 Sektionsdateien, eine Überblicksdatei und eine Lizenzdatei. Keine Sektion fehlt.
- **Graph:** [.arc42-graph_demo_results/FullReviewRunGPT61Sol/arc-doc.graphml](.arc42-graph_demo_results/FullReviewRunGPT61Sol/arc-doc.graphml), mit [Manifest](.arc42-graph_demo_results/FullReviewRunGPT61Sol/arc-doc.manifest.json) und [Extraktion](.arc42-graph_demo_results/FullReviewRunGPT61Sol/arc-doc.extraction.json).
- **Graphbereitstellung:** Am vorgesehenen Pfad existierte kein Graph. Er wurde ausschließlich aus der aktuellen Dokumentation einschließlich ihrer Abbildungen neu aufgebaut. Das Build-Skript und die unabhängige Schema-/Manifestprüfung liefen erfolgreich: 159 Knoten, 458 Kanten, 0 Fehler, 0 Warnungen. 55 Hinweise betreffen Knoten ohne semantische Verknüpfung, nicht Dokumentationsmängel.
- **Evidenz:** 81 explizite, 366 strukturelle und 11 inferierte Kanten. Inferierte Zuordnungen sind keine expliziten Zusagen. Fehlende Graphkanten wurden nicht als Beweis fehlender Dokumentation behandelt.
- **Verfahren:** zwölf spezialisierte Sektionsagenten und sieben spezialisierte Konfliktagenten; anschließende Konsolidierung und gezielte Quellenprüfung bei widersprüchlichen oder unsicheren Aussagen. Die Analyse bleibt graphbasiert; Originaltexte und Bilder dienten der Verifikation, nicht einem alternativen vollständigen Datei-Review.
- **Unabhängigkeit:** Keine bestehenden Review-Ergebnisse wurden gelesen, weder aus `.arc42-graph_demo_results` noch aus dem Repository-Root. Das Ergebnis enthält keine Quellcodeprüfung und keine Aussage über tatsächlich ausgeführte Funktionstests.

**Gesamtstatus: 🔴.** Drei unmittelbar belegte Problemstellungen sind vorrangig: vollständige FIDE-Regeln trotz ausdrücklich ausgelassener Remisregeln, Z02 trotz fehlender Zulässigkeitsprüfung der Startstellung und F01 trotz möglicher ungültiger Eröffnungsbuchzüge. Dies sind Widersprüche in der Dokumentation, keine nachgewiesenen Implementierungsfehler.

### Sektionsmapping

| Sektion | Quellen | Dateien |
|---|---|---:|
| S1 | [Einführung und Ziele](arc-doc/01-Einfuehrung-und-Ziele/) | 3 |
| S2 | [Randbedingungen](arc-doc/02-Randbedingungen/) | 3 |
| S3 | [Kontextabgrenzung](arc-doc/03-Kontextabgrenzung/) | 2 |
| S4 | [Lösungsstrategie](arc-doc/04-Loesungsstrategie/) | 4 |
| S5 | [Bausteinsicht](arc-doc/05-Bausteinsicht/) | 8 |
| S6 | [Laufzeitsicht](arc-doc/06-Laufzeitsicht/) | 1 |
| S7 | [Verteilungssicht](arc-doc/07-Verteilungssicht/) | 1 |
| S8 | [Konzepte](arc-doc/08-Konzepte/) | 7 |
| S9 | [Entscheidungen](arc-doc/09-Entscheidungen/) | 2 |
| S10 | [Qualitätsanforderungen](arc-doc/10-Qualitaetsanforderungen/) | 2 |
| S11 | [Risiken](arc-doc/11-Risiken/) | 3 |
| S12 | [Glossar](arc-doc/12-Glossar/) | 2 |

## Gesamtübersicht

Der Status dieser Tabelle folgt den lokalen Sektionsbefunden. Sektionsübergreifende Widersprüche stehen zusätzlich in der Konflikttabelle und bestimmen ebenfalls den Gesamtstatus.

| Sektion | Status | Befunde |
|---|---|---|
| 1. Einführung und Ziele | 🔴 | Vollständiger FIDE-Umfang widerspricht den dokumentierten Ausnahmen; Stakeholdererwartungen ergänzen. |
| 2. Randbedingungen | 🟡 | Geltungsstand, Bindungsgrad, Hardwareprofil und Auswirkungen präzisieren. |
| 3. Kontextabgrenzung | 🟡 | Datenflüsse und Computergegner-Anbindung klären; Remisangebote abgrenzen. |
| 4. Lösungsstrategie | 🟡 | Spielstärkeziel einheitlich benennen; Effizienzspielraum und Formatwahl erläutern. |
| 5. Bausteinsicht | 🟡 | Zerlegung begründen und FIDE-Zweckbeschreibung enger formulieren. |
| 6. Laufzeitsicht | 🟡 | Abbruch und verspätete Suchereignisse als Laufzeitfall ergänzen. |
| 7. Verteilungssicht | 🟡 | Motivation des Startmechanismus und Referenzumgebung ergänzen. |
| 8. Konzepte | 🟡 | Bausteinverweise und Grenzen des Fortsetzens nach Fehlern ergänzen. |
| 9. Entscheidungen | 🟡 | Historische Frontend-Matrix und Performance-Messgrundlage einordnen. |
| 10. Qualitätsanforderungen | 🟡 | Messbarkeit und Reproduzierbarkeit einzelner Szenarien verbessern. |
| 11. Risiken | 🟡 | Bewertung, Status und überprüfbare Maßnahmen vervollständigen. |
| 12. Glossar | 🟡 | Drei Definitionen schärfen und zwei zentrale Begriffe ergänzen. |

## Sektions-Reviews

### Sektion 1: Einführung und Ziele

Anforderungsüberblick, fünf grob priorisierte Qualitätsziele und Stakeholdertabelle sind vorhanden. Alle fünf Ziele besitzen strategische Ansätze und Qualitätsszenarien. Zusätzliche Anforderungen müssen nicht zwangsläufig in die fünf priorisierten Qualitätsziele aufgenommen werden.

#### [S01-01] Vollständige FIDE-Regeln widersprechen dem beschriebenen Umfang

**Schwere:** 🔴 Kritisch  
**Datei:** [Aufgabenstellung](arc-doc/01-Einfuehrung-und-Ziele/01-01-Aufgabenstellung.md)  
**Kriterium:** Zutreffender und konsistenter Anforderungsüberblick.

**Befund:** `s01-req-fide-regeln` fordert eine „Vollständige Implementierung der FIDE-Schachregeln“. [Spielregeln](arc-doc/05-Bausteinsicht/05-03-Spielregeln.md) schließen dagegen Remiserkennung außer Patt, insbesondere 50-Züge-Regel und Stellungswiederholung, ausdrücklich aus. Der Widerspruch wurde an beiden Originalen geprüft.

**Änderungsvorschlag:** Bei Beibehaltung des beschriebenen Implementierungsumfangs den Feature-Eintrag ersetzen:
> Unterstützung der FIDE-Schachregeln mit dokumentierten Ausnahmen: Die 50-Züge-Regel und die Stellungswiederholung werden derzeit nicht erkannt; weitere Remisfälle außer Patt sind ebenfalls nicht abgedeckt (siehe Abschnitt 5.3).

#### [S01-02] Menschliche Spieler als Stakeholder ergänzen

**Schwere:** 🟡 Empfehlung  
**Datei:** [Stakeholder](arc-doc/01-Einfuehrung-und-Ziele/01-03-Stakeholder.md)  
**Kriterium:** Relevante Nutzergruppen und Erwartungen erfassen.

**Befund:** Die vier Stakeholderknoten nennen Architekturschaffende, Entwickelnde, Stefan Zörner und oose. `s03-partner-mensch`, K01 und E02 beschreiben menschliche Spieler, ohne diese Nutzergruppe in der Stakeholderliste abzubilden.

**Änderungsvorschlag:** Tabellenzeile ergänzen:
> | Menschliche Spielerinnen und Spieler | Spielen gegen DokChess; Erwartungen an Spielstärke und Partieerlebnis: TODO mit der Nutzergruppe klären. |

#### [S01-03] Erwartungen von oose benennen

**Schwere:** 🟡 Empfehlung  
**Datei:** [Stakeholder](arc-doc/01-Einfuehrung-und-Ziele/01-03-Stakeholder.md)  
**Kriterium:** Rolle und Erwartungen eines Stakeholders unterscheiden.

**Befund:** Die Beschreibung von oose nennt Schulungsunternehmen, Arbeitgeber und Seminarangebot, aber keine konkrete Erwartung an Architektur oder Dokumentation.

**Änderungsvorschlag:** Tabellenzeile präzisieren:
> | oose Innovative Informatik | Schulungsunternehmen und Arbeitgeber von Stefan Zörner zum Zeitpunkt der Konzeption; Erwartungen an DokChess als Schulungs- und Architekturbeispiel: TODO klären. |

### Sektion 2: Randbedingungen

Technische, organisatorische und Konventions-Constraints sind getrennt und tabellarisch erläutert. Windows ist ausdrücklich nicht zwingend; frei verfügbare Fremdsoftware wird als Präferenz formuliert. Historische Angaben wurden nicht als automatisch fortgeltende Muss-Vorgaben gewertet.

#### [S02-01] Geltungsstand und Verbindlichkeit präzisieren

**Schwere:** 🟡 Empfehlung  
**Datei:** [Technische Randbedingungen](arc-doc/02-Randbedingungen/02-01-Technisch.md), [Organisatorische Randbedingungen](arc-doc/02-Randbedingungen/02-02-Organisatorisch.md)  
**Kriterium:** Bindungsgrad und zeitlicher Geltungsbereich der Constraints.

**Befund:** Java SE 6, 7 und 11 stehen für unterschiedliche Entwicklungsstände; Zeitplan und Versionsverwaltung sind historisch formuliert. `s02-constraint-java`, `s02-constraint-zeitplan` und `s02-constraint-versionsverwaltung` lassen den für das Review maßgeblichen Stand offen.

**Änderungsvorschlag:** Den betreffenden Einträgen hinzufügen:
> Geltungsstand: TODO Architekturstand oder Bezugsdatum. Verbindlichkeit: TODO verbindlich, Ziel, Präferenz oder historischer Stand. Aktuelle Java-Laufzeitbasis: TODO Version/Versionsbereich; Bedeutung früherer Entwicklungsstände: TODO.

#### [S02-02] Hardware-Randbedingung konkretisieren

**Schwere:** 🟡 Empfehlung  
**Datei:** [Technische Randbedingungen](arc-doc/02-Randbedingungen/02-01-Technisch.md)  
**Kriterium:** Überprüfbare technische Randbedingungen.

**Befund:** `s02-constraint-hardware` nennt ein „marktübliches Standard-Notebook“, ohne Referenzprofil. Die etwa 30 Prozent längere Laufzeit aus ADR 09-02 kann damit nicht auf eine definierte Umgebung bezogen werden.

**Änderungsvorschlag:**
> Referenzhardware: TODO repräsentatives Notebook oder CPU-/Speicherprofil. Relevante Ressourcen- oder Laufzeitgrenzen: TODO. Bis zur Festlegung ist die Hardwareangabe ein qualitatives Ziel, kein überprüfbares Mindestprofil.

#### [S02-03] Konsequenzen und Freiheitsgrade ausweisen

**Schwere:** 🟡 Empfehlung  
**Datei:** [Technische Randbedingungen](arc-doc/02-Randbedingungen/02-01-Technisch.md), [Organisatorische Randbedingungen](arc-doc/02-Randbedingungen/02-02-Organisatorisch.md), [Konventionen](arc-doc/02-Randbedingungen/02-03-Konventionen.md)  
**Kriterium:** Architekturfolgen und verbleibenden Spielraum erläutern.

**Befund:** Hintergründe und Begründungen sind vorhanden; Folgen für Entwurf und Erweiterbarkeit werden jedoch nicht durchgängig ausgewiesen. Das Verbot eigener Datenformate ist ein Beispiel für eine klare Vorgabe ohne systematische Konsequenzbeschreibung.

**Änderungsvorschlag:** Eine Spalte „Konsequenzen und verbleibender Spielraum“ aufnehmen; je Eintrag mit folgendem Text vervollständigen:
> Konsequenz: TODO konkrete Auswirkung auf Architektur oder Umsetzung. Spielraum: TODO innerhalb der Vorgabe frei, nicht verhandelbar oder lediglich Präferenz.

#### [S02-04] Build- und Testanforderungen von Werkzeugpräferenzen abgrenzen

**Schwere:** 🟡 Empfehlung  
**Datei:** [Organisatorische Randbedingungen](arc-doc/02-Randbedingungen/02-02-Organisatorisch.md)  
**Kriterium:** Technische und organisatorische Bindungen erkennbar unterscheiden.

**Befund:** `s02-constraint-werkzeuge` und `s02-constraint-testwerkzeuge` bündeln Werkzeugauswahl mit bindenden Anforderungen wie „allein mit Gradle, also ohne IDE baubar“. Das ist kein Verstoß durch die Tabellenposition, erschwert aber die Unterscheidung von Muss-Anforderung und Präferenz.

**Änderungsvorschlag:** Als technische Anforderung oder mit entsprechendem Querverweis ausweisen:
> Der Build muss mit Gradle ohne IDE ausführbar sein. Tests verwenden JUnit im Annotationsstil. Die konkret zu prüfenden Effizienzgrenzen sind in TODO Szenario-/Testreferenzen festgelegt; organisatorische Werkzeugpräferenzen bleiben hiervon getrennt.

#### [S02-05] Abdeckung weiterer organisatorischer Vorgaben bestätigen

**Schwere:** 🟢 Hinweis  
**Datei:** [Organisatorische Randbedingungen](arc-doc/02-Randbedingungen/02-02-Organisatorisch.md)  
**Kriterium:** Geltungsbereich der Constraint-Erhebung transparent machen.

**Befund:** Politische Vorgaben oder Bindungen durch andere Organisationssysteme sind nicht ausgewiesen. Daraus lässt sich weder deren Existenz noch deren Nichtvorhandensein ableiten.

**Änderungsvorschlag:**
> Weitere politische oder durch Organisationssysteme vorgegebene Randbedingungen: TODO prüfen und benennen. Falls keine bekannt sind, diesen Stand einschließlich Bezugsdatum ausdrücklich bestätigen.

### Sektion 3: Kontextabgrenzung

Fachlicher und technischer Blackbox-Kontext sowie sechs Partnerknoten sind vorhanden. Endspielbibliotheken sind ausdrücklich optional und nicht implementiert; ihr fehlender Adapter ist deshalb kein Befund.

#### [S03-01] Datenflüsse für alle Partner konkretisieren

**Schwere:** 🟡 Empfehlung  
**Datei:** [Fachlicher Kontext](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md), [Technischer Kontext](arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md)  
**Kriterium:** Richtungen und Inhalte des Informationsaustauschs beschreiben.

**Befund:** Partner und Verbindungen sind erkennbar, aber die fachlichen Ein-/Ausgaben sind nicht für alle Partner gleichermaßen konkretisiert. Der Computergegner verweist pauschal auf dieselben Anforderungen wie der menschliche Gegner.

**Änderungsvorschlag:** Austausch-Tabelle ergänzen:
> | Partner | Eingang in DokChess | Ausgang aus DokChess |
> | Menschlicher oder programmatischer Gegner | Gegenzug; weitere Kommandos: TODO | Ermittelte Züge; weitere Antworten: TODO |
> | Eröffnungsbibliothek | Passender Buchzug, falls vorhanden | Anfrage zu einer Stellung |
> | Endspielbibliothek, nur geplant | Gewinn-/Remis-/Verlustaussage, gegebenenfalls Gewinnzug | Anfrage zu einer Stellung |

#### [S03-02] Technischen Pfad des Computergegners klären

**Schwere:** 🟡 Empfehlung  
**Datei:** [Fachlicher Kontext](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md), [Technischer Kontext](arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md)  
**Kriterium:** Fachliche Partner technischen Kanälen zuordnen.

**Befund:** `s03-partner-computergegner` ist beschrieben. Unklar bleibt, ob ein gegnerisches Programm direkt oder über Frontend/Engine-Manager mit DokChess kommuniziert. Die vorhandene XBoard-Schnittstelle belegt diese konkrete Zuordnung nicht. Siehe auch KKB-01.

**Änderungsvorschlag:**
> Menschliche Gegner werden über ein XBoard-kompatibles Frontend angebunden. Der technische Weg für einen Computergegner ist noch zu bestätigen: TODO direkte XBoard-Kommunikation oder Vermittlung über Frontend/Engine-Manager festlegen und dem Port stdin/stdout aus Abschnitt 5.2 zuordnen.

#### [S03-03] Remisangebote vom aktuellen Umfang abgrenzen

**Schwere:** 🟡 Empfehlung  
**Datei:** [Fachlicher Kontext](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md), [XBoard-Protokoll](arc-doc/05-Bausteinsicht/05-02-XBoard-Protokoll.md)  
**Kriterium:** Konsistenter fachlicher und technischer Schnittstellenumfang.

**Befund:** S3 nennt Austausch über Remisangebote; S5.2 führt diese unter nicht unterstützten Funktionen. Die Formulierung „beispielsweise“ lässt offen, ob S3 eine aktuelle Anforderung oder eine allgemeine Interaktionsmöglichkeit beschreibt.

**Änderungsvorschlag:**
> Zum allgemeinen fachlichen Austausch können Remisangebote gehören. Die aktuelle XBoard-Implementierung unterstützt sie nicht (siehe Abschnitt 5.2). Ihr Status als zukünftige Anforderung ist noch festzulegen.

#### [S03-04] Schnittstellenqualitäten verknüpfen

**Schwere:** 🟢 Hinweis  
**Datei:** [Technischer Kontext](arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md)  
**Kriterium:** Qualitätsanforderungen der Schnittstellen auffindbar machen.

**Befund:** K01 und E01/E02 dokumentieren Einbindung und Antwortzeiten; im technischen Kontext fehlt die entsprechende Verknüpfung. Die Qualitätsanforderungen selbst fehlen nicht.

**Änderungsvorschlag:**
> Für die Qualitätsanforderungen an die Frontend-Anbindung und die Antwortzeiten siehe K01, E01 und E02 in Abschnitt 10.2.

#### [S03-05] Frontend-Risikostatus im Kontext verweisen

**Schwere:** 🟢 Hinweis  
**Datei:** [Technischer Kontext](arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md)  
**Kriterium:** Relevante Integrationsrisiken zuordnen.

**Befund:** Der Kontext verweist beim Endspielwissen auf Risiken, nicht aber auf `s11-risk-frontend`. Der aktuelle Status der Frontend-Integration ist dort nicht ersichtlich.

**Änderungsvorschlag:**
> Das Integrationsrisiko der Frontend-Anbindung ist in Abschnitt 11.1 beschrieben. Aktueller Status und verbleibende Auswirkungen: TODO offen, mitigiert oder erledigt bestätigen.

### Sektion 4: Lösungsstrategie

Die Strategie ist kompakt, beschreibt die Top-Level-Zerlegung und ordnet allen fünf Qualitätszielen Ansätze zu. XBoard und Unveränderlichkeit sind mit ADRs begründet. Organisatorische Entscheidungen oder zusätzliche ADRs wurden nicht allein aufgrund fehlender Graphkanten eingefordert.

#### [S04-01] Qualitätsziel Spielstärke einheitlich benennen

**Schwere:** 🟡 Empfehlung  
**Datei:** [Strategie-Einstieg](arc-doc/04-Loesungsstrategie/04-01-Einstieg.md), [Qualitätsziele](arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md)  
**Kriterium:** Konsistente Bezeichnung der Qualitätsziele.

**Befund:** S4 nennt „Attraktive Spielstärke (Attraktivität)“, S1 „Akzeptable Spielstärke (Funktionale Eignung)“. Die Zuordnung ist inhaltlich nachvollziehbar, die Namen und Qualitätsmerkmale weichen aber ab.

**Änderungsvorschlag:** In S4 die Zeilenbezeichnung ersetzen:
> Akzeptable Spielstärke (Funktionale Eignung)

#### [S04-02] Lesbarkeit und Effizienz abgrenzen

**Schwere:** 🟡 Empfehlung  
**Datei:** [Strategie-Einstieg](arc-doc/04-Loesungsstrategie/04-01-Einstieg.md), [Aufbau](arc-doc/04-Loesungsstrategie/04-02-Aufbau.md)  
**Kriterium:** Trade-offs und Geltungsbereiche der Ansätze erläutern.

**Befund:** `s04-approach-domain-efficient` nennt ein effizientes Domänenmodell; `s04-approach-domain-readability` priorisiert Lesbarkeit gegenüber Effizienz. Das ist kein zwingender Widerspruch, solange Optimierungsumfang und akzeptierte Grenzen abgegrenzt werden.

**Änderungsvorschlag:**
> Bei fachlich motivierten Datenstrukturen wird Lesbarkeit gegenüber Effizienz priorisiert. Welche Teile dennoch gezielt optimiert werden und welche Effizienzgrenzen dabei verbindlich bleiben, ist noch festzulegen: TODO Optimierungsumfang und Szenariobezug.

#### [S04-03] Polyglot-Auswahl begründen

**Schwere:** 🟡 Empfehlung  
**Datei:** [Spielstrategie](arc-doc/04-Loesungsstrategie/04-03-Spielstrategie.md)  
**Kriterium:** Fundamentale Technologieentscheidungen nachvollziehbar machen.

**Befund:** Polyglot und der Nutzen von Buchwissen sind genannt. Auswahlkriterien gegenüber anderen etablierten Eröffnungsformaten fehlen; das allgemeine Standards-Constraint ersetzt die konkrete Auswahlbegründung nicht.

**Änderungsvorschlag:**
> Polyglot ist das implementierte Eröffnungsformat. Die Auswahl wurde anhand von TODO Kriterien getroffen; betrachtete Alternativen und Ausschlag für Polyglot: TODO. Die Wahl erfüllt die Konvention, etablierte Schachdatenformate zu verwenden.

### Sektion 5: Bausteinsicht

Vier Ebene-1-Subsysteme und die Engine-Verfeinerung einschließlich Schnittstellen sind beschrieben. Die Domänentypen sind verknüpft. Geplante Endspieldatenbanken wurden nicht als fehlender Baustein gewertet.

#### [S05-01] Zerlegung begründen

**Schwere:** 🟡 Empfehlung  
**Datei:** [Ebene 1](arc-doc/05-Bausteinsicht/05-01-Ebene-1.md)  
**Kriterium:** Motivation der statischen Zerlegung.

**Befund:** Die vier Subsysteme und ihre Aufgaben sind beschrieben; die Begründung, warum diese Verantwortlichkeiten getrennt werden, bleibt implizit.

**Änderungsvorschlag:**
> Die Zerlegung orientiert sich an getrennten Verantwortlichkeiten: XBoard kapselt die Client-Kommunikation, Spielregeln ermittelt zulässige Züge und Spielsituationen, die Engine bestimmt den nächsten Zug, und Eröffnung stellt optional Bibliothekszüge bereit. Dadurch sind Protokollkommunikation, Regelwerk, Zugermittlung und Eröffnungswissen getrennt austauschbar.

#### [S05-02] Zweck des Regelbausteins enger formulieren

**Schwere:** 🟡 Empfehlung  
**Datei:** [Spielregeln](arc-doc/05-Bausteinsicht/05-03-Spielregeln.md)  
**Kriterium:** Zutreffende Blackbox-Verantwortlichkeit.

**Befund:** „Spielregeln … gemäß FIDE“ steht einer ausdrücklich beschriebenen Beschränkung auf Schach, Matt und Patt gegenüber. Die offene-Punkte-Liste ist vorhanden, die einleitende Zweckbeschreibung sollte sie nicht überdecken. Verwandt mit S01-01.

**Änderungsvorschlag:**
> Das Subsystem ermittelt zu einer Stellung alle nach den unterstützten Regeln gültigen Züge und erkennt Schach, Matt oder Patt. Weitere Remisgründe, insbesondere 50-Züge-Regel und Stellungswiederholung, werden derzeit nicht erkannt.

### Sektion 6: Laufzeitsicht

Der normale Zugablauf ist durch Walkthrough und Sequenzdiagramm nachvollziehbar. Beteiligte Bausteine, Methoden und Granularität passen zu S5; eine künstliche Mindestzahl von Szenarien wurde nicht unterstellt.

#### [S06-01] Abbruch laufender Zugermittlung ergänzen

**Schwere:** 🟡 Empfehlung  
**Datei:** [Zugermittlung](arc-doc/06-Laufzeitsicht/06-01-Zugermittlung.md), [Engine](arc-doc/05-Bausteinsicht/05-04-Engine.md)  
**Kriterium:** Architekturrelevante Ausnahmeabläufe erklären.

**Befund:** `s06-scenario-zugermittlung` erklärt Asynchronität mit weiterer Eingabeverarbeitung. S5 sieht Abbruch durch `ziehen` und `figurenAufbauen` vor; S6 zeigt weder diesen Ablauf noch die Behandlung bereits erzeugter oder verspäteter Observer-Ereignisse.

**Änderungsvorschlag:** Neues Laufzeitszenario aufnehmen:
> **Abbruch einer laufenden Zugermittlung:** Während die Engine asynchron Zugkandidaten meldet, wird `ziehen` oder `figurenAufbauen` aufgerufen. Diese Aufrufe brechen laut Engine-Schnittstelle die laufende Ermittlung ab. TODO Behandlung bereits gesendeter oder verspäteter Observer-Ereignisse und zulässige XBoard-Ausgaben nach dem Abbruch dokumentieren.

### Sektion 7: Verteilungssicht

Das Windows-Einzel-PC-Beispiel beschreibt Arena, JRE, JAR und Batch-Datei sowie deren Zusammenarbeit. Sämtliche Module befinden sich im JAR. Weitere Plattformen oder eine Eröffnungsbibliothek sind im Beispiel nicht verpflichtend.

#### [S07-01] Konkrete Deployment-Variante begründen

**Schwere:** 🟡 Empfehlung  
**Datei:** [Windows-Infrastruktur](arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md)  
**Kriterium:** Motivation der Infrastruktur- und Verpackungsentscheidungen.

**Befund:** Arena/XBoard sind über ADR 09-01 begründet. Der Einsatz von Über-JAR und Batch-Start ist beschrieben, dessen Motivation aber nicht.

**Änderungsvorschlag:**
> Arena wird aufgrund seiner XBoard- und Debugging-Unterstützung verwendet (Entscheidung 9.1). `dokchess.bat` startet `DokChess.jar` über die Java-Laufzeit. Gründe für Über-JAR-Verpackung und Batch-Start sowie berücksichtigte Alternativen: TODO ergänzen.

#### [S07-02] Zielumgebung und Leistungsbezug präzisieren

**Schwere:** 🟡 Empfehlung  
**Datei:** [Windows-Infrastruktur](arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md)  
**Kriterium:** Relevante Infrastrukturmerkmale nachvollziehbar machen.

**Befund:** Windows-PC und Java SE 11 oder höher sind angegeben. Unterstützte Windows-Version/Architektur und ein Hardwareprofil für die Leistungszusagen fehlen; eine Einzel-PC-Lösung benötigt jedoch keine zusätzliche Cloud-/Cluster-Dokumentation.

**Änderungsvorschlag:**
> Unterstützte Windows-Versionen und Systemarchitektur: TODO. Referenzprozessor und Arbeitsspeicher: TODO oder ausdrücklich nicht festgelegt. Die Antwortzeitvorgaben E01/E02 werden auf TODO Referenzumgebung geprüft.

### Sektion 8: Querschnittliche Konzepte

Sieben relevante Konzepte sind gegliedert; Domänenmodell, UI und Entscheidungen sind überwiegend verknüpft. Kritische Widersprüche der Validierung zu F01 und Z02 werden unter KRQ-01 und KRQ-04 behandelt, nicht als Implementierungsfehler behauptet.

#### [S08-01] Konzept-Bausteinverweise vervollständigen

**Schwere:** 🟡 Empfehlung  
**Datei:** [Validierung](arc-doc/08-Konzepte/08-04-Validierung.md), [Fehlerbehandlung](arc-doc/08-Konzepte/08-05-Fehlerbehandlung.md), [Testbarkeit](arc-doc/08-Konzepte/08-07-Testbarkeit.md)  
**Kriterium:** Konzepte und betroffene Bausteine verknüpfen.

**Befund:** Bausteine werden inhaltlich genannt, aber nicht durchgängig auf ihre Blackbox-Beschreibungen verlinkt. Bestehende Domänenmodell- und UI-Verknüpfungen sind dagegen nachvollziehbar.

**Änderungsvorschlag:** Den jeweiligen Konzepttexten hinzufügen und beim Einfügen mit den entsprechenden S5-Seiten verlinken:
> 8.4: Die Zuständigkeiten der beteiligten Bausteine sind in 5.2 XBoard-Protokoll, 5.3 Spielregeln und 5.5 Eröffnung beschrieben. 8.5: Die Fehlerbehandlung betrifft insbesondere XBoard-Protokoll (5.2) und Engine (5.4). 8.7: Spielregeln (5.3) und Engine (5.4) sind zentrale Gegenstände der beschriebenen Funktionalitäts- und Integrationstests.

#### [S08-02] Fortsetzungsverhalten nach Fehlern abgrenzen

**Schwere:** 🟡 Empfehlung  
**Datei:** [Validierung](arc-doc/08-Konzepte/08-04-Validierung.md), [Fehlerbehandlung](arc-doc/08-Konzepte/08-05-Fehlerbehandlung.md)  
**Kriterium:** Einheitliches, nachvollziehbares Fehlerbehandlungskonzept.

**Befund:** S8.4 nennt mögliche Engine-Fehler bei unzulässigen Stellungen. S8.5 erklärt, XBoard fange „sämtliche Exceptions“, danach arbeite DokChess „normal“ weiter. Ob dies für jeden Fehler einen konsistenten Spielzustand voraussetzt, ist offen; die Protokollmeldung ersetzt keine Zustandsbeschreibung.

**Änderungsvorschlag:** Als zu bestätigende Soll-Regel ergänzen:
> Nach `tellusererror` ist die Fortsetzung nur für Fehlerarten vorgesehen, bei denen der Spiel- und Enginezustand konsistent bleibt. TODO Fehlerklassen, Zustandsprüfung sowie Fälle mit notwendiger Neuinitialisierung oder Abbruch festlegen.

### Sektion 9: Architekturentscheidungen

Beide ADRs enthalten Titel, Status, Kontext, Entscheidung, Konsequenzen und Datum; Status ist jeweils `accepted`. Alternativen und Gründe sind vorhanden. Ein fehlender Status wurde daher nicht bemängelt. Die Strategie fasst die Entscheidungen sinnvoll zusammen.

#### [S09-01] Historische Frontend-Matrix einordnen

**Schwere:** 🟡 Empfehlung  
**Datei:** [Frontend-Anbindung](arc-doc/09-Entscheidungen/09-01-Anbindung.md)  
**Kriterium:** Aktualität der Entscheidungsgrundlage transparent machen.

**Befund:** `s09-adr-01-anbindung` dokumentiert untersuchte Frontends mit „Stand 2011“, während der ADR-Status mit 2026-03-10 datiert ist. Die historische Untersuchung ist nicht automatisch falsch, belegt aber keine heutige Kompatibilität.

**Änderungsvorschlag:**
> Die Kompatibilitätsmatrix dokumentiert den untersuchten Stand 2011, nicht die heutige Unterstützung. Aktuell relevante Frontends und Versionen sowie Ergebnis und Datum einer erneuten Prüfung: TODO. Bis dahin bleibt die aktuelle Kompatibilitätsaussage auf den dokumentierten Untersuchungsstand beschränkt.

#### [S09-02] Performance-Abwägung reproduzierbar machen

**Schwere:** 🟡 Empfehlung  
**Datei:** [Stellungsobjekte](arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md)  
**Kriterium:** Nachvollziehbare Messgrundlage einer Entscheidung.

**Befund:** `s09-adr-02-stellungsobjekte` nennt etwa 30 Prozent längere Laufzeit und weiterhin eingehaltene Grenzen, aber keine Hardware, Messaufgabe, Laufzeitumgebung oder absoluten Werte. Der Bezug zu E01/E02 ist nicht belegt.

**Änderungsvorschlag:**
> Der Prototypvergleich erfolgte auf TODO Hardware und Laufzeitumgebung mit TODO Messaufgabe. Laufzeiten der beiden Varianten: TODO absolute Werte. Maßgebliche Grenze: TODO Referenz auf Qualitätsszenario oder anderen Grenzwert. Die Messung zeigt unter diesen Bedingungen TODO Ergebnis.

### Sektion 10: Qualitätsanforderungen

Qualitätsbaum und 15 Szenarien sind vorhanden. Der Baum umfasst auch zusätzliche Merkmale jenseits der fünf priorisierten Ziele; das ist zulässig. W05 ist mehrfach zugeordnet, einschließlich Analysierbarkeit. Konkrete Grenzen sind unter anderem W01: 15 Minuten, W05: eine Woche, K01: zehn Minuten, E01: fünf Sekunden, E02: zehn Sekunden für den Zug und fünf Sekunden für eine Rückmeldung.

#### [S10-01] W02 und W03 mit überprüfbaren Grenzen versehen

**Schwere:** 🟡 Empfehlung  
**Datei:** [Qualitätsszenarien](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md)  
**Kriterium:** Messbarkeit von Nutzungsszenarien.

**Befund:** `s10-qs-w02` fordert „unverzüglich“, `s10-qs-w03` „ohne Umwege oder fremde Hilfe“. Eine einheitliche Akzeptanzentscheidung ist ohne Definition dieser Begriffe nicht möglich.

**Änderungsvorschlag:**
> W02: Das Beispiel zu einem arc42-Kapitel wird innerhalb von TODO Minuten gefunden. W03: Die Modulimplementierung wird innerhalb von TODO Minuten ohne TODO konkret definierte externe Hilfestellung gefunden. Testpersonen und Ausgangsinformationen: TODO.

#### [S10-02] Änderungsaufwand für W04 und P01 bestimmen

**Schwere:** 🟡 Empfehlung  
**Datei:** [Qualitätsszenarien](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md)  
**Kriterium:** Änderbarkeit mit Aufwand/Dauer konkretisieren.

**Befund:** W04 und P01 besitzen überprüfbare strukturelle Kriterien, jedoch keine Aufwandsgrenze. Das macht sie nicht wertlos, lässt aber den geforderten Grad der einfachen Erweiterbarkeit offen; W05 ist bereits zeitlich begrenzt.

**Änderungsvorschlag:**
> W04: Implementierung und Integration der neuen Stellungsbewertung benötigen höchstens TODO Personentage bei TODO Vorwissen. P01: Implementierung und Einbindung des zusätzlichen Protokolls benötigen höchstens TODO Personentage bei TODO Vorwissen. Die bestehenden Kriterien ohne Änderung vorhandenen Codes bleiben erhalten.

#### [S10-03] Taktische Szenarien reproduzierbar spezifizieren

**Schwere:** 🟡 Empfehlung  
**Datei:** [Qualitätsszenarien](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md)  
**Kriterium:** Reproduzierbare Akzeptanzkriterien.

**Befund:** F02–F04 beschreiben taktische Ergebnisse, nicht konkrete Stellungen, Engine-Konfigurationen oder Ausführungsbedingungen. „Schwacher Spieler“ und „frei von Sinn“ sind zusätzlich interpretationsabhängig.

**Änderungsvorschlag:**
> Für F02–F04 gelten die festgelegten Ausgangsstellungen TODO FEN-Testset und die Konfiguration TODO Suchtiefe/Zeitbudget/Eröffnungsbuch. Erfolg: TODO erwartete Züge oder Folgezüge werden in TODO Anteil der Testfälle unter den angegebenen Bedingungen erreicht.

#### [S10-04] Z02 mit konkreten Fehler- und Abbruchkriterien versehen

**Schwere:** 🟡 Empfehlung  
**Datei:** [Qualitätsszenarien](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md)  
**Kriterium:** Fehlerreaktion als Akzeptanzkriterium beschreiben.

**Befund:** Z02 fordert Erkennung einer unzulässigen Anfangsstellung und Spielende, definiert jedoch weder die Ungültigkeitsklassen noch die beobachtbare Abbruchreaktion. Der grundlegende Widerspruch zu S8.4 steht separat unter KRQ-01.

**Änderungsvorschlag:** Nach Entscheidung über den Soll-Umfang:
> Z02: Eingabe einer Anfangsstellung aus TODO festgelegten Ungültigkeitsklassen/Testfällen. Erwartete Reaktion: TODO definierte Fehlermeldung und beobachtbarer Spielabbruch. Nach dem Abbruch darf für diese Stellung kein weiterer Zug ausgegeben werden; erneuter Spielbeginn: TODO festlegen.

### Sektion 11: Risiken und technische Schulden

Drei Risiken sind beschrieben. Alle besitzen Maßnahmen in ihren Texten; das Fehlen eigener Mitigation-Knoten ist kein fehlender Maßnahmenplan. Bewertungen sind nicht angegeben und wurden nicht erfunden. Historische Projekttermine sind als solche erkennbar, ihr Erledigungsstand fehlt jedoch.

#### [S11-01] Bewertung und Steuerbarkeit vervollständigen

**Schwere:** 🟡 Empfehlung  
**Datei:** [Frontend-Risiko](arc-doc/11-Risiken/11-01-Frontend.md), [Aufwandsrisiko](arc-doc/11-Risiken/11-02-Aufwand.md), [Spielstärkerisiko](arc-doc/11-Risiken/11-03-Spielstaerke.md)  
**Kriterium:** Priorisierte, aktuelle und steuerbare Risiken.

**Befund:** Alle Risk-Knoten haben Priorität „nicht angegeben“. Wahrscheinlichkeit, Auswirkung, Status und Zuständigkeit fehlen; die Eventualfälle zu Vorträgen im März/Mai 2011 sind nicht abgeschlossen eingeordnet. Für das kleine Projekt genügt eine knappe Bewertung statt eines umfangreichen Verwaltungsprozesses.

**Änderungsvorschlag:** Je Risiko ergänzen:
> Wahrscheinlichkeit: TODO; Auswirkung: TODO; Priorität: TODO; Status: TODO; Verantwortlich: TODO; nächster Prüftermin: TODO. Erforderliche Ressourcen oder bewusst kein eigenes Budget: TODO. Historische Eventualfälle von 2011: TODO Ergebnis und heutige Relevanz.

#### [S11-02] Frontend-Proof-of-Concept operationalisieren

**Schwere:** 🟡 Empfehlung  
**Datei:** [Frontend-Risiko](arc-doc/11-Risiken/11-01-Frontend.md)  
**Kriterium:** Überprüfbare Gegenmaßnahmen und Eventualfallauslöser.

**Befund:** „Frühestmöglich Sicherheit durch Proof of concept“ benennt eine Maßnahme, aber weder Umfang noch Erfolgskriterium, Ergebnis oder Entscheidungspunkt für alternative UI-Lösungen.

**Änderungsvorschlag:**
> Proof of Concept: TODO Frontend, Version und Protokoll. Erfolgskriterium: TODO nachgewiesener Ablauf und Qualitätsgrenze. Prüftermin/Ergebnis: TODO; verantwortlich: TODO. Bei Nichterreichen bis TODO wird zwischen textuellem UI und eigenem grafischem Frontend entschieden.

#### [S11-03] Aussage zur Korrektheit bei ausgelassenen Regeln begrenzen

**Schwere:** 🟡 Empfehlung  
**Datei:** [Aufwandsrisiko](arc-doc/11-Risiken/11-02-Aufwand.md)  
**Kriterium:** Folgen einer Risikominderung zutreffend darstellen.

**Befund:** Nach Verzicht auf 50-Züge-Regel und Stellungswiederholung behauptet S11.2 „keine [Konsequenzen] bezüglich der Korrektheit des Spiels der Engine“. Legalität einzelner Züge und Vollständigkeit der Partie-/Remisentscheidung werden nicht unterschieden. Ein fehlender Remisfall beweist keinen illegalen Einzelzug.

**Änderungsvorschlag:**
> Die 50-Züge-Regel und die Stellungswiederholung werden zunächst nicht implementiert. Dadurch werden diese Remisfälle nicht erkannt. Das bedeutet nicht zwangsläufig, dass einzelne erzeugte Züge illegal sind; die vollständige Abwicklung der FIDE-Regeln ist jedoch nicht gewährleistet. Akzeptierter Umfang und Status einer späteren Umsetzung: TODO.

#### [S11-04] Spielstärke-Maßnahmen mit Abnahme verbinden

**Schwere:** 🟡 Empfehlung  
**Datei:** [Spielstärkerisiko](arc-doc/11-Risiken/11-03-Spielstaerke.md)  
**Kriterium:** Wirksamkeit einer Gegenmaßnahme überprüfen.

**Befund:** Der Text erklärt ausdrücklich, die Grenze unangemessen schwacher Spielstärke sei unklar. Tests und Szenarien sind vorgesehen, aber Abnahmeschwelle und Entscheidung über das verbleibende Risiko fehlen.

**Änderungsvorschlag:**
> Zur Bewertung werden F02–F04 sowie E01/E02 verwendet. Teststellungen/Referenzgegner, Messverfahren und Akzeptanzschwellen: TODO. Prüfungsergebnis und Entscheidung über das Restrisiko: TODO; verantwortlich und nächster Prüftermin: TODO.

#### [S11-05] Betrachtete Risikoquellen transparent machen

**Schwere:** 🟡 Empfehlung  
**Datei:** [Frontend-Risiko](arc-doc/11-Risiken/11-01-Frontend.md), [Aufwandsrisiko](arc-doc/11-Risiken/11-02-Aufwand.md), [Spielstärkerisiko](arc-doc/11-Risiken/11-03-Spielstaerke.md)  
**Kriterium:** Abdeckung der Risikoerhebung nachvollziehbar machen.

**Befund:** Schnittstellen-, Aufwands- und Spielstärkerisiken sind vorhanden. Ob Stakeholder-, Daten- oder weitere Entwurfsrisiken geprüft wurden, ist nicht dokumentiert. Dies belegt keine tatsächlich vorhandenen weiteren Risiken.

**Änderungsvorschlag:** Kurzen Prüfvermerk hinzufügen:
> Betrachtete Risikoquellen: Stakeholder, externe Schnittstellen, Entwicklungsprozess, Daten/Datenstrukturen und Entwurf/Implementierung. Je Perspektive: TODO identifiziertes Risiko oder nach Prüfung kein weiteres Risiko identifiziert. Prüfdatum und Beteiligte: TODO.

### Sektion 12: Glossar

Das Glossar enthält 24 alphabetisch angeordnete Begriffe und Definitionen. Eine Übersetzungstabelle ist für die deutsche Dokumentation nicht erforderlich. Definitionen von Remisregeln behaupten nicht deren Implementierung.

#### [S12-01] 50-Züge-Regel präzisieren

**Schwere:** 🟡 Empfehlung  
**Datei:** [Glossarbegriffe](arc-doc/12-Glossar/12-02-Begriffe.md)  
**Kriterium:** Eindeutige Begriffsdefinition.

**Befund:** `s12-term-50-zuege` lässt mit „50 Züge lang“ die Unterscheidung zu insgesamt 50 Halbzügen offen.

**Änderungsvorschlag:** Definition ersetzen:
> Ein Spieler kann Remis reklamieren, wenn in den letzten 50 Zügen beider Spieler, also 100 Halbzügen, weder ein Bauer gezogen noch eine Figur geschlagen wurde.

#### [S12-02] Zeitliche Grenze des En-passant-Schlags ergänzen

**Schwere:** 🟡 Empfehlung  
**Datei:** [Glossarbegriffe](arc-doc/12-Glossar/12-02-Begriffe.md)  
**Kriterium:** Vollständige Definition einer Sonderregel.

**Befund:** `s12-term-en-passant` beschreibt den Schlag, nicht dessen Beschränkung auf den unmittelbar nächsten Zug.

**Änderungsvorschlag:**
> Ein Bauer darf einen gegnerischen Bauern unmittelbar im nächsten Zug en passant schlagen, wenn dieser von seiner Ausgangsstellung zwei Felder vorgezogen ist und dabei ein Feld übersprungen hat, auf dem der schlagende Bauer ihn hätte schlagen können. Der schlagende Bauer zieht auf das übersprungene Feld; der geschlagene Bauer wird entfernt.

#### [S12-03] Endspiel über Figurenzahl statt Figurenarten beschreiben

**Schwere:** 🟡 Empfehlung  
**Datei:** [Glossarbegriffe](arc-doc/12-Glossar/12-02-Begriffe.md)  
**Kriterium:** Verständliche, zutreffende Definition.

**Befund:** „Wenige Figurenarten“ bedeutet wenige verschiedene Typen, nicht wenige Figuren; dadurch wird `s12-term-endspiel` missverständlich.

**Änderungsvorschlag:**
> Späte Phase einer Schachpartie, in der im Vergleich zum Mittelspiel meist weniger Figuren auf dem Brett stehen. Eine feste Grenze für den Beginn des Endspiels gibt es nicht.

#### [S12-04] Zentralen Begriff Stellung ergänzen

**Schwere:** 🟡 Empfehlung  
**Datei:** [Glossarbegriffe](arc-doc/12-Glossar/12-02-Begriffe.md), [Domänenmodell](arc-doc/08-Konzepte/08-02-Domaenenmodell.md)  
**Kriterium:** Zentrale Domänenbegriffe gemeinsam definieren.

**Befund:** `s08-dm-stellung` ist zentral für alle Module, wird aber nicht im Glossar erklärt.

**Änderungsvorschlag:** Alphabetisch ergänzen:
> | Stellung | Gesamtsituation einer Schachpartie zu einem Zeitpunkt: Anordnung der Figuren auf dem Brett, Spieler am Zug sowie bestehende Rochaderechte und die Möglichkeit eines en-passant-Schlags. |

#### [S12-05] Stellungsbewertung ergänzen

**Schwere:** 🟡 Empfehlung  
**Datei:** [Glossarbegriffe](arc-doc/12-Glossar/12-02-Begriffe.md), [Stellungsbewertung](arc-doc/05-Bausteinsicht/05-08-Stellungsbewertung.md)  
**Kriterium:** Zusammenhängende Computerschachbegriffe erläutern.

**Befund:** Minimax und Alpha-Beta sind definiert, die für beide zentrale Stellungsbewertung fehlt.

**Änderungsvorschlag:** Alphabetisch ergänzen:
> | Stellungsbewertung | Numerische Einschätzung einer Schachstellung aus Sicht eines Spielers: 0 steht für eine ausgeglichene Situation, positive Werte für einen Vorteil und negative für einen Nachteil. Der Betrag beschreibt die Stärke des Vor- oder Nachteils. |

## Sektionsübergreifende Konflikte

| Konfliktdimension | Status | Befunde |
|---|---|---|
| Qualitätsstrang (S1 ↔ S4 ↔ S10) | 🟡 | Spielstärkeziel nicht vollständig abnehmbar; zusätzliche Qualitätsmerkmale nur als Traceability-Hinweis. |
| Strategie ↔ Entscheidungen (S4 ↔ S9) | 🟢 | Bestehende ADRs aligned; zusätzliche reaktive ADR nur optionaler Hinweis. |
| Constraint-Compliance (S2 ↔ S4/S8/S9) | 🟢 | Kein belegter Constraint-Verstoß; Austauschformat-Begriff kann geschärft werden. |
| Kontext ↔ Bausteine (S3 ↔ S5) | 🟡 | Computergegner-Zuordnung und Remisangebote klärungsbedürftig. |
| Sichten-Konsistenz (S5 ↔ S6 ↔ S7) | 🟢 | Kein belastbarer Widerspruch zwischen Bausteinen, Laufzeit und Deployment. |
| Konzepte ↔ Entscheidungen (S8 ↔ S9) | 🟢 | Konzepte setzen ADRs um; framework-neutrale DI optional separat dokumentierbar. |
| Risiken ↔ Qualität (S11 ↔ S1/S10) | 🔴 | Z02 und F01 widersprechen Validierungsgrenzen; FIDE-Umfang kollidiert mit Aufwandsreduktion. |

### 1. Qualitätsstrang (S1 ↔ S4 ↔ S10)

Community: `c-qs`. Alle fünf Ziele haben passende Strategien und Szenarien.

| Qualitätsziel, Priorität | Strategische Ansätze | Konkretisierende Szenarien | Ergebnis |
|---|---|---|---|
| Zugängliches Beispiel, 1 | arc42, Domänenmodell, deutsche Namen, Javadoc | W01, W02, W03, W05 | Abgedeckt; W05-Zuordnung auch im Qualitätsbaum belegt. |
| Experimentierplattform, 2 | Java, Kernschnittstellen, Unveränderlichkeit, DI, Tests | W04, W05, P01 | Abgedeckt. |
| Interoperabilität, 3 | XBoard, portables Java | K01 | Abgedeckt. |
| Spielstärke, 4 | Eröffnung, Minimax/Bewertung, taktische Tests | F02, F03, F04 | Zugeordnet, aber breites Ziel nicht reproduzierbar abnehmbar. |
| Effizienz, 5 | Reactive Extensions, Alpha-Beta, Domänenmodell, Zeitprüfungen | E01, E02 | Konkrete Antwortzeitgrenzen vorhanden. |

#### [KQS-01] Zusätzliche Qualitätsmerkmale explizit einordnen

**Konflikttyp:** K4, Traceability-Hinweis, kein belegter Zielwiderspruch  
**Schwere:** 🟢 Hinweis  
**Betroffene Dateien:** [Qualitätsziele](arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md), [Aufbau](arc-doc/04-Loesungsstrategie/04-02-Aufbau.md), [Qualitätsbaum](arc-doc/10-Qualitaetsanforderungen/10-01-Qualitaetsbaum.md), [Qualitätsszenarien](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md).

**Beschreibung:** F01 und Z01/Z02 betreffen weitere Merkmale des Qualitätsbaums. Dass sie nicht zu den fünf priorisierten Zielen gehören, ist zulässig und kein Vollständigkeitsmangel von S1. Der Spezialagent empfahl zusätzliche Ziel-/Strategiezuordnung; die Konsolidierung begrenzt dies auf eine optionale Erläuterung. Der konkrete Z02-Widerspruch steht unter KRQ-01.

**Lösungsvorschlag:**
> Abschnitt 1.2 nennt die fünf architekturprägenden Qualitätsziele, nicht sämtliche Qualitätsanforderungen. Der Qualitätsbaum enthält zusätzlich Korrektheit und Fehlertoleranz mit F01 sowie Z01/Z02. Deren Umsetzung und Abgrenzung sind mit dem Validierungskonzept in 8.4 abzustimmen.

#### [KQS-02] Taktische Einzelfälle belegen nicht das breite Spielstärkeziel

**Konflikttyp:** K5  
**Schwere:** 🟡 Warnung  
**Betroffene Dateien:** [Qualitätsziele](arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md), [Strategie-Einstieg](arc-doc/04-Loesungsstrategie/04-01-Einstieg.md), [Spielstrategie](arc-doc/04-Loesungsstrategie/04-03-Spielstrategie.md), [Qualitätsszenarien](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md).

**Beschreibung:** `s01-qg-spielstaerke` verlangt, schwache Gegner sicher zu schlagen und Gelegenheitsspieler zu fordern. F02–F04 prüfen einzelne taktische Fähigkeiten; Referenzgegner, Partiebedingungen und Erfolgsquote fehlen. Die Aussage, die einfache Implementierung erfülle die Szenarien, belegt deshalb nicht das ganze Ziel.

**Lösungsvorschlag:** Zusätzliches Abnahmeszenario vorschlagen:
> Gegen TODO festgelegte Referenzgegner spielt DokChess TODO Anzahl Partien unter TODO Zeitkontrolle und Konfiguration. Erfolg für das Spielstärkeziel: TODO festgelegte Punktquote. F02–F04 bleiben ergänzende taktische Tests, nicht alleiniger Nachweis des Partieziels.

K1: alle priorisierten Ziele abgedeckt. K2: Lesbarkeit/Effizienz-Trade-off ausdrücklich benannt. K3: keine belegte Prioritätsumkehr. Messpräzisierungen stehen zusätzlich in S10.

### 2. Strategie ↔ Entscheidungen (S4 ↔ S9)

Community: `c-sd`; 24 Strategieansätze, zwei akzeptierte ADRs.

| Strategische Festlegung | Entscheidungszuordnung | Ergebnis |
|---|---|---|
| XBoard / stdin/stdout | ADR 09-01, explizite Zuordnung/Referenz | Aligned. |
| Unveränderliche Objekte | ADR 09-02, explizite `realizes`-Kante | Aligned. |
| Modulare Struktur, Lesbarkeit, paralleler Minimax | Thematischer Bezug zu ADRs; keine zusätzliche explizite Zusage | Kein belegter Widerspruch. |
| Weitere Ansätze wie Domänenmodell, Javadoc, DI, Tests, Alpha-Beta, Polyglot und Batch-Start | Nicht jeweils durch eigenständige ADR belegt | Kein automatischer ADR-Zwang. |
| Reaktive Engine-Anbindung | In S4 beschrieben, keine eigenständige ADR | Optionaler Dokumentationshinweis. |

#### [KSE-01] Reaktive Anbindung optional als Entscheidung dokumentieren

**Konflikttyp:** K4, bedingter Dokumentationshinweis  
**Schwere:** 🟢 Hinweis  
**Betroffene Dateien:** [Anbindung](arc-doc/04-Loesungsstrategie/04-04-Anbindung.md), [Stellungsobjekte](arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md).

**Beschreibung:** S4 legt Reactive Extensions zur Responsivität fest, ohne eigene ADR. Eine ADR ist nur sinnvoll, wenn Alternativen und relevante Folgen abgewogen wurden. Der Spezialagent beschreibt ausdrücklich einen Prüffall, keinen sicher belegten Mangel; deshalb kein Warnstatus.

**Lösungsvorschlag:** Falls eine eigenständige Abwägung dokumentiert werden soll:
> Kontext: DokChess muss während der Zugermittlung weitere Kommandos verarbeiten können. Entscheidung: reaktive Engine-Anbindung mit Reactive Extensions. Alternativen und Auswahlgründe: TODO. Folgen für Abbruch, Ereignisreihenfolge, Fehlerbehandlung und Performance: TODO. Status und Datum: TODO.

Keine direkten Strategie-/ADR-Widersprüche, keine problematische Redundanz, kein veralteter Strategieverweis und keine widersprüchliche Entscheidungskette belegt. Die etwa 30 Prozent Laufzeitmehrkosten passen zum benannten Lesbarkeits-Trade-off.

### 3. Constraint-Compliance (S2 ↔ S4/S8/S9)

Community: `c-cc`; alle 15 Constraints geprüft. „Kein Widerspruch“ bedeutet Dokumentationskonsistenz, nicht technisch getestete Erfüllung.

| Constraint | Kategorie | Bewertung gegen S4/S8/S9 |
|---|---|---|
| Moderate Hardware | Technisch | Kein dokumentierter Widerspruch; Referenzprofil offen. |
| Windows | Technisch | Unterstützte Beispielumgebung; keine zwingende Exklusivität. |
| Java | Technisch | Konform; historischen Versionsstand klären. |
| Frei verfügbare Fremdsoftware | Technisch | Präferenz, kein hartes Lizenzverbot; kein belegter Verstoß. |
| Team | Organisatorisch | Kein Widerspruch; historische Angabe. |
| Zeitplan | Organisatorisch | Kein Widerspruch; historische Termine. |
| Vorgehensmodell | Organisatorisch | Kein Widerspruch. |
| Entwicklungswerkzeuge | Organisatorisch | Kein Widerspruch. |
| Versionsverwaltung | Organisatorisch | Kein Widerspruch; Geltungsstand offen. |
| Testwerkzeuge/-prozesse | Organisatorisch | JUnit/Testkonzept passend. |
| Open-Source-Veröffentlichung | Organisatorisch | Kein Widerspruch. |
| Architekturdokumentation | Konvention | arc42-Struktur vorhanden. |
| Java-Kodierrichtlinien | Konvention | Kein dokumentierter Widerspruch; Code nicht geprüft. |
| Sprache | Konvention | Deutsche fachliche Namen passend. |
| Schachdatenformate | Konvention | XBoard/FEN/Polyglot passend; Begriff intern/extern schärfbar. |

#### [KRC-01] Internes Domänenmodell und Austauschformate begrifflich trennen

**Konflikttyp:** K4, mögliche Begriffsunklarheit, kein belegter Constraint-Verstoß  
**Schwere:** 🟢 Hinweis  
**Betroffene Dateien:** [Konventionen](arc-doc/02-Randbedingungen/02-03-Konventionen.md), [Aufbau](arc-doc/04-Loesungsstrategie/04-02-Aufbau.md), [Domänenmodell](arc-doc/08-Konzepte/08-02-Domaenenmodell.md).

**Beschreibung:** S2 verbietet eigene Schachnotationen/Austauschformate. S4/S8 verwenden eigene Java-Domänenklassen für Modulparameter. Ein In-Memory-Objektmodell ist nicht automatisch ein selbst erfundenes serialisiertes Austauschformat. Die Spezialanalyse fand deshalb keine belegte Verletzung; der Geltungsbereich kann eindeutiger formuliert werden.

**Lösungsvorschlag:** Als präzisierte Konvention vorschlagen und bestätigen:
> Das Verbot eigener Formate betrifft externe oder persistente Schachnotationen und Austauschformate. Interne Java-Domänenobjekte wie `Zug` und `Stellung` sind davon zu unterscheiden. Extern werden etablierte Formate wie XBoard, FEN und Polyglot verwendet; weitere Formate und Ausnahmen: TODO bestätigen.

Keine konkrete Technologie-, Lizenz- oder Plattformverletzung belegt. Mögliche Spring-/CDI-Nutzung in S8 ist keine dokumentierte Auswahl einer verpflichtenden Abhängigkeit.

### 4. Kontext ↔ Bausteine (S3 ↔ S5)

Community: `c-cb`.

| Externer Partner | Zuordnung in S5 | Ergebnis |
|---|---|---|
| Menschlicher Gegner | XBoard-Client / XBoard-Protokoll, stdin/stdout | Grundsätzlich konsistent; Remisumfang klären. |
| Computergegner | Passender generischer Port vorhanden | Konkrete technische Vermittlung offen. |
| Eröffnungsbibliothek | Interner Adapter Eröffnung / Dateiport | Konsistent. |
| Endspielbibliothek | Kein implementierter Adapter | Bewusst nicht implementiert, kein Konflikt. |
| XBoard-Client | XBoard-Protokoll | Konsistent. |
| Polyglot-Buch | Eröffnung, lesender Dateizugriff | Konsistent. |

#### [KKB-01] Computergegner nicht eindeutig dem Außenport zugeordnet

**Konflikttyp:** K1  
**Schwere:** 🟡 Warnung  
**Betroffene Dateien:** [Fachlicher Kontext](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md), [Technischer Kontext](arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md), [Ebene 1](arc-doc/05-Bausteinsicht/05-01-Ebene-1.md), [XBoard-Protokoll](arc-doc/05-Bausteinsicht/05-02-XBoard-Protokoll.md).

**Beschreibung:** S3 erlaubt Partien gegen eine andere Engine; S3.2 beschreibt vor allem grafische Frontends. S5 hat stdin/stdout und einen XBoard-Client-Port, ordnet den Computergegner aber nicht ausdrücklich zu. Text und Diagramme wurden geprüft. Es fehlt die eindeutige Zuordnung, nicht nachweislich ein Baustein. Verwandt mit S03-02.

**Lösungsvorschlag:**
> Anbindung eines Computergegners: TODO klären, ob eine fremde Engine direkt als XBoard-Client oder vermittelt durch ein Frontend/einen Engine-Manager kommuniziert. Den bestätigten Weg hier und in 5.2 einschließlich stdin/stdout dokumentieren; falls ein anderer Port nötig ist, diesen in 5.1 ergänzen.

#### [KKB-02] Remisangebote sind fachlich genannt, technisch nicht unterstützt

**Konflikttyp:** K4  
**Schwere:** 🟡 Warnung  
**Betroffene Dateien:** [Fachlicher Kontext](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md), [XBoard-Protokoll](arc-doc/05-Bausteinsicht/05-02-XBoard-Protokoll.md).

**Beschreibung:** `s03-partner-mensch` nennt Remisangebote als Austauschbeispiel; `s05-bb-xboard` führt „Remis-Angebote und Aufgabe der anderen Seite“ als nicht unterstützt. Wegen „beispielsweise“ ist die Verbindlichkeit unklar; deshalb Warnung statt kritischer Funktionswiderspruch.

**Lösungsvorschlag:** Bei Beibehaltung der dokumentierten Implementierung:
> Der aktuelle Informationsaustausch umfasst Züge. Remisangebote und die Aufgabe des Gegners werden derzeit nicht unterstützt (siehe 5.2). Ob diese Funktionen künftig zum geforderten Umfang gehören, bleibt zu entscheiden.

Keine zusätzlichen unbekannten externen Partner, kein belegter Terminologiekonflikt und keine verschobene Systemgrenze. „Eröffnungen“ als externe Bücher und „Eröffnung“ als interner Adapter sind unterschiedliche Rollen, kein Namenswiderspruch.

### 5. Sichten-Konsistenz (S5 ↔ S6 ↔ S7)

Community: `c-vc`. **Keine belastbaren Konflikte nach K1–K6.**

| Baustein | S5 | S6 | S7 | Bewertung |
|---|---|---|---|---|
| XBoard-Protokoll | Ebene 1 | Eingabe, Koordination, Ausgabe | Im JAR | Konsistent. |
| Spielregeln | Ebene 1 | Prüfung und Kandidaten | Im JAR | Konsistent. |
| Engine | Ebene 1 | Zustand und asynchrone Ermittlung | Im JAR | Konsistent. |
| Eröffnung | Ebene 1 | Anfrage, im Beispiel ohne Treffer | Modul im JAR; Beispiel ohne Buchdatei | Konsistent, Bibliothek optional. |
| Engine-Whitebox | Ebene 2 | Unter Engine-Lifeline erläutert | Durch sämtliche Module im JAR umfasst | Konsistent. |
| Zugsuche | Ebene 2 | Suchaktivität beschrieben | Durch sämtliche Module im JAR umfasst | Konsistent. |
| Stellungsbewertung | Ebene 2 | Bewertung beschrieben | Durch sämtliche Module im JAR umfasst | Konsistent. |

Belege: [Ebene 1](arc-doc/05-Bausteinsicht/05-01-Ebene-1.md), [Engine-Ebene 2](arc-doc/05-Bausteinsicht/05-06-Ebene-2-Engine.md), [Zugsuche](arc-doc/05-Bausteinsicht/05-07-Zugsuche.md), [Zugermittlung](arc-doc/06-Laufzeitsicht/06-01-Zugermittlung.md), [Deployment](arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md).

Keine unbekannten Bausteine, verwaisten Deployment-Zuordnungen, widersprüchlichen Schnittstellen, Granularitätsverletzungen oder Verantwortlichkeitswechsel. XBoard führt laut S6 den Zug auf der Engine aus; die Engine führt nicht selbständig ihre eigenen Suchergebnisse aus. Infrastrukturartefakte sind keine zusätzlich zu erfindenden S5-Bausteine.

### 6. Konzepte ↔ Entscheidungen (S8 ↔ S9)

Community: `c-ke`; sieben Konzepte und zwei ADRs.

| Konzept/Entscheidung | Einordnung | Ergebnis |
|---|---|---|
| Abhängigkeiten | DI-Regeln, Setter, framework-neutrale Verdrahtung | Konzept passend; separate ADR optional. |
| Domänenmodell | Gemeinsame unveränderliche Fachobjekte | Umsetzung von ADR 09-02, explizit verwiesen. |
| Benutzungsoberfläche | Textbasiertes XBoard, externe Frontends | Umsetzung von ADR 09-01, explizit verwiesen. |
| Validierung | Prüfung und benannte Prüfgrenzen | Konzept; Qualitätswidersprüche separat KRQ. |
| Fehlerbehandlung | Exceptions, onError, tellusererror | Konzept; Fortsetzungsumfang lokal S08-02 offen. |
| Logging | Client-Tracing statt feinkörnigem Logging | Begründetes Konzept, keine ADR-Pflicht belegt. |
| Testbarkeit | JUnit, FEN, Integration-/Effizienztests | Konzept. |
| ADR 09-01 | Wahl XBoard | Kontext, Alternativen und Folgen vorhanden. |
| ADR 09-02 | Wahl unveränderlicher Stellungen | Kontext, Alternativen und Folgen vorhanden. |

#### [KKE-01] Framework-neutrale DI optional als ADR auslagern

**Konflikttyp:** K2/K4, optionaler Strukturhinweis  
**Schwere:** 🟢 Hinweis  
**Betroffene Dateien:** [Abhängigkeiten](arc-doc/08-Konzepte/08-01-Abhaengigkeiten.md), [Entscheidungen](arc-doc/09-Entscheidungen/).

**Beschreibung:** S8.1 erläutert Setter-basierte DI und den begründeten Verzicht auf ein verpflichtendes Framework. Der Spezialagent empfiehlt eine separate ADR. Ein Konzept darf solche Regeln samt Begründung enthalten; es liegt weder ein Widerspruch noch zwingend eine fehlende Entscheidung vor. Eine Auslagerung ist sinnvoll, wenn Auswahlhistorie und Alternativen erhalten werden sollen.

**Lösungsvorschlag:** Optionaler ADR-Entwurf, nicht als bereits akzeptiert behauptet:
> **Framework-neutrale Abhängigkeitsauflösung.** Status: proposed; Datum: TODO. Kontext: lose Kopplung und alternative Modulimplementierungen. Entscheidung: kein verpflichtendes DI-Framework; Abhängigkeiten über Java-Schnittstellen und Setter, Auflösung durch den Verwender. Begründung: Erweiternde behalten die Wahl der DI-Implementierung. Folgen: Verdrahtung im Glue-Code oder durch den Verwender; Spring/CDI bleiben optional. Betrachtete Alternativen und Bestätigung des Geltungsbereichs: TODO.

Keine Konzept-/ADR-Widersprüche, keine problematische Redundanz und keine fehlende Umsetzung der beiden bestehenden ADRs festgestellt.

### 7. Risiken ↔ Qualität (S11 ↔ S1/S10)

Community: `c-rq`, bei belegtem Prüfbedarf um Nachbarn aus S8 ergänzt. Die drei Risk-Knoten enthalten Maßnahmen; fehlende `mitigates`-Kanten belegen nicht deren Abwesenheit.

| Qualitätsziel/Anforderung | Risiko und Maßnahme | Ergebnis |
|---|---|---|
| Zugängliches Beispiel | Spielstärkerisiko nennt Konflikt mit einfacher Lösung; Szenarien/Tests | Thematische, teilweise inferierte Abdeckung; Ergebnis offen. |
| Experimentierplattform | Allgemeiner Aufwand, keine konkrete W04/W05-Risikobewertung | Erhebungsfrage, kein nachgewiesener blinder Fleck. |
| Interoperabilität | Frontend-Risiko, Proof of Concept | Maßnahme vorhanden, aktuelles Ergebnis offen. |
| Spielstärke | Spielstärkerisiko, taktische Tests | Maßnahme vorhanden, Akzeptanzschwelle offen. |
| Effizienz | Zu lange Wartezeiten, Tests; E01/E02 | Vorgaben und Maßnahme vorhanden, Messergebnis nicht belegt. |
| Vollständige FIDE-Regeln | Aufwandsreduktion durch Verzicht auf Remisregeln | Expliziter Umfangskonflikt. |
| Z02 | S8.4 schließt Zulässigkeitsprüfung aus | Direkter Qualitäts-/Konzeptwiderspruch. |
| F01 | S8.4 erlaubt ungültige Buchzüge als Extremfall | Direkter Qualitäts-/Konzeptwiderspruch. |

#### [KRQ-01] Z02 widerspricht der fehlenden Startstellungsprüfung

**Konflikttyp:** K4  
**Schwere:** 🔴 Kritisch  
**Betroffene Dateien:** [Qualitätsszenarien](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md), [Validierung](arc-doc/08-Konzepte/08-04-Validierung.md), [Spielstärkerisiko](arc-doc/11-Risiken/11-03-Spielstaerke.md).

**Beschreibung:** `s10-qs-z02` verlangt Erkennung einer unzulässigen Anfangsstellung und Spielende. `s08-concept-validation` sagt ausdrücklich: „nicht aber, ob die Position zulässig ist“, mit möglichen späteren Engine-Fehlern. S11 behandelt diese Einschränkung nicht als eigenes Qualitätsrisiko. Beide entscheidenden Originalstellen wurden geprüft. Ein abgefangener Laufzeitfehler ist nicht automatisch eine definierte Zulässigkeitsprüfung mit kontrolliertem Spielende.

**Lösungsvorschlag:** Wenn Z02 verbindlich bleibt, folgende Soll-Regel in S8.4 aufnehmen und ihre Umsetzung nachweisen:
> Beim Aufbau einer Stellung prüft DokChess neben der Protokollkonformität auch TODO definierte Zulässigkeitskriterien. Bei einer unzulässigen Anfangsstellung wird das Spiel kontrolliert beendet und der Fehler über TODO Protokollreaktion gemeldet. Z02 wird durch die festgelegten ungültigen Teststellungen nachgewiesen. Umsetzungsstatus, Verantwortliche und Termin: TODO.

Alternativ den begrenzten aktuellen Umfang ausdrücklich in Z02 und S11 dokumentieren, statt die Erkennung als erfüllt darzustellen.

#### [KRQ-02] Aufwandssenkung steht dem vollständigen FIDE-Umfang entgegen

**Konflikttyp:** K3  
**Schwere:** 🟡 Warnung  
**Betroffene Dateien:** [Aufgabenstellung](arc-doc/01-Einfuehrung-und-Ziele/01-01-Aufgabenstellung.md), [Aufwandsrisiko](arc-doc/11-Risiken/11-02-Aufwand.md).

**Beschreibung:** `s11-risk-aufwand` benennt ausgelassene Remisregeln als bewusste Maßnahme, während S1 vollständige FIDE-Regeln verspricht. Der kritische Umfangswiderspruch ist bereits S01-01; hier wird dessen Risikomaßnahmen-Aspekt ohne erneute kritische Einstufung behandelt. F01 allein ist kein Test der vollständigen Remisabwicklung.

**Lösungsvorschlag:**
> Der aktuelle Umfang schließt 50-Züge-Regel und Stellungswiederholung aus; die entsprechenden Remisfälle werden nicht erkannt. Dies senkt den Implementierungsaufwand, erfüllt aber nicht den ursprünglichen Anspruch vollständiger FIDE-Regeln. Akzeptierte Umfangsentscheidung, Geltungszeitraum und gegebenenfalls Zieltermin für Ergänzungen: TODO. Aufgabenstellung und Blackbox-Beschreibung werden entsprechend angepasst.

#### [KRQ-03] Änderbarkeitsrisiken bei nächster Erhebung prüfen

**Konflikttyp:** K1, begrenzter Verdachtsfall  
**Schwere:** 🟢 Hinweis  
**Betroffene Dateien:** [Qualitätsziele](arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md), [Qualitätsszenarien](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md), [Aufwandsrisiko](arc-doc/11-Risiken/11-02-Aufwand.md).

**Beschreibung:** W04/W05 haben keine eigene erkennbare Risikobetrachtung. Daraus folgt weder ein tatsächlich bestehendes Risiko noch die Pflicht, zu jedem Qualitätsziel ein Risiko zu erfinden. Der Spezialagent formuliert einen Verdachtsfall; die Konsolidierung behandelt ihn deshalb als Erhebungshinweis.

**Lösungsvorschlag:**
> Bei der nächsten Risikoerhebung wird geprüft, ob die Integration neuer Bewertungen ohne Änderungen bestehenden Codes und der Austausch der Brettrepräsentation innerhalb einer Woche gefährdet sind. Prüfergebnis: TODO Risiko mit Bewertung/Maßnahme oder nach Prüfung kein relevantes Risiko identifiziert.

#### [KRQ-04] Ungültige Buchzüge widersprechen F01

**Konflikttyp:** K4  
**Schwere:** 🔴 Kritisch  
**Betroffene Dateien:** [Validierung](arc-doc/08-Konzepte/08-04-Validierung.md), [Qualitätsszenarien](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md), [Risiken](arc-doc/11-Risiken/).

**Beschreibung:** Ergänzung der Konsolidierung aus `s08-concept-validation` und `s10-qs-f01`, an beiden Originalen verifiziert: F01 verspricht bei vorhandenen legalen Zügen einen dieser Züge. S8.4 prüft Buchinhalte nicht und erklärt ausdrücklich: „Im Extremfall antwortet die Engine mit einem ungültigen Zug.“ Die Verantwortung des Anwenders für Bibliotheksqualität ist keine im Szenario definierte Vorbedingung. Die dokumentierte Erkennung ungültiger Gegenzüge über Z01 sichert eigene Buchzüge nicht ab.

**Lösungsvorschlag:** Bei Beibehaltung von F01 folgende neue Soll-Regel vorsehen und testen:
> Ein aus der Eröffnungsbibliothek gelieferter Zug wird vor Verwendung gegen die gültigen Züge der aktuellen Stellung geprüft. Ein unzulässiger Buchzug wird verworfen; die Engine ermittelt stattdessen einen legalen Zug ohne diesen Bucheintrag. Umsetzungsstatus: TODO. F01 wird zusätzlich mit einer syntaktisch lesbaren Bibliothek geprüft, die für eine Stellung einen unzulässigen Zug enthält.

Alternativ F01 ausdrücklich auf vorab validierte Bibliotheken begrenzen und das verbleibende Korrektheitsrisiko in S11 dokumentieren. Das wäre eine bewusste Einschränkung, kein Nachweis der ursprünglichen unbedingten Zusage.

K2: Alle drei bestehenden Risiken haben Maßnahmen; kein Befund wegen angeblich fehlender Minderung. K5: Keine inkonsistente Risikopriorisierung belegbar, weil die Prioritäten nicht angegeben sind. Die Verwendung inferierter Kanten bleibt als thematische Zuordnung gekennzeichnet.

## Konfliktkarte

Gezählt werden alle elf Konflikt-/Hinweisbefunde der Konfliktanalysen, nicht die lokalen Sektionsbefunde. Auch eine reine Hinweisbeteiligung bedeutet keinen nachgewiesenen Widerspruch. Bei KRQ-02 ist S10 nur zur Abgrenzung geprüft und deshalb nicht als Konfliktbeteiligung gezählt.

| Sektion | Involviert in Konflikten/Hinweisen |
|---|---:|
| S10 — Qualitätsanforderungen | 5 |
| S1 — Einführung und Ziele | 4 |
| S4 — Lösungsstrategie | 4 |
| S8 — Konzepte | 4 |
| S11 — Risiken | 4 |
| S3 — Kontextabgrenzung | 2 |
| S5 — Bausteinsicht | 2 |
| S9 — Entscheidungen | 2 |
| S2 — Randbedingungen | 1 |

Die Beteiligungen sind: KQS-01/02 jeweils S1/S4/S10; KSE-01 S4/S9; KRC-01 S2/S4/S8; KKB-01/02 S3/S5; KKE-01 S8/S9; KRQ-01 S8/S10/S11; KRQ-02 S1/S11; KRQ-03 S1/S10/S11; KRQ-04 S8/S10/S11.

## Zusammenfassung

| Kategorie | Anzahl |
|---|---:|
| 🔴 Kritische Befunde | 3 |
| 🟡 Warnungen / Empfehlungen | 39 |
| 🟢 Hinweise | 8 |
| **Gesamt** | **50** |

39 lokale Sektionsbefunde (1 kritisch, 35 Empfehlungen, 3 Hinweise) und elf Konfliktbefunde (2 kritisch, 4 Warnungen, 5 Hinweise). Die Zahlen zählen Befund-IDs, nicht 50 unabhängige Ursachen. Beispielsweise beschreiben S01-01, S05-02, S11-03 und KRQ-02 unterschiedliche Dokumentationsstellen desselben FIDE-Umfangsproblems; S03-02/KKB-01 und S03-03/KKB-02 überschneiden sich ebenfalls.

### Handlungsempfehlungen

1. **FIDE-Umfang vereinheitlichen:** Aufgabenstellung, Regelbaustein und Aufwandsrisiko auf denselben verbindlichen Funktionsumfang bringen; Legalität einzelner Züge von vollständiger Remis-/Partieabwicklung unterscheiden (S01-01, S05-02, S11-03, KRQ-02).
2. **Z02 entscheiden:** Zulässigkeitsprüfung und kontrollierten Abbruch verbindlich als Soll-Verhalten festlegen und nachweisen oder Szenario und akzeptiertes Risiko ausdrücklich einschränken (KRQ-01, S10-04).
3. **F01 gegen fehlerhafte Bibliotheken absichern:** Buchzüge vor Verwendung validieren und den Fallback dokumentieren oder die Szenariovoraussetzungen bewusst einschränken; den Status nicht als bereits implementiert darstellen (KRQ-04).
4. **Abbruch- und Fehlerabläufe ergänzen:** Verspätete Suchereignisse, zulässige Ausgaben und konsistente Fortsetzung nach Fehlern beschreiben (S06-01, S08-02).
5. **Qualitätsabnahme konkretisieren:** Reproduzierbare taktische Tests, Referenzgegner, Messumgebung und Änderungsaufwand festlegen (KQS-02, S09-02, S10-01 bis S10-03).
6. **Zeitstand und Integrationsumfang klären:** Historische Constraints/ADRs/Risiken einordnen, Computergegner und Remisangebote abgrenzen, Risikobewertungen vervollständigen. Weitere ADRs nur bei tatsächlichem Nutzen ergänzen.

### Konsolidierung und Grenzen

- Die Empfehlungen der Spezialagenten wurden geprüft, nicht ungefiltert übernommen. KQS-01 wurde auf einen Hinweis begrenzt, weil S1 nur priorisierte Ziele nennt. KSE-01 und KKE-01 begründen keine allgemeine Pflicht zu zusätzlichen ADRs. KRC-01 belegt keinen Verstoß durch interne Java-Objekte. KRQ-03 belegt kein tatsächlich vorhandenes Änderbarkeitsrisiko. Diese fünf Befunde werden deshalb als Hinweise gezählt.
- KRQ-04 wurde bei der Konsolidierung ergänzt, weil die ausdrückliche Einschränkung im Graphen direkt F01 gegenübersteht und beide Originale den Widerspruch bestätigen.
- Schema- und Hashvalidierung beweisen Aktualität und formale Konsistenz des Graphen, nicht lückenlose semantische Extraktion. Die Spezialprüfungen stellten fest: W05 ist im Qualitätsbaum auch Analysierbarkeit zugeordnet, obwohl die entsprechende Graphkante fehlt; S8.3 verweist ausdrücklich auf ADR 09-01, obwohl eine entsprechende `based_on`-Kante fehlt. Diese Quellenbelege wurden berücksichtigt, nicht als Dokumentationsmängel gezählt.
- Eine `involves`-Kante zur Zugsuche ist als explizit markiert, während S6 die Suchaktivität beschreibt, den Ebene-2-Modulnamen aber nicht ausdrücklich nennt. Die Sichtenmatrix verwendet sie nur als funktionale Zuordnung; daraus wurde kein Konflikt abgeleitet.
- Keine Grenzwerte, Risikostufen, Zuständigkeiten, Budgets, aktuellen Frontend-Versionen oder Messergebnisse wurden erfunden. TODOs in den direkt übernehmbaren Vorschlägen kennzeichnen noch zu entscheidende Angaben; sie sind keine Behauptung abgeschlossener Umsetzung.
- Das Review beurteilt ausschließlich die Dokumentation. Ob die beschriebenen Zusagen im aktuellen Programm erfüllt sind, erfordert getrennte Implementierungs- und Funktionstests; solche Tests waren nicht Teil dieses Auftrags.