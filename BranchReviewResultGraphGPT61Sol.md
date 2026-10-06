# arc42 Branch-Review

## Überblick

**Branch:** `Konflikt/ADR` (`a0556b0`)
**Basis:** `origin/main` (`2bbef73`), Vergleich `origin/main...HEAD`
**Geänderte Dateien:** 1; keine zusätzlichen uncommitteten Änderungen unter `arc-doc/`.
**Betroffene Sektionen:** S9; S2, S4 und S8 ausschließlich als Änderungskontext.
**Modus:** GRAPH-MODUS und DELTA-MODUS; Dokumentationswurzel `arc-doc/`, Multi-Folder-Layout mit Sektionsordnern S1 bis S12.
**Graph:** [.arc42-graph_demo_results/FullReviewRunGPT61Sol/arc-doc.graphml](.arc42-graph_demo_results/FullReviewRunGPT61Sol/arc-doc.graphml)

Der bereitgestellte Graph war für den unveränderten Bestand aktuell, enthielt die neue ADR aber noch nicht. Ihre Extraktion wurde inkrementell ergänzt, ohne den Bestand neu zu extrahieren. Der aktualisierte Graph enthält 160 Knoten und 471 Kanten, mit `changed=true` und `change_type=added` für ADR 9.3. Die automatische Graphvalidierung meldet 0 Fehler und 0 Warnungen; 58 strukturelle Hinweise zum Bestand sind keine Delta-Befunde. Inferierte Beziehungen wurden für belastbare Befunde anhand der Originalquellen überprüft.

**Gesamtstatus: 🔴** Ein direkt belegter Dokumentationswiderspruch; kein Nachweis eines Implementierungsfehlers. Die fünf Befund-IDs betreffen drei Ursachen.

## Geänderte Dateien

| Datei | Änderungstyp | Sektion |
|---|---|---|
| [arc-doc/09-Entscheidungen/09-03-Brettrepraesentation.md](arc-doc/09-Entscheidungen/09-03-Brettrepraesentation.md) | Added, gesamte Datei (73 Zeilen) | S9 |

## Sektions-Reviews

| Sektion | Status | Befunde |
|---|---|---|
| 9. Architekturentscheidungen | 🟡 | Messbegründung und Abgrenzung zur bisherigen Strategie präzisieren. |

Die neue ADR wurde vollständig geprüft: Titel, datierter Status, Kontext, Alternativen, eindeutige Entscheidung sowie positive und negative Konsequenzen sind vorhanden. Unveränderte ADRs wurden nur als Kontext herangezogen.

### [S09-01] Leistungsbegründung nicht nachvollziehbar

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/09-Entscheidungen/09-03-Brettrepraesentation.md](arc-doc/09-Entscheidungen/09-03-Brettrepraesentation.md#L48)
**Kriterium:** Nachvollziehbare Begründung der Entscheidung.
**Zitat:** „Performance-Messungen haben gezeigt, dass die Zuggeneration mit Bitboards um den Faktor 8-12 schneller ist als mit dem objektorientierten Modell.“

**Befund:** Messhardware, JVM, Teststellungen, Verfahren und Vergleichsbedingungen fehlen. Auch die behauptete zusätzliche Suchtiefe in Zeile 49 lässt sich nicht überprüfen. Dies belegt keine falschen Zahlen. Die pauschale Aussage zum Einsatz in allen leistungsstarken Engines in Zeile 50 ist ebenfalls nicht belegt. Siehe auch KRC-01.

**Änderungsvorschlag:** Die Messbegründung um folgenden Nachweis ergänzen; nicht rekonstruierbare Zahlen als unbestätigt kennzeichnen:
> Messnachweis: TODO – Benchmarkartefakt, Teststellungen, Hardware, Java-/JVM-Version und JVM-Bitness, Messverfahren und Vergleichsbedingungen dokumentieren. Bis dahin sind die Faktoren 8-12 und die zusätzliche Suchtiefe von 2-3 Halbzügen nicht nachvollziehbar belegt. TODO – Die Aussage zum Einsatz in anderen Engines mit Quellen und Versionsangaben belegen oder streichen.

### [S09-02] Grenze zwischen fachlichen Abstraktionen und Interna offen

**Schwere:** 🟡 Empfehlung
**Datei:** [arc-doc/09-Entscheidungen/09-03-Brettrepraesentation.md](arc-doc/09-Entscheidungen/09-03-Brettrepraesentation.md#L53)
**Kriterium:** Abgrenzung und Konsistenz der Architekturentscheidung.
**Zitat:** „Die oeffentlichen Schnittstellen der Module bleiben unveraendert; die Bitboard-Repraesentation ist ein Implementierungsdetail hinter den bestehenden Abstraktionen.“

**Befund:** Die Schnittstellenzusage macht Bitboards mit fachlichen Klassen grundsätzlich vereinbar. Es bleibt jedoch offen, welche Klassen ihre bisherige Rolle behalten und wo Bitboards gekapselt beziehungsweise konvertiert werden. Das ist kein belegter Widerspruch zwischen OO-Abstraktionen und Bitboards. Siehe auch KSE-01.

**Änderungsvorschlag:** Die zugesagte Kapselung konkretisieren, ohne eine unbekannte Umsetzung zu behaupten:
> Die öffentlichen Modulschnittstellen bleiben unverändert. TODO – Festhalten, welche fachlichen Klassen weiterhin als Aufruf- und Rückgabeparameter dienen, in welcher Klasse die Bitboards gespeichert werden und an welcher Grenze eine Umwandlung erforderlich ist.

## Konfliktanalyse

| Konfliktdimension | Status | Befunde |
|---|---|---|
| Strategie ↔ Entscheidungen (S4 ↔ S9), `c-sd` | 🟡 | Geltungsbereich der Lesbarkeitspräferenz gegenüber internen Bitboards unklar. |
| Konzepte ↔ Entscheidungen (S8 ↔ S9), `c-ke` | 🔴 | S8.2 legt intern ein Array fest, ADR 9.3 dagegen Bitboards. |
| Constraint-Compliance (S2 ↔ S4/S8/S9), `c-cc` | 🟡 | Leistungsangaben nicht auf die Hardware-/Java-Randbedingungen bezogen; kein belegter funktionaler Verstoß. |

Alle drei Analysen wurden genau einmal im Delta-Modus durchgeführt. Weitere Dimensionen wurden durch die Änderung in S9 nicht ausgelöst; der übrige Bestand wurde nicht vollständig reviewt.

### Strategie ↔ Entscheidungen

| Strategischer Ansatz | Bewertung gegenüber ADR 9.3 |
|---|---|
| Explizites OO-Domänenmodell | Fachliche Klassen und interne Bitboards können koexistieren. |
| Lesbarkeit vor Effizienz | Reichweite dieser Priorisierung muss präzisiert werden. |
| Effiziente Implementierung des Domänenmodells | Thematisch durch Bitboards konkretisiert; Graphbeziehung ist inferiert. |

### [KSE-01] Lesbarkeitsstrategie nicht gegen Bitboards abgegrenzt

**Konflikttyp:** K3 – Strategische Präzisierung
**Schwere:** 🟡 Warnung
**Betroffene Dateien:** [arc-doc/04-Loesungsstrategie/04-02-Aufbau.md](arc-doc/04-Loesungsstrategie/04-02-Aufbau.md#L20) und [arc-doc/09-Entscheidungen/09-03-Brettrepraesentation.md](arc-doc/09-Entscheidungen/09-03-Brettrepraesentation.md#L44).
**Zitat S4:** „Auch hier ging bei der Implementierung der fachlich motivierten Klasse dazu Lesbarkeit vor Effizienz.“
**Zitat S9:** „DokChess verwendet **Bitboards (Option 2)** als interne Brettrepraesentation.“

**Beschreibung:** Die neue ADR priorisiert intern Effizienz und nennt erhebliche Nachteile für Verständlichkeit und Debugging. S4 beschreibt weiterhin die Lesbarkeitspräferenz bei der Implementierung der Stellung. Wegen der zugesagten unveränderten Schnittstellen ist das nicht zwingend widersprüchlich; eine klare Eingrenzung der bisherigen Aussage fehlt. Siehe auch S09-02.

**Lösungsvorschlag:** S4.2 um eine ausdrücklich abgegrenzte Ausnahme ergänzen:
> Die fachlichen Modulabstraktionen bleiben bestehen. Für die interne Brettrepräsentation legt Entscheidung 9.3 jedoch Bitboards fest und nimmt deren höhere Komplexität zugunsten von Effizienz in Kauf. Die bisherige Aussage zur Lesbarkeitspräferenz gilt daher nicht uneingeschränkt für die interne Brettrepräsentation.

### Konzepte ↔ Entscheidungen

| Beziehung | Bewertung |
|---|---|
| S8.2 interne Brettrepräsentation ↔ ADR 9.3 | Direkter Widerspruch: Array versus Bitboards. |
| S8.7 FEN-basierte Tests ↔ ADR 9.3 | Kein neuer Konflikt: FEN legt die interne Repräsentation nicht fest. |
| ADR 9.2 Unveränderlichkeit ↔ ADR 9.3 | Konsistent: Unveränderlichkeit wird ausdrücklich beibehalten. |

### [KKE-01] S8.2 dokumentiert eine andere interne Brettrepräsentation

**Konflikttyp:** K1 – Direkter Widerspruch
**Schwere:** 🔴 Kritisch
**Betroffene Dateien:** [arc-doc/08-Konzepte/08-02-Domaenenmodell.md](arc-doc/08-Konzepte/08-02-Domaenenmodell.md#L28) und [arc-doc/09-Entscheidungen/09-03-Brettrepraesentation.md](arc-doc/09-Entscheidungen/09-03-Brettrepraesentation.md#L44).
**Zitat S8:** „Vor allem sind das die Figuren auf dem Brett, das intern als zweidimensionales Array (8 x 8) implementiert ist.“
**Zitat S9:** „DokChess verwendet **Bitboards (Option 2)** als interne Brettrepraesentation.“

**Beschreibung:** Beide Aussagen legen die interne Darstellung desselben Bretts unterschiedlich fest. Anders als die abstrakten OO-Schnittstellen ist die konkrete Array-Implementierung mit der verbindlichen Bitboard-Entscheidung nicht vereinbar. Dies ist ein durch die neue ADR eingeführter Dokumentationswiderspruch, kein festgestellter Codefehler. Die Quelle bestätigt die inferierte Graphbeziehung.

**Lösungsvorschlag:** Array- und Null-Belegungsaussagen in S8.2 ersetzen und die dort eingebundene Stellung-Abbildung auf dieselbe Repräsentation bringen:
> Die Klasse Stellung stellt die aktuelle Spielsituation dar. Die Figurenbelegung wird intern gemäß Entscheidung 9.3 durch Bitboards repräsentiert: Jede Figurenart und -farbe wird als 64-Bit-Wert (`long`) gespeichert. Die öffentlichen Modulschnittstellen und die Unveränderlichkeit der Stellung bleiben erhalten. Informationen zu Spieler am Zug, Rochaderechten und en passant gehören weiterhin zur Spielsituation.

### Constraint-Compliance

| Randbedingung | Bewertung gegenüber ADR 9.3 |
|---|---|
| Marktübliches Standard-Notebook | Kein belegter Verstoß; Messhardware nicht angegeben. |
| Implementierung in Java | Java-`long` ist vereinbar; eine funktionale 64-Bit-JVM-Pflicht wird nicht festgelegt. |
| Hardwareabhängige Antwortzeittests | Leistungsfaktoren lassen sich ohne Messbedingungen nicht einordnen. |

### [KRC-01] Leistungsnachweis nicht den Randbedingungen zugeordnet

**Konflikttyp:** K1 – Technische Randbedingung
**Schwere:** 🟡 Warnung
**Betroffene Dateien:** [arc-doc/02-Randbedingungen/02-01-Technisch.md](arc-doc/02-Randbedingungen/02-01-Technisch.md#L7) und [arc-doc/09-Entscheidungen/09-03-Brettrepraesentation.md](arc-doc/09-Entscheidungen/09-03-Brettrepraesentation.md#L48).
**Zitat S2:** „Betrieb der Lösung auf einem marktüblichen Standard-Notebook, um sie im Rahmen von Seminaren und Konferenzen auf einem solchen zeigen zu können.“
**Zitat S9:** „Performance-Messungen haben gezeigt, dass die Zuggeneration mit Bitboards um den Faktor 8-12 schneller ist als mit dem objektorientierten Modell.“

**Beschreibung:** Die neue ADR nennt moderne 64-Bit-JVMs als Annahme, ordnet ihre Messungen aber keinem konkreten Notebook und keiner JVM zu. Damit ist die Übertragbarkeit auf die dokumentierten Betriebsbedingungen offen. Ein Verstoß gegen Java-Kompatibilität oder Hardwareausstattung ist nicht belegt. Gleiche Messbeleg-Ursache wie S09-01; kein zusätzlich nachgewiesenes Laufzeitproblem.

**Lösungsvorschlag:** Den Messnachweis aus S09-01 um die Reichweite der Ergebnisse ergänzen:
> TODO – Prüfen und dokumentieren, ob die Messumgebung die technischen Randbedingungen aus Abschnitt 2.1 erfüllt. Die Leistungsfaktoren gelten ausschließlich für die dokumentierten Messbedingungen; ihre Übertragbarkeit auf andere unterstützte Java-/JVM-Versionen und Hardware ist gesondert nachzuweisen.

## Zusammenfassung

| Kategorie | Anzahl |
|---|---|
| 🔴 Kritische Befunde | 1 |
| 🟡 Warnungen / Empfehlungen | 4 |
| 🟢 Hinweise | 0 |

Die Zahlen zählen Befund-IDs, nicht unabhängige Mängel: **Messnachweis** bündelt S09-01 und KRC-01; **Strategieabgrenzung** bündelt S09-02 und KSE-01; **interne Repräsentation** betrifft KKE-01. Es liegen somit drei Ursachen vor. Allgemeine Graphhinweise wurden nicht als Dokumentationsbefunde gezählt.

### Handlungsempfehlungen

1. S8.2 einschließlich Stellung-Diagramm mit der akzeptierten Bitboard-Entscheidung synchronisieren; bis dahin bleibt die interne Repräsentation widersprüchlich dokumentiert.
2. S4.2 und ADR 9.3 hinsichtlich fachlicher Abstraktionen, interner Bitboards und Lesbarkeitspriorität abgrenzen.
3. Benchmarkbelege und Geltungsbereich nachtragen oder die unbestätigten Leistungszahlen entsprechend kennzeichnen.

Die Dokumentation wurde nicht verändert. Aktualisiert wurden ausschließlich die drei Graphartefakte im angegebenen Ordner; zusätzlich wurde dieser Review-Bericht erstellt.