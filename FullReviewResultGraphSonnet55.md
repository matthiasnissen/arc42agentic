# arc42 Dokumentations-Review (Graph-Modus, `arc-doc/`)

Es gab keinen Graphen, er wurde neu aufgebaut. Er liegt unter [.arc42-graph_demo_results/FullReviewRunSonnet55/arc-doc.graphml](.arc42-graph_demo_results/FullReviewRunSonnet55/arc-doc.graphml) mit Manifest und Extraktion im selben Ordner. Er hat 158 Knoten und 557 Kanten, die Validierung lief mit 0 Fehlern und 0 Warnungen. Die Diagramme (Ebene 1, Ebene 2 Engine, Walkthrough, Deployment, Qualitätsbaum) wurden ausgewertet, die zugehörigen Kanten sind daher `explicit`.

## Gesamtübersicht

| Sektion | Status | Befunde |
|---|---|---|
| 1. Einführung und Ziele | 🟡 | Stakeholder unvollständig (Spielende, Demo-Verantwortliche), Rollen und Erwartungen unscharf |
| 2. Randbedingungen | 🟡 | Versionsstände (Java, Git/SVN) vermischt, keine Referenzhardware, Lizenz- und Veröffentlichungsumfang offen |
| 3. Kontextabgrenzung | 🟡 | Remisangebote ohne Abgrenzung, keine Datenflüsse im Diagramm, Endspiel-Status unklar |
| 4. Lösungsstrategie | 🟡 | Zielname „Attraktive Spielstärke“ weicht von 1.2 ab, Effizienz vs. Lesbarkeit, Reaktivität mit Suchbeschleunigung vermischt |
| 5. Bausteinsicht | 🟡 | Remisangebote vs. XBoard-Umfang, asynchroner Schnittstellenvertrag mit offenen Randfällen |
| 6. Laufzeitsicht | 🟡 | Nur der Normalfall: kein Abbruch-/Fehlerpfad, Engine-Interna implizit |
| 7. Verteilungssicht | 🟡 | Keine Motivation, keine Umgebungsabgrenzung, kein Ressourcenbedarf |
| 8. Konzepte | 🔴 | Z02 (unzulässige Stellung) wird vom Konzept nicht erfüllt, `onError`-Pfad unpräzise, Antwortzeittests nicht reproduzierbar |
| 9. Entscheidungen | 🟡 | ADR-Datum 2026 bei Erhebungsstand 2011, Messbasis der „30 %“ nicht belegt |
| 10. Qualitätsanforderungen | 🔴 | Spielstärkeziel nicht vollständig prüfbar, E01/E02 überlappen, subjektive Kriterien |
| 11. Risiken | 🔴 | Validierungsrisiko fehlt, keine Bewertung/Priorisierung, zurückgestellte Regeln nicht als technische Schuld geführt |
| 12. Glossar | 🟡 | Definitionslücken (en passant, Endspiel, Minimax, Engine), Bitboard und Stellung fehlen |

## Sektions-Reviews

### Sektion 1: Einführung und Ziele

#### S01-01 Stakeholder fehlen
**Schwere:** 🟡 Empfehlung
**Datei:** [01-03-Stakeholder.md](arc-doc/01-Einfuehrung-und-Ziele/01-03-Stakeholder.md)

**Befund:** Spielende fehlen trotz der Anforderung „Spiel gegen menschliche Gegner“. Verantwortliche für Installation und Live-Demonstration sind nicht erfasst.

**Änderungsvorschlag:**
> | Gelegenheitsspielerinnen und Gelegenheitsspieler | Erwarten regelkonformes Spiel, eine angemessene Herausforderung und kurze Antwortzeiten über ein vorhandenes Schach-Frontend. |
> | Verantwortliche für Live-Demonstrationen | Erwarten nachvollziehbare Installations- und Konfigurationsschritte sowie einen zuverlässigen Ablauf auf einem Standard-Notebook. Diese Rolle kann vom Autor übernommen werden. |

#### S01-02 Rollen und Erwartungen teilweise unbestimmt
**Schwere:** 🟡 Empfehlung
**Datei:** [01-03-Stakeholder.md](arc-doc/01-Einfuehrung-und-Ziele/01-03-Stakeholder.md)

**Befund:** `oose Innovative Informatik` hat nur eine Unternehmensbeschreibung, keine Erwartung an Architektur oder Dokumentation. Zörners Entwicklerrolle bleibt implizit.

**Änderungsvorschlag:**
> | Stefan Zörner – Autor, Entwickler und Vortragender | Benötigt attraktive Beispiele für sein Buch sowie verständliche Architektur- und Implementierungsbeschreibungen für Weiterentwicklung, Workshops und Vorträge. |
> | oose Innovative Informatik – Schulungsunternehmen | Erwartet fachlich nachvollziehbares und zuverlässig demonstrierbares Anschauungsmaterial für Seminare, Workshops und Coaching. |

#### S01-03 Status weiterführender Anforderungsdokumente
**Schwere:** 🟢 Hinweis
**Datei:** [01-01-Aufgabenstellung.md](arc-doc/01-Einfuehrung-und-Ziele/01-01-Aufgabenstellung.md)

**Befund:** Verweise auf separate Anforderungsdokumente fehlen. Falls eine Spezifikation geführt wird, ist sie zu verlinken.

### Sektion 2: Randbedingungen

#### S02-01 Gültigkeit historischer und späterer Vorgaben unklar
**Schwere:** 🟡 Empfehlung
**Datei:** [02-01-Technisch.md](arc-doc/02-Randbedingungen/02-01-Technisch.md), [02-02-Organisatorisch.md](arc-doc/02-Randbedingungen/02-02-Organisatorisch.md)

**Befund:** `s02-c-java`, `s02-c-zeitplan` und `s02-c-versionsverwaltung` vermischen Vorgaben und spätere Entwicklungen (Java SE 6/7/11, SVN/Git) ohne Versionszuordnung.

**Änderungsvorschlag:**
> Die Termine bis Februar 2012 beziehen sich auf DokChess 1.0. Für diese Version wurde Java SE 6 verwendet; spätere Entwicklungsstände verwendeten Java SE 7 beziehungsweise 11 sowie Git bei GitHub statt Subversion bei SourceForge. Die Unterstützung zukünftiger Java-Versionen ist ein Kompatibilitätsziel, keine geprüfte Zusicherung.

#### S02-02 Hardwaregrenze nicht überprüfbar
**Schwere:** 🟡 Empfehlung
**Datei:** [02-01-Technisch.md](arc-doc/02-Randbedingungen/02-01-Technisch.md)

**Befund:** „Marktübliches Standard-Notebook“ ist keine reproduzierbare Prüfgrundlage, besonders weil Effizienztests laut 8.7 hardwareabhängig sind.

**Änderungsvorschlag:**
> Die Effizienzvorgaben werden auf einer dokumentierten Referenzkonfiguration überprüft (CPU, Kerne, Arbeitsspeicher, Betriebssystem, JVM-Version, JVM-Speicherlimit). Die konkrete Konfiguration ist noch festzulegen.

#### S02-03 Veröffentlichungsumfang und Lizenzfolgen offen
**Schwere:** 🟡 Empfehlung
**Datei:** [02-02-Organisatorisch.md](arc-doc/02-Randbedingungen/02-02-Organisatorisch.md)

**Befund:** „oder zumindest Teile“ lässt den Veröffentlichungsumfang offen. Folgen für mitverteilte Fremdsoftware unter GPLv3 fehlen.

**Änderungsvorschlag:**
> Der verbindliche Umfang der Open-Source-Veröffentlichung ist komponentenweise festzulegen. Vor der Aufnahme mitverteilter Fremdsoftware ist deren Lizenz auf Vereinbarkeit mit GPLv3 zu prüfen. Separat installierte Frontends sind von mitverteilten Komponenten zu unterscheiden.

#### S02-04 Konsequenzen und Freiheitsgrade nur teilweise erklärt
**Schwere:** 🟡 Empfehlung
**Datei:** [02-02-Organisatorisch.md](arc-doc/02-Randbedingungen/02-02-Organisatorisch.md)

**Befund:** Bei Team, Werkzeugen und Tests bleibt die Verbindlichkeit unklar. Ausdrücklich als Muss formuliert ist nur die IDE-unabhängige Gradle-Baubarkeit.

### Sektion 3: Kontextabgrenzung

#### S03-01 Remisangebote ohne Implementierungsabgrenzung
**Schwere:** 🟡 Empfehlung
**Datei:** [03-01-Fachlicher-Kontext.md](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md)

**Befund:** Der Kontext nennt Remisangebote, [5.2](arc-doc/05-Bausteinsicht/05-02-XBoard-Protokoll.md) schließt ihre Unterstützung aus.

**Änderungsvorschlag:**
> Der realisierte Informationsaustausch umfasst insbesondere die Spielzüge. Remisangebote werden von der aktuellen XBoard-Implementierung nicht unterstützt (siehe Abschnitt 5.2).

#### S03-02 Datenflüsse und Erweiterungsstatus fehlen im Diagramm
**Schwere:** 🟡 Empfehlung
**Datei:** [03-01-Fachlicher-Kontext.md](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md)

**Befund:** Das Diagramm hat unbeschriftete, ungerichtete Verbindungen. Endspiele erscheinen gleichrangig mit realisierten Anbindungen, obwohl nicht implementiert.

**Änderungsvorschlag:**
> Verbindungen beschriften und richten: Gegner → DokChess: gegnerische Züge; DokChess → Gegner: eigene Züge; DokChess → Eröffnungsbibliothek: Stellung; Bibliothek → DokChess: Zugkandidaten. Endspielanbindung gestrichelt als „Erweiterungsoption, nicht implementiert“.

#### S03-03 Fachlich-technisches Mapping unvollständig
**Schwere:** 🟡 Empfehlung
**Datei:** [03-02-Technischer-Kontext.md](arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md)

**Befund:** Nur menschliche Spieler sind ausdrücklich dem Frontend zugeordnet. Der Computergegner läuft laut 8.3 ebenfalls über das Frontend.

**Änderungsvorschlag:**
> Menschlicher Gegner und Computergegner werden über einen vorgeschalteten XBoard-Client vermittelt (Standardeingabe/-ausgabe). Fachliches Eröffnungswissen wird durch optionale Polyglot-Buchdateien bereitgestellt, die ausschließlich lesend genutzt werden. Für Endspielwissen besteht kein implementierter technischer Kanal.

#### S03-04 Schnittstellenrisiken und Qualitätsanforderungen nicht zugeordnet
**Schwere:** 🟡 Empfehlung
**Datei:** [03-02-Technischer-Kontext.md](arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md)

**Befund:** Frontend-Integrationsrisiko (11.1), Schnittstellenszenarien (K01, E01, E02, Z01) und die fehlende fachliche Validierung von Buchdateien (8.4) werden in Sektion 3 nicht benannt.

### Sektion 4: Lösungsstrategie

#### S04-01 Qualitätsziel Spielstärke abweichend bezeichnet
**Schwere:** 🟡 Empfehlung
**Datei:** [04-01-Einstieg.md](arc-doc/04-Loesungsstrategie/04-01-Einstieg.md)

**Befund:** Die Tabelle nennt „Attraktive Spielstärke (Attraktivität)“, 1.2 dagegen „Akzeptable Spielstärke (Funktionale Eignung)“.

**Änderungsvorschlag:** Zielbezeichnung auf „Akzeptable Spielstärke (Funktionale Eignung)“ angleichen.

#### S04-02 Effizienzansatz nicht gegen Lesbarkeitspriorität abgegrenzt
**Schwere:** 🟡 Empfehlung
**Datei:** [04-01-Einstieg.md](arc-doc/04-Loesungsstrategie/04-01-Einstieg.md), [04-02-Aufbau.md](arc-doc/04-Loesungsstrategie/04-02-Aufbau.md)

**Befund:** „Effiziente Implementierung des Domänenmodells“ (4.1) steht gegen „auf Kosten von Effizienz“ (4.2). Die Abwägung bleibt offen.

**Änderungsvorschlag:**
> Ersetze durch „Domänenmodell mit Vorrang für Verständlichkeit; Effizienzabsicherung durch Integrationstests mit Zeitvorgaben (siehe Abschnitt 4.2 und 10.2).“

#### S04-03 Reaktivität und Suchbeschleunigung vermischt
**Schwere:** 🟡 Empfehlung
**Datei:** [04-01-Einstieg.md](arc-doc/04-Loesungsstrategie/04-01-Einstieg.md), [04-04-Anbindung.md](arc-doc/04-Loesungsstrategie/04-04-Anbindung.md)

**Befund:** Reactive Extensions sind in 4.1 dem schnellen Berechnen zugeordnet, in 4.4 aber der Ansprechbarkeit. Die Basisimplementierung ist laut 4.3 nicht nebenläufig.

**Änderungsvorschlag:**
> Reactive Extensions halten die Anbindung während der Zugermittlung ansprechbar und übermitteln bessere Züge als Events. Die Suchbeschleunigung erfolgt durch Alpha-Beta-Suche; ein paralleler Minimax ist als austauschbares Beispiel enthalten.

#### S04-04 Organisatorische Strategie nicht angebunden
**Schwere:** 🟢 Hinweis
**Datei:** [04-01-Einstieg.md](arc-doc/04-Loesungsstrategie/04-01-Einstieg.md)

**Befund:** Das risikogetriebene, iterative Vorgehen aus 2.2 hat in Sektion 4 keine Einordnung oder keinen Verweis.

### Sektion 5: Bausteinsicht

#### S05-01 Protokollumfang nicht mit dem fachlichen Kontext abgeglichen
**Schwere:** 🟡 Empfehlung
**Datei:** [05-02-XBoard-Protokoll.md](arc-doc/05-Bausteinsicht/05-02-XBoard-Protokoll.md)

**Befund:** 3.1 nennt Remisangebote, 5.2 schließt sie aus und erklärt den Umfang zugleich für ausreichend.

**Änderungsvorschlag:**
> Der in Abschnitt 3.1 beschriebene Informationsaustausch umfasst auch Remisangebote. Diese werden vom aktuellen XBoard-Subsystem nicht unterstützt.

#### S05-02 Asynchroner Schnittstellenvertrag lässt Randfälle offen
**Schwere:** 🟡 Empfehlung
**Datei:** [05-04-Engine.md](arc-doc/05-Bausteinsicht/05-04-Engine.md), [05-07-Zugsuche.md](arc-doc/05-Bausteinsicht/05-07-Zugsuche.md)

**Befund:** Offen sind: Abschluss ohne Zugkandidaten, Ereignisse nach Abbruch, überlappende Suchaufträge, Verwendung von Ergebnissen einer abgebrochenen Suche für eine geänderte Stellung.

#### S05-03 Zerlegungsbegründung besser erschließbar machen
**Schwere:** 🟢 Hinweis
**Datei:** [05-01-Ebene-1.md](arc-doc/05-Bausteinsicht/05-01-Ebene-1.md)

**Befund:** Die Begründung steht in 4.2, 5.1 verweist nicht darauf.

### Sektion 6: Laufzeitsicht

#### S06-01 Reaktion auf Eingaben während der Zugberechnung fehlt
**Schwere:** 🟡 Empfehlung
**Datei:** [06-01-Zugermittlung.md](arc-doc/06-Laufzeitsicht/06-01-Zugermittlung.md)

**Befund:** Der Walkthrough begründet den asynchronen Aufruf mit Ansprechbarkeit, zeigt aber nur eine ungestört abgeschlossene Suche. Sofortiges Ziehen (4.4) und `sucheAbbrechen` (5.7) kommen nicht vor.

**Änderungsvorschlag:**
> Ergänzendes Szenario „Eingabe während laufender Zugermittlung“: Weiterleitung an die Engine, Abbruch der Zugsuche, Ausgabe des ausgewählten Zuges. Fall ohne bisher gelieferten Kandidaten und verspätete Ereignisse sind festzulegen.

#### S06-02 Fehlerpfad an der externen Schnittstelle fehlt
**Schwere:** 🟡 Empfehlung
**Datei:** [06-01-Zugermittlung.md](arc-doc/06-Laufzeitsicht/06-01-Zugermittlung.md)

**Befund:** Validierung wird nur für einen zulässigen Zug gezeigt, [8.4](arc-doc/08-Konzepte/08-04-Validierung.md) beschreibt „Illegal move“.

**Änderungsvorschlag:**
> Alternativablauf „Unzulässiger Gegnerzug“: XBoard prüft mit den Spielregeln, antwortet mit „Illegal move“ und gibt den Zug nicht an die Engine weiter. Es wird keine Zugermittlung gestartet.

#### S06-03 Zusammenarbeit innerhalb der Engine implizit
**Schwere:** 🟡 Empfehlung
**Datei:** [06-01-Zugermittlung.md](arc-doc/06-Laufzeitsicht/06-01-Zugermittlung.md)

**Befund:** Zugsuche und Stellungsbewertung werden nur textlich („untersucht und bewertet“) erwähnt, im Diagramm fehlen sie.

**Änderungsvorschlag:**
> Verfeinerung auf Ebene 2: Liefert die Eröffnungsbibliothek keinen Zug, delegiert die Engine an die Zugsuche. Diese exploriert mit den Spielregeln den Spielbaum bis zur Suchtiefe und bewertet mit der Stellungsbewertung. Bessere Kandidaten kommen per `onNext`, der Abschluss per `onComplete`.

### Sektion 7: Verteilungssicht

#### S07-01 Motivation der Deployment-Struktur fehlt
**Schwere:** 🟡 Empfehlung
**Datei:** [07-01-Infrastruktur-Windows.md](arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md)

**Befund:** Die Wahl der lokalen Ein-Rechner-Struktur ist nicht begründet.

**Änderungsvorschlag:**
> Die Variante bündelt Frontend und Engine auf einem Windows-PC und ermöglicht den lokalen Spielbetrieb ohne Server oder Netzwerkdienste. Die Kommunikation erfolgt lokal über Standardeingabe und -ausgabe.

#### S07-02 Entwicklungs-, Test- und Betriebsumgebung nicht abgegrenzt
**Schwere:** 🟡 Empfehlung
**Datei:** [07-01-Infrastruktur-Windows.md](arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md)

**Befund:** Das Diagramm beschreibt den Spielbetrieb. Entwicklungs- und Testumgebung sind nicht zugeordnet.

#### S07-03 Ressourcenbedarf fehlt
**Schwere:** 🟡 Empfehlung
**Datei:** [07-01-Infrastruktur-Windows.md](arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md)

**Befund:** CPU- und Speicherbedarf fehlen, besonders relevant bei paralleler Zugsuche.

### Sektion 8: Konzepte

#### S8-01 Ungültige Anfangsstellungen: Konzept erfüllt Z02 nicht
**Schwere:** 🔴 Kritisch
**Datei:** [08-04-Validierung.md](arc-doc/08-Konzepte/08-04-Validierung.md), [08-05-Fehlerbehandlung.md](arc-doc/08-Konzepte/08-05-Fehlerbehandlung.md)

**Befund:** 8.4 prüft beim Stellungsaufbau „nicht aber, ob die Position zulässig ist“. 8.5 behandelt ungültige Stellungen nur „falls erkannt“ und arbeitet „normal“ weiter. [Z02](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md) verlangt, dass die Engine die Situation erkennt und das Spiel beendet.

**Änderungsvorschlag:**
> Bekannte Abweichung zu Z02: Der beschriebene Ansatz garantiert weder die Erkennung einer unzulässigen Anfangsstellung noch die Beendigung der Partie. Zur Erfüllung muss vor der Zugermittlung eine fachliche Stellungsvalidierung erfolgen; bei Ungültigkeit meldet das XBoard-Subsystem den Fehler und verhindert weitere Zugermittlungen.

#### S8-02 Asynchrone Fehlerbehandlung unpräzise
**Schwere:** 🟡 Empfehlung
**Datei:** [08-05-Fehlerbehandlung.md](arc-doc/08-Konzepte/08-05-Fehlerbehandlung.md)

**Befund:** Wie `onError` in eine Protokollmeldung überführt wird und welcher Zustand nach fehlgeschlagener Zugermittlung bleibt, ist nicht beschrieben.

**Änderungsvorschlag:**
> Das XBoard-Subsystem behandelt synchrone Runtime Exceptions und asynchrone `onError`-Signale über denselben Meldepfad zu `tellusererror`. Ein `onError` beendet die betroffene Zugermittlung. Ein Bibliotheksfehler erlaubt das Spiel ohne Eröffnungsbibliothek, eine ungültige Stellung erfordert eine neue gültige Ausgangsstellung.

#### S8-03 Antwortzeittests nicht reproduzierbar spezifiziert
**Schwere:** 🟡 Empfehlung
**Datei:** [08-07-Testbarkeit.md](arc-doc/08-Konzepte/08-07-Testbarkeit.md)

**Befund:** „Der Erfolg dieser Tests hängt von der eingesetzten Hardware ab.“ Referenzumgebung, Suchkonfiguration und Messung der „denkt“-Rückmeldung (E02) fehlen.

**Änderungsvorschlag:**
> Antwortzeittests werden E01 und E02 zugeordnet und dokumentieren FEN-Eingabestellung, Suchkonfiguration, Hardware, JVM-Version sowie Beginn und Ende der Messung. Die Rückmeldung „denkt“ (5 s) und der erste Zug (10 s) werden getrennt geprüft.

### Sektion 9: Architekturentscheidungen

#### S09-01 Historische Bewertungsbasis nicht zum Entscheidungsdatum eingeordnet
**Schwere:** 🟡 Empfehlung
**Datei:** [09-01-Anbindung.md](arc-doc/09-Entscheidungen/09-01-Anbindung.md)

**Befund:** `Accepted (2026-03-10)` bei einer Frontend-Erhebung „Stand 2011“. Offen ist, ob nachdokumentiert oder neu bewertet wurde.

**Änderungsvorschlag:**
> Die Vergleichstabelle beschreibt den Erhebungsstand 2011. Eine erneute Prüfung zum Statusdatum 2026-03-10 ist nicht dokumentiert; daraus lässt sich keine aktuelle Kompatibilitätszusage ableiten.

#### S09-02 Leistungsbegründung nicht nachprüfbar
**Schwere:** 🟡 Empfehlung
**Datei:** [09-02-Stellungsobjekte.md](arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md)

**Befund:** Zu „ca. 30 Prozent“ und „geforderten Grenzen“ fehlen Ausgangsstellung, absolute Laufzeiten, Hardware, JVM, Messverfahren und Grenzwerte.

**Änderungsvorschlag:**
> Das Ergebnis ist ein orientierender Hinweis, kein reproduzierbarer Nachweis. Messdaten und das zugehörige Qualitätsszenario mit Grenzwert sind zu ergänzen.

### Sektion 10: Qualitätsanforderungen

#### S10-01 Spielstärkeziel nicht vollständig prüfbar
**Schwere:** 🔴 Kritisch
**Datei:** [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md)

**Befund:** F02–F04 prüfen einzelne taktische Fähigkeiten, nicht „schwache Gegner sicher zu schlagen und Gelegenheitsspieler zumindest zu fordern“ (1.2).

**Änderungsvorschlag:**
> F05: DokChess spielt je 100 Partien gegen vorab festgelegte Referenzgegner für schwache Spieler und Gelegenheitsspieler (gleiche Zeitbudgets, ausgeglichene Farbverteilung). Akzeptanz: mindestens 80 % der möglichen Punkte gegen schwache Gegner und 40 % gegen Gelegenheitsspieler. Gegner, Versionen, Einstellungen und Ergebnisse werden protokolliert.

Die Schwellenwerte sind Vorschläge zur Abstimmung, keine bestehenden Anforderungen.

#### S10-02 Zeitgrenzen und Messbedingungen nicht eindeutig
**Schwere:** 🟡 Empfehlung
**Datei:** [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md)

**Befund:** E01 fordert fünf Sekunden generell, E02 erlaubt zehn für den ersten Zug. Hardware, Laufzeitumgebung, Suchkonfiguration und Messbeginn fehlen.

**Änderungsvorschlag:**
> E01 gilt ab dem zweiten Engine-Zug; für den ersten gilt ausschließlich E02. Gemessen wird vom vollständigen Empfang des gegnerischen Zugs bis zur vollständigen Ausgabe des Antwortzugs, auf einem versionierten Messprofil.

#### S10-03 Analysierbarkeit teilweise subjektiv bewertet
**Schwere:** 🟡 Empfehlung
**Datei:** [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md)

**Befund:** „Erschließen“, „unverzüglich“, „ohne Umwege“ (W01–W03) ergeben keine eindeutige Bestehensentscheidung.

**Änderungsvorschlag:**
> W01 bestanden, wenn die Testperson binnen 15 Minuten Hauptbausteine, Verantwortlichkeiten und Ablauf der Zugermittlung korrekt erläutert. W02: Beispielinhalt binnen einer Minute. W03: Paket und Implementierungsklasse binnen fünf Minuten benennen.

#### S10-04 Änderungsaufwand nur teilweise begrenzt
**Schwere:** 🟡 Empfehlung
**Datei:** [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md)

**Befund:** W04 und P01 haben keine Aufwandsgrenze, W05 lässt offen, ob „eine Woche“ Kalenderdauer oder Personenaufwand ist.

#### S10-05 Funktionale und Fehlerszenarien nicht reproduzierbar
**Schwere:** 🟡 Empfehlung
**Datei:** [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md)

**Befund:** F01–F04 und Z01/Z02 haben keine Referenzstellungen und keine zulässigen Ergebnisse. Z01 verlangt Fehlermeldung, unveränderten Zustand und Weiterspielen mit legalem Zug, Z02 Fehlermeldung ohne Zugberechnung.

### Sektion 11: Risiken und technische Schulden

#### S11-01 Bekannte Validierungsrisiken fehlen
**Schwere:** 🔴 Kritisch
**Datei:** [11-02-Aufwand.md](arc-doc/11-Risiken/11-02-Aufwand.md)

**Befund:** Kein Risiko erfasst die Validierungslücken aus [8.4](arc-doc/08-Konzepte/08-04-Validierung.md): Unzulässige Stellungen können Laufzeitfehler verursachen, fehlerhafte Eröffnungsbibliotheken ungültige Züge.

**Änderungsvorschlag:**
> Risiko „Unzureichend validierte Eingaben“: Unzulässige Ausgangsstellungen und fehlerhafte Eröffnungsdaten können Laufzeitfehler bzw. ungültige Engine-Züge verursachen (siehe 8.4). Maßnahmen: Ausgangsstellungen vor Suchbeginn plausibilisieren, Bibliothekszüge auf Regelkonformität prüfen und bei Ungültigkeit auf die Zugsuche zurückfallen; Negativtests für beide Eingabekanäle.

#### S11-02 Risikobewertung und Priorisierung fehlen
**Schwere:** 🟡 Empfehlung
**Datei:** [11-01-Frontend.md](arc-doc/11-Risiken/11-01-Frontend.md), [11-02-Aufwand.md](arc-doc/11-Risiken/11-02-Aufwand.md), [11-03-Spielstaerke.md](arc-doc/11-Risiken/11-03-Spielstaerke.md)

**Befund:** Alle drei Risiken sind unbewertet. Verantwortliche, Maßnahmenstatus und Prüftermine fehlen.

**Änderungsvorschlag:**
> Eintrittswahrscheinlichkeit und Auswirkung je Risiko als niedrig, mittel oder hoch bewerten, daraus eine Priorität ableiten und je Eintrag Verantwortliche, Maßnahmenstatus, Prüftermin und Restrisiko dokumentieren.

#### S11-03 Zurückgestellte Regeln nicht als technische Schuld geführt
**Schwere:** 🟡 Empfehlung
**Datei:** [11-02-Aufwand.md](arc-doc/11-Risiken/11-02-Aufwand.md)

**Befund:** 50-Züge-Regel und Stellungswiederholung sind zurückgestellt, ohne spätere Bearbeitung festzulegen. Das steht in Spannung zu „Vollständige Implementierung der FIDE-Schachregeln“ (1.1).

**Änderungsvorschlag:**
> Technische Schuld: 50-Züge-Regel und Stellungswiederholung sind vorläufig nicht implementiert (betrifft Remiserkennung, nicht die Legalität einzelner Züge). Nachimplementierung als eigener Arbeitspunkt; Verantwortlichkeit, Zieltermin oder eine akzeptierte Scope-Ausnahme festlegen.

#### S11-04 Maßnahmen ohne überprüfbaren Abschluss
**Schwere:** 🟡 Empfehlung
**Datei:** [11-01-Frontend.md](arc-doc/11-Risiken/11-01-Frontend.md), [11-03-Spielstaerke.md](arc-doc/11-Risiken/11-03-Spielstaerke.md)

**Befund:** Der Proof of Concept hat keine Abnahmekriterien, bei den Schachaufgaben-Tests fehlt eine Reaktion auf unzureichende Ergebnisse.

**Änderungsvorschlag:**
> Der Frontend-Proof-of-Concept ist abgeschlossen, wenn Einbindung und Test gemäß K01 gelingen und eine Partie samt Beendigung funktioniert. Für 11.3 werden F02–F04 sowie E01–E02 automatisiert geprüft; bei Nichterfüllung werden Suchstrategie bzw. Bewertung angepasst.

#### S11-05 Breite der Risikoermittlung nicht nachvollziehbar
**Schwere:** 🟡 Empfehlung
**Datei:** [11-02-Aufwand.md](arc-doc/11-Risiken/11-02-Aufwand.md)

**Befund:** Eine systematische Risikoermittlung mit Stakeholdern ist nicht dokumentiert. Die XBoard-Teilimplementierung aus 5.2 ist nicht als Schuld oder akzeptierte Scope-Grenze bewertet.

### Sektion 12: Glossar

#### S12-01 Zeitliche Bedingung für en passant fehlt
**Schwere:** 🟡 Empfehlung
**Datei:** [12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md)

**Änderungsvorschlag:**
> En passant ist ein besonderer Bauernschlag unmittelbar nach einem gegnerischen Bauerndoppelschritt aus der Grundstellung. Ein benachbarter eigener Bauer darf den gegnerischen Bauern so schlagen, als wäre dieser nur ein Feld vorgerückt.

#### S12-02 Endspiel verwechselt Figurenanzahl mit Figurenarten
**Schwere:** 🟡 Empfehlung
**Datei:** [12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md)

**Änderungsvorschlag:**
> Endspiel bezeichnet die späte Phase einer Schachpartie mit typischerweise deutlich reduziertem Material.

#### S12-03 Minimax suggeriert uneingeschränkte Optimalität
**Schwere:** 🟡 Empfehlung
**Datei:** [12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md)

**Änderungsvorschlag:**
> Minimax bewertet einen Spielbaum unter der Annahme bestmöglicher gegnerischer Antworten. DokChess untersucht ihn bis zu einer festgelegten Suchtiefe und wählt den gemäß Bewertungsfunktion besten Zug; globale Optimalität ist nicht garantiert.

#### S12-04 Zwei Bedeutungen von Engine ungetrennt
**Schwere:** 🟡 Empfehlung
**Datei:** [12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md)

**Befund:** 1.1 bezeichnet das Gesamtsystem als Schach-Engine, 5.4 einen internen Baustein.

**Änderungsvorschlag:**
> Schach-Engine bezeichnet die Software zur Berechnung von Schachzügen, hier DokChess insgesamt. „Subsystem Engine“ bezeichnet den internen Baustein aus Abschnitt 5.4.

#### S12-05 Zug und Stellung brauchen eindeutige Einordnung
**Schwere:** 🟡 Empfehlung
**Datei:** [12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md)

**Befund:** „Halbzug“ verwendet „Zug“ für ein Zugpaar, die Klasse `Zug` ist eine einzelne Aktion. „Stellung“ fehlt als Eintrag.

**Änderungsvorschlag:**
> Halbzug: Einzelne Spieleraktion; die Klasse Zug repräsentiert einen Halbzug. Stellung: Figurenanordnung einschließlich Spieler am Zug, Rochaderechten und möglicher En-passant-Schlagoption (siehe Abschnitt 8.2).

#### S12-06 Bitboard fehlt
**Schwere:** 🟡 Empfehlung
**Datei:** [12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md)

**Befund:** W05 verwendet „Bitboard-Repräsentation“ ohne Glossareintrag.

**Änderungsvorschlag:**
> Bitboard: Darstellung einer Menge von Schachbrettfeldern durch 64 Bits, eines je Feld.

#### S12-07 Englische Bildbeschriftungen ohne Übersetzung
**Schwere:** 🟡 Empfehlung
**Datei:** [12-01-Einstieg.md](arc-doc/12-Glossar/12-01-Einstieg.md)

**Befund:** Die Bilder verwenden englische Begriffe, entgegen der Sprachkonvention 2.3. Für die Bilder existieren keine Graphknoten.

**Änderungsvorschlag:**
> Figuren: Pawn = Bauer, Bishop = Läufer, Knight = Springer, Rook = Turm, Queen = Dame, King = König. Brett: Square = Feld, Ranks = Reihen (1–8), Files = Linien (a–h).

## Sektionsübergreifende Konflikte

| Konfliktdimension | Status | Befunde |
|---|---|---|
| Qualitätsstrang (S1 ↔ S4 ↔ S10) | 🟡 | E01/E02 überlappen, taktische Tests belegen die Spielstärkezusage nicht |
| Strategie ↔ Entscheidungen (S4 ↔ S9) | 🟡 | DI/Zerlegung/Reactive Extensions und Polyglot-Wahl ohne ADR |
| Constraint-Compliance (S2 ↔ S4/S8/S9) | 🟢 | Keine Verletzung. Nur Hinweis: Gradle/CheckStyle/GPLv3-Nachweise fehlen |
| Kontext ↔ Bausteine (S3 ↔ S5) | 🟡 | Remisangebote, Endspiel-Status |
| Sichten-Konsistenz (S5 ↔ S6 ↔ S7) | 🟢 | Keine Konflikte |
| Konzepte ↔ Entscheidungen (S8 ↔ S9) | 🟡 | DI-Framework-Verzicht und Logging-Verzicht sind Entscheidungen, stehen aber nur in S8 |
| Risiken ↔ Qualität (S11 ↔ S1/S10) | 🔴 | Validierungsrisiko fehlt, Änderbarkeit ohne Risiko, Maßnahme 11.3 deckt den Zielkonflikt nur teilweise ab |

### 1. Qualitätsstrang (S1 ↔ S4 ↔ S10)

| Qualitätsziel (Rang) | Strategieansatz (S4) | Szenario (S10) | Status |
|---|---|---|---|
| Analysierbarkeit (1) | arc42-Überblick, Domänenmodell, deutsche Bezeichner, javadoc | W01, W02, W03, W05 | ✅ |
| Änderbarkeit (2) | Java, Schnittstellen, unveränderliche Objekte, DI, Tests | W04, W05, P01 | ✅ |
| Interoperabilität (3) | XBoard, portables Java | K01 | ✅ |
| Spielstärke (4) | Eröffnungsbibliotheken, Minimax, taktische Tests | F02, F03, F04 | ⚠️ Partienstärke nicht abgesichert |
| Effizienz (5) | Reactive Extensions, Alpha-Beta, effizientes Domänenmodell, Zeitvorgaben | E01, E02 | ⚠️ Überlappende Zeitgrenzen |

#### KQS-01 Unterschiedliche Zeitgrenzen für den ersten Antwortzug
**Konflikttyp:** K5 – Uneindeutige Akzeptanzkriterien
**Schwere:** 🟡 Warnung
**Betroffene Dateien:**
- [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md) — E01: „innerhalb von fünf Sekunden“, E02: erster Antwortzug „innerhalb von maximal zehn Sekunden“.
- [04-01-Einstieg.md](arc-doc/04-Loesungsstrategie/04-01-Einstieg.md) — „Integrationstests mit Zeitvorgaben“.

**Beschreibung:** Eine Antwort nach acht Sekunden erfüllt E02, verletzt aber E01. Eine Ausnahme für Initialisierung ist nicht definiert.

**Lösungsvorschlag:**
> Nach dem ersten Antwortzug gemäß E02 antwortet die Engine während einer Partie auf jeden gegnerischen Zug innerhalb von fünf Sekunden mit einem Zug.

#### KQS-02 Taktische Tests belegen das Spielstärkeniveau nicht
**Konflikttyp:** K5 – Messbarkeits-Lücke
**Schwere:** 🟡 Warnung
**Betroffene Dateien:**
- [01-02-Qualitaetsziele.md](arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md) — „schwache Gegner sicher zu schlagen und Gelegenheitsspieler zumindest zu fordern“.
- [04-02-Aufbau.md](arc-doc/04-Loesungsstrategie/04-02-Aufbau.md) — akzeptable Spielstärke werde durch das Durchspielen der Szenarien gezeigt.
- [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md) — F02, F03, F04.

**Beschreibung:** Die Szenarien haben prüfbare taktische Ergebnisse, aber kein Kriterium für die Leistung über vollständige Partien.

**Lösungsvorschlag:**
> Die zugeordneten Qualitätsszenarien prüfen taktische Mindestfähigkeiten. Ob DokChess schwache Gegner zuverlässig schlägt und Gelegenheitsspieler fordert, ist dadurch noch nicht nachgewiesen.

Zusätzlich ein Partienszenario mit festgelegten Gegnern, Zeitbudget, Stichprobengröße und Erfolgsschwelle aufnehmen.

### 2. Strategie ↔ Entscheidungen (S4 ↔ S9)

| Strategische Festlegung (S4) | Entscheidung (S9) | Status |
|---|---|---|
| XBoard, Anbindung über stdin/stdout | ADR 09-01 (`realizes`) | ✅ |
| Unveränderliche fachliche Objekte | ADR 09-02 (`realizes`) | ✅ für `Stellung` belegt |
| Lesbarkeit vor Effizienz | ADR 09-02 (Verweis aus 4.2) | ✅ bewerteter Zielkonflikt |
| Schnittstellen, Zerlegung, Dependency Injection | keine ADR | 🔲 |
| Reactive Extensions | keine ADR | 🔲 |
| Eröffnungsbibliotheken, Polyglot | keine ADR | 🔲 |

#### KSE-01 Zentrale Struktur- und Nebenläufigkeitsentscheidungen ohne ADR
**Konflikttyp:** K4 – Strategie ohne Entscheidungsgrundlage
**Schwere:** 🟡 Warnung
**Betroffene Dateien:**
- [04-02-Aufbau.md](arc-doc/04-Loesungsstrategie/04-02-Aufbau.md) — „Alle Teile sind durch Schnittstellen abstrahiert, die Implementierungen werden per Dependency Injection zusammengesteckt.“
- [04-04-Anbindung.md](arc-doc/04-Loesungsstrategie/04-04-Anbindung.md) — Anbindung über „Reactive Extensions“.

**Beschreibung:** `s04-sa-zerlegung`, `s04-sa-dependency-injection`, `s04-sa-schnittstellen-kernabstraktionen` und `s04-sa-reactive-extensions` haben keine eingehende `realizes`-Kante. Alternativen und Abwägung fehlen. Es ist eine Dokumentationslücke, keine fehlende Umsetzung.

**Lösungsvorschlag:** Zwei ADRs ergänzen:
> Die vier Hauptteile werden über Schnittstellen entkoppelt und per Dependency Injection zusammengesetzt, damit Implementierungen unabhängig austauschbar und testbar bleiben.
> Die Engine-Anbindung verwendet Reactive Extensions, damit DokChess während der Zugermittlung ansprechbar bleibt.

#### KSE-02 Polyglot-Formatwahl ohne Entscheidungsabwägung
**Konflikttyp:** K4 – Strategie ohne Entscheidungsgrundlage
**Schwere:** 🟡 Warnung
**Betroffene Dateien:**
- [04-03-Spielstrategie.md](arc-doc/04-Loesungsstrategie/04-03-Spielstrategie.md) — „Für die Integration von Eröffnungsbibliotheken wurde das Dateiformat ‚Polyglot Opening Book‘ implementiert“.

**Beschreibung:** Die Auswahl des Formats ist nicht begründet, keine ADR behandelt sie.

**Lösungsvorschlag:**
> DokChess integriert Eröffnungsbibliotheken zunächst im Format Polyglot Opening Book. Die Formatanbindung bleibt hinter einem austauschbaren Adapter gekapselt.

### 3. Constraint-Compliance (S2 ↔ S4/S8/S9)

Geprüft: 15 Constraints, 16 `constrains`-Kanten (3 explizit, 13 inferiert). Keine belegte Verletzung.

#### KRC-01 Prozess-, Build- und Konventionsvorgaben nicht durchgängig nachverfolgbar
**Konflikttyp:** K2/K3 – ungeprüfte Randbedingungen, keine belegte Verletzung
**Schwere:** 🟢 Hinweis
**Betroffene Dateien:**
- [02-02-Organisatorisch.md](arc-doc/02-Randbedingungen/02-02-Organisatorisch.md) — „allein mit Gradle, also ohne IDE baubar“; GPLv3.
- [02-03-Konventionen.md](arc-doc/02-Randbedingungen/02-03-Konventionen.md) — CheckStyle.
- [08-07-Testbarkeit.md](arc-doc/08-Konzepte/08-07-Testbarkeit.md) — keine Gradle-/CheckStyle-Ausführung oder Lizenzprüfung.

**Beschreibung:** Sieben Constraints haben keine ausgehende `constrains`-Kante (Team, Zeitplan, Vorgehensmodell, Entwicklungswerkzeuge, Versionsverwaltung, Open Source, Kodierrichtlinien).

**Lösungsvorschlag:**
> Für jede veröffentlichte Version werden der IDE-unabhängige Gradle-Build, die Unit- und Integrationstests sowie die CheckStyle-Prüfung dokumentiert. Der Veröffentlichungsnachweis benennt die unter GPLv3 bereitgestellten Quelltexte und die Lizenzbedingungen eingebundener Abhängigkeiten.

### 4. Kontext ↔ Bausteine (S3 ↔ S5)

| Externer Partner | Kontext (S3) | Bausteinsicht (S5) | Status |
|---|---|---|---|
| Menschlicher Gegner | Züge und Remisangebote | XBoard-Protokoll, keine Remisangebote | 🟡 |
| Computergegner | gleicher Austausch | XBoard-Protokoll (inferiert) | 🟡 |
| XBoard Client | externes Frontend | Standard-Ein-/Ausgabe → XBoard | ✅ |
| Eröffnungen / Polyglot | optional, nur lesend | Subsystem Eröffnung, PolyglotOpeningBook | ✅ |
| Endspiele | S3.1 optional, S3.2 nicht implementiert | keine Anbindung | 🟡 |

#### KKB-01 Remisangebote im Kontext vorgesehen, im Baustein ausgeschlossen
**Konflikttyp:** K1 – Kontextschnittstelle nur teilweise abgedeckt
**Schwere:** 🟡 Warnung
**Betroffene Dateien:**
- [03-01-Fachlicher-Kontext.md](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md) — „beispielsweise über ihre Züge, oder über Remisangebote“.
- [05-02-XBoard-Protokoll.md](arc-doc/05-Bausteinsicht/05-02-XBoard-Protokoll.md) — „Remis-Angebote und Aufgabe der anderen Seite“ nicht unterstützt, zugleich „reicht aber für die an DokChess gestellten Anforderungen aus“.

**Lösungsvorschlag:**
> Der aktuell unterstützte Informationsaustausch umfasst Spielzüge. Remisangebote werden von der XBoard-Anbindung derzeit nicht unterstützt. Diese Einschränkung gilt für menschliche Gegner und Computergegner.

#### KKB-02 Endspielpartner ohne Kennzeichnung als Erweiterungsoption
**Konflikttyp:** K1 – Kontextschnittstelle ohne Zuordnung in der Bausteinsicht
**Schwere:** 🟡 Warnung
**Betroffene Dateien:**
- [03-01-Fachlicher-Kontext.md](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md) — „Endspiele (Fremdsystem)“.
- [05-01-Ebene-1.md](arc-doc/05-Bausteinsicht/05-01-Ebene-1.md) — keine Schnittstelle.

**Beschreibung:** [3.2](arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md) erklärt den Implementierungsverzicht, in 3.1 und im Diagramm fehlt die Trennung zwischen aktuellem Umfang und Erweiterungsoption.

**Lösungsvorschlag:**
> Endspielbibliotheken sind eine mögliche Erweiterung, keine aktuell verfügbare optionale Anbindung. In der Bausteinsicht ist hierfür keine Schnittstelle vorgesehen; siehe Abschnitt 3.2 „Zu Endspielen“.

### 5. Sichten-Konsistenz (S5 ↔ S6 ↔ S7)

| Baustein | S5 | S6 | S7 | Status |
|---|---|---|---|---|
| DokChess | Whitebox 5.1 | Subsysteme beteiligt | DokChess.jar (E) | ✅ |
| XBoard-Protokoll | 5.2 | Zugermittlung (E) | DokChess.jar (E) | ✅ |
| Spielregeln | 5.3 | Zugermittlung (E) | DokChess.jar (E) | ✅ |
| Engine | 5.4 | Zugermittlung (E) | DokChess.jar (E) | ✅ |
| Eröffnung | 5.5 | Zugermittlung (E) | DokChess.jar (E), Nutzung optional | ✅ |
| Zugsuche | 5.7 | innerhalb der Engine (I) | DokChess.jar (I) | ✅ plausibel |
| Stellungsbewertung | 5.8 | innerhalb der Engine (I) | DokChess.jar (I) | ✅ plausibel |

Keine belastbaren Konflikte nach K1–K6. Arena, JRE und Startskript sind externe Software bzw. Infrastruktur. S7 zeigt bewusst eine Konfiguration ohne Eröffnungsbibliothek. `ziehen` ändert den Engine-Zustand, `ermittleDeinenZug` führt keine Züge aus; das ist kein Widerspruch.

### 6. Konzepte ↔ Entscheidungen (S8 ↔ S9)

| Element | Zuordnung | Bezug |
|---|---|---|
| 8.1 Abhängigkeiten | teilweise: Framework-Verzicht ist Entscheidung | KKE-01 |
| 8.2 Domänenmodell | ja | `based_on` → ADR 09-02 |
| 8.3 Benutzungsoberfläche | ja | `based_on` → ADR 09-01 |
| 8.4 / 8.5 / 8.7 | ja | keine ADR zwingend |
| 8.6 Logging | teilweise: begründeter Verzicht ist Entscheidung | KKE-02 |

#### KKE-01 Framework-Verzicht nur im Abhängigkeitskonzept dokumentiert
**Konflikttyp:** K2/K4
**Schwere:** 🟡 Warnung
**Betroffene Dateien:**
- [08-01-Abhaengigkeiten.md](arc-doc/08-Konzepte/08-01-Abhaengigkeiten.md) — „DokChess verzichtet auf die Verwendung eines speziellen DI Frameworks.“

**Beschreibung:** Setter-Injection gehört nach S8. Der bewusste Verzicht auf ein DI-Framework und auf annotationsgetriebene Konfiguration ist eine systemweite Entscheidung (Alternativen Spring/CDI genannt), die in S9 fehlt.

**Lösungsvorschlag:** ADR in S9 mit dem Kern:
> DokChess bindet kein DI-Framework verbindlich ein und verwendet keine annotationsgetriebene Konfiguration. Die Standardverdrahtung erfolgt in Glue-Code und Unit-Tests. Die Wahl eines DI-Frameworks bleibt für Erweiterungen offen; die Standardverdrahtung muss manuell gepflegt werden.

#### KKE-02 Verzicht auf internes Logging und Tracing verbleibt in S8
**Konflikttyp:** K2/K4
**Schwere:** 🟡 Warnung
**Betroffene Dateien:**
- [08-06-Logging.md](arc-doc/08-Konzepte/08-06-Logging.md) — „Aufgrund ihrer Verfügbarkeit wurde auf die Implementierung eines Kommunikationsprotokoll-Tracings innerhalb von DokChess verzichtet.“
- [09-01-Anbindung.md](arc-doc/09-Entscheidungen/09-01-Anbindung.md) — nennt Debugging-Unterstützung durch Arena, entscheidet aber nicht über den Verzicht.

**Lösungsvorschlag:** ADR in S9 mit dem Kern:
> DokChess verzichtet auf feinkörniges internes Logging, eine integrierte Logging-Bibliothek und eigenes XBoard-Kommunikationstracing. Zur Diagnose dienen Unit-Tests und die Protokollierung des vorgeschalteten Clients. Interne Abläufe sind nicht über eigene Laufzeitlogs nachvollziehbar, Kommunikationstraces hängen vom Client ab.

### 7. Risiken ↔ Qualität (S11 ↔ S1/S10)

| Qualitätsziel (Rang) | Bedrohende Risiken | Maßnahmen | Status |
|---|---|---|---|
| Analysierbarkeit (1) | 11.1, 11.3 | Proof of Concept; Schachaufgaben-Tests sichern Verständlichkeit nicht | ⚠️ |
| Änderbarkeit (2) | keine | keine | ⚠️ Verdachtsfall |
| Interoperabilität (3) | 11.1 | Proof of Concept | ✅ |
| Spielstärke (4) | 11.2, 11.3 | Umfangsreduktion, Schachaufgaben-Tests | ✅ |
| Effizienz (5) | 11.3 | Zeitprüfungen außerhalb S11, nicht zugeordnet | ⚠️ |

#### KRQ-01 Bekannte Validierungsrisiken fehlen im Risikokatalog
**Konflikttyp:** K4
**Schwere:** 🔴 Kritisch
**Betroffene Dateien:**
- [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md) — F01 (regelkonformer Zug), Z02 (unzulässige Startstellung erkennen, Spiel beenden).
- [08-04-Validierung.md](arc-doc/08-Konzepte/08-04-Validierung.md) — keine semantische Stellungsprüfung, „Im Extremfall antwortet die Engine mit einem ungültigen Zug.“
- [08-05-Fehlerbehandlung.md](arc-doc/08-Konzepte/08-05-Fehlerbehandlung.md) — „DokChess arbeitet dann ‚normal‘ weiter“.
- [11-01-Frontend.md](arc-doc/11-Risiken/11-01-Frontend.md), [11-02-Aufwand.md](arc-doc/11-Risiken/11-02-Aufwand.md), [11-03-Spielstaerke.md](arc-doc/11-Risiken/11-03-Spielstaerke.md) — kein Validierungsrisiko.

**Beschreibung:** Diese bekannten Gefährdungen von F01 und Z02 fehlen in S11. Schachaufgaben-Tests schließen sie nicht nachweislich.

**Lösungsvorschlag:**
> Risiko „Unzulässige Eingaben und Bibliothekszüge“ ergänzen: gefährdet F01 und Z02. Maßnahmen: Startstellungen vor der Zugermittlung semantisch validieren und bei Unzulässigkeit das Spiel beenden; Bibliothekszüge vor Ausgabe auf Regelkonformität prüfen; negative Integrationstests für beide Fälle. 8.4 und 8.5 entsprechend anpassen.

#### KRQ-02 Änderbarkeit ohne eigene Risikobetrachtung
**Konflikttyp:** K1
**Schwere:** 🟡 Warnung
**Betroffene Dateien:**
- [01-02-Qualitaetsziele.md](arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md) — Änderbarkeit, Rang 2.
- [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md) — W04, W05, P01.
- [09-02-Stellungsobjekte.md](arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md) — Schnittstellenänderungen betreffen das Gesamtsystem.

**Beschreibung:** Keine eingehende `threatens`-Kante. Die breit wirkende Stellungsschnittstelle macht W05 zum plausiblen Restrisiko (Verdachtsfall, kein Nachweis).

**Lösungsvorschlag:**
> Risiko „Austauschbarkeit zentraler Komponenten nicht nachgewiesen“ ergänzen (gefährdet W04, W05, P01). Maßnahmen: exemplarische Austauschversuche mit dokumentiertem Aufwand; Einhaltung der Szenariogrenzen als Abnahmekriterium.

#### KRQ-03 Risikominderung deckt den Zielkonflikt nur teilweise ab
**Konflikttyp:** K2
**Schwere:** 🟡 Warnung
**Betroffene Dateien:**
- [11-03-Spielstaerke.md](arc-doc/11-Risiken/11-03-Spielstaerke.md) — gefährdet Spielstärke, Zugänglichkeit und Effizienz, Maßnahme präzisiert vor allem Spielstärke.
- [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md) — W01, E01, E02.

**Lösungsvorschlag:**
> Risikominderung 11.3 ergänzen: Schachaufgaben-Tests sichern F02–F04, die Zeitprüfungen aus 8.7 sichern E01/E02 auf definierter Referenzhardware. Änderungen zur Steigerung der Spielstärke werden anhand W01 auf Verständlichkeit geprüft; verbleibende Zielkonflikte werden dokumentiert.

K3 (Maßnahmenwiderspruch) nicht belegt. K5 nicht bewertbar, da alle Risiken `priority=nicht angegeben` tragen.

## Konfliktkarte

| Sektion | Involviert in Konflikten |
|---|---|
| S9 — Entscheidungen | 5 |
| S10 — Qualitätsanforderungen | 5 |
| S4 — Lösungsstrategie | 4 |
| S8 — Konzepte | 4 |
| S11 — Risiken | 3 |
| S1 — Einführung/Ziele | 2 |
| S3 — Kontextabgrenzung | 2 |
| S5 — Bausteinsicht | 2 |
| S2 — Randbedingungen | 1 |

## Zusammenfassung

| Kategorie | Anzahl |
|---|---|
| 🔴 Kritische Befunde | 4 (S8-01, S10-01, S11-01, KRQ-01) |
| 🟡 Warnungen / Empfehlungen | 50 |
| 🟢 Hinweise | 4 |

Die Befunde S8-01, S11-01 und KRQ-01 haben dieselbe Ursache, nämlich die fehlende Stellungs- und Bibliotheksvalidierung gegenüber Z02/F01.

### Handlungsempfehlungen
1. **Validierungslücke schließen:** Entscheiden, ob DokChess unzulässige Stellungen und Bibliothekszüge validiert. Danach 8.4/8.5 anpassen, Z02/F01 abgleichen und ein Risiko in Sektion 11 aufnehmen (S8-01, S11-01, KRQ-01).
2. **Messbare Qualitätsszenarien:** Partienszenario für Spielstärke ergänzen, E01/E02 entflechten und Referenzhardware sowie Teststellungen festlegen (S10-01/02/05, S02-02, S8-03).
3. **Risikobewertung:** Wahrscheinlichkeit, Auswirkung und Priorität ergänzen. Änderbarkeit als Risiko aufnehmen und 11.3 auf alle gefährdeten Ziele ausweiten (S11-02, KRQ-02/03).
4. **Fehlende ADRs:** DI/Zerlegung, Reactive Extensions, Polyglot-Format, DI-Framework-Verzicht und Logging-Verzicht dokumentieren (KSE-01/02, KKE-01/02).
5. **Remisangebote und Endspiele klarstellen:** Umfang in 3.1 und 5.2 abgleichen, Endspiele als Erweiterungsoption kennzeichnen (S03-01, S05-01, KKB-01/02).
6. **Zielnamen und Datierungen bereinigen:** „Attraktive Spielstärke“ auf 1.2 angleichen und ADR-Datum bzw. Messbasis einordnen (S04-01, S09-01/02).
7. **Laufzeitsicht ergänzen:** Abbruch-/Fehlerpfade und Ebene-2-Zusammenspiel aufnehmen (S06-01/02/03, S05-02).
8. **Glossar und Stakeholder nachziehen** (S12-01 bis S12-07, S01-01/02).
