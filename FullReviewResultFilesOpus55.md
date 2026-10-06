# arc42 Dokumentations-Review

**Dokumentation:** `arc-doc/` (DokChess)
**Strukturtyp:** Multi-Folder (Typ A), Sektionen S1–S12 vollständig vorhanden, zusätzlich `00-Ueberblick/`
**Analyse-Modus:** DATEI-MODUS (Analyse direkt auf den Markdown-Dateien, kein Wissensgraph)
**Review-Modus:** Vollständiges Review (alle 12 Sektionen + 7 Konfliktdimensionen)

## Gesamtübersicht

| Sektion | Status | Befunde |
|---------|--------|---------|
| 1. Einführung und Ziele | 🟡 | Kein Verweis auf Anforderungsdokumente, Business-Ziel implizit, Spieler und Frontend-Entwickler fehlen als Stakeholder. |
| 2. Randbedingungen | 🟡 | Hardware-, Windows-, Java- und Lizenzvorgaben unscharf; Konsequenzen/Freiheitsgrade und konkrete Schachformate fehlen. |
| 3. Kontextabgrenzung | 🟡 | Datenflüsse unbeschriftet, Remisangebote widersprechen S5, Endspieldatenbank wirkt wie realisierte Schnittstelle. |
| 4. Lösungsstrategie | 🟡 | Qualitätsziel „Spielstärke“ abweichend benannt; reaktive Ausführung vs. paralleler Minimax unklar abgegrenzt. |
| 5. Bausteinsicht | 🟡 | Remisangebote inkonsistent zu S3; Zuständigkeit für die Eröffnungsbibliothek im Level-2-Diagramm unklar. |
| 6. Laufzeitsicht | 🟡 | Nur Erfolgsszenario; Fehlerpfad und Unterbrechung der Suche fehlen. |
| 7. Verteilungssicht | 🟡 | Motivation, Baustein-Mapping und Bezug zu Performanceszenarien fehlen. |
| 8. Querschnittliche Konzepte | 🟡 | FEN vs. Stellungsmodell, ungeprüfte Eröffnungszüge, pauschale Fehlerfortsetzung; fehlende Verweise auf S5/S9. |
| 9. Architekturentscheidungen | 🟡 | Veraltete Grundlage (Stand 2011) für ADR 9.1; Laufzeitaussage in ADR 9.2 nicht gegen E01/E02 belegt. |
| 10. Qualitätsanforderungen | 🔴 | Spielstärke nicht messbar konkretisiert; Messbedingungen und Akzeptanzkriterien mehrerer Szenarien unbestimmt. |
| 11. Risiken und technische Schulden | 🟡 | Keine Priorisierung, veraltete Risiken, ausgelassene Remisregeln, fehlende Eingabe-/Datenrisiken. |
| 12. Glossar | 🟡 | Zentrale Begriffe (Zug, Stellung, Zugsuche …) fehlen; mehrere Definitionen fachlich ungenau. |

## Sektions-Reviews

### Sektion 1: Einführung und Ziele

Geprüft: [01-01-Aufgabenstellung.md](arc-doc/01-Einfuehrung-und-Ziele/01-01-Aufgabenstellung.md), [01-02-Qualitaetsziele.md](arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md), [01-03-Stakeholder.md](arc-doc/01-Einfuehrung-und-Ziele/01-03-Stakeholder.md)

Qualitätsziele, Priorisierung und Verweis auf Abschnitt 10 sind vorhanden. Die fünf Ziele liegen im vorgegebenen Rahmen; der Qualitätsbaum ordnet ihnen konkrete Szenarien zu.

#### S01-01 Anforderungen nicht auf externe Anforderungen bezogen

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [01-01-Aufgabenstellung.md](arc-doc/01-Einfuehrung-und-Ziele/01-01-Aufgabenstellung.md), Abschnitt „Wesentliche Features“
**Kriterium:** Anforderungsüberblick: Verweise auf bestehende Anforderungsdokumente

**Problem:** Die funktionalen Anforderungen sind knapp aufgelistet, ohne Verweis auf ein zugrunde liegendes Anforderungsdokument. Ob ein solches existiert, ist nicht ersichtlich.

**Änderungsvorschlag:**
> Die Anforderungen sind in diesem Abschnitt zusammengefasst. Weiterführende Anforderungen sind im Dokument „…“ beschrieben.
>
> Falls kein separates Anforderungsdokument existiert: „Ein separates Anforderungsdokument liegt nicht vor; die wesentlichen Anforderungen sind in diesem Abschnitt zusammengefasst.“

#### S01-02 Business-Ziel bleibt implizit

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [01-01-Aufgabenstellung.md](arc-doc/01-Einfuehrung-und-Ziele/01-01-Aufgabenstellung.md), Abschnitt „Was ist DokChess?“
**Kriterium:** Anforderungsüberblick: Business-Ziele hervorheben

**Problem:** Der Zweck als Anschauungsbeispiel wird beschrieben, der Nutzen für Buch, Seminare und Workshops aber nicht als Business-Ziel kenntlich gemacht; dieser Bezug steht erst bei den Stakeholdern.

**Änderungsvorschlag:**
> **Business-Ziel:** DokChess stellt ein verständliches, praxistaugliches Beispiel bereit, mit dem Architekturentwurf und Architekturdokumentation in Buch, Seminaren und Workshops vermittelt werden können.

#### S01-03 Nutzergruppen der Engine fehlen in der Stakeholderliste

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [01-03-Stakeholder.md](arc-doc/01-Einfuehrung-und-Ziele/01-03-Stakeholder.md), Stakeholder-Tabelle
**Kriterium:** Stakeholder: relevante Nutzergruppen und ihre Erwartungen abdecken

**Problem:** Erfasst sind vor allem die Zielgruppe der Dokumentation sowie Autor und Unternehmen. Spielerinnen/Spieler und Entwickler von Schach-Frontends fehlen, obwohl die Aufgabenstellung das Spielen gegen Menschen und die Frontend-Integration nennt.

**Änderungsvorschlag:**
> | Gelegenheitsspielerinnen und -spieler | Möchten gegen DokChess spielen und dabei eine verständliche, angemessene Herausforderung erleben. |
> | Entwicklerinnen und Entwickler von Schach-Frontends | Möchten DokChess mit vertretbarem Aufwand integrieren und über ein unterstütztes Protokoll ansprechen können. |

**Zählung:** 🔴 0 · 🟡 3 · 🟢 0

### Sektion 2: Randbedingungen

Geprüft: [02-01-Technisch.md](arc-doc/02-Randbedingungen/02-01-Technisch.md), [02-02-Organisatorisch.md](arc-doc/02-Randbedingungen/02-02-Organisatorisch.md), [02-03-Konventionen.md](arc-doc/02-Randbedingungen/02-03-Konventionen.md)

Formal gut gegliedert: technische und organisatorische Randbedingungen sowie Konventionen sind getrennt und tabellarisch erläutert. Die Befunde betreffen vor allem unklare Geltungsbereiche und fehlende Konsequenzen.

#### S02-01 Unbestimmte Hardwareanforderung

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [02-01-Technisch.md](arc-doc/02-Randbedingungen/02-01-Technisch.md), „Moderate Hardwareausstattung“
**Kriterium:** Technische Randbedingungen müssen nachvollziehbar und prüfbar sein.

**Problem:** „Marktübliches Standard-Notebook“ legt keine Mindestanforderungen fest; die Vorgabe ist nicht überprüfbar.

**Änderungsvorschlag:**
> | Moderate Hardwareausstattung | Die Lösung muss auf einem Notebook mit mindestens [Prozessormodell oder Leistungsklasse], [Arbeitsspeicher] und [Betriebssystem] lauffähig sein. Die Einhaltung wird anhand des Szenarios [konkretes Ausführungsszenario] geprüft. |

#### S02-02 Windows-Unterstützung nicht eingegrenzt

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [02-01-Technisch.md](arc-doc/02-Randbedingungen/02-01-Technisch.md), „Betrieb auf Windows Desktop Betriebssystemen“
**Kriterium:** Plattform- und Betriebssystemeinschränkungen klar dokumentieren.

**Problem:** Weder Windows-Versionen noch Architektur sind genannt. „Wünschenswert, aber nicht zwingend erforderlich“ lässt offen, ob Linux/macOS getestet werden.

**Änderungsvorschlag:**
> | Betriebssysteme | Verbindlich unterstützt werden Windows [Versionen] in der [32-/64-Bit]-Variante. Linux und macOS sind [nicht unterstützt / unverbindlich lauffähig, aber nicht getestet / ebenfalls getestet]. Die Plattformunterstützung wird durch [Build- und Testverfahren] überprüft. |

#### S02-03 Java-Versionen und Kompatibilitätsziel sind uneindeutig

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [02-01-Technisch.md](arc-doc/02-Randbedingungen/02-01-Technisch.md), „Implementierung in Java“
**Kriterium:** Technische Vorgaben müssen den Lösungsraum erkennbar begrenzen.

**Problem:** Historische Stände (Java SE 6, 7, 11) werden mit dem offenen Ziel „neuere Java-Versionen“ vermischt. Mindestversion und Testmatrix fehlen.

**Änderungsvorschlag:**
> | Implementierung in Java | Die Lösung wird mit Java [Version] entwickelt. Mindestlaufzeit ist Java [Version]; unterstützt und getestet werden Java [Versionen]. Frühere Java-Versionen sind [nicht unterstützt / nur für historische Releases relevant]. |

#### S02-04 Fremdsoftware- und Lizenzvorgabe nicht verbindlich genug

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [02-01-Technisch.md](arc-doc/02-Randbedingungen/02-01-Technisch.md), „Fremdsoftware frei verfügbar“
**Kriterium:** Einschränkungen und ihre Konsequenzen sollen klar sein.

**Problem:** „Sollte idealerweise“ ist nur eine Präferenz; Lizenzkompatibilität zur GPLv3-Veröffentlichung ist nicht geregelt.

**Änderungsvorschlag:**
> | Fremdsoftware und Lizenzen | Abhängigkeiten müssen [kostenlos nutzbar sein / unter einer festgelegten Lizenz stehen]. Ihre Lizenz muss mit der Veröffentlichung unter GPLv3 vereinbar sein. Abweichungen bedürfen einer dokumentierten Freigabe durch [Rolle]. |

#### S02-05 Organisatorische und politische Einschränkungen nicht abgegrenzt

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [02-02-Organisatorisch.md](arc-doc/02-Randbedingungen/02-02-Organisatorisch.md), gesamte Tabelle
**Kriterium:** Organisatorische/politische Constraints berücksichtigen oder ausdrücklich als nicht zutreffend dokumentieren.

**Problem:** Es bleibt offen, ob Vorgaben des Schulungsunternehmens, der Veranstalter oder anderer Systeme fehlen oder nur nicht dokumentiert sind.

**Änderungsvorschlag:**
> Ergänzend gelten folgende organisatorische oder politische Randbedingungen: [Vorgaben]. Sofern keine weiteren Vorgaben bestehen: „Zum Zeitpunkt der Konzeption sind keine zusätzlichen organisatorischen oder politischen Randbedingungen bekannt.“

#### S02-06 Konsequenzen und verbleibende Freiheitsgrade fehlen

**Schwere:** 🟡 Empfehlung
**Fundstelle:** Erläuterungsspalten in allen drei Dateien von S2
**Kriterium:** Konsequenzen der Constraints und Freiheitsgrade erkennbar machen.

**Problem:** Die Erläuterungen geben Hintergründe wieder, aber nicht, welche Entscheidungen festgelegt werden und welche offenbleiben.

**Änderungsvorschlag:**
> Je Randbedingung eine Spalte „Konsequenzen und Freiheitsgrade“ ergänzen. Beispiel: „Die Java-Laufzeit und die unterstützten Betriebssysteme sind verbindlich. Innerhalb dieser Grenzen bleiben die Wahl der Entwicklungsumgebung und die interne Zerlegung der Engine frei.“

#### S02-07 Schachspezifische Standards bleiben unbenannt

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [02-03-Konventionen.md](arc-doc/02-Randbedingungen/02-03-Konventionen.md), „Schach-Spezifische Datenformate“
**Kriterium:** Konventionen müssen konkret anwendbar sein.

**Problem:** „Etablierte Standards“ werden nicht benannt.

**Änderungsvorschlag:**
> | Schachspezifische Datenformate | Für Stellungen wird FEN verwendet, für Partien PGN, für Eröffnungsbibliotheken Polyglot, für die Frontend-Kommunikation XBoard/WinBoard. Eigene Formate werden nur eingeführt, wenn kein geeigneter offener Standard existiert; die Abweichung ist zu begründen. |

#### S02-08 Regel für deutsche Java-Bezeichner ist auslegungsbedürftig

**Schwere:** 🟢 Hinweis
**Fundstelle:** [02-03-Konventionen.md](arc-doc/02-Randbedingungen/02-03-Konventionen.md), „Sprache (Deutsch vs. Englisch)“
**Kriterium:** Namenskonventionen eindeutig formulieren.

**Problem:** Die Ausnahme „es sei denn, die Java-Kodierrichtlinien stehen dem im Wege“ ist nicht konkretisiert.

**Änderungsvorschlag:**
> | Sprache und Bezeichner | Dokumentation und fachliche Bezeichner werden auf Deutsch verfasst. Namen aus Java- und Fremdbibliotheken sowie Bezeichner, die durch externe Protokolle oder Standards vorgegeben sind, werden unverändert übernommen. |

**Zählung:** 🔴 0 · 🟡 7 · 🟢 1

### Sektion 3: Kontextabgrenzung

Geprüft: [03-01-Fachlicher-Kontext.md](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md), [03-02-Technischer-Kontext.md](arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md)

#### S03-01 Fachliche Datenflüsse bleiben unbestimmt

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [03-01-Fachlicher-Kontext.md](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md)
**Kriterium:** Fachliche Ein-/Ausgaben je Kommunikationspartner spezifizieren.

**Problem:** Die Verbindungen im Diagramm sind weder beschriftet noch gerichtet; eine Übersicht der Ein- und Ausgaben fehlt.

**Änderungsvorschlag:**
> | Kommunikationspartner | Eingaben an DokChess | Ausgaben von DokChess |
> | --- | --- | --- |
> | Menschlicher Gegner | Züge des Gegners | Züge von DokChess |
> | Computergegner | Züge des Gegners | Züge von DokChess |
> | Eröffnungsbibliothek | Eröffnungszüge zur aktuellen Stellung | Anfrage mit der aktuellen Stellung |
>
> Verbindungen im Diagramm entsprechend beschriften.

#### S03-02 Fachliche und technische Schnittstellen nur teilweise aufeinander abgebildet

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [03-02-Technischer-Kontext.md](arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md)
**Kriterium:** Fachliche Ein-/Ausgaben auf technische Kanäle abbilden.

**Problem:** Die Kanäle stdin/stdout werden nicht benannt; die Abbildung fachlicher Vorgänge auf XBoard bzw. Polyglot-Datei fehlt.

**Änderungsvorschlag:**
> Die Züge zwischen Gegner und DokChess werden über das textbasierte XBoard-Protokoll ausgetauscht. Ein XBoard-kompatibles Frontend sendet gegnerische Züge an DokChess und empfängt die Züge der Engine über Standardeingabe und Standardausgabe. Eröffnungszüge werden durch lesenden Zugriff auf eine Datei im Polyglot-Format ermittelt.

#### S03-03 Remisangebote sind als Austausch genannt, aber nicht unterstützt

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [03-01-Fachlicher-Kontext.md](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md) ↔ [05-02-XBoard-Protokoll.md](arc-doc/05-Bausteinsicht/05-02-XBoard-Protokoll.md)
**Kriterium:** Fachliche Schnittstellen konsistent zu den Bausteinen beschreiben.

**Problem:** S3 nennt Remisangebote als Austausch, S5 führt sie als nicht unterstütztes Feature (siehe auch S05-01, KKB-01).

**Änderungsvorschlag:**
> „Menschlicher Gegner und DokChess tauschen ihre Züge aus. Remisangebote und deren Annahme oder Ablehnung werden von der aktuellen XBoard-Implementierung nicht unterstützt.“

#### S03-04 Endspieldatenbanken erscheinen im Diagramm als angebundener Partner

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [03-01-Fachlicher-Kontext.md](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md), [03-02-Technischer-Kontext.md](arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md)
**Kriterium:** Systemgrenze eindeutig und konsistent darstellen.

**Problem:** Das fachliche Diagramm zeigt „Endspiele“ ohne Kennzeichnung, der technische Kontext sagt, dass keine Endspieldatenbank angebunden ist.

**Änderungsvorschlag:**
> „Endspieldatenbanken“ im Diagramm als „nicht implementiert / mögliche Erweiterung“ kennzeichnen und gestrichelt darstellen. Im Text ergänzen: „Endspieldatenbanken gehören derzeit nicht zu den angebundenen externen Schnittstellen. Eine spätere Integration ist als Erweiterung möglich.“

#### S03-05 Schnittstellenrisiken sind im Kontext nicht sichtbar

**Schwere:** 🟢 Hinweis
**Fundstelle:** [03-02-Technischer-Kontext.md](arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md)
**Kriterium:** Risiken im Kontext explizit aufzeigen.

**Problem:** Die unvollständige XBoard-Implementierung (keine Zeitkontrolle, keine Remisangebote) ist hier nicht erwähnt.

**Änderungsvorschlag:**
> „Die XBoard-Implementierung unterstützt nicht alle Protokollfunktionen. Insbesondere Zeitkontrolle und Remisangebote werden nicht unterstützt; Frontends oder Einsatzszenarien, die diese Funktionen voraussetzen, sind nur eingeschränkt kompatibel.“

**Zählung:** 🔴 0 · 🟡 4 · 🟢 1

### Sektion 4: Lösungsstrategie

Geprüft: [04-01-Einstieg.md](arc-doc/04-Loesungsstrategie/04-01-Einstieg.md), [04-02-Aufbau.md](arc-doc/04-Loesungsstrategie/04-02-Aufbau.md), [04-03-Spielstrategie.md](arc-doc/04-Loesungsstrategie/04-03-Spielstrategie.md), [04-04-Anbindung.md](arc-doc/04-Loesungsstrategie/04-04-Anbindung.md)

#### S04-01 Qualitätsziel uneinheitlich benannt

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [04-01-Einstieg.md](arc-doc/04-Loesungsstrategie/04-01-Einstieg.md), Tabelle
**Kriterium:** Zuordnung der Lösungsansätze zu den Qualitätszielen aus S1.2

**Problem:** Die Tabelle führt „Attraktive Spielstärke (Attraktivität)“, S1.2 dagegen „Akzeptable Spielstärke (Funktionale Eignung)“.

**Änderungsvorschlag:**
> Tabellenzeile umbenennen in „Akzeptable Spielstärke (Funktionale Eignung)“.

#### S04-02 Reaktive Ausführung und parallele Suche nicht klar abgegrenzt

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [04-01-Einstieg.md](arc-doc/04-Loesungsstrategie/04-01-Einstieg.md), [04-03-Spielstrategie.md](arc-doc/04-Loesungsstrategie/04-03-Spielstrategie.md)
**Kriterium:** Lösungsansätze nachvollziehbar beschreiben

**Problem:** S4.1 nennt Reactive Extensions für „nebenläufige Berechnung“; S4.3 beschreibt die Basis-Minimax-Suche als nicht nebenläufig und parallelen Minimax als Alternative. Unklar ist, worauf sich „nebenläufig“ bezieht (siehe auch KQS-04).

**Änderungsvorschlag:**
> Effizienz-Zeile: „Reactive Extensions führen die Zugsuche nebenläufig zur Protokollverarbeitung aus; gefundene bessere Züge werden als Events gemeldet. Das hält die Engine während der Berechnung ansprechbar.“
>
> In S4.3 ergänzen: „Die reaktive Ausführung ist von einer Parallelisierung innerhalb des Minimax-Algorithmus zu unterscheiden: Die Basisimplementierung sucht sequenziell; paralleler Minimax ist eine separate Alternative.“

**Zählung:** 🔴 0 · 🟡 2 · 🟢 0

### Sektion 5: Bausteinsicht

Geprüft: alle acht Dateien unter [05-Bausteinsicht](arc-doc/05-Bausteinsicht/05-01-Ebene-1.md). Ebene 1, die Verfeinerung der Engine und die Blackbox-Beschreibungen sind vorhanden.

#### S05-01 Remisangebote im Kontext, aber nicht im XBoard-Umfang

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [03-01-Fachlicher-Kontext.md](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md#L13), [05-02-XBoard-Protokoll.md](arc-doc/05-Bausteinsicht/05-02-XBoard-Protokoll.md#L42)
**Kriterium:** Konsistenz der externen Schnittstellen mit Sektion 3

**Problem:** Siehe S03-03 / KKB-01 — gleicher Sachverhalt aus Sicht der Bausteinsicht.

**Änderungsvorschlag:**
> In S3.1: „DokChess übernimmt die Rolle eines der Gegner. Im aktuellen Implementierungsumfang werden Züge über das XBoard-Protokoll ausgetauscht; Remisangebote werden nicht unterstützt (siehe Abschnitt 5.2).“

#### S05-02 Zuständigkeit für die Eröffnungsbibliothek ist in der Whitebox unklar

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [05-06-Ebene-2-Engine.md](arc-doc/05-Bausteinsicht/05-06-Ebene-2-Engine.md#L6), [05-04-Engine.md](arc-doc/05-Bausteinsicht/05-04-Engine.md)
**Kriterium:** Konsistente Verfeinerung und klare Zuständigkeiten

**Problem:** Der Text sagt, die Engine frage zuerst die Eröffnungsbibliothek ab; im Level-2-Diagramm ist die Bibliothek direkt mit „Zugsuche“ verbunden, deren Beschreibung sie nicht nennt.

**Änderungsvorschlag:**
> „Die Abfrage der Eröffnungsbibliothek wird von `DefaultEngine` gesteuert: Sie ruft zunächst `Eroeffnungsbibliothek.liefereZug(Stellung)` auf. Liefert die Bibliothek keinen Zug, startet `DefaultEngine` die Zugsuche. Die Bibliotheksabhängigkeit liegt damit bei `DefaultEngine`, nicht beim Modul `Zugsuche`.“
>
> Diagramm anpassen: Abhängigkeit zur Eröffnungsbibliothek an der Engine-Grenze statt am Modul „Zugsuche“ darstellen.

**Zählung:** 🔴 0 · 🟡 2 · 🟢 0

### Sektion 6: Laufzeitsicht

Geprüft: [06-01-Zugermittlung.md](arc-doc/06-Laufzeitsicht/06-01-Zugermittlung.md). Das Szenario ist schematisch und mit S5 konsistent.

#### S06-01 Fehlerpfad der asynchronen Zugermittlung fehlt

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [06-01-Zugermittlung.md](arc-doc/06-Laufzeitsicht/06-01-Zugermittlung.md)
**Kriterium:** Fehler- und Ausnahmeszenarien

**Problem:** Nur der Erfolgsfall ist dargestellt. Der in S8.5 beschriebene Fehlerpfad (`onError` → `tellusererror` → Weiterarbeit) fehlt.

**Änderungsvorschlag:**
> Szenario „Fehler bei der Zugermittlung“ ergänzen: Während der Engine-Suche tritt ein Fehler auf und wird über `onError` an das XBoard-Protokoll-Subsystem gemeldet. Dieses gibt eine `tellusererror`-Meldung an den Client aus. Anschließend bleibt DokChess für weitere Protokollkommandos verfügbar.

#### S06-02 Unterbrechung der Suche durch einen sofortigen Zug fehlt

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [06-01-Zugermittlung.md](arc-doc/06-Laufzeitsicht/06-01-Zugermittlung.md)
**Kriterium:** Szenarioauswahl; architekturrelevantes Zusammenspiel

**Problem:** Der Text betont die Ansprechbarkeit während der Suche, das Diagramm zeigt aber keine Eingabe während der Suche.

**Änderungsvorschlag:**
> Szenario „Sofortigen Zug während der Suche erzwingen“ ergänzen: Während die Engine Kandidaten liefert, sendet der Client den entsprechenden XBoard-Befehl. Das XBoard-Protokoll-Subsystem beendet die laufende Suche, übernimmt den aktuell besten Zug, führt ihn auf der Engine aus und sendet ihn an den Client.

**Zählung:** 🔴 0 · 🟡 2 · 🟢 0

### Sektion 7: Verteilungssicht

Geprüft: [07-01-Infrastruktur-Windows.md](arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md). Die Ein-PC-Verteilung ist grundsätzlich nachvollziehbar.

#### S07-01 Motivation der Deployment-Struktur nicht explizit

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [07-01-Infrastruktur-Windows.md](arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md), Abschnitt 7.1
**Kriterium:** Motivation der Deployment-Struktur

**Problem:** Der Bezug zu den technischen Randbedingungen (Windows, Standard-Notebook) bleibt implizit.

**Änderungsvorschlag:**
> Die Verteilung auf einem einzelnen Windows-PC folgt den technischen Randbedingungen: DokChess soll auf marktüblichen Standard-Notebooks vorführbar sein und Windows-Desktop-Systeme unterstützen. Arena dient als beispielhaftes Frontend. Die Bereitstellung als JAR mit Startskript ermöglicht den Start der Java-Engine über ein XBoard-kompatibles Frontend.

#### S07-02 Baustein-Mapping nur auf Artefaktebene

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [07-01-Infrastruktur-Windows.md](arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md), Deployment-Diagramm und Absatz „DokChess.jar enthält …“
**Kriterium:** Mapping der Bausteine aus S5 auf Infrastruktur-Elemente

**Problem:** Welche Subsysteme in der JAR laufen und welcher Baustein über stdin/stdout kommuniziert, ist nicht explizit.

**Änderungsvorschlag:**
> **Software-Hardware-Mapping:** Die Subsysteme XBoard-Protokoll, Spielregeln und Engine werden als Java-Klassen aus *DokChess.jar* innerhalb der Java Runtime Environment ausgeführt. Das XBoard-Protokoll kommuniziert über stdin/stdout mit Arena. In der dargestellten Installation ist keine Eröffnungsbibliothek eingebunden.

#### S07-03 Performanceziele ohne Infrastrukturbezug

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [07-01-Infrastruktur-Windows.md](arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md), „Software-Voraussetzungen auf dem PC“; [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md)
**Kriterium:** Qualitäts- und Performance-Merkmale der Infrastruktur

**Problem:** E01/E02 fordern 5 bzw. 10 Sekunden, eine Referenzkonfiguration fehlt.

**Änderungsvorschlag:**
> Die Laufzeitszenarien E01 und E02 sind Zielwerte für den Betrieb auf einem marktüblichen Standard-Notebook unter Windows mit der Referenzkonfiguration [CPU, RAM, Java-Version].

#### S07-04 Geltungsbereich der Umgebungen offen

**Schwere:** 🟢 Hinweis
**Fundstelle:** [07-01-Infrastruktur-Windows.md](arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md), gesamte Datei
**Kriterium:** Dokumentation der Umgebungen

**Problem:** Ob Entwicklungs-/Testumgebungen abweichen, ist nicht angegeben.

**Änderungsvorschlag:**
> Diese Verteilungssicht beschreibt den lokalen Einsatz von DokChess mit einem Windows-Frontend. Separate Entwicklungs- und Testumgebungen sind nicht Gegenstand dieser Darstellung.

#### S07-05 Ungenaue Beschreibung des JAR-Inhalts

**Schwere:** 🟢 Hinweis
**Fundstelle:** [07-01-Infrastruktur-Windows.md](arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md), Absatz „*DokChess.jar* enthält …“
**Kriterium:** Technisch präzise Erklärung der Artefakte

**Problem:** „Kompilierten Java-Quelltext“ vermischt Quelltext und Bytecode.

**Änderungsvorschlag:**
> *DokChess.jar* enthält die kompilierten Java-Klassen sämtlicher Module und alle nötigen Abhängigkeiten („Über-JAR“).

**Zählung:** 🔴 0 · 🟡 3 · 🟢 2

### Sektion 8: Querschnittliche Konzepte

Geprüft: alle sieben Dateien unter [08-Konzepte](arc-doc/08-Konzepte/08-01-Abhaengigkeiten.md). Nachvollziehbar gegliedert, überwiegend konkret, mehrfach mit der Bausteinsicht verknüpft.

#### S08-01 Widerspruch zwischen Domänenmodell und FEN

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [08-02-Domaenenmodell.md](arc-doc/08-Konzepte/08-02-Domaenenmodell.md), [08-07-Testbarkeit.md](arc-doc/08-Konzepte/08-07-Testbarkeit.md)
**Kriterium:** Konzeptuelle Konsistenz des Datenmodells

**Problem:** Die Testbarkeitssektion bezeichnet FEN als vollständige Spielsituation inkl. Halbzug- und Zugnummer; das Stellungsmodell enthält diese Zähler nicht. Offen ist, ob der FEN-Roundtrip verlustfrei ist.

**Änderungsvorschlag:**
> Entweder die Zähler im Stellungsmodell ergänzen oder: „DokChess übernimmt aus FEN nur die für die Zugermittlung verwendeten Stellungsdaten. Halbzug- und Zugzähler werden nicht gespeichert und beim Aufruf von `toString()` nicht verlustfrei zurückgegeben.“

#### S08-02 Gültigkeit von Eröffnungszügen bleibt ungeklärt

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [08-04-Validierung.md](arc-doc/08-Konzepte/08-04-Validierung.md)
**Kriterium:** Validierung; Grenzen des Konzepts

**Problem:** Die Eröffnungsbibliothek prüft ihre Einträge nicht; die Engine könnte einen ungültigen Zug ausgeben. Ein nachgelagerter Legalitätscheck ist nicht beschrieben.

**Änderungsvorschlag:**
> „Jeder aus der Eröffnungsbibliothek gelieferte Zug wird vor der Ausgabe gegen die gültigen Züge der aktuellen Stellung geprüft. Ist er nicht enthalten, wird er verworfen und die Engine ermittelt einen Zug über die Zugsuche.“

#### S08-03 Fehlerbehandlung benennt keine Wiederherstellungsgrenzen

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [08-05-Fehlerbehandlung.md](arc-doc/08-Konzepte/08-05-Fehlerbehandlung.md)
**Kriterium:** Verhalten nach Fehlern

**Problem:** Das XBoard-Subsystem fängt „sämtliche Exceptions“ und arbeitet „normal“ weiter, ohne Aussage zur Konsistenz des Spielzustands nach unerwarteten Fehlern.

**Änderungsvorschlag:**
> „Erwartete, behandelbare Fehler (z. B. ungültiger Zug) lassen den Spielzustand unverändert; DokChess setzt das Spiel fort. Bei unerwarteten Fehlern bricht DokChess die laufende Zugermittlung ab, meldet den Fehler über das XBoard-Protokoll und setzt nur fort, wenn der Spielzustand nachweislich konsistent ist.“

#### S08-04 Bausteinverweise fehlen bei Validierung und Fehlerbehandlung

**Schwere:** 🟢 Hinweis
**Fundstelle:** [08-04-Validierung.md](arc-doc/08-Konzepte/08-04-Validierung.md), [08-05-Fehlerbehandlung.md](arc-doc/08-Konzepte/08-05-Fehlerbehandlung.md)
**Kriterium:** Verknüpfung Bausteine ↔ Konzepte

**Problem:** Genannte Subsysteme sind nicht auf S5 verlinkt.

**Änderungsvorschlag:**
> In 8.4 „Spielregeln-Subsystem“ und „Eröffnungs-Subsystem“ auf `../05-Bausteinsicht/05-03-Spielregeln.md` bzw. `../05-Bausteinsicht/05-05-Eroeffnung.md` verlinken; in 8.5 „XBoard-Subsystem“ und „Engine-Subsystem“ auf `../05-Bausteinsicht/05-02-XBoard-Protokoll.md` bzw. `../05-Bausteinsicht/05-04-Engine.md`.

#### S08-05 Architekturentscheidungen sind nicht mit Sektion 9 verbunden

**Schwere:** 🟢 Hinweis
**Fundstelle:** [08-01-Abhaengigkeiten.md](arc-doc/08-Konzepte/08-01-Abhaengigkeiten.md), [08-06-Logging.md](arc-doc/08-Konzepte/08-06-Logging.md)
**Kriterium:** Abgrenzung Konzepte ↔ Entscheidungen

**Problem:** Verzicht auf DI-Framework und auf internes Logging sind Entscheidungen ohne ADR in S9 (siehe KKE-01).

**Änderungsvorschlag:**
> In S9 ADRs für den Verzicht auf ein DI-Framework und für den Verzicht auf internes Logging/Tracing ergänzen und aus 8.1 bzw. 8.6 darauf verweisen.

**Zählung:** 🔴 0 · 🟡 3 · 🟢 2

### Sektion 9: Architekturentscheidungen

Geprüft: [09-01-Anbindung.md](arc-doc/09-Entscheidungen/09-01-Anbindung.md), [09-02-Stellungsobjekte.md](arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md). Beide ADRs enthalten Titel, Status, Kontext, Entscheidung und Konsequenzen; Alternativen und Abwägungen sind benannt.

#### S09-01 Veraltete Grundlage für den Protokollvergleich

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [09-01-Anbindung.md](arc-doc/09-Entscheidungen/09-01-Anbindung.md)
**Kriterium:** Nachvollziehbarkeit des Entscheidungskontexts

**Problem:** Der Frontend-Vergleich trägt „Stand 2011“, die Entscheidung ist auf den 10.03.2026 datiert. Unklar, ob die Kompatibilitätsdaten zum Entscheidungszeitpunkt noch galten.

**Änderungsvorschlag:**
> **Grundlage des Protokollvergleichs:** Die Frontend-Kompatibilität wurde am [Datum] anhand der Versionen [Versionen] geprüft.
>
> *Falls keine aktuelle Prüfung vorliegt:* „Die Tabelle dokumentiert den historischen Prüfstand von 2011 und belegt keine aktuelle Frontend-Kompatibilität. Die Entscheidung für XBoard priorisiert plattformübergreifende Unterstützung durch frei verfügbare Frontends.“

#### S09-02 Laufzeitaussage ist nicht anhand der Qualitätsszenarien prüfbar

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [09-02-Stellungsobjekte.md](arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md)
**Kriterium:** Begründung der Abwägung

**Problem:** ~30 % Mehrlaufzeit gelten als „innerhalb der Grenzen“, ohne absolute Messwerte, Testumgebung oder Bezug zu E01/E02.

**Änderungsvorschlag:**
> „Im Prototypvergleich für ‚Matt in 3‘ benötigte die unveränderliche Variante [x] s und die veränderliche Variante [y] s auf [Hardware, Java-Version]. Damit wurde Qualitätsszenario [E01/E02] (höchstens [n] s) eingehalten. Die relative Laufzeitdifferenz betrug ca. 30 Prozent.“

**Zählung:** 🔴 0 · 🟡 2 · 🟢 0

### Sektion 10: Qualitätsanforderungen

Geprüft: [10-01-Qualitaetsbaum.md](arc-doc/10-Qualitaetsanforderungen/10-01-Qualitaetsbaum.md), [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md). Der Qualitätsbaum ist strukturiert und ordnet die Ziele aus S1.2 Szenarien zu; Messbarkeit und Wiederholbarkeit sind eingeschränkt.

#### S10-01 Spielstärke ist nicht messbar konkretisiert

**Schwere:** 🔴 Kritisch
**Fundstelle:** [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md), F02–F04; [01-02-Qualitaetsziele.md](arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md)
**Kriterium:** Messbarkeit der Qualitätsszenarien

**Problem:** F02–F04 beschreiben einzelne taktische Situationen, aber keine messbare Spielstärke. „Schwacher Spieler“ ist nicht definiert, Testumfang und Erfolgsquote fehlen. Die Erreichung des Qualitätsziels ist nicht bewertbar (siehe auch KQS-01, S11-05, KRQ-04).

**Änderungsvorschlag:**
> **F05:** DokChess spielt je 20 Partien mit festgelegter Bedenkzeit gegen zwei versionierte Referenzgegner (schwacher Gegner, Gelegenheitsspieler-Niveau). Gegen den schwachen Gegner erzielt DokChess mindestens 70 % der möglichen Punkte, gegen den Gelegenheitsspieler-Gegner zwischen 40 % und 75 %. Referenzgegner, Versionen und Konfiguration werden dokumentiert.

*Schwellenwerte vor Übernahme gegen die gewünschte Spielstärke prüfen.*

#### S10-02 Leistungswerte sind nicht reproduzierbar eingegrenzt

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md), E01–E02
**Kriterium:** Wiederholbare Performance-Messungen

**Problem:** Zeitgrenzen ohne Referenzhardware, Engine-Konfiguration oder repräsentativen Stellungssatz.

**Änderungsvorschlag:**
> „Die Antwortzeiten werden auf einer dokumentierten Referenzplattform mit festgelegter Engine-Konfiguration anhand eines dokumentierten Satzes repräsentativer Stellungen gemessen.“

#### S10-03 Szenarien zur Analysierbarkeit enthalten unbestimmte Kriterien

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md), W01–W03
**Kriterium:** Spezifität und Messbarkeit

**Problem:** W01 „erschließen sich“ ist nicht beobachtbar; W02 „unverzüglich“ und W03 „ohne Umwege“ sind nicht prüfbar (siehe auch KQS-03).

**Änderungsvorschlag:**
> W01: „Nach höchstens 15 Minuten kann die Testperson die zentralen Bausteine und deren Zusammenwirken anhand der Dokumentation korrekt benennen.“
> W02: „Eine Architektin oder ein Architekt findet zu einem zufällig gewählten arc42-Kapitel innerhalb von zwei Minuten ein konkretes Beispiel, ohne fremde Hilfe.“
> W03: Prüfkriterium für das Auffinden des Quelltexts und die Zuordnung zum Modul definieren (z. B. „innerhalb von fünf Minuten“).

#### S10-04 Aufwand von Protokoll- und Strategieerweiterungen bleibt offen

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md), W04, P01
**Kriterium:** Änderungsszenarien mit Aufwandsmetrik

**Problem:** Nur W05 begrenzt den Aufwand; W04 und P01 sind rein qualitativ.

**Änderungsvorschlag:**
> W04/P01 ergänzen: „Die Implementierung und Integration ist für eine erfahrene Java-Entwicklerin oder einen erfahrenen Java-Entwickler innerhalb von höchstens zwei Arbeitstagen möglich; bestehende Klassen bleiben unverändert.“

#### S10-05 Fehlerbehandlung ist nicht hinreichend spezifiziert

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md), Z01–Z02
**Kriterium:** Konkrete Akzeptanzkriterien für Fehlerszenarien

**Problem:** „Fehlerfrei weiter“ und „beendet das Spiel“ lassen offen, wie die Ablehnung erkennbar ist und welcher Zustand garantiert wird.

**Änderungsvorschlag:**
> Z01: „Die Engine weist den Zug mit einer dokumentierten Fehlermeldung zurück, verändert den Spielzustand nicht und nimmt anschließend einen gültigen Zug entgegen.“
> Z02: „Die Engine weist die Stellung mit einer dokumentierten Fehlermeldung zurück, startet keine Zugsuche und beendet die Partie.“

**Zählung:** 🔴 1 · 🟡 4 · 🟢 0

### Sektion 11: Risiken und technische Schulden

Geprüft: [11-01-Frontend.md](arc-doc/11-Risiken/11-01-Frontend.md), [11-02-Aufwand.md](arc-doc/11-Risiken/11-02-Aufwand.md), [11-03-Spielstaerke.md](arc-doc/11-Risiken/11-03-Spielstaerke.md)

#### S11-01 Risiken sind nicht priorisiert

**Schwere:** 🟡 Empfehlung
**Fundstelle:** alle drei Dateien von S11
**Kriterium:** Risiken nach Priorität ordnen

**Problem:** Keine Priorität, Eintrittswahrscheinlichkeit oder Auswirkung.

**Änderungsvorschlag:**
> Für jedes Risiko Priorität, Eintrittswahrscheinlichkeit, Auswirkung, Verantwortliche und Frühindikator ergänzen; Einträge nach Priorität (= Eintrittswahrscheinlichkeit × Auswirkung) sortieren.

#### S11-02 Frontend-Risiko entspricht nicht mehr dem dokumentierten Architekturstand

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [11-01-Frontend.md](arc-doc/11-Risiken/11-01-Frontend.md)
**Kriterium:** Aktualität der Risiken

**Problem:** Der Eintrag behauptet fehlendes Protokollwissen, obwohl XBoard entschieden (ADR 9.1) und implementiert ist.

**Änderungsvorschlag:**
> „Die grundlegende Anbindung ist durch die Implementierung des XBoard-Protokolls adressiert. Verbleibende Risiken betreffen die Kompatibilität mit konkreten Frontends und Protokollvarianten; wir prüfen sie anhand einer festgelegten Liste unterstützter Frontends und dokumentierter Integrationstests.“

#### S11-03 Zeitplan-Risiko bezieht sich auf abgelaufene Termine

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [11-02-Aufwand.md](arc-doc/11-Risiken/11-02-Aufwand.md)
**Kriterium:** Aktuelle Gesamtrisikoanalyse

**Problem:** Auslöser sind Termine aus 2011/2012; aktueller Status fehlt.

**Änderungsvorschlag:**
> „Die ursprünglichen Terminziele (März 2011, Mai 2011, Februar 2012) sind abgelaufen. Der Eintrag wird als historisch markiert; der Aufwand wird anhand des aktuellen Projektstands und des nächsten verbindlichen Meilensteins neu bewertet.“

#### S11-04 Ausgelassene Remisregeln widersprechen dem Vollständigkeitsziel

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [11-02-Aufwand.md](arc-doc/11-Risiken/11-02-Aufwand.md), [05-03-Spielregeln.md](arc-doc/05-Bausteinsicht/05-03-Spielregeln.md)
**Kriterium:** Auswirkungen bekannter Probleme dokumentieren

**Problem:** 50-Züge-Regel und Stellungswiederholung fehlen, angeblich ohne Konsequenzen für die Korrektheit — im Widerspruch zur Forderung vollständiger FIDE-Regeln (eskaliert in KRQ-03).

**Änderungsvorschlag:**
> „Die fehlende 50-Züge-Regel und Stellungswiederholung verhindern derzeit eine vollständige Umsetzung der FIDE-Regeln und können zu falschen Partieergebnissen führen. Wir kennzeichnen dies als technische Schuld, legen Priorität und Termin für die Umsetzung fest und ergänzen Tests für beide Remisbedingungen.“

#### S11-05 Für die Spielstärke fehlt ein überprüfbarer Maßstab

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [11-03-Spielstaerke.md](arc-doc/11-Risiken/11-03-Spielstaerke.md)
**Kriterium:** Konkrete, umsetzbare Maßnahmen

**Problem:** Unklar, wann die Spielstärke unangemessen ist; die Maßnahme legt keinen Abnahmemaßstab fest.

**Änderungsvorschlag:**
> „Vor der Bewertung legen wir messbare Abnahmekriterien fest: einen definierten Testsatz mit erwarteten Ergebnissen, eine Mindestleistung gegen Referenzgegner (siehe F05) sowie die Antwortzeiten aus E01/E02. Wir halten fest, ab welcher Abweichung Gegenmaßnahmen ausgelöst werden.“

#### S11-06 Dokumentierte Eingabe- und Datenrisiken fehlen in der Risikoübersicht

**Schwere:** 🟡 Empfehlung
**Fundstelle:** S11 gesamt; [08-04-Validierung.md](arc-doc/08-Konzepte/08-04-Validierung.md)
**Kriterium:** Risiken aus externen Schnittstellen und Daten

**Problem:** S8.4 dokumentiert Laufzeitfehler durch unzulässige Stellungen und ungültige Züge aus fehlerhaften Eröffnungsbibliotheken; S11 führt diese nicht.

**Änderungsvorschlag:**
> **Risiko: Ungültige Eingaben oder Eröffnungsdaten beeinträchtigen den Spielbetrieb.** Unzulässige Stellungen können Laufzeitfehler auslösen; fehlerhafte Eröffnungsdaten können zu ungültigen Zügen führen. Wir validieren Stellungen beim Aufbau, prüfen jeden Bibliothekszug gegen die gültigen Züge und ergänzen entsprechende Tests.

**Zählung:** 🔴 0 · 🟡 6 · 🟢 0

### Sektion 12: Glossar

Geprüft: [12-01-Einstieg.md](arc-doc/12-Glossar/12-01-Einstieg.md), [12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md). Tabellarisch und weitgehend alphabetisch; Terminologie stellenweise unpräzise.

#### S12-01 Spaltenbezeichnung entspricht nicht dem geforderten Format

**Schwere:** 🟢 Hinweis
**Fundstelle:** [12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md#L3)

**Problem:** Die zweite Spalte heißt „Erklärung“ statt „Definition“.

**Änderungsvorschlag:**
> `| Begriff | Definition |`

#### S12-02 Zentrale Begriffe des Domänenmodells fehlen

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md); [08-02-Domaenenmodell.md](arc-doc/08-Konzepte/08-02-Domaenenmodell.md#L17)

**Problem:** `Zug` und `Stellung` fehlen im Glossar.

**Änderungsvorschlag:**
> `| Stellung | Aktuelle Spielsituation mit Figuren auf dem Brett, dem Spieler am Zug sowie den geltenden Rochade- und en-passant-Rechten. |`
> `| Zug | Aktion eines Spielers, bei der eine Figur von einem Ausgangs- auf ein Zielfeld bewegt wird; Sonderzüge wie Rochade und Umwandlung folgen den jeweiligen Schachregeln. |`

#### S12-03 Die 50-Züge-Regel ist missverständlich beschrieben

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md#L5)

**Problem:** „50 Züge lang“ lässt offen, ob Einzel- oder vollständige Züge gemeint sind.

**Änderungsvorschlag:**
> `| 50-Züge-Regel | Regel, nach der ein Spieler Remis reklamieren kann, wenn in den letzten 50 Zügen beider Spieler weder ein Bauer gezogen noch eine Figur geschlagen wurde. |`

#### S12-04 Beim en-passant-Schlag fehlt die Frist

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md#L10)

**Problem:** Dass der Schlag unmittelbar im folgenden Zug erfolgen muss, fehlt.

**Änderungsvorschlag:**
> `| en passant | Sonder-Schlagzug eines Bauern: Hat ein Bauer von seiner Grundstellung aus zwei Felder vorgezogen und dabei ein Feld übersprungen, auf dem ihn ein gegnerischer Bauer hätte schlagen können, darf dieser ihn unmittelbar im folgenden Zug so schlagen, als wäre er nur ein Feld vorgezogen. |`

#### S12-05 FEN wird zu knapp als Stellungsdarstellung definiert

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md#L12)

**Problem:** FEN kodiert sechs Felder, nicht nur die Figurenaufstellung (vgl. S8.7).

**Änderungsvorschlag:**
> `| FEN | Forsyth-Edwards-Notation: standardisiertes Textformat zur Beschreibung einer Schachstellung. Es kodiert Figurenaufstellung, Spieler am Zug, Rochaderechte, en-passant-Ziel sowie Halbzug- und Zugzähler. |`

#### S12-06 „Einstellen“ ist zu eng definiert

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md#L7)

**Problem:** Beschränkt auf das Ziehen auf ein angegriffenes Feld.

**Änderungsvorschlag:**
> `| Einstellen | Eine Figur einstellen heißt, sie durch einen Zug so preiszugeben, dass der Gegner sie schlagen kann, ohne dafür eine angemessene Gegenleistung zu geben. |`

#### S12-07 Das Endspiel ist ungenau abgegrenzt

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md#L8)

**Problem:** „Wenige Figurenarten“ statt reduzierter Figurenbestand.

**Änderungsvorschlag:**
> `| Endspiel | Phase einer Schachpartie, die typischerweise nach dem Abtausch vieler Figuren beginnt und in der nur noch wenige Figuren auf dem Brett stehen. Eine feste Grenze zwischen Mittel- und Endspiel gibt es nicht. |`

#### S12-08 Minimax lässt die Annahme optimaler Gegenzüge offen

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md#L17)

**Problem:** Auswahlprinzip und begrenzte Suchtiefe fehlen.

**Änderungsvorschlag:**
> `| Minimax-Algorithmus | Suchalgorithmus, der den Zug mit dem besten erwarteten Ergebnis auswählt, unter der Annahme, dass beide Spieler jeweils den für sie besten Zug spielen. DokChess untersucht dazu den Spielbaum bis zu einer festgelegten Suchtiefe und bewertet die erreichten Stellungen. |`

#### S12-09 Alpha-Beta-Suche wird unpräzise als Verbesserung beschrieben

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md#L6)

**Problem:** „Deutliche Verbesserung“ ist unspezifisch.

**Änderungsvorschlag:**
> `| Alpha-Beta-Suche | Verfahren zur Beschleunigung des Minimax-Algorithmus. Es beschneidet Suchzweige, die das Ergebnis nicht mehr beeinflussen können, und liefert bei gleicher Suchtiefe dasselbe Ergebnis wie Minimax. |`

#### S12-10 Die Definition des Spießes trifft das taktische Motiv nicht präzise

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md#L23)

**Problem:** Wertverhältnis der Figuren fehlt.

**Änderungsvorschlag:**
> `| Spieß | Taktisches Motiv, bei dem eine wertvollere gegnerische Figur angegriffen wird und hinter ihr auf derselben Linie, Reihe oder Diagonale eine weniger wertvolle Figur steht. Zieht die vordere Figur aus dem Angriff, kann die dahinterstehende geschlagen werden. |`

#### S12-11 Stellungswiederholung lässt offen, was als gleiche Stellung gilt

**Schwere:** 🟡 Empfehlung
**Fundstelle:** [12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md#L25)

**Problem:** Spieler am Zug, Rochade- und en-passant-Rechte fehlen als Bedingungen.

**Änderungsvorschlag:**
> `| Stellungswiederholung | Regel, nach der ein Spieler Remis reklamieren kann, wenn dieselbe Stellung mindestens zum dritten Mal auftritt. Dafür müssen auch derselbe Spieler am Zug und dieselben Zugmöglichkeiten gelten, einschließlich Rochaderechten und en-passant-Möglichkeit. |`

#### S12-12 Schach960-Eintrag ist grammatikalisch fehlerhaft und ungenau

**Schwere:** 🟢 Hinweis
**Fundstelle:** [12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md#L22)

**Änderungsvorschlag:**
> `| Schach960 | Schachvariante, bei der die Grundstellung der Figuren zufällig aus 960 zulässigen Anordnungen ausgewählt wird. Auch als Fischer-Random-Chess bekannt. |`

#### S12-13 Wichtige Architekturbegriffe fehlen im Glossar

**Schwere:** 🟢 Hinweis
**Fundstelle:** [12-02-Begriffe.md](arc-doc/12-Glossar/12-02-Begriffe.md); [05-05-Eroeffnung.md](arc-doc/05-Bausteinsicht/05-05-Eroeffnung.md), [05-07-Zugsuche.md](arc-doc/05-Bausteinsicht/05-07-Zugsuche.md), [05-08-Stellungsbewertung.md](arc-doc/05-Bausteinsicht/05-08-Stellungsbewertung.md)

**Änderungsvorschlag:**
> `| Eröffnungsbibliothek | Sammlung gespeicherter Eröffnungsstellungen und zugehöriger Züge, aus der eine Engine bekannte Züge abrufen kann. |`
> `| Stellungsbewertung | Funktion, die einer Schachstellung aus Sicht eines Spielers einen Zahlenwert zuordnet. |`
> `| Zugsuche | Verfahren, das mögliche Zugfolgen untersucht und anhand von Stellungsbewertungen einen Zug auswählt. |`

**Zählung:** 🔴 0 · 🟡 10 · 🟢 3

## Sektionsübergreifende Konflikte

| Konfliktdimension | Status | Befunde |
|---|---|---|
| Qualitätsstrang (S1 ↔ S4 ↔ S10) | 🟡 | Spielstärke nicht belegt, Z01/Z02 ohne Ziel/Strategie, W02 unprüfbar, Nebenläufigkeit uneindeutig. |
| Strategie ↔ Entscheidungen (S4 ↔ S9) | 🟡 | Reaktive Zugermittlung und Suchstrategie ohne ADR; Geltungsbereich der Unveränderlichkeit abweichend. |
| Constraint-Compliance (S2 ↔ S4/S8/S9) | 🟡 | ADRs teilweise auf Englisch entgegen der deutschen Dokumentationskonvention. |
| Kontext ↔ Bausteine (S3 ↔ S5) | 🟡 | Remisangebote inkonsistent; Engine-zu-Engine-Fall keiner Schnittstelle eindeutig zugeordnet. |
| Sichten-Konsistenz (S5 ↔ S6 ↔ S7) | 🟢 | Keine Konflikte; Bausteine in allen drei Sichten konsistent. |
| Konzepte ↔ Entscheidungen (S8 ↔ S9) | 🟡 | DI-Verdrahtung ohne ADR; Unveränderlichkeit des gesamten Domänenmodells nicht durch ADR 9.2 gedeckt. |
| Risiken ↔ Qualität (S11 ↔ S1/S10) | 🔴 | Ausgelassene FIDE-Regeln widersprechen S1; Risiken für Analysierbarkeit und Änderbarkeit fehlen. |

### 1. Qualitätsstrang (S1 ↔ S4 ↔ S10)

| Qualitätsziel (S1.2) | Strategieansätze (S4) | Szenarien (S10) | Status |
|---|---|---|---|
| Zugängliches Beispiel (Analysierbarkeit) | arc42-Gliederung, Domänenmodell, deutsche Namen, Javadoc | W01–W03 | ⚠️ W02 nicht messbar |
| Einladende Experimentierplattform (Änderbarkeit) | Schnittstellen, unveränderliche Objekte, DI, Tests | W04–W05, P01 | ✅ |
| Bestehende Frontends nutzen (Interoperabilität) | XBoard, austauschbare Protokollkomponente | K01, P01 | ✅ |
| Akzeptable Spielstärke | Eröffnungsbuch, Minimax, Bewertung, Alpha-Beta | F02–F04 | ⚠️ Nur Einzelmotive |
| Schnelles Antworten (Effizienz) | Reaktive Anbindung, Alpha-Beta, Zeit-Tests | E01–E02 | ✅ |

#### [KQS-01] Szenarien belegen die angestrebte Spielstärke nicht

**Konflikttyp:** K5 · **Schwere:** 🟡 Warnung · **Sektionen:** S1, S4, S10
**Fundstellen:** [01-01-Aufgabenstellung.md](arc-doc/01-Einfuehrung-und-Ziele/01-01-Aufgabenstellung.md), [01-02-Qualitaetsziele.md](arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md), [04-03-Spielstrategie.md](arc-doc/04-Loesungsstrategie/04-03-Spielstrategie.md), [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md) (F02–F04)

**Beschreibung:** F02–F04 prüfen Figurengewinn, Springergabel und Matt in zwei, nicht aber „schwache Gegner sicher schlagen“ bzw. „Gelegenheitsspieler fordern“. S4.3 behauptet dennoch, die Szenarien belegten die Spielstärke.

**Lösungsvorschlag:** Szenario F05 gemäß S10-01 ergänzen und in S4.3 darauf verweisen, statt die Spielstärke allein aus taktischen Einzelszenarien abzuleiten.

#### [KQS-02] Zuverlässigkeitsszenarien ohne Ziel und Strategie im Qualitätsstrang

**Konflikttyp:** K4 · **Schwere:** 🟡 Warnung · **Sektionen:** S1, S4, S10
**Fundstellen:** [01-02-Qualitaetsziele.md](arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md), [04-01-Einstieg.md](arc-doc/04-Loesungsstrategie/04-01-Einstieg.md), [04-02-Aufbau.md](arc-doc/04-Loesungsstrategie/04-02-Aufbau.md), [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md) (Z01–Z02)

**Beschreibung:** Z01/Z02 sind im Qualitätsbaum der Fehlertoleranz zugeordnet, haben aber weder ein Ziel in S1.2 noch eine strategische Antwort in S4.

**Lösungsvorschlag:** Entweder in S1.2 ergänzen „**Kontrollierte Fehlerbehandlung:** Unzulässige Züge und Stellungen werden erkannt und so behandelt, dass kein inkonsistenter Spielzustand entsteht.“ und in S4: „Zugeingaben werden vor der Übernahme in den Spielzustand auf Regelkonformität geprüft. Unzulässige Züge werden abgelehnt; unzulässige Startstellungen führen zu einem kontrollierten Spielabbruch.“ — oder Z01/Z02 im Qualitätsbaum als nachrangige Qualitätsanforderungen außerhalb der Top-Ziele kennzeichnen.

#### [KQS-03] „Unverzüglich“ macht W02 nicht überprüfbar

**Konflikttyp:** K5 · **Schwere:** 🟡 Warnung · **Sektionen:** S1, S4, S10
**Fundstellen:** [01-02-Qualitaetsziele.md](arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md), [04-01-Einstieg.md](arc-doc/04-Loesungsstrategie/04-01-Einstieg.md), [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md) (W02)

**Beschreibung:** Für das höchstpriorisierte Ziel Analysierbarkeit ist W02 ohne Zeitgrenze; die Wirksamkeit der Dokumentationsstrategie ist nicht bewertbar.

**Lösungsvorschlag:**
> **W02:** Eine Architektin oder ein Architekt wählt eines der zwölf arc42-Kapitel zufällig aus und findet ein konkretes Beispiel dafür innerhalb von zwei Minuten in der Dokumentation, ohne fremde Hilfe.

#### [KQS-04] Status der nebenläufigen Zugberechnung bleibt uneindeutig

**Konflikttyp:** K2 · **Schwere:** 🟡 Warnung · **Sektionen:** S4, S10
**Fundstellen:** [04-01-Einstieg.md](arc-doc/04-Loesungsstrategie/04-01-Einstieg.md), [04-03-Spielstrategie.md](arc-doc/04-Loesungsstrategie/04-03-Spielstrategie.md), [04-04-Anbindung.md](arc-doc/04-Loesungsstrategie/04-04-Anbindung.md), [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md) (E01–E02)

**Beschreibung:** S4.1 nennt nebenläufige Berechnung, S4.3 eine nicht nebenläufige Basissuche; offen ist, welche Variante E01/E02 erfüllt.

**Lösungsvorschlag:**
> „Die reaktive Anbindung hält die Kommandoschnittstelle während der Zugberechnung ansprechbar und meldet bessere Zwischenzüge als Events. Die Minimax-Basissuche selbst ist sequenziell. Eine parallele Minimax-Variante ist als austauschbares Beispiel enthalten; sie ist nicht Voraussetzung für die Reaktionsfähigkeit der Schnittstelle.“

**Zählung:** 🔴 0 · 🟡 4 · 🟢 0

### 2. Strategie ↔ Entscheidungen (S4 ↔ S9)

| Strategische Festlegung (S4) | Entscheidung (S9) | Status |
|---|---|---|
| XBoard als Protokoll, alternative Protokolle ergänzbar | ADR 9.1 | ✅ |
| Unveränderliche Stellung | ADR 9.2 | ✅ (Geltungsbereich siehe KSD-03) |
| Minimax, Materialbewertung, Alpha-Beta, paralleler Minimax | — | 🔲 KSD-02 |
| Reaktive Zugermittlung mit Events | — | 🔲 KSD-01 |
| Polyglot Opening Book | — | kein eigenständiger Konflikt |

#### [KSD-01] Reaktive Zugermittlung ohne dokumentierte Architekturentscheidung

**Konflikttyp:** K4 · **Schwere:** 🟡 Warnung · **Sektionen:** S4, S9
**Fundstellen:** [04-01-Einstieg.md](arc-doc/04-Loesungsstrategie/04-01-Einstieg.md) (Effizienz-Zeile), [04-04-Anbindung.md](arc-doc/04-Loesungsstrategie/04-04-Anbindung.md)

**Beschreibung:** S4 beschreibt einen konkreten Architekturansatz (Reactive Extensions), S9 dokumentiert weder Wahl noch Alternativen.

**Lösungsvorschlag:** ADR „9.3 Reaktive Zugermittlung“ ergänzen und aus S4.4 verweisen:
> **Entscheidung:** DokChess ermittelt Züge reaktiv. Während der Zugermittlung bleibt die Engine ansprechbar; neu gefundene bessere Züge werden als Events ausgegeben.
> Alternativen (z. B. synchroner Aufruf, Threads mit Callbacks) sowie Auswirkungen auf Abbruch, Antwortverhalten und Testbarkeit festhalten.

#### [KSD-02] Suchstrategie und Bewertungsansatz ohne dokumentierte ADR

**Konflikttyp:** K4 · **Schwere:** 🟡 Warnung · **Sektionen:** S4, S9
**Fundstellen:** [04-01-Einstieg.md](arc-doc/04-Loesungsstrategie/04-01-Einstieg.md), [04-03-Spielstrategie.md](arc-doc/04-Loesungsstrategie/04-03-Spielstrategie.md)

**Beschreibung:** Die zentrale Abwägung zwischen Spielstärke, Effizienz und Nebenläufigkeit liegt außerhalb der Entscheidungsdokumentation.

**Lösungsvorschlag:** ADR „9.4 Suchstrategie“ ergänzen und aus S4.3 verweisen:
> **Entscheidung:** Die Basis-Engine verwendet Minimax mit fester Suchtiefe und materialbasierter Stellungsbewertung. Alpha-Beta-Suche und paralleler Minimax werden als Varianten zur Verbesserung von Effizienz bzw. Spielstärke betrachtet.

#### [KSD-03] Geltungsbereich der Unveränderlichkeit nicht deckungsgleich

**Konflikttyp:** K4 · **Schwere:** 🟢 Hinweis · **Sektionen:** S4, S9
**Fundstellen:** [04-01-Einstieg.md](arc-doc/04-Loesungsstrategie/04-01-Einstieg.md), [04-02-Aufbau.md](arc-doc/04-Loesungsstrategie/04-02-Aufbau.md), [09-02-Stellungsobjekte.md](arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md)

**Beschreibung:** S4 spricht von Unveränderlichkeit aller fachlichen Klassen, ADR 9.2 entscheidet nur über `Stellung` (vgl. KKE-02).

**Lösungsvorschlag:** Geltungsbereich in ADR 9.2 erweitern oder S4.2 präzisieren: „Die Klasse `Stellung` ist unveränderlich (siehe Entscheidung 9.2). Für weitere fachliche Klassen ist die jeweilige Unveränderlichkeit separat festgelegt.“

**Zählung:** 🔴 0 · 🟡 2 · 🟢 1

### 3. Constraint-Compliance (S2 ↔ S4/S8/S9)

| Constraint (S2) | S4 | S8 | S9 | Status |
|---|---|---|---|---|
| Standard-Notebook | ✅ | ✅ | ✅ | Erfüllt |
| Windows Desktop | ✅ | ✅ | ✅ | Erfüllt |
| Java | ✅ | ✅ | ✅ | Erfüllt |
| Freie Fremdsoftware | — | ✅ | ✅ | Kein Konflikt |
| JUnit-Tests | ✅ | ✅ | — | Erfüllt |
| Deutsche arc42-Terminologie | ✅ | ✅ | ⚠️ | Abweichung (KCC-01) |
| Deutsche Bezeichner | ✅ | ✅ | ✅ | Kein Konflikt |
| Offene Schachformate | ✅ | ✅ | ✅ | Erfüllt |
| Team, Zeitplan, Gradle, VCS, GPLv3 | — | — | — | Nicht behandelt (kein Verstoß) |

#### [KCC-01] ADRs sind nicht durchgängig auf Deutsch dokumentiert

**Konflikttyp:** K3 – Konventions-Verletzung · **Schwere:** 🟡 Warnung · **Sektionen:** S2, S9
**Fundstellen:** [02-03-Konventionen.md](arc-doc/02-Randbedingungen/02-03-Konventionen.md#L7); [09-01-Anbindung.md](arc-doc/09-Entscheidungen/09-01-Anbindung.md#L7) („Context“), [Zeile 46](arc-doc/09-Entscheidungen/09-01-Anbindung.md#L46) („Decision“), [Zeile 54](arc-doc/09-Entscheidungen/09-01-Anbindung.md#L54) („Consequences“); [09-02-Stellungsobjekte.md](arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md#L7)

**Beschreibung:** S2 legt deutsche arc42-Terminologie fest; die ADRs nutzen englische Überschriften, 09-01 zusätzlich englischen Fließtext.

**Lösungsvorschlag:** `Context` → `Kontext`, `Decision` → `Entscheidung`, `Consequences` → `Konsequenzen` in beiden ADRs; englischen Fließtext in 09-01 übersetzen, z. B.:
> Eine zentrale Anforderung ist, dass DokChess mit vorhandenen Schach-Frontends zusammenarbeitet. Das verwendete Kommunikationsprotokoll bestimmt, mit welchen Frontends die Engine kompatibel ist und wie gut sie an zukünftige Schachsoftware angepasst werden kann.

**Zählung:** 🔴 0 · 🟡 1 · 🟢 0

### 4. Kontext ↔ Bausteine (S3 ↔ S5)

| Externer Partner | S3 | S5 | Status |
|---|---|---|---|
| Menschlicher Gegner via XBoard-Client | Züge und Remisangebote | XBoard-Protokoll mit Client | ⚠️ Remisangebote nicht unterstützt |
| Computergegner / andere Engine | Gleicher Austausch | Nur „Client“, Beispiel GUI | ⚠️ Zuordnung offen |
| Polyglot Opening Book | Optional, lesend | Eröffnungs-Subsystem | ✅ |
| Endspieldatenbank | Nicht umgesetzt | Kein Baustein | ✅ |

#### [KKB-01] Remisangebote im Kontext vorgesehen, im Protokoll nicht unterstützt

**Konflikttyp:** K4 – Datenfluss-Inkonsistenz · **Schwere:** 🟡 Warnung · **Sektionen:** S3, S5
**Fundstellen:** [03-01-Fachlicher-Kontext.md](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md#L13), [05-02-XBoard-Protokoll.md](arc-doc/05-Bausteinsicht/05-02-XBoard-Protokoll.md#L42)

**Beschreibung:** Fachlicher Austauschumfang und Protokollunterstützung stimmen nicht überein; betrifft menschlichen und Computergegner.

**Lösungsvorschlag:** S3 präzisieren: „DokChess tauscht mit dem Gegner insbesondere Züge aus. Remisangebote werden in der aktuellen Implementierung nicht unterstützt.“ — oder, falls fachlich gefordert, die Einschränkung in S5.2 entfernen und Remisangebote implementieren/dokumentieren.

#### [KKB-02] Schnittstelle für den Engine-zu-Engine-Fall nicht eindeutig zugeordnet

**Konflikttyp:** K1 · **Schwere:** 🟡 Warnung · **Sektionen:** S3, S5
**Fundstellen:** [03-01-Fachlicher-Kontext.md](arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md#L17), [03-02-Technischer-Kontext.md](arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md#L9), [05-01-Ebene-1.md](arc-doc/05-Bausteinsicht/05-01-Ebene-1.md#L15), [05-02-XBoard-Protokoll.md](arc-doc/05-Bausteinsicht/05-02-XBoard-Protokoll.md#L7)

**Beschreibung:** S3 nennt eine andere Engine als Gegner; S5 kennt nur einen „Client“ mit GUI als Beispiel.

**Lösungsvorschlag:** In S5.2 ergänzen:
> Der XBoard-Client kann neben einer grafischen Oberfläche auch als Vermittler zu einer weiteren XBoard-kompatiblen Engine dienen. In diesem Fall wickelt das XBoard-Protokoll den Nachrichtenaustausch mit der gegnerischen Engine über das Frontend ab.

**Zählung:** 🔴 0 · 🟡 2 · 🟢 0

### 5. Sichten-Konsistenz (S5 ↔ S6 ↔ S7)

| Baustein | S5 | S6 | S7 | Status |
|---|---|---|---|---|
| XBoard-Protokoll | Subsystem | Validiert, fordert Zug an, gibt aus | In `DokChess.jar` | ✅ |
| Spielregeln | Subsystem | Validiert, liefert Kandidaten | In `DokChess.jar` | ✅ |
| Engine | Subsystem, zustandsbehaftet | Ermittelt und führt Zug aus | In `DokChess.jar` | ✅ |
| Eröffnung | Optional | Zuerst abgefragt, im Beispiel ohne Treffer | Deployment ohne Bibliothek | ✅ |
| Zugsuche | Ebene-2-Baustein | Aggregiert in Engine | In `DokChess.jar` | ✅ |
| Stellungsbewertung | Ebene-2-Baustein | Aggregiert in Engine | In `DokChess.jar` | ✅ |

Keine Konflikte festgestellt. Die eingebetteten Diagramme wurden nicht ausgewertet; die Aussagen stützen sich auf den Markdown-Text.

**Zählung:** 🔴 0 · 🟡 0 · 🟢 0

### 6. Konzepte ↔ Entscheidungen (S8 ↔ S9)

| Element | Sektion | Zuordnung |
|---|---|---|
| Abhängigkeiten / DI | S8.1 | ⚠️ Enthält Entscheidung ohne ADR |
| Domänenmodell / Unveränderlichkeit | S8.2 | ⚠️ Geht über ADR 9.2 hinaus |
| Benutzungsoberfläche, Validierung, Fehlerbehandlung, Logging, Testbarkeit | S8.3–S8.7 | ✅ |
| Anbindung an Frontends | S9.1 | ✅ |
| Unveränderlichkeit von `Stellung` | S9.2 | ✅ (begrenzter Umfang) |

#### [KKE-01] DI-Verdrahtung ist als Konzept beschrieben, aber nicht als Entscheidung dokumentiert

**Konflikttyp:** K2/K4 · **Schwere:** 🟡 Warnung · **Sektionen:** S8.1, S9
**Fundstellen:** [08-01-Abhaengigkeiten.md](arc-doc/08-Konzepte/08-01-Abhaengigkeiten.md#L8), [Zeile 12](arc-doc/08-Konzepte/08-01-Abhaengigkeiten.md#L12), [Zeile 15](arc-doc/08-Konzepte/08-01-Abhaengigkeiten.md#L15)

**Beschreibung:** Setter-Injection und Verzicht auf ein DI-Framework sind konkrete Architekturentscheidungen ohne ADR.

**Lösungsvorschlag:** ADR ergänzen:
> **Entscheidung:** DokChess injiziert Abhängigkeiten über Java-Schnittstellen und Setter-Methoden. Ein DI-Framework und annotationsgetriebene Konfiguration werden nicht verwendet. Das Zusammenstecken erfolgt im Glue-Code (Main-Klasse) und in Tests.
> **Begründung:** Die Module bleiben unabhängig von einem konkreten DI-Framework; Erweiterer können eigene Frameworks einsetzen.
> **Konsequenzen:** Die Verdrahtung muss an den Zusammensetzungsstellen explizit gepflegt werden.

#### [KKE-02] Unveränderlichkeit des gesamten Domänenmodells nicht durch ADR 9.2 abgedeckt

**Konflikttyp:** K4 · **Schwere:** 🟡 Warnung · **Sektionen:** S8.2, S9.2
**Fundstellen:** [08-02-Domaenenmodell.md](arc-doc/08-Konzepte/08-02-Domaenenmodell.md#L19), [Zeile 34](arc-doc/08-Konzepte/08-02-Domaenenmodell.md#L34), [09-02-Stellungsobjekte.md](arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md#L9), [Zeile 44](arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md#L44)

**Beschreibung:** S8.2 erklärt alle Domänenobjekte für unveränderlich; ADR 9.2 entscheidet nur über `Stellung`.

**Lösungsvorschlag:** In ADR 9.2 ergänzen:
> **Geltungsbereich:** Die Entscheidung für unveränderliche Objekte gilt für alle Klassen des Domänenmodells, einschließlich `Figur`, `Feld`, `Zug` und `Stellung`.

Alternativ S8.2 präzisieren: „Die Klasse `Figur` ist unveränderlich. Für `Stellung` gilt die in Entscheidung 9.2 festgelegte Unveränderlichkeit.“

**Zählung:** 🔴 0 · 🟡 2 · 🟢 0

### 7. Risiken ↔ Qualität (S11 ↔ S1/S10)

| Qualitätsziel (S1.2) | Bedrohende Risiken (S11) | Status |
|---|---|---|
| Analysierbarkeit | Keine | ⚠️ Lücke (KRQ-01) |
| Änderbarkeit | Nur allgemeiner Aufwand | ⚠️ Lücke (KRQ-02) |
| Interoperabilität | 11.1 Frontend-Anbindung | ✅ |
| Spielstärke | 11.3; 11.2 lässt FIDE-Regeln aus | ❌ Widerspruch (KRQ-03) |
| Effizienz | 11.3 Wartezeiten | ⚠️ Teilweise (KRQ-04) |

#### [KRQ-01] Risiken für die Zugänglichkeit als Architekturbeispiel fehlen

**Konflikttyp:** K1 · **Schwere:** 🟡 Warnung · **Sektionen:** S1, S10, S11
**Fundstellen:** [01-02-Qualitaetsziele.md](arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md#L9), [01-03-Stakeholder.md](arc-doc/01-Einfuehrung-und-Ziele/01-03-Stakeholder.md#L5), [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L12), [11-03-Spielstaerke.md](arc-doc/11-Risiken/11-03-Spielstaerke.md#L5)

**Beschreibung:** Das höchstpriorisierte Ziel hat kein Risiko und keine Gegenmaßnahme in S11.

**Lösungsvorschlag:** S11 ergänzen:
> „Unzureichende Verständlichkeit oder Auffindbarkeit der Architektur und ihrer Dokumentation gefährdet den Nutzen von DokChess als Anschauungsmaterial (W01–W03). Zur Risikominderung prüfen wir die Verständlichkeit in Architektur-Walkthroughs mit Personen aus den Zielgruppen und überarbeiten Stellen, an denen Entwurf, Dokumentation und Implementierung nicht ohne fremde Hilfe nachvollziehbar sind.“

#### [KRQ-02] Risiken für die Änderbarkeit sind nicht konkretisiert

**Konflikttyp:** K1 · **Schwere:** 🟡 Warnung · **Sektionen:** S1, S10, S11
**Fundstellen:** [01-02-Qualitaetsziele.md](arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md#L10), [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L15), [11-02-Aufwand.md](arc-doc/11-Risiken/11-02-Aufwand.md#L3), [11-01-Frontend.md](arc-doc/11-Risiken/11-01-Frontend.md#L3)

**Beschreibung:** W04, W05 und P01 versprechen Erweiterbarkeit; das Risiko zu starker Kopplung ist nicht betrachtet.

**Lösungsvorschlag:** S11 ergänzen:
> „Zu starke Kopplung zwischen Spielregeln, Stellungsrepräsentation, Bewertungsstrategie und Protokoll kann die in W04, W05 und P01 geforderte Erweiterbarkeit verhindern. Zur Risikominderung prototypisieren wir früh den Austausch einer Bewertungsstrategie und die Anbindung eines zusätzlichen Protokolls ohne Änderung bestehenden Codes und erfassen für W05 den Aufwand eines Austauschs der Stellungsrepräsentation.“

#### [KRQ-03] Geplante Ausnahmen widersprechen der vollständigen FIDE-Regelimplementierung

**Konflikttyp:** K3 – Kontraproduktive Maßnahme · **Schwere:** 🔴 Kritisch · **Sektionen:** S1, S10, S11
**Fundstellen:** [01-01-Aufgabenstellung.md](arc-doc/01-Einfuehrung-und-Ziele/01-01-Aufgabenstellung.md#L14), [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L18) (F01), [11-02-Aufwand.md](arc-doc/11-Risiken/11-02-Aufwand.md#L21)

**Beschreibung:** Als Risikominderung sollen 50-Züge-Regel und Stellungswiederholung entfallen — im direkten Widerspruch zur zugesagten vollständigen FIDE-Regelimplementierung. Die Behauptung „keine Konsequenzen für die Korrektheit“ ist unzutreffend, da beide Regeln Partieenden beeinflussen.

**Lösungsvorschlag:** In S11.2 ersetzen durch:
> „Die 50-Züge-Regel und Stellungswiederholung werden als Bestandteil der vollständigen Regelimplementierung umgesetzt und durch Regeltests abgesichert. Wir planen dafür eigene Implementierungs- und Testschritte ein.“

Falls sie ausgeschlossen bleiben: S1.1 auf „Implementierung der FIDE-Schachregeln mit Ausnahme der 50-Züge-Regel und der Stellungswiederholung“ ändern und F01 entsprechend einschränken.

#### [KRQ-04] Maßnahmen sichern Spielstärke und Antwortzeit nicht anhand klarer Kriterien ab

**Konflikttyp:** K2 · **Schwere:** 🟡 Warnung · **Sektionen:** S1, S10, S11
**Fundstellen:** [01-02-Qualitaetsziele.md](arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md#L12), [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L19), [11-03-Spielstaerke.md](arc-doc/11-Risiken/11-03-Spielstaerke.md#L9)

**Beschreibung:** Die Maßnahme (Schachaufgaben als Tests) legt weder ein Gesamtmaß für Spielstärke noch eine Prüfung der Antwortzeiten aus E01/E02 fest.

**Lösungsvorschlag:** Maßnahme in S11.3 ergänzen:
> „Wir definieren einen reproduzierbaren Spielstärke-Benchmark mit festgelegten Referenzgegnern, Bedenkzeiten und einer Mindest-Erfolgsquote. Zusätzlich prüfen automatisierte Tests die Antwortzeiten aus E01 und E02 auf einer festgelegten Referenzumgebung. Abweichungen werden vor einer Live-Demonstration bewertet.“

#### [KRQ-05] Ungültige Startstellungen sind nicht als eigenes Risiko betrachtet

**Konflikttyp:** K4 · **Schwere:** 🟡 Warnung · **Sektionen:** S10, S11
**Fundstellen:** [10-02-Qualitaetsszenarien.md](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md#L25) (Z02), [11-02-Aufwand.md](arc-doc/11-Risiken/11-02-Aufwand.md#L3), [11-01-Frontend.md](arc-doc/11-Risiken/11-01-Frontend.md#L3)

**Beschreibung:** Z02 fordert die Erkennung unzulässiger Startstellungen; S11 betrachtet dieses Risiko an der Systemgrenze nicht (vgl. S11-06).

**Lösungsvorschlag:** S11 ergänzen:
> „Eine unzulässige Startstellung kann bei der Übernahme vom Frontend unentdeckt bleiben und zu einem fehlerhaften Spielverlauf führen. Wir validieren Startstellungen vor Spielbeginn und ergänzen Tests für ungültige Stellungen, die das Spiel kontrolliert beenden (Z02).“

**Zählung:** 🔴 1 · 🟡 4 · 🟢 0

## Konfliktkarte

| Sektion | Involviert in Konflikten |
|---|---|
| S10 — Qualitätsanforderungen | 9 |
| S1 — Einführung/Ziele | 7 |
| S4 — Lösungsstrategie | 7 |
| S9 — Entscheidungen | 6 |
| S11 — Risiken | 5 |
| S3 — Kontextabgrenzung | 2 |
| S5 — Bausteinsicht | 2 |
| S8 — Konzepte | 2 |
| S2 — Randbedingungen | 1 |

## Zusammenfassung

| Kategorie | Anzahl |
|---|---|
| 🔴 Kritische Befunde | 2 |
| 🟡 Warnungen / Empfehlungen | 63 |
| 🟢 Hinweise | 10 |

Davon Sektions-Reviews: 🔴 1 · 🟡 48 · 🟢 9 (58 Befunde); Konfliktanalyse: 🔴 1 · 🟡 15 · 🟢 1 (17 Befunde). Gesamt: 75 Befunde.

### Handlungsempfehlungen

1. **FIDE-Regelumfang klären (🔴 KRQ-03, S11-04):** Entweder 50-Züge-Regel und Stellungswiederholung umsetzen und testen oder die Zusage in S1.1 und F01 ausdrücklich auf den eingeschränkten Regelumfang anpassen; die Aussage „keine Konsequenzen für die Korrektheit“ in S11.2 streichen.
2. **Spielstärke messbar machen (🔴 S10-01, KQS-01, S11-05, KRQ-04):** Szenario F05 mit Referenzgegnern und Erfolgsquote ergänzen, S4.3 und die Maßnahme in S11.3 darauf ausrichten.
3. **Fehlende ADRs ergänzen (KSD-01, KSD-02, KKE-01, S08-05):** Reaktive Zugermittlung, Suchstrategie und DI-Verdrahtung als ADRs in S9 dokumentieren; Geltungsbereich der Unveränderlichkeit in ADR 9.2 klären (KSD-03, KKE-02).
4. **Schnittstellen zwischen S3 und S5 angleichen (S03-03, S05-01, KKB-01, KKB-02, S03-04):** Remisangebote, Engine-zu-Engine-Fall und Endspieldatenbank einheitlich darstellen.
5. **Nebenläufigkeit präzisieren (S04-02, KQS-04):** Reaktive Anbindung und sequenzielle bzw. parallele Suche in S4 klar trennen.
6. **Messbedingungen der Qualitätsszenarien festlegen (S10-02 bis S10-05, KQS-03, S07-03, S09-02):** Referenzumgebung, Zeitgrenzen und beobachtbare Nachbedingungen ergänzen.
7. **Risikoliste aktualisieren (S11-01 bis S11-03, S11-06, KRQ-01, KRQ-02, KRQ-05):** Priorisieren, historische Risiken als erledigt markieren, Risiken für Analysierbarkeit, Änderbarkeit und ungültige Eingaben aufnehmen.
8. **Validierung und Fehlerbehandlung schärfen (S08-02, S08-03, S06-01, S06-02, KQS-02):** Legalitätsprüfung für Eröffnungszüge, Wiederherstellungsgrenzen und Fehler-/Unterbrechungsszenarien in S6 ergänzen.
9. **Randbedingungen präzisieren (S02-01 bis S02-07):** Hardware, Windows-/Java-Versionen, Lizenzen, Formate sowie Konsequenzen und Freiheitsgrade festlegen.
10. **ADR-Sprache und Glossar vereinheitlichen (KCC-01, S12-01 bis S12-13):** ADR-Überschriften eindeutschen, fehlende Begriffe ergänzen und ungenaue Definitionen korrigieren.
