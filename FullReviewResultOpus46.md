# arc42 Dokumentations-Review

## Gesamtübersicht

| Sektion | Status | Kritisch | Empfehlung | Hinweis | Kurzbefund |
|---------|--------|----------|------------|---------|------------|
| 1. Einführung und Ziele | 🟡 | 0 | 4 | 2 | Stakeholder-Tabelle weicht vom arc42-Template ab; Endanwender-Perspektive fehlt; treibende Kräfte nicht explizit |
| 2. Randbedingungen | 🟢 | 0 | 2 | 3 | Solide Struktur; Konsequenzen/Freiheitsgrade könnten expliziter sein |
| 3. Kontextabgrenzung | 🟡 | 0 | 3 | 4 | Keine Schnittstellentabelle; fehlendes Mapping fachlich↔technisch |
| 4. Lösungsstrategie | 🟡 | 1 | 1 | 3 | Inkonsistente Benennung Qualitätsziel „Spielstärke" (kritisch); fehlende Klammer |
| 5. Bausteinsicht | 🟡 | 0 | 3 | 4 | Keine Begründung der Zerlegung; Tippfehler „Püft" |
| 6. Laufzeitsicht | 🔴 | 1 | 3 | 1 | Nur ein einziges Szenario (kritisch); Fehlerszenarien fehlen |
| 7. Verteilungssicht | 🟡 | 1 | 3 | 2 | Kein Baustein-zu-Infrastruktur-Mapping (kritisch); Eröffnungsbibliothek fehlt |
| 8. Querschnittliche Konzepte | 🟡 | 0 | 6 | 3 | Systematisch fehlende Querverweise zu Sektion 5; Tippfehler |
| 9. Architekturentscheidungen | 🟢 | 0 | 2 | 2 | Nur 2 ADRs; weitere architekturrelevante Entscheidungen ohne ADR |
| 10. Qualitätsanforderungen | 🟡 | 0 | 4 | 2 | Qualitätsbaum nur als Bild; terminologische Abweichung zu S1.2 |
| 11. Risiken und techn. Schulden | 🔴 | 2 | 5 | 1 | Keine Übersichtstabelle (kritisch); technische Schulden nicht dokumentiert (kritisch) |
| 12. Glossar | 🟡 | 1 | 3 | 3 | Zentrale Domänenbegriffe (Stellung, Zug, Figur, Feld) fehlen (kritisch) |

**Legende:** 🟢 = gut, wenige Hinweise | 🟡 = akzeptabel, Verbesserungsbedarf | 🔴 = wesentliche Lücken

---

## Kritische Befunde

Diese Befunde sollten zeitnah behoben werden:

### 1. [S04-01] Inkonsistente Benennung Qualitätsziel „Spielstärke"

**Datei:** `arc-doc/04-Loesungsstrategie/04-01-Einstieg.md`

In der Strategietabelle steht „Attraktive Spielstärke (Attraktivität)" statt „Akzeptable Spielstärke (Funktionale Eignung)" wie in Sektion 1.2. Sowohl der Name als auch das ISO-25010-Merkmal weichen ab.

> **Fix:** In Zeile 9 der Tabelle ändern zu `| Akzeptable Spielstärke (Funktionale Eignung) |`

---

### 2. [S06-01] Nur ein einziges Laufzeitszenario

**Datei:** `arc-doc/06-Laufzeitsicht/`

Die gesamte Laufzeitsicht besteht aus einem einzigen Szenario (Zugermittlung). Fehler-, Start- und Alternativpfad-Szenarien fehlen vollständig.

> **Fix:** Mindestens ein weiteres Szenario ergänzen (z.B. Eröffnungstreffer, ungültiger Zug).

---

### 3. [S07-02] Kein Baustein-zu-Infrastruktur-Mapping

**Datei:** `arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md`

Die vier Subsysteme aus Sektion 5 werden nicht auf die Infrastruktur-Elemente gemappt. Nur „DokChess.jar" und „dokchess.bat" werden genannt.

> **Fix:** Zuordnungstabelle (Baustein → Artefakt → Infrastruktur) ergänzen:
>
> ```markdown
> ### Zuordnung Bausteine zu Infrastruktur
>
> Alle Subsysteme aus der Bausteinsicht Ebene 1 werden gemeinsam in *DokChess.jar* paketiert und laufen in einer einzigen JVM-Instanz auf dem Windows-PC:
>
> | Baustein (Sektion 5) | Deployment-Artefakt | Infrastruktur-Element |
> |---|---|---|
> | XBoard-Protokoll | DokChess.jar | JVM auf Windows-PC |
> | Spielregeln | DokChess.jar | JVM auf Windows-PC |
> | Engine | DokChess.jar | JVM auf Windows-PC |
> | Eröffnung | DokChess.jar | JVM auf Windows-PC |
> ```

---

### 4. [S11-01] Fehlende Risiko-Übersichtstabelle

**Datei:** `arc-doc/11-Risiken/`

Keine konsolidierte Tabelle mit Priorisierung, Eintrittswahrscheinlichkeit, Schadenspotenzial und Status. Für Management-Stakeholder nicht nutzbar.

> **Fix:** Datei `11-00-Uebersicht.md` mit priorisierter Risikotabelle anlegen:
>
> ```markdown
> # Risiken und technische Schulden
>
> ## Übersicht
>
> | ID | Risiko | Eintrittswahrscheinlichkeit | Schadenspotenzial | Priorität | Maßnahmen | Status |
> | --- | --- | --- | --- | --- | --- | --- |
> | 11.1 | Anbindung an das Frontend schlägt fehl | Mittel | Hoch | 1 | Proof of Concept | Umgesetzt |
> | 11.2 | Aufwand der Implementierung zu hoch | Mittel | Hoch | 2 | Scope-Reduktion | Umgesetzt |
> | 11.3 | Erreichen der Spielstärke scheitert | Mittel | Mittel | 3 | Testfälle aus Schachliteratur | Umgesetzt |
> ```

---

### 5. [S11-03] Technische Schulden nicht dokumentiert

**Datei:** `arc-doc/11-Risiken/`

Bewusst nicht implementierte Features (50-Züge-Regel, Stellungswiederholung, Endspieldatenbanken) werden nirgends als technische Schulden klassifiziert.

> **Fix:** Datei `11-04-Technische-Schulden.md` mit Tabelle der bewussten Schulden anlegen:
>
> ```markdown
> # Technische Schulden
>
> ## 11.4 Bewusst in Kauf genommene technische Schulden
>
> | ID | Beschreibung | Auswirkung | Referenz |
> | --- | --- | --- | --- |
> | TS-1 | 50-Züge-Regel nicht implementiert | Keine Erkennung von Remis nach 50 Zügen ohne Bauernzug oder Schlagzug | 11-02-Aufwand.md |
> | TS-2 | Stellungswiederholung nicht implementiert | Keine Erkennung von Remis durch dreifache Stellungswiederholung | 11-02-Aufwand.md |
> | TS-3 | Keine Anbindung von Endspieldatenbanken | Schwächere Spielführung im Endspiel | 03-02-Technischer-Kontext.md |
> | TS-4 | Eröffnungsbibliotheken niedrig priorisiert | Engine muss Eröffnungen selbst berechnen | 11-02-Aufwand.md |
> ```

---

### 6. [S12-01] Zentrale Domänenbegriffe fehlen im Glossar

**Datei:** `arc-doc/12-Glossar/12-02-Begriffe.md`

Die vier Kernklassen des Domänenmodells (Figur, Feld, Zug, Stellung) aus Sektion 8.2 fehlen im Glossar, obwohl sie in der gesamten Dokumentation verwendet werden.

> **Fix:** Vier Einträge alphabetisch einsortieren:
>
> | Feld | Ein Quadrat auf dem Schachbrett, bezeichnet durch Linie (a–h) und Reihe (1–8), z.B. „e4". Kann von maximal einer *Figur* besetzt sein. |
> | Figur | Eine Schachfigur, gekennzeichnet durch Farbe (schwarz oder weiß) und Art (König, Dame, Turm, Läufer, Springer oder Bauer). |
> | Stellung | Die aktuelle Spielsituation auf dem Schachbrett: Welche *Figuren* auf welchen *Feldern* stehen, wer am Zug ist, ob noch *Rochaden* möglich sind und ob *en passant* geschlagen werden kann. Siehe auch *FEN*. |
> | Zug | Die Bewegung einer *Figur* von einem *Feld* zu einem anderen. Spezialfälle sind *Rochade*, *en passant* und *Umwandlung*. |

---

## Sektions-Reviews im Detail

### Sektion 1 — Einführung und Ziele

| ID | Schwere | Kurztitel |
|---|---|---|
| S01-01 | 🟡 Empfehlung | Fehlende Verweise auf existierende Anforderungsdokumente |
| S01-02 | 🟡 Empfehlung | Treibende Kräfte und Business-Ziele nicht explizit hervorgehoben |
| S01-03 | 🟢 Hinweis | Qualitätsziele ohne zugeordnete Kurzszenarien |
| S01-04 | 🟡 Empfehlung | Stakeholder-Tabelle weicht vom arc42-Template ab (3 Spalten empfohlen) |
| S01-05 | 🟡 Empfehlung | Fehlende Stakeholder-Gruppe: Endanwender (Schachspieler) |
| S01-06 | 🟢 Hinweis | Kein Verweis von Stakeholder-Erwartungen auf Qualitätsziele |

**Gesamtbewertung:** Solide Grundlage. Aufgabenstellung, Qualitätsziele und Stakeholder sind vorhanden und nachvollziehbar. Verbesserungspotenzial bei Tabellenstruktur und Vollständigkeit der Stakeholder.

---

### Sektion 2 — Randbedingungen

| ID | Schwere | Kurztitel |
|---|---|---|
| S02-01 | 🟢 Hinweis | Tippfehler „Schulungsunternehmenin" |
| S02-02 | 🟡 Empfehlung | Fehlende Darstellung von Freiheitsgraden und Konsequenzen |
| S02-03 | 🟡 Empfehlung | Technische Constraints ohne Design-/Architekturvorgaben |
| S02-04 | 🟢 Hinweis | Fehlende Einleitung / Überblick für Sektion 2 |
| S02-05 | 🟢 Hinweis | Fehlender Bezug zu Constraints durch das XBoard-Protokoll |

**Gesamtbewertung:** Gut aufgebaut mit klarer Kategorisierung. Hauptverbesserungspotenzial bei expliziten Konsequenzen der Constraints.

---

### Sektion 3 — Kontextabgrenzung

| ID | Schwere | Kurztitel |
|---|---|---|
| S03-01 | 🟡 Empfehlung | Fehlende Schnittstellentabelle im fachlichen Kontext |
| S03-02 | 🟡 Empfehlung | Fehlende explizite Datenflüsse im fachlichen Kontext |
| S03-03 | 🟡 Empfehlung | Fehlendes Mapping zwischen fachlichem und technischem Kontext |
| S03-04 | 🟢 Hinweis | Kommunikationskanal für XBoard nicht beschrieben |
| S03-05 | 🟢 Hinweis | Computergegner fehlt im technischen Kontext |
| S03-06 | 🟢 Hinweis | Keine Qualitätsanforderungen an Schnittstellen |
| S03-07 | 🟢 Hinweis | Konsistenzcheck Bausteinsicht — konsistent, kein Handlungsbedarf |

**Gesamtbewertung:** Keine kritischen Befunde. Beide Kontexte vorhanden mit Diagrammen. Empfehlungen betreffen strukturierte Tabellen und Mapping.

---

### Sektion 4 — Lösungsstrategie

| ID | Schwere | Kurztitel |
|---|---|---|
| S04-01 | 🔴 Kritisch | Inkonsistente Benennung des Qualitätsziels „Spielstärke" |
| S04-02 | 🟡 Empfehlung | Fehlende schließende Klammer im Markdown-Link |
| S04-03 | 🟢 Hinweis | Fehlende organisatorische Entscheidungen |
| S04-04 | 🟢 Hinweis | Kein expliziter Verweis auf S8 in der Einstiegstabelle |
| S04-05 | 🟢 Hinweis | Fehlende Begründung für Sprachwahl Deutsch |

**Gesamtbewertung:** Gut strukturiert und kompakt. Die Zuordnung Qualitätsziele→Lösungsansätze ist ein Pluspunkt. Der Namenskonflikt bei „Spielstärke" ist zeitnah zu beheben.

---

### Sektion 5 — Bausteinsicht

| ID | Schwere | Kurztitel |
|---|---|---|
| S05-01 | 🟡 Empfehlung | Fehlende Begründung der Zerlegung auf Ebene 1 |
| S05-02 | 🟡 Empfehlung | Fehlende Zuordnung externer Schnittstellen aus dem Kontext |
| S05-03 | 🟢 Hinweis | Endspiele aus dem Kontext nicht in Bausteinsicht adressiert |
| S05-04 | 🟢 Hinweis | Tippfehler „Püft" statt „Prüft" |
| S05-05 | 🟡 Empfehlung | Fehlende Begründung der Zerlegung auf Ebene 2 (Engine) |
| S05-06 | 🟢 Hinweis | Tabellenunterschriften als Tabellenzeilen formatiert |
| S05-07 | 🟢 Hinweis | Referenz nur auf S3.2, fachlicher Kontext (S3.1) fehlt |

**Gesamtbewertung:** Gut strukturiert und hierarchisch aufgebaut. Keine kritischen Mängel. Empfehlungen betreffen Begründungen der Zerlegung.

---

### Sektion 6 — Laufzeitsicht

| ID | Schwere | Kurztitel |
|---|---|---|
| S06-01 | 🔴 Kritisch | Nur ein einziges Laufzeitszenario |
| S06-02 | 🟡 Empfehlung | Fehler-/Ausnahmeszenario fehlt |
| S06-03 | 🟡 Empfehlung | Ebene-2-Bausteine nicht explizit im Szenario benannt |
| S06-04 | 🟡 Empfehlung | Erfolgreicher Eröffnungsbibliothek-Pfad nicht gezeigt |
| S06-05 | 🟢 Hinweis | Begriffliche Inkonsistenz „Reactive Extensions" vs. Bausteinsicht |

**Gesamtbewertung:** Das vorhandene Szenario ist gut beschrieben. Hauptdefizit ist die geringe Anzahl — mindestens ein bis zwei weitere Szenarien nötig.

---

### Sektion 7 — Verteilungssicht

| ID | Schwere | Kurztitel |
|---|---|---|
| S07-01 | 🟡 Empfehlung | Fehlende Motivation / Begründung der Deployment-Struktur |
| S07-02 | 🔴 Kritisch | Unvollständiges Software-Hardware-Mapping |
| S07-03 | 🟡 Empfehlung | Fehlende Beschreibung weiterer Umgebungen |
| S07-04 | 🟡 Empfehlung | Fehlende Beschreibung der Kommunikationskanäle |
| S07-05 | 🟢 Hinweis | Fehlende Qualitäts-/Performance-Merkmale der Infrastruktur |
| S07-06 | 🟢 Hinweis | Keine Infrastrukturebene 2 — bei einfachem Desktop-Deployment akzeptabel |

**Gesamtbewertung:** Grundlegendes Deployment korrekt beschrieben. Kritischste Lücke ist das fehlende Baustein-zu-Infrastruktur-Mapping.

---

### Sektion 8 — Querschnittliche Konzepte

| ID | Schwere | Kurztitel |
|---|---|---|
| S08-01 | 🟡 Empfehlung | Fehlende Querverweise von 08-01 (Abhängigkeiten) zu Bausteinen in S5 |
| S08-02 | 🟡 Empfehlung | Fehlende Querverweise von 08-02 (Domänenmodell) zu Bausteinen in S5 |
| S08-03 | 🟡 Empfehlung | Fehlende Hyperlinks zu Subsystemen in 08-04 (Validierung) |
| S08-04 | 🟡 Empfehlung | Fehlende Hyperlinks zu Subsystemen in 08-05 (Fehlerbehandlung) |
| S08-05 | 🟡 Empfehlung | Keine Verweise auf Bausteine in 08-06 (Logging) |
| S08-06 | 🟡 Empfehlung | Fehlende Querverweise in 08-07 (Testbarkeit) zu S5 und Konzept 8.1 |
| S08-07 | 🟢 Hinweis | Tippfehler „inder Regel" in 08-03 |
| S08-08 | 🟢 Hinweis | Fehlende schließende Klammer in 08-05 |
| S08-09 | 🟢 Hinweis | 08-06 Logging: Abgrenzung Konzept vs. Entscheidung unklar |

**Gesamtbewertung:** 7 relevante Konzepte gut strukturiert. Hauptschwäche: systematisch fehlende Rückverweise zu Sektion 5.

---

### Sektion 9 — Architekturentscheidungen

| ID | Schwere | Kurztitel |
|---|---|---|
| S09-01 | 🟡 Empfehlung | Veraltete Evaluationsbasis in ADR 09-01 (Stand 2011) |
| S09-02 | 🟢 Hinweis | Prototyp-Testbedingungen nicht dokumentiert |
| S09-03 | 🟡 Empfehlung | Geringe Abdeckung architekturrelevanter Entscheidungen (nur 2 ADRs) |
| S09-04 | 🟢 Hinweis | Konsequenzen-Kategorie „neutral" nicht explizit benannt in 09-02 |

**Gesamtbewertung:** Beide vorhandenen ADRs sind formal solide. Hauptdefizit: Zu wenige ADRs — weitere Entscheidungen (Reactive Extensions, Suchalgorithmus, DI) verdienen eigene ADRs.

---

### Sektion 10 — Qualitätsanforderungen

| ID | Schwere | Kurztitel |
|---|---|---|
| S10-01 | 🟡 Empfehlung | Qualitätsbaum nur als Bild ohne textuelle Entsprechung |
| S10-02 | 🟡 Empfehlung | ID-Präfix-Konvention nur mit einem Beispiel erklärt |
| S10-03 | 🟡 Empfehlung | Terminologische Abweichung zwischen S1.2 und S10.2 |
| S10-04 | 🟢 Hinweis | Szenarien ohne explizite Quelle/Stimulus/Metrik-Trennung |
| S10-05 | 🟡 Empfehlung | Einzelne Szenarien mit unzureichend messbaren Akzeptanzkriterien (W02 „unverzüglich") |
| S10-06 | 🟢 Hinweis | Zuverlässigkeitsszenarien Z01/Z02 nicht in Qualitätszielen verankert |

**Gesamtbewertung:** Alle Qualitätsziele aus S1.2 werden durch Szenarien abgedeckt. Hauptverbesserung: textuelle Aufbereitung des Qualitätsbaums und Terminologie-Konsistenz.

---

### Sektion 11 — Risiken und technische Schulden

| ID | Schwere | Kurztitel |
|---|---|---|
| S11-01 | 🔴 Kritisch | Fehlende Übersichtstabelle der Risiken |
| S11-02 | 🟡 Empfehlung | Keine Priorisierung der Risiken |
| S11-03 | 🔴 Kritisch | Technische Schulden nicht dokumentiert |
| S11-04 | 🟡 Empfehlung | Fehlende Risikoanalyse der Java-Plattformwahl |
| S11-05 | 🟡 Empfehlung | Keine Risikoanalyse externer Schnittstellen jenseits Frontend |
| S11-06 | 🟡 Empfehlung | Fehlende Risiken zu Analysierbarkeit und Änderbarkeit |
| S11-07 | 🟢 Hinweis | Veraltete Zeitreferenzen (2011) |
| S11-08 | 🟡 Empfehlung | Fehlende Statusangaben zu den Risiken |

**Gesamtbewertung:** Die drei projektspezifischen Risiken sind gut beschrieben. Kritische Lücken: fehlende Übersichtstabelle und fehlende technische Schulden.

---

### Sektion 12 — Glossar

| ID | Schwere | Kurztitel |
|---|---|---|
| S12-01 | 🔴 Kritisch | Zentrale Domänenbegriffe (Figur, Feld, Zug, Stellung) fehlen |
| S12-02 | 🟡 Empfehlung | Alphabetische Sortierung falsch bei „en passant" |
| S12-03 | 🟡 Empfehlung | Begriff „Spielbaum" fehlt |
| S12-04 | 🟢 Hinweis | Grammatikfehler „bei die Anfangsstellung" |
| S12-05 | 🟡 Empfehlung | Begriff „Eröffnungsbibliothek" fehlt als eigenständiger Eintrag |
| S12-06 | 🟢 Hinweis | Begriff „UCI" fehlt als Gegenstück zu „XBoard-Protokoll" |
| S12-07 | 🟢 Hinweis | Externer Link auf FIDE-Regeln über HTTP statt HTTPS |

**Gesamtbewertung:** Grundsätzlich vorhanden und gut strukturiert. Kritischste Lücke: Domänenbegriffe aus dem Domänenmodell fehlen.

---

## Empfehlungen

### Struktur und Vollständigkeit
- **[S01-04]** Stakeholder-Tabelle auf drei Spalten umstellen (Rolle, Kontakt, Erwartung an Architektur)
- **[S01-05]** Endanwender (Schachspieler) als Stakeholder-Gruppe ergänzen
- **[S03-01]** Schnittstellentabelle im fachlichen Kontext ergänzen
- **[S03-03]** Mapping-Tabelle fachlicher↔technischer Kontext ergänzen
- **[S05-01]** Begründung der Zerlegung auf Ebene 1 ergänzen
- **[S05-05]** Begründung der Zerlegung auf Ebene 2 (Engine) ergänzen
- **[S10-01]** Qualitätsbaum zusätzlich als Text/Tabelle darstellen (nicht nur Bild)
- **[S11-02]** Risiken mit Eintrittswahrscheinlichkeit und Schadenspotenzial priorisieren
- **[S11-08]** Statusangaben (offen/mitigiert/geschlossen) zu allen Risiken ergänzen

### Konsistenz und Querverweise
- **[S08-01 bis S08-06]** Systematisch Hyperlinks von Konzepten zu Bausteinen in Sektion 5 ergänzen (6 Befunde)
- **[S10-02]** ID-Präfixe aller Szenariokategorien aufschlüsseln (nicht nur „W")
- **[S10-03]** Terminologische Zuordnung S1.2 ↔ S10 explizit machen

### Inhaltliche Vertiefung
- **[S06-02]** Fehler-/Ausnahmeszenario ergänzen (ungültiger Zug)
- **[S06-03]** Ebene-2-Bausteine (Zugsuche, Stellungsbewertung) im Szenario namentlich benennen
- **[S09-03]** Weitere ADRs für architekturrelevante Entscheidungen (Reactive Extensions, Suchalgorithmus, DI)
- **[S07-03]** Weitere Umgebungen (Entwicklung, andere Betriebssysteme) beschreiben

### Formale Korrekturen
- **[S05-04]** Tippfehler „Püft" → „Prüft" in `05-03-Spielregeln.md`
- **[S08-07]** Tippfehler „inder Regel" → „in der Regel" in `08-03-Benutzungsoberflaeche.md`
- **[S04-02]** Fehlende schließende Klammer in `04-02-Aufbau.md`
- **[S08-08]** Fehlende schließende Klammer in `08-05-Fehlerbehandlung.md`
- **[S12-02]** Alphabetische Sortierung korrigieren (en passant vor Endspiel)
- **[S12-04]** Grammatikfehler „bei die Anfangsstellung" → „bei der die Anfangsstellung"

---

## Sektionsübergreifende Konflikte

| Konfliktdimension | Status | Befunde |
|---|---|---|
| Qualitätsstrang (S1↔S4↔S10) | ⚠️ | 2 Warnungen, 3 Hinweise |
| Strategie↔Entscheidungen (S4↔S9) | ⚠️ | 3 Warnungen, 3 Hinweise |
| Constraint-Compliance (S2↔S4/S8/S9) | ✅ | 1 Warnung, 1 Hinweis |
| Kontext↔Bausteine (S3↔S5) | ⚠️ | 2 Warnungen, 2 Hinweise |
| Sichten-Konsistenz (S5↔S6↔S7) | ⚠️ | 3 Warnungen, 2 Hinweise |
| Konzepte↔Entscheidungen (S8↔S9) | ⚠️ | 2 Warnungen, 2 Hinweise |
| Risiken↔Qualität (S11↔S1/S10) | ⚠️ | 4 Warnungen, 1 Hinweis |

---

### Qualitätsstrang (S1 ↔ S4 ↔ S10)

#### [KQS-01] Inkonsistente Benennung des Qualitätsziels „Spielstärke"

**Konflikttyp:** K2 — Widersprüchliche Ansätze
**Schwere:** 🟡 Warnung
**Betroffene Dateien:**
- `01-02-Qualitaetsziele.md` — „**Akzeptable** Spielstärke (**Funktionale Eignung**)"
- `04-01-Einstieg.md` — „**Attraktive** Spielstärke (**Attraktivität**)"

**Beschreibung:** Doppelter Widerspruch — sowohl semantisch („akzeptabel" vs. „attraktiv") als auch bei der ISO-25010-Zuordnung.

**Lösungsvorschlag:** In `04-01-Einstieg.md` an S1.2 angleichen: `| Akzeptable Spielstärke (Funktionale Eignung) |`

#### [KQS-02] Verwaiste Szenarien Z01 und Z02

**Konflikttyp:** K4 — Szenarien ohne strategische Grundlage
**Schwere:** 🟡 Warnung
**Betroffene Dateien:**
- `10-02-Qualitaetsszenarien.md` — Z01, Z02 (Zuverlässigkeit)
- `01-02-Qualitaetsziele.md` — kein Qualitätsziel für Zuverlässigkeit

**Beschreibung:** Die Szenarien Z01/Z02 betreffen Zuverlässigkeit, die in S1.2 kein Qualitätsziel hat und in S4 keine Strategie besitzt.

**Lösungsvorschlag:** Entweder ein Qualitätsziel ergänzen oder in S10 als „ergänzende Szenarien ohne Verankerung in den Top-Qualitätszielen" kennzeichnen.

#### [KQS-03] Prioritätsumkehr bei Szenarioanzahl

**Schwere:** 🟢 Hinweis

Das viertpriorisierte Ziel „Funktionale Eignung" hat mit 4 Szenarien die höchste Abdeckung. Erläuternden Absatz in S10.2 ergänzen.

#### [KQS-04] Szenario W02 ohne messbares Akzeptanzkriterium

**Schwere:** 🟢 Hinweis

„findet ihn unverzüglich" → „findet ihn innerhalb von einer Minute" konkretisieren.

#### [KQS-05] Trade-off Verständlichkeit vs. Effizienz nur in Strategie-Detail

**Schwere:** 🟢 Hinweis

Zielkonflikt fehlt in der Strategieübersichtstabelle. Expliziten Absatz „Zielkonflikte" ergänzen.

---

### Strategie ↔ Entscheidungen (S4 ↔ S9)

#### [KSE-01] Fehlende Entscheidung zur Wahl der Programmiersprache Java
**Schwere:** 🟡 Warnung — Java wird als Hebel für zwei Qualitätsziele genutzt, ohne ADR.

#### [KSE-02] Fehlende Entscheidung zum Suchalgorithmus (Minimax/Alpha-Beta)
**Schwere:** 🟡 Warnung — Zentrale architektonische Entscheidung ohne ADR.

#### [KSE-03] Fehlende Entscheidung zum reaktiven Ansatz (Reactive Extensions)
**Schwere:** 🟡 Warnung — Spezifisches Architekturmuster prominent in S4, ohne ADR.

#### [KSE-04] Fehlende Entscheidung zum Eröffnungsbibliotheksformat
**Schwere:** 🟢 Hinweis — Geringere Tragweite, Austauschbarkeit bereits architektonisch verankert.

#### [KSE-05] Fehlende Entscheidung zur Design-Philosophie „Lesbarkeit vor Effizienz"
**Schwere:** 🟢 Hinweis — Grundlegendes Designprinzip, indirekt durch ADR 09-02 gestützt.

#### [KSE-06] Fehlende Entscheidung zu Dependency Injection
**Schwere:** 🟢 Hinweis — Etabliertes Muster, in Konzept 8.1 erläutert.

**Gesamtbewertung:** Von 8 strategischen Festlegungen sind nur 2 durch formale ADRs unterlegt. Keine Widersprüche, aber signifikante Dokumentationslücken.

---

### Constraint-Compliance (S2 ↔ S4/S8/S9)

#### [KRC-01] Englische Strukturüberschriften in Architekturentscheidungen

**Schwere:** 🟡 Warnung

Die ADRs verwenden englische Überschriften (Status, Context, Decision, Consequences), obwohl die Sprachkonvention Deutsch vorsieht.

**Lösungsvorschlag:** Überschriften verdeutschen: Context → Kontext, Decision → Entscheidung, Consequences → Konsequenzen.

#### [KRC-02] ADR-Format weicht von arc42-v6.0-Konvention ab
**Schwere:** 🟢 Hinweis — MADR-Format statt arc42-v6.0-Stil. Konvention sollte das erlaubte Format explizit benennen.

**Gesamtbewertung:** Alle 15 technischen und organisatorischen Constraints werden eingehalten. Nur formale Konventionsabweichungen in S9.

---

### Kontext ↔ Bausteine (S3 ↔ S5)

#### [KKB-01] Computergegner im fachlichen Kontext fehlt in der Bausteinsicht
**Schwere:** 🟡 Warnung — S3.1 führt den Computergegner als separaten Partner, S5.2 spricht nur von „Client".

**Lösungsvorschlag:** In `05-02-XBoard-Protokoll.md` ergänzen: „…einer grafischen Oberfläche oder einer anderen Schach-Engine…"

#### [KKB-02] Endspiele ohne Entsprechung in der Bausteinsicht
**Schwere:** 🟢 Hinweis — Bewusster Verzicht in S3.2, aber nicht in S5 vermerkt.

#### [KKB-03] Terminologie-Unterschied: „Eröffnungen" (Plural) vs. „Eröffnung" (Singular)
**Schwere:** 🟢 Hinweis — Kein zwingender Handlungsbedarf.

#### [KKB-04] Remisangebote im Kontext genannt, in S5 explizit nicht unterstützt
**Schwere:** 🟡 Warnung — Fachlicher Kontext suggeriert Austausch von Remisangeboten, S5.2 listet dies als „nicht unterstützt".

**Lösungsvorschlag:** Im fachlichen Kontext den Verzicht benennen oder den beispielhaften Charakter stärker hervorheben.

---

### Sichten-Konsistenz (S5 ↔ S6 ↔ S7)

#### [KSV-01] Namensinkonsistenz: „Eröffnung" (S5) vs. „Eröffnungsbibliothek" (S6)
**Schwere:** 🟡 Warnung — Subsystem-Name und Schnittstellenname werden vermischt.

**Lösungsvorschlag:** In S6 den Subsystem-Namen „Eröffnung" verwenden.

#### [KSV-02] Deployment ohne Eröffnungsbibliothek, obwohl S5/S6 sie nutzen
**Schwere:** 🟡 Warnung — S7 zeigt Deployment explizit „ohne Eröffnungsbibliothek". Alternatives Deployment-Szenario fehlt.

#### [KSV-03] Polyglot Opening Book-Datei fehlt als Infrastruktur-Artefakt
**Schwere:** 🟡 Warnung — Die Binärdatei wird nirgends als Deployment-Artefakt aufgeführt.

#### [KSV-04] Keine explizite Subsystem-zu-Artefakt-Zuordnung in S7
**Schwere:** 🟢 Hinweis — „sämtliche Module" ohne Aufschlüsselung.

#### [KSV-05] Level-2-Bausteine nur implizit im Laufzeitszenario
**Schwere:** 🟢 Hinweis — Zugsuche und Stellungsbewertung nicht namentlich in S6.

---

### Konzepte ↔ Entscheidungen (S8 ↔ S9)

#### [KKE-01] Entscheidung „Kein DI-Framework" in Konzept-Sektion versteckt
**Schwere:** 🟡 Warnung — `08-01-Abhaengigkeiten.md` enthält eine implizite Architekturentscheidung ohne eigenen ADR.

**Lösungsvorschlag:** ADR `09-03-Dependency-Injection.md` anlegen. In 08-01 auf die neue Entscheidung verweisen.

#### [KKE-02] Entscheidung „Kein Logging-Framework" in Konzept-Sektion versteckt
**Schwere:** 🟡 Warnung — `08-06-Logging.md` trifft zwei Architekturentscheidungen ohne ADR.

**Lösungsvorschlag:** ADR `09-04-Logging-Strategie.md` anlegen.

#### [KKE-03] Fehlerbehandlungsstrategie (Runtime Exceptions) ohne formale Entscheidung
**Schwere:** 🟢 Hinweis — Geringere Tragweite, optional als ADR formalisieren.

#### [KKE-04] Überschneidung: XBoard-Protokolldetails in S8 und S9
**Schwere:** 🟢 Hinweis — Minimale Redundanz, kein Widerspruch. Kein Handlungsbedarf.

**Gesamtbewertung:** Keine inhaltlichen Widersprüche. Hauptschwäche: Zwei implizite Entscheidungen in S8 gehören nach S9.

---

### Risiken ↔ Qualität (S11 ↔ S1/S10)

#### [KRQ-01] Analysierbarkeit (Prio 1) ohne Risikobetrachtung
**Schwere:** 🟡 Warnung — Das höchstpriorisierte Qualitätsziel hat kein Risiko in S11, obwohl R11.3 den Zielkonflikt explizit benennt.

**Lösungsvorschlag:** In `11-03-Spielstaerke.md` Risikominderung für Analysierbarkeit ergänzen.

#### [KRQ-02] Änderbarkeit (Prio 2) ohne Risikobetrachtung
**Schwere:** 🟡 Warnung — Zweitwichtigstes Ziel ohne eigenes Risiko.

**Lösungsvorschlag:** In `11-02-Aufwand.md` als Nebeneffekt aufnehmen.

#### [KRQ-03] Effizienz-Risiko ohne explizite Maßnahme
**Schwere:** 🟡 Warnung — R11.3 erwähnt „zu lange Wartezeiten", aber alle Maßnahmen adressieren nur Spielstärke.

**Lösungsvorschlag:** Effizienz-Tests (gegen E01/E02-Zeitgrenzen) als Maßnahme ergänzen.

#### [KRQ-04] Zuverlässigkeitsszenarien Z01/Z02 implizieren undokumentiertes Risiko
**Schwere:** 🟢 Hinweis — Komplexität der Spielregeln als Risiko für fehlerhafte Validierung.

#### [KRQ-05] R11.3 sichert nur die niedrigpriore Seite des Zielkonflikts ab
**Schwere:** 🟡 Warnung — Priorisierungsregel fehlt: Analysierbarkeit vor Spielstärke.

**Lösungsvorschlag:** Explizit machen: „Im Zielkonflikt hat Analysierbarkeit (Prio 1) Vorrang vor Spielstärke (Prio 4)."

**Gesamtbewertung:** Risiken decken niedrigpriorisierte Ziele gut ab. Wesentliche Lücke: Die beiden höchstpriorisierten Ziele (Analysierbarkeit, Änderbarkeit) haben keinen Risikoschutz.

---

## Übergreifende Muster

1. **ADR-Lücke:** Sektion 9 enthält nur 2 formale ADRs. Mindestens 3–4 weitere architekturrelevante Entscheidungen (Suchalgorithmus, Reactive Extensions, kein DI-Framework, kein Logging-Framework) sind über Sektion 4 und 8 verstreut, ohne eigene ADR-Dokumentation.

2. **Risiko-Qualitäts-Asymmetrie:** Die Risikoanalyse adressiert primär die niedrigpriorisierten Qualitätsziele (Interoperabilität Prio 3, Spielstärke Prio 4), während die höchstpriorisierten Ziele (Analysierbarkeit Prio 1, Änderbarkeit Prio 2) ohne Risikoschutz bleiben.

3. **Querverweise S8→S5:** Alle Konzepte werden von der Bausteinsicht referenziert, aber kein einziges Konzept verlinkt systematisch zurück auf die betroffenen Bausteine. Dies ist ein durchgängiges Muster über 6 von 7 Konzept-Dateien.

4. **Namensinkonsistenzen:** Die Benennung des Eröffnungs-Subsystems wechselt zwischen „Eröffnung" (S5), „Eröffnungsbibliothek" (S6) und „Eröffnungen" (S3). Das Qualitätsziel Spielstärke heißt in S1 „Akzeptable Spielstärke" und in S4 „Attraktive Spielstärke".

---

## Statistik

| Kategorie | 🔴 Kritisch | 🟡 Empfehlung/Warnung | 🟢 Hinweis | Gesamt |
|---|---|---|---|---|
| Sektions-Reviews | 6 | 38 | 27 | 71 |
| Konfliktanalysen | 0 | 17 | 14 | 31 |
| **Gesamt** | **6** | **55** | **41** | **102** |
