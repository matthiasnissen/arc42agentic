# arc42 Dokumentations-Review — DokChess

**Datum:** 24.03.2026  
**Modus:** Vollständiges Review  
**Geprüfte Sektionen:** 12 von 12  
**Konfliktdimensionen:** 7 von 7

---

## Gesamtübersicht

| Sektion | Status | Befunde |
|---------|--------|---------|
| 1. Einführung und Ziele | 🟢 | 0/4/3 — Solide Grundlage; fehlende Anforderungsquellen, Stakeholder-Erwartungsspalte und Endnutzer-Stakeholder |
| 2. Randbedingungen | 🟢 | 0/3/3 — Gute Struktur; fehlende Konsequenzen/Freiheitsgrade, XBoard als Constraint fehlt |
| 3. Kontextabgrenzung | 🟡 | 1/3/3 — Fehlende Ein-/Ausgabe-Spezifikation pro Kommunikationspartner (kritisch) |
| 4. Lösungsstrategie | 🟡 | 1/1/1 — Inkonsistente Benennung Qualitätsziel „Spielstärke", fehlende Klammer |
| 5. Bausteinsicht | 🟢 | 0/2/4 — Konsistente Blackbox/Whitebox-Templates; fehlende Zerlegungsbegründung |
| 6. Laufzeitsicht | 🟢 | 0/1/4 — Gutes Kernzenario; nur ein Szenario, Alternativpfade fehlen |
| 7. Verteilungssicht | 🔴 | 1/4/2 — Fehlendes Baustein-auf-Infrastruktur-Mapping (kritisch), keine Motivation |
| 8. Querschnittliche Konzepte | 🟡 | 0/6/3 — Fehlende Querverweise zu Bausteinen, fehlendes Nebenläufigkeitskonzept |
| 9. Architekturentscheidungen | 🟡 | 1/1/1 — ADR 09-03 (Bitboards) widerspricht Lösungsstrategie |
| 10. Qualitätsanforderungen | 🟡 | 1/2/2 — Qualitätsbaum nur als Bild, Szenarien ohne explizite Struktur |
| 11. Risiken | 🔴 | 1/3/3 — Technische Schulden nicht dokumentiert (kritisch) |
| 12. Glossar | 🟡 | 1/4/2 — Zentraler Begriff „Stellung" fehlt im Glossar |

**Legende:** Kritisch/Empfehlung/Hinweis

---

## Kritische Befunde

Die folgenden Befunde erfordern sofortige Aufmerksamkeit:

### 1. Bitboard-Entscheidung (ADR 09-03) nicht in Dokumentation zurückgeflossen

**Schwere:** 🔴 Kritisch — betrifft S4, S8, S9 und mehrere Konfliktdimensionen  
**Befund-IDs:** S04-01, S09-01, KSE-01/02/03, KRC-01/02, KKE-01

Dies ist der **gravierendste Befund** des gesamten Reviews. Die Entscheidung für Bitboards als interne Brettrepräsentation (ADR 09-03) wurde offensichtlich nachträglich hinzugefügt, ohne die restliche Dokumentation anzupassen:

- **Sektion 4** (Lösungsstrategie) propagiert weiterhin „Verständlichkeit vor Effizienz" und „objektorientiertes Domänenmodell" — das exakte Gegenteil der Bitboard-Entscheidung
- **Sektion 8** (Domänenmodell 08-02) beschreibt die Stellung als „zweidimensionales Array (8×8)" — direkt widersprüchlich zu Bitboards
- **Sektion 4** referenziert ADR 09-03 nirgends, obwohl ADRs 09-01 und 09-02 korrekt verlinkt sind
- Die Bezeichnung in S4 weicht ab: „Attraktive Spielstärke (Attraktivität)" statt korrekt „Akzeptable Spielstärke (Funktionale Eignung)"

**Empfohlene Maßnahmen:**

1. `04-02-Aufbau.md` um einen Absatz zur Bitboard-Ausnahme ergänzen
2. `04-01-Einstieg.md` Qualitätsziel-Bezeichnung korrigieren und Bitboard-Verweis in Effizienz-Tabelle aufnehmen
3. `08-02-Domaenenmodell.md` die 2D-Array-Beschreibung durch Bitboard-Referenz ersetzen

### 2. Technische Schulden nicht dokumentiert (S11)

**Schwere:** 🔴 Kritisch — Befund S11-03  

Mehrere bewusste Auslassungen (50-Züge-Regel, Stellungswiederholung, Endspieldatenbank) werden in anderen Sektionen referenziert, sind aber in Sektion 11 nicht als technische Schulden erfasst.

**Empfohlene Maßnahme:** Neue Datei `11-04-Technische-Schulden.md` mit TS-1 bis TS-4 anlegen.

### 3. Fehlendes Baustein-auf-Infrastruktur-Mapping (S7)

**Schwere:** 🔴 Kritisch — Befund S07-02  

Die Verteilungssicht nennt „DokChess.jar" als Artefakt, mappt aber keines der vier Subsysteme aus Sektion 5 explizit darauf. Eine Kernaufgabe der Verteilungssicht wird nicht erfüllt.

**Empfohlene Maßnahme:** Mapping-Tabelle (Baustein → Artefakt → Infrastruktur-Element) in `07-01-Infrastruktur-Windows.md` ergänzen.

### 4. Fehlende Ein-/Ausgabe-Spezifikation im fachlichen Kontext (S3)

**Schwere:** 🔴 Kritisch — Befund S03-01  

Der fachliche Kontext beschreibt vier Kommunikationspartner in Prosa, spezifiziert aber nicht die konkreten fachlichen Ein-/Ausgaben pro Partner. Eine Kernanforderung der arc42-Kontextabgrenzung.

**Empfohlene Maßnahme:** Tabelle mit Ein-/Ausgaben je Partner in `03-01-Fachlicher-Kontext.md` ergänzen.

### 5. Qualitätsbaum nur als Bild (S10)

**Schwere:** 🔴 Kritisch — Befund S10-01  

Die Qualitätsübersicht existiert ausschließlich als PNG-Bild, nicht durchsuchbar und nicht versionierbar.

**Empfohlene Maßnahme:** Textuelle Tabelle in `10-01-Qualitaetsbaum.md` ergänzen.

### 6. Zentraler Domänenbegriff „Stellung" fehlt im Glossar (S12)

**Schwere:** 🔴 Kritisch — Befund S12-01  

Der meist verwendete Fachbegriff der gesamten Dokumentation hat keinen Glossareintrag.

**Empfohlene Maßnahme:** Glossareintrag in `12-02-Begriffe.md` ergänzen.

---

## Empfehlungen

| Prio | Bereich | Empfehlung |
|------|---------|------------|
| 1 | S8/S9 | Fehlendes Nebenläufigkeitskonzept (08-08) für parallele Zugsuche und Observer-Pattern anlegen |
| 2 | S8 | Durchgängig Querverweise von Konzepten zu betroffenen Bausteinen in S5 ergänzen (S08-01 bis S08-06, S08-09) |
| 3 | S9 | ADR für Minimax/Alpha-Beta-Algorithmus-Wahl erstellen (KSE-07) |
| 4 | S11 | Übersichtstabelle mit Priorisierung für Management-Stakeholder anlegen (S11-01, S11-02) |
| 5 | S7 | Deployment-Szenario mit Eröffnungsbibliothek dokumentieren (KSV-01, S07-06) |
| 6 | S7 | Motivation, Infrastruktur-Knoten, weitere Plattformen ergänzen (S07-01/03/05) |
| 7 | S3 | Mapping fachliche Partner → technische Kanäle explizit darstellen (S03-03) |
| 8 | S10 | Szenarien um Stimulus/Metrik-Spalten erweitern (S10-02), Legende ergänzen (S10-04) |
| 9 | S1 | Stakeholder-Tabelle um Erwartungsspalte und Schachspieler ergänzen (S01-05, S01-06) |
| 10 | S12 | Glossareinträge für „Spielbaum", „Bitboard", „UCI" ergänzen (S12-02, S12-03, S12-05) |

---

## Sektionsübergreifende Konflikte

| Konfliktdimension | Status | Befunde |
|---|---|---|
| Qualitätsstrang (S1↔S4↔S10) | ⚠️ | 3 Warnungen, 3 Hinweise — Bezeichnungskonflikt „Spielstärke", Widerspruch Domänenmodell-Effizienz in S4, verwaiste Z-Szenarien ohne Qualitätsziel |
| Strategie↔Entscheidungen (S4↔S9) | ❌ | **3 Kritisch**, 3 Warnungen, 2 Hinweise — ADR 09-03 widerspricht fundamental dem Grundprinzip „Verständlichkeit vor Effizienz" und dem OO-Domänenmodell-Ansatz. S4 wurde nach ADR 09-03 nicht aktualisiert. |
| Constraint-Compliance (S2↔S4/S8/S9) | ❌ | **2 Kritisch**, 3 Warnungen — Alle 5 Konflikte gehen auf ADR 09-03 (Bitboards) zurück. Die übrigen 13 Constraints werden vollständig eingehalten. Bitboard-Terminologie verletzt deutsche Bezeichner-Konvention. |
| Kontext↔Bausteine (S3↔S5) | ⚠️ | 2 Warnungen, 3 Hinweise — Computergegner nicht explizit in S5 abgebildet; Remisangebote im Kontext versprochen, aber in S5 als nicht unterstützt gelistet |
| Sichten-Konsistenz (S5↔S6↔S7) | ⚠️ | 1 Warnung, 4 Hinweise — Eröffnungs-Subsystem ohne Deployment-Mapping; Ebene-2-Module nur implizit in S6; Verteilungssicht operiert auf gröberer Granularität |
| Konzepte↔Entscheidungen (S8↔S9) | ❌ | **1 Kritisch**, 3 Warnungen, 2 Hinweise — Domänenmodell beschreibt 2D-Array, ADR 09-03 wählt Bitboards. DI-Framework-Entscheidung fälschlich in S8. Fehlendes Bitboard-Konzept. |
| Risiken↔Qualität (S11↔S1/S10) | ⚠️ | 4 Warnungen, 2 Hinweise — Die beiden höchstpriorisierten Qualitätsziele (Analysierbarkeit, Änderbarkeit) haben keine Risikobetrachtung. Effizienz-Risiko nur implizit in R3 mitbehandelt. |

---

## Detailbefunde je Sektion

### Sektion 1 — Einführung und Ziele

#### [S01-01] Fehlender Verweis auf Anforderungsdokumente

**Schwere:** 🟡 Empfehlung  
**Datei:** `arc-doc/01-Einfuehrung-und-Ziele/01-01-Aufgabenstellung.md`  
**Kriterium:** Formale Prüfung – Werden Verweise auf existierende Anforderungsdokumente gegeben?

**Befund:** Der Abschnitt beschreibt die Aufgabenstellung kompakt, enthält aber keinerlei Verweise auf weiterführende Anforderungsquellen (z. B. das Buch von Stefan Zörner, eine Feature-Liste oder ein Anforderungsdokument).

**Änderungsvorschlag:**
> Am Ende der Datei einen Abschnitt ergänzen:
>
> ```markdown
> ### Anforderungsquellen
>
> - Stefan Zörner: *Softwarearchitekturen dokumentieren und bewerten*, Carl Hanser Verlag (Kapitel zu DokChess)
> - Vollständige Anforderungsliste: siehe [Aufgabenstellung auf arc42.org](https://www.dokchess.de)
> ```

#### [S01-02] Treibende Kräfte nicht explizit benannt

**Schwere:** 🟡 Empfehlung  
**Datei:** `arc-doc/01-Einfuehrung-und-Ziele/01-01-Aufgabenstellung.md`  
**Kriterium:** Inhaltliche Prüfung – Werden die wesentlichen treibenden Kräfte beschrieben?

**Befund:** Die Aufgabenstellung beschreibt *was* DokChess ist und welche Features es hat, benennt aber die treibenden Kräfte hinter dem System nicht explizit.

**Änderungsvorschlag:**
> Zwischen „Was ist DokChess?" und „Wesentliche Features" einen Abschnitt einfügen:
>
> ```markdown
> ### Treibende Kräfte
>
> - Bedarf an einem verständlichen, realistischen Fallbeispiel für Architektur-Schulungen und -Vorträge
> - Die Engine soll als Experimentierplattform für Architektur- und Entwurfsentscheidungen dienen
> - Kein kommerzielles Produkt – Fokus liegt auf Nachvollziehbarkeit, nicht auf maximaler Spielstärke
> ```

#### [S01-03] Keine Gruppierung der Anforderungen

**Schwere:** 🟢 Hinweis  
**Datei:** `arc-doc/01-Einfuehrung-und-Ziele/01-01-Aufgabenstellung.md`  
**Kriterium:** Inhaltliche Prüfung – Sind die Anforderungen gruppiert oder geclustert?

**Befund:** Die Anforderungen sind in zwei Listen aufgeteilt, deren Trennung nicht explizit benannt ist.

**Änderungsvorschlag:**
> Die Überschriften präzisieren: „Was ist DokChess?" → **„Überblick und Business-Ziele"**, „Wesentliche Features" → **„Wesentliche funktionale Anforderungen"**

#### [S01-04] Qualitätsziele: 5 Ziele am oberen Limit

**Schwere:** 🟢 Hinweis  
**Datei:** `arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md`  
**Kriterium:** Formale Prüfung – Sind maximal 3–5 Qualitätsziele aufgeführt?

**Befund:** Mit exakt 5 Qualitätszielen liegt die Auflistung am oberen Rand der arc42-Empfehlung. Kein Handlungsbedarf.

#### [S01-05] Stakeholder-Tabelle: Spalte „Erwartungen an Architektur" fehlt

**Schwere:** 🟡 Empfehlung  
**Datei:** `arc-doc/01-Einfuehrung-und-Ziele/01-03-Stakeholder.md`  
**Kriterium:** Formale Prüfung – Ist eine Stakeholder-Tabelle mit Rolle, Name/Beschreibung und Erwartungen vorhanden?

**Befund:** Die Tabelle enthält die Spalten „Wer?" und „Interesse, Bezug". Arc42 empfiehlt explizit eine Spalte für die **Erwartungen an die Architektur und deren Dokumentation**.

**Änderungsvorschlag:**
> Die Tabelle um eine dritte Spalte „Erwartungen an Architektur/Dokumentation" erweitern.

#### [S01-06] Fehlende Stakeholder-Gruppen: Endnutzer und Betrieb

**Schwere:** 🟡 Empfehlung  
**Datei:** `arc-doc/01-Einfuehrung-und-Ziele/01-03-Stakeholder.md`  
**Kriterium:** Inhaltliche Prüfung – Werden alle relevanten Stakeholder-Gruppen abgedeckt?

**Befund:** Es fehlen Schachspieler/Endnutzer als Stakeholder.

**Änderungsvorschlag:**
> Folgende Zeile ergänzen:
>
> ```markdown
> | Schachspieler (Gelegenheitsspieler) | Nutzer der Engine über ein grafisches Frontend; erwarten faire, zügig berechnete Züge | Akzeptable Spielstärke; schnelle Antwortzeiten; Kompatibilität mit gängigen Frontends |
> ```

#### [S01-07] Qualitätsziele: Konkretisierung der Messbarkeit

**Schwere:** 🟢 Hinweis  
**Datei:** `arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md`  
**Kriterium:** Inhaltliche Prüfung – Sind die Qualitätsziele konkret und messbar?

**Befund:** Formulierungen bleiben qualitativ vage: „erschließen sich rasch", „leicht implementiert". Konkretisierung erfolgt korrekt über Verweis auf Sektion 10.

---

### Sektion 2 — Randbedingungen

#### [S02-01] Fehlende Einleitung zur Sektion

**Schwere:** 🟡 Empfehlung  
**Datei:** `arc-doc/02-Randbedingungen/` (alle Dateien)  
**Kriterium:** Existiert ein Abschnitt für Randbedingungen mit einführender Erläuterung?

**Befund:** Es fehlt eine übergreifende Einleitung, die den Zweck der Sektion erläutert.

#### [S02-02] Konsequenzen und Freiheitsgrade nicht explizit dargestellt

**Schwere:** 🟡 Empfehlung  
**Datei:** `arc-doc/02-Randbedingungen/02-01-Technisch.md`, `02-02-Organisatorisch.md`, `02-03-Konventionen.md`  
**Kriterium:** Werden die Konsequenzen der Constraints erläutert?

**Befund:** Die Spalte „Erläuterungen, Hintergrund" beschreibt die Motivation, aber nicht die architektonischen Konsequenzen. Es wird nicht dargestellt, wo Freiheitsgrade bestehen.

**Änderungsvorschlag:**
> Ergänzung einer dritten Spalte „Konsequenz / Freiheitsgrad" in jeder Tabelle.

#### [S02-03] Tippfehler in organisatorischen Randbedingungen

**Schwere:** 🟢 Hinweis  
**Datei:** `arc-doc/02-Randbedingungen/02-02-Organisatorisch.md`  
**Kriterium:** Formale Korrektheit

**Befund:** „Schulungsunternehmenin" (zusammengeschrieben) statt „Schulungsunternehmen in".

#### [S02-04] Fehlende Constraints zu externen Systemen / Schnittstellen

**Schwere:** 🟡 Empfehlung  
**Datei:** `arc-doc/02-Randbedingungen/02-01-Technisch.md`  
**Kriterium:** Werden Constraints anderer Systeme berücksichtigt?

**Befund:** Die Bindung an das XBoard-Protokoll fehlt als technische Randbedingung.

**Änderungsvorschlag:**
> Ergänzung in der Tabelle:
>
> ```markdown
> | Kommunikation über XBoard-Protokoll | Anbindung an grafische Schach-Frontends über das verbreitete XBoard-Protokoll. Textbasiert über stdin/stdout. |
> ```

#### [S02-05] Keine Versionierung oder Gültigkeitszeitraum der Constraints

**Schwere:** 🟢 Hinweis  
**Datei:** `arc-doc/02-Randbedingungen/02-01-Technisch.md`  
**Kriterium:** Werden technische Einschränkungen vollständig dokumentiert?

**Befund:** Es bleibt unklar, welche Java-Version aktuell verbindlich ist.

#### [S02-06] Inkonsistente Überschriften-Hierarchie

**Schwere:** 🟢 Hinweis  
**Datei:** Alle Dateien der Sektion 2  
**Kriterium:** Formale Korrektheit und Konsistenz

**Befund:** Die H1-Überschrift ist generisch einwortig, während die H2-Überschrift die eigentlich aussagekräftige Überschrift ist.

---

### Sektion 3 — Kontextabgrenzung

#### [S03-01] Fehlende Ein-/Ausgabe-Spezifikation der Kommunikationspartner

**Schwere:** 🔴 Kritisch  
**Datei:** `arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md`  
**Kriterium:** Werden alle Kommunikationspartner mit fachlichen Ein-/Ausgaben spezifiziert?

**Befund:** Der fachliche Kontext beschreibt vier Kommunikationspartner in Prosaform, spezifiziert jedoch nicht die konkreten fachlichen Ein- und Ausgaben pro Partner.

**Änderungsvorschlag:**
> Ergänze nach dem Diagramm eine Tabelle:
>
> ```markdown
> | Kommunikationspartner | Eingabe (an DokChess) | Ausgabe (von DokChess) |
> | --- | --- | --- |
> | Menschlicher Gegner | Züge des Gegners, Remisangebote, Spielstart/-abbruch | Eigene Züge, Spielergebnis |
> | Computergegner | Züge des Gegners, Remisangebote, Spielstart/-abbruch | Eigene Züge, Spielergebnis |
> | Eröffnungen (Bibliothek) | Aktuelle Stellung | Eröffnungszug (falls bekannt) |
> | Endspiele (Bibliothek) | Aktuelle Stellung mit wenigen Figuren | Bewertung, optimaler Zug |
> ```

#### [S03-02] Fehlende Datenflüsse im fachlichen Kontext

**Schwere:** 🟡 Empfehlung  
**Datei:** `arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md`  
**Kriterium:** Werden Datenflüsse im fachlichen Kontext gezeigt?

**Befund:** Die textuelle Beschreibung stellt keine expliziten Datenflüsse (Richtung, Inhalt) dar.

#### [S03-03] Fehlende explizite Zuordnung des Computergegners im technischen Kontext

**Schwere:** 🟡 Empfehlung  
**Datei:** `arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md`  
**Kriterium:** Gibt es ein Mapping zwischen fachlichen Ein-/Ausgaben und technischen Kanälen?

**Befund:** Es wird nicht explizit erklärt, dass sowohl der menschliche Gegner als auch der Computergegner über denselben technischen Kanal (XBoard-Protokoll via stdin/stdout) angebunden sind.

**Änderungsvorschlag:**
> Ergänze eine Zuordnungstabelle:
>
> ```markdown
> | Fachlicher Partner | Technischer Kanal | Protokoll/Format |
> | --- | --- | --- |
> | Menschlicher Gegner | XBoard Client (stdin/stdout) | XBoard-Protokoll (textbasiert) |
> | Computergegner | XBoard Client (stdin/stdout) | XBoard-Protokoll (textbasiert) |
> | Eröffnungen | Polyglot Opening Book (Dateizugriff) | Polyglot-Binärformat (lesend) |
> | Endspiele | — (nicht implementiert) | Siehe Risiko 11.2 |
> ```

#### [S03-04] Technischer Kontext: Protokollbeschreibung unzureichend

**Schwere:** 🟡 Empfehlung  
**Datei:** `arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md`  
**Kriterium:** Werden Protokolle oder Kanäle beschrieben?

**Befund:** Technische Eckdaten des XBoard-Protokolls fehlen im Kontextabschnitt (textbasiert, stdin/stdout, Befehl-Antwort-Schema).

#### [S03-05] Fehlende Qualitätsanforderungen an externen Schnittstellen

**Schwere:** 🟢 Hinweis  
**Datei:** `arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md`  
**Kriterium:** Werden Qualitätsanforderungen an externen Schnittstellen beachtet?

**Befund:** Keine Qualitätsanforderungen an die externen Schnittstellen genannt (Antwortzeiten, Dateigröße).

#### [S03-06] Endspiele-Schnittstelle ohne Pendant in Bausteinsicht

**Schwere:** 🟢 Hinweis  
**Datei:** `arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md`  
**Kriterium:** Konsistenz mit Bausteinsicht

**Befund:** „Endspiele" als Fremdsystem im fachlichen Kontext, in Bausteinsicht nicht erwähnt. Nachvollziehbar begründet, aber der Status „nicht implementiert" sollte deutlicher kennzeichnet werden.

#### [S03-07] Fehlende Risiken im fachlichen Kontext

**Schwere:** 🟢 Hinweis  
**Datei:** `arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md`  
**Kriterium:** Werden Risiken im Kontext aufgezeigt?

**Befund:** Im fachlichen Kontext fehlen jegliche Risikohinweise.

---

### Sektion 4 — Lösungsstrategie

#### [S04-01] Inkonsistente Benennung des Qualitätsziels „Spielstärke"

**Schwere:** 🔴 Kritisch  
**Datei:** `arc-doc/04-Loesungsstrategie/04-01-Einstieg.md`  
**Kriterium:** Konsistenz mit Qualitätszielen aus Sektion 1.2

**Befund:** In der Zuordnungstabelle wird das vierte Qualitätsziel als **„Attraktive Spielstärke (Attraktivität)"** bezeichnet. In Sektion 1.2 lautet es jedoch **„Akzeptable Spielstärke (Funktionale Eignung)"**. Sowohl der Name als auch die Qualitätskategorie weichen ab.

**Änderungsvorschlag:**
> Ändern von `| Attraktive Spielstärke (Attraktivität) |` zu `| Akzeptable Spielstärke (Funktionale Eignung) |`

#### [S04-02] Fehlende schließende Klammer in Querverweis

**Schwere:** 🟡 Empfehlung  
**Datei:** `arc-doc/04-Loesungsstrategie/04-02-Aufbau.md`  
**Kriterium:** Formale Korrektheit

**Befund:** In Zeile 11 fehlt eine schließende Klammer `)` am Ende des Satzes mit Querverweisen.

#### [S04-03] Fehlende organisatorische Entscheidungen

**Schwere:** 🟢 Hinweis  
**Datei:** Sektion 4 insgesamt  
**Kriterium:** Dokumentation relevanter organisatorischer Entscheidungen

**Befund:** Nur technische Entscheidungen behandelt, keine organisatorischen.

---

### Sektion 5 — Bausteinsicht

#### [S05-01] Fehlende Begründung der Zerlegung in Ebene 1

**Schwere:** 🟡 Empfehlung  
**Datei:** `arc-doc/05-Bausteinsicht/05-01-Ebene-1.md`  
**Kriterium:** Whitebox Gesamtsystem soll Begründung der Zerlegung enthalten

**Befund:** Der Text beschreibt *wie* DokChess in vier Subsysteme zerfällt, nennt aber nicht *warum* diese Zerlegung gewählt wurde.

#### [S05-02] Endspiele aus Kontextabgrenzung nicht in Bausteinsicht adressiert

**Schwere:** 🟡 Empfehlung  
**Datei:** `arc-doc/05-Bausteinsicht/05-01-Ebene-1.md`  
**Kriterium:** Konsistenz mit dem Kontext aus Sektion 3

**Befund:** Der fachliche Kontext führt „Endspiele (Fremdsystem)" als externen Akteur auf. In der Bausteinsicht fehlt jeglicher Hinweis darauf, dass dieses System bewusst nicht abgebildet wird.

#### [S05-03] Computergegner nicht explizit in XBoard-Protokoll erwähnt

**Schwere:** 🟢 Hinweis  
**Datei:** `arc-doc/05-Bausteinsicht/05-02-XBoard-Protokoll.md`  
**Kriterium:** Konsistenz mit Sektion 3

**Befund:** XBoard-Protokoll spricht nur von „Client (z.B. einer grafischen Oberfläche)". Computergegner nicht erwähnt.

**Änderungsvorschlag:**
> Ändern zu: „Kommunikation mit einem Client (z.B. einer grafischen Oberfläche oder einem anderen Schachprogramm)"

#### [S05-04] Tippfehler in Spielregeln-Schnittstelle

**Schwere:** 🟢 Hinweis  
**Datei:** `arc-doc/05-Bausteinsicht/05-03-Spielregeln.md`  
**Kriterium:** Formale Korrektheit

**Befund:** „Püft" statt „Prüft" bei `aufSchachPruefen`.

#### [S05-05] Ebene 2: Begründung der Verfeinerung nur implizit

**Schwere:** 🟢 Hinweis  
**Datei:** `arc-doc/05-Bausteinsicht/05-06-Ebene-2-Engine.md`  
**Kriterium:** Whitebox-Template soll Begründung der Zerlegung enthalten

**Befund:** Fehlt explizite Begründung, *warum* die Engine in Zugsuche und Stellungsbewertung zerlegt wird.

#### [S05-06] Qualitäts-/Performance-Merkmale bei keiner Blackbox genannt

**Schwere:** 🟢 Hinweis  
**Datei:** Alle Blackbox-Beschreibungen  
**Kriterium:** Blackbox-Beschreibungen können optional Qualitäts-/Performance-Merkmale enthalten

**Befund:** Keine der Blackbox-Beschreibungen nennt Qualitäts- oder Performance-Merkmale.

---

### Sektion 6 — Laufzeitsicht

#### [S06-01] Nur ein einzelnes Laufzeitszenario vorhanden

**Schwere:** 🟡 Empfehlung  
**Datei:** `arc-doc/06-Laufzeitsicht/06-01-Zugermittlung.md`  
**Kriterium:** Abdeckung architekturrelevanter Szenarien

**Befund:** Die gesamte Laufzeitsicht besteht aus einem einzigen Szenario (Zugermittlung). Es fehlen Partie-Start, Fehlerfall und Eröffnungsbibliothek-Treffer-Szenarien.

#### [S06-02] Fehlender alternativer Pfad: Eröffnungsbibliothek liefert Zug

**Schwere:** 🟢 Hinweis  
**Datei:** `arc-doc/06-Laufzeitsicht/06-01-Zugermittlung.md`  
**Kriterium:** Bemerkenswerte Aspekte der Interaktion

**Befund:** Das Szenario zeigt nur den Fall „Eröffnungsbibliothek gibt nichts her". Der architekturrelevante Positivfall fehlt.

#### [S06-03] Konsistenz der Bausteine mit Sektion 5 gegeben

**Schwere:** 🟢 Hinweis  
**Befund:** Alle vier Ebene-1-Subsysteme korrekt referenziert. **Kein Handlungsbedarf.**

#### [S06-04] Darstellungsform des Szenarios ist geeignet

**Schwere:** 🟢 Hinweis  
**Befund:** Sequenzdiagramm + Fließtext. Geeignete Darstellungsform. Optional nummerierte Schritte ergänzen.

#### [S06-05] Querverweis auf Konzept 8.4 vorhanden

**Schwere:** 🟢 Hinweis  
**Befund:** Querverweise sind korrekt und ausreichend. **Kein Handlungsbedarf.**

---

### Sektion 7 — Verteilungssicht

#### [S07-01] Fehlende Motivation für die Deployment-Struktur

**Schwere:** 🟡 Empfehlung  
**Datei:** `arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md`  
**Kriterium:** Beschreibung der Motivation für diese Deployment-Struktur

**Befund:** Es fehlt eine Begründung, warum DokChess als monolithisches Jar auf einem einzelnen Windows-PC betrieben wird.

#### [S07-02] Fehlendes explizites Mapping von Bausteinen auf Infrastruktur

**Schwere:** 🔴 Kritisch  
**Datei:** `arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md`  
**Kriterium:** Mapping von Software-Bausteinen (Sektion 5) auf Infrastruktur-Elemente

**Befund:** Die vier Subsysteme aus Sektion 5 werden nicht namentlich genannt und ihr Mapping auf das Deployment-Artefakt wird nicht dargestellt.

**Änderungsvorschlag:**
> ```markdown
> | Baustein (Sektion 5) | Deployment-Artefakt | Infrastruktur-Element |
> | --- | --- | --- |
> | XBoard-Protokoll | DokChess.jar | JVM auf Windows-PC |
> | Spielregeln | DokChess.jar | JVM auf Windows-PC |
> | Engine | DokChess.jar | JVM auf Windows-PC |
> | Eröffnung | DokChess.jar | JVM auf Windows-PC |
> ```

#### [S07-03] Unvollständige Beschreibung der Infrastruktur-Knoten

**Schwere:** 🟡 Empfehlung  
**Datei:** `arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md`  
**Kriterium:** Infrastruktur-Knoten werden erklärt

**Befund:** Knoten nicht einzeln als benannte Knoten mit Beschreibung aufgeführt.

#### [S07-04] Fehlende Qualitäts-/Performance-Merkmale der Infrastruktur

**Schwere:** 🟡 Empfehlung  
**Datei:** `arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md`  
**Kriterium:** Qualitäts- und/oder Performance-Merkmale der Infrastruktur

**Befund:** Keine Angaben zu minimalen Hardware-Anforderungen.

#### [S07-05] Fehlende Dokumentation weiterer Umgebungen und Plattformen

**Schwere:** 🟡 Empfehlung  
**Datei:** `arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md`  
**Kriterium:** Werden die verschiedenen Umgebungen dokumentiert?

**Befund:** Ausschließlich Windows beschrieben. Keine Hinweise auf Linux/macOS oder Entwicklungs-/Testumgebung.

#### [S07-06] Deployment mit Eröffnungsbibliothek nicht dokumentiert

**Schwere:** 🟢 Hinweis  
**Datei:** `arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md`  
**Kriterium:** Vollständigkeit der Deployment-Szenarien

**Befund:** Nur Deployment „ohne Eröffnungsbibliothek" beschrieben.

#### [S07-07] Kommunikationskanal zwischen Arena und Engine nicht textlich beschrieben

**Schwere:** 🟢 Hinweis  
**Datei:** `arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md`  
**Kriterium:** Physische Verbindungen zwischen den Elementen

**Befund:** Es fehlt eine explizite Angabe, dass die Verbindung über stdin/stdout (Pipes) erfolgt.

---

### Sektion 8 — Querschnittliche Konzepte

#### [S08-01] Fehlende Querverweise von Konzept 8.1 zu Sektion 5

**Schwere:** 🟡 Empfehlung  
**Datei:** `arc-doc/08-Konzepte/08-01-Abhaengigkeiten.md`  
**Kriterium:** Gibt es Links zwischen Bausteinen (Sektion 5) und Konzepten?

**Befund:** Konzept beschreibt DI als durchgängigen Ansatz, verweist aber auf keinen einzigen Baustein aus Sektion 5.

#### [S08-02] Fehlende Querverweise von Domänenmodell 8.2 zu Sektion 5

**Schwere:** 🟡 Empfehlung  
**Datei:** `arc-doc/08-Konzepte/08-02-Domaenenmodell.md`  
**Kriterium:** Verknüpfungen zwischen Bausteinen und Konzepten

**Befund:** 8.2 verweist nicht zurück auf die Bausteine, die das Modell verwenden.

#### [S08-03] Konzept 8.3 „Benutzungsoberfläche" ist nicht querschnittlich

**Schwere:** 🟡 Empfehlung  
**Datei:** `arc-doc/08-Konzepte/08-03-Benutzungsoberflaeche.md`  
**Kriterium:** Querschnittlichkeit

**Befund:** Betrifft im Wesentlichen nur ein einziges Subsystem (XBoard-Protokoll). Kein echtes querschnittliches Konzept.

#### [S08-04] Tippfehler in 8.3

**Schwere:** 🟢 Hinweis  
**Datei:** `arc-doc/08-Konzepte/08-03-Benutzungsoberflaeche.md`  
**Kriterium:** Formale Prüfung

**Befund:** „inder Regel" statt „in der Regel".

#### [S08-05] Fehlende Querverweise von Konzept 8.4 zu Bausteinen

**Schwere:** 🟡 Empfehlung  
**Datei:** `arc-doc/08-Konzepte/08-04-Validierung.md`  
**Kriterium:** Verknüpfungen

**Befund:** Erwähnt „Spielregeln-Subsystem" und „Eröffnung-Subsystem" ohne Links auf die Bausteinbeschreibungen 5.3 und 5.5.

#### [S08-06] Fehlende Querverweise von Konzept 8.5 zu Bausteinen

**Schwere:** 🟡 Empfehlung  
**Datei:** `arc-doc/08-Konzepte/08-05-Fehlerbehandlung.md`  
**Kriterium:** Verknüpfungen

**Befund:** Erwähnt „Engine-Subsystem" und „XBoard-Subsystem" ohne Links zu 5.4 und 5.2.

#### [S08-07] Konzept 8.6 „Logging" enthält implizite Architekturentscheidung

**Schwere:** 🟢 Hinweis  
**Datei:** `arc-doc/08-Konzepte/08-06-Logging.md`  
**Kriterium:** Abgrenzung Konzept vs. Entscheidung

**Befund:** Entscheidung, auf ein Logging-Framework zu verzichten, gehört eigentlich in Sektion 9.

#### [S08-08] Fehlendes Konzept für Nebenläufigkeit/Parallelität

**Schwere:** 🟡 Empfehlung  
**Datei:** *(fehlend — betrifft gesamte Sektion 8)*  
**Kriterium:** Konzept-Definition

**Befund:** Parallele Zugsuche mit asynchroner Ergebnislieferung über Observer-Pattern ist ein querschnittlicher Aspekt, der in Sektion 8 nicht dokumentiert ist.

#### [S08-09] Konzept 8.7 ohne Querverweise zu Bausteinen

**Schwere:** 🟢 Hinweis  
**Datei:** `arc-doc/08-Konzepte/08-07-Testbarkeit.md`  
**Kriterium:** Verknüpfungen

**Befund:** Nennt keinen einzigen Baustein aus Sektion 5 als Beispiel.

---

### Sektion 9 — Architekturentscheidungen

#### [S09-01] Widerspruch zwischen ADR 09-03 (Bitboards) und Lösungsstrategie

**Schwere:** 🔴 Kritisch  
**Datei:** `arc-doc/09-Entscheidungen/09-03-Brettrepraesentation.md`  
**Kriterium:** Konsistenz mit Lösungsstrategie (Sektion 4)

**Befund:** ADR 09-03 entscheidet sich für Bitboards und priorisiert Effizienz über Lesbarkeit. Dies widerspricht dem Grundsatz in Sektion 4: „Hier wurde bewusst eine bessere Verständlichkeit angestrebt, auf Kosten von Effizienz."

**Änderungsvorschlag:**
> 1. In `04-02-Aufbau.md` eine Ausnahme für die interne Brettrepräsentation ergänzen
> 2. In ADR 09-03 die Spannung zum Lesbarkeits-Prinzip explizit benennen

#### [S09-02] ADR 09-03 fehlt als Querverweis in Sektion 4

**Schwere:** 🟡 Empfehlung  
**Datei:** `arc-doc/04-Loesungsstrategie/04-01-Einstieg.md`  
**Kriterium:** Nachvollziehbarkeit

**Befund:** ADR 09-01 und 09-02 werden aus S4 referenziert, ADR 09-03 nicht.

#### [S09-03] Neutrale Konsequenzen nicht einheitlich gekennzeichnet

**Schwere:** 🟢 Hinweis  
**Datei:** `arc-doc/09-Entscheidungen/09-02-Stellungsobjekte.md`, `09-03-Brettrepraesentation.md`  
**Kriterium:** ADR-Format nach Nygard

**Befund:** ADR 09-01 kennzeichnet die dritte Kategorie als „Neutrale/Folgen fuer die Weiterentwicklung". ADR 09-02 und 09-03 verwenden nur „Folgen fuer die Weiterentwicklung" ohne „neutral".

---

### Sektion 10 — Qualitätsanforderungen

#### [S10-01] Qualitätsbaum nur als Bild vorhanden

**Schwere:** 🔴 Kritisch  
**Datei:** `arc-doc/10-Qualitaetsanforderungen/10-01-Qualitaetsbaum.md`  
**Kriterium:** 10.1 — Qualitätsübersicht muss als Tabelle, Liste oder Mindmap strukturiert sein

**Befund:** Die Qualitätsübersicht besteht ausschließlich aus einem eingebetteten Bild. Keine textuelle Darstellung.

**Änderungsvorschlag:**
> ```markdown
> | Qualitätsmerkmal | Untermerkmal | Szenarien |
> |---|---|---|
> | Wartbarkeit (#flexible) | Analysierbarkeit | W01, W02, W03 |
> | Wartbarkeit (#flexible) | Änderbarkeit | W04, W05 |
> | Kompatibilität (#usable) | Interoperabilität | K01, P01 |
> | Funktionale Eignung (#reliable) | Korrektheit | F01, F02, F03, F04 |
> | Effizienz (#efficient) | Zeitverhalten | E01, E02 |
> | Zuverlässigkeit (#reliable) | Fehlertoleranz | Z01, Z02 |
> ```

#### [S10-02] Szenarien ohne explizite Strukturierung in Kontext/Stimulus/Metrik

**Schwere:** 🟡 Empfehlung  
**Datei:** `arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md`  
**Kriterium:** Szenarien sollen Kontext, Stimulus und Metrik enthalten

**Befund:** Die drei Bestandteile sind im Text implizit enthalten, aber nicht explizit getrennt.

#### [S10-03] Fehlende Messbarkeit bei mehreren funktionalen Szenarien

**Schwere:** 🟡 Empfehlung  
**Datei:** `arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md`  
**Kriterium:** Szenarien sollen als Akzeptanzkriterien dienen

**Befund:** F01, F02, F03 definieren keine quantitative Metrik.

#### [S10-04] Keine explizite Zuordnung zu Qualitätsmodell-Kategorien

**Schwere:** 🟢 Hinweis  
**Datei:** `arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md`  
**Kriterium:** Kategorien nach ISO 25010

**Befund:** Szenario-Präfixe (W, K, F, E, Z, P) ohne vollständige Legende.

#### [S10-05] Fehlende Sicherheits- und Betreibbarkeitsszenarien

**Schwere:** 🟢 Hinweis  
**Datei:** `arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md`  
**Kriterium:** Auch weniger wichtige Qualitätsanforderungen sollen dokumentiert werden

**Befund:** Kategorien `#secure`, `#safe`, `#operable`, `#testable` nicht adressiert. Bewusste Auslassung sollte dokumentiert werden.

---

### Sektion 11 — Risiken und technische Schulden

#### [S11-01] Fehlende Übersichtsliste oder -tabelle der Risiken

**Schwere:** 🟡 Empfehlung  
**Datei:** `arc-doc/11-Risiken/` (Sektionsebene)  
**Kriterium:** Existiert eine Übersichtstabelle?

**Befund:** Drei Risiken auf separate Dateien verteilt, aber keine zentrale Übersichtstabelle.

#### [S11-02] Keine explizite Priorisierung der Risiken

**Schwere:** 🟡 Empfehlung  
**Datei:** `arc-doc/11-Risiken/` (alle Dateien)  
**Kriterium:** Sind die Risiken nach Priorität geordnet?

**Befund:** Keine Angabe von Eintrittswahrscheinlichkeit, Schadenshöhe oder Priorität.

#### [S11-03] Technische Schulden nicht dokumentiert

**Schwere:** 🔴 Kritisch  
**Datei:** `arc-doc/11-Risiken/` (Sektionsebene)  
**Kriterium:** Werden technische Schulden identifiziert?

**Befund:** Ausschließlich Risiken behandelt. Mehrere bekannte technische Schulden (50-Züge-Regel, Stellungswiederholung, Endspieldatenbank, Eröffnungsbibliothek) nicht als solche klassifiziert.

**Änderungsvorschlag:**
> Neue Datei `11-04-Technische-Schulden.md`:
>
> ```markdown
> | Nr. | Schuld | Auswirkung | Referenz |
> | --- | --- | --- | --- |
> | TS-1 | 50-Züge-Regel nicht implementiert | Partien können nicht korrekt als Remis erkannt werden | Risiko 11.2 |
> | TS-2 | Stellungswiederholung nicht implementiert | Partien können sich in Schleifen verfangen | Risiko 11.2 |
> | TS-3 | Endspieldatenbank nicht angebunden | Gewonnene Endspiele werden möglicherweise nicht sicher gewonnen | Technischer Kontext 3.2 |
> | TS-4 | Eröffnungsbibliothek niedrig priorisiert | Eröffnungsphase basiert allein auf Algorithmen | Risiko 11.2 |
> ```

#### [S11-04] Risiken externer Schnittstellen nicht vollständig analysiert

**Schwere:** 🟡 Empfehlung  
**Datei:** `arc-doc/11-Risiken/` (Sektionsebene)  
**Kriterium:** Wurden externe Schnittstellen auf Risiken analysiert?

**Befund:** Polyglot Opening Book und Computergegner nicht als Risikoquellen betrachtet.

#### [S11-05] Stakeholder-Perspektive bei Risiko-Identifikation nicht erkennbar

**Schwere:** 🟢 Hinweis  
**Datei:** `arc-doc/11-Risiken/` (Sektionsebene)  
**Kriterium:** Wurde mit verschiedenen Stakeholdern nach Risiken gesucht?

**Befund:** Risiken aus Zielgruppen-Sicht (z.B. „Beispiel zu komplex für Einsteiger") fehlen.

#### [S11-06] Veraltete Zeitangaben in Risiko 11.2

**Schwere:** 🟢 Hinweis  
**Datei:** `arc-doc/11-Risiken/11-02-Aufwand.md`  
**Kriterium:** Ist die Liste für Management-Stakeholder nutzbar?

**Befund:** Referenziert Termine aus 2011. Status unklar (historisch oder aktuell?).

#### [S11-07] Quellcode-Risiken nicht analysiert

**Schwere:** 🟢 Hinweis  
**Datei:** `arc-doc/11-Risiken/` (Sektionsebene)  
**Kriterium:** Wurde Quellcode auf Risiken analysiert?

**Befund:** Keine Risiken aus Codequalität, Architektur oder Drittbibliotheken identifiziert.

---

### Sektion 12 — Glossar

#### [S12-01] Fehlender Glossareintrag: Stellung

**Schwere:** 🔴 Kritisch  
**Datei:** `arc-doc/12-Glossar/12-02-Begriffe.md`  
**Kriterium:** Begriffsauswahl — domänenspezifische Begriffe

**Befund:** „Stellung" ist das zentrale Konzept des Domänenmodells und wird in praktisch jeder Sektion verwendet. Fehlt im Glossar.

**Änderungsvorschlag:**
> ```markdown
> | Stellung | Darstellung der gesamten Spielsituation auf dem Schachbrett. Umfasst neben den Positionen der Figuren auch die Information, wer am Zug ist, welche Rochaden noch möglich sind und ob ein en-passant-Schlag erlaubt ist. In DokChess als unveränderliches (immutable) Objekt implementiert (→ Domänenmodell 8.2, Entscheidung 9.2). |
> ```

#### [S12-02] Fehlender Glossareintrag: Spielbaum

**Schwere:** 🟡 Empfehlung  
**Datei:** `arc-doc/12-Glossar/12-02-Begriffe.md`  
**Kriterium:** Technische Begriffe aus dem Computerschach

**Befund:** Zentraler Begriff der Zugsuche. Minimax und Alpha-Beta-Suche sind definiert, Spielbaum nicht.

#### [S12-03] Fehlender Glossareintrag: Bitboard

**Schwere:** 🟡 Empfehlung  
**Datei:** `arc-doc/12-Glossar/12-02-Begriffe.md`  
**Kriterium:** Konsistenz mit ADR 09-03

**Befund:** Wird in Entscheidung 09-03 und Qualitätsszenario W05 verwendet. Spezifischer Computerschach-Fachbegriff ohne Glossareintrag.

#### [S12-04] Tippfehler im Eintrag „Schach960"

**Schwere:** 🟢 Hinweis  
**Datei:** `arc-doc/12-Glossar/12-02-Begriffe.md`  
**Kriterium:** Definitionsqualität

**Befund:** „bei die Anfangsstellung" statt „bei der die Anfangsstellung".

#### [S12-05] Fehlender Glossareintrag: UCI

**Schwere:** 🟢 Hinweis  
**Datei:** `arc-doc/12-Glossar/12-02-Begriffe.md`  
**Kriterium:** Konsistenz mit ADR 09-01

**Befund:** UCI als Alternative in Entscheidung 09-01 diskutiert, aber nicht im Glossar definiert.

#### [S12-06] Kein Verweis zwischen Glossar und Domänenmodell

**Schwere:** 🟡 Empfehlung  
**Datei:** `arc-doc/12-Glossar/12-01-Einstieg.md`  
**Kriterium:** Zusammenspiel mit Konzepten

**Befund:** Das Glossar verweist nicht auf das Domänenmodell als ergänzende Quelle.

#### [S12-07] Inkonsistenz: 2D-Array vs. Bitboards

**Schwere:** 🟡 Empfehlung  
**Datei:** `arc-doc/12-Glossar/12-02-Begriffe.md`  
**Kriterium:** Konsistenz mit dem Rest der Dokumentation

**Befund:** Domänenmodell (08-02) beschreibt 2D-Array, ADR 09-03 wählt Bitboards. Bei Aufnahme von „Stellung" muss die Definition implementierungsneutral formuliert werden.

---

## Sektionsübergreifende Konflikte — Detailbefunde

### Qualitätsstrang (S1 ↔ S4 ↔ S10)

#### [KQS-01] Bezeichnungskonflikt beim Qualitätsziel „Spielstärke"

**Konflikttyp:** K2 — Widersprüchliche Aussagen  
**Schwere:** 🟡 Warnung  
**Betroffene Dateien:**
- `01-02-Qualitaetsziele.md` — „**Akzeptable Spielstärke** (Funktionale Eignung)"
- `04-01-Einstieg.md` — „**Attraktive Spielstärke** (Attraktivität)"

**Beschreibung:** Sowohl der Name als auch das zugeordnete ISO-25010-Qualitätsmerkmal weichen ab.

**Lösungsvorschlag:** In `04-01-Einstieg.md` die Bezeichnung zu „Akzeptable Spielstärke (Funktionale Eignung)" vereinheitlichen.

#### [KQS-02] Widerspruch zur Effizienz des Domänenmodells innerhalb von S4

**Konflikttyp:** K2 — Widersprüchliche Ansätze  
**Schwere:** 🟡 Warnung  
**Betroffene Dateien:**
- `04-01-Einstieg.md` — Unter Effizienz: „Effiziente Implementierung des Domänenmodells"
- `04-02-Aufbau.md` — „bewusst eine bessere Verständlichkeit angestrebt, **auf Kosten von Effizienz**"

**Beschreibung:** Direkter Widerspruch innerhalb der Lösungsstrategie. S4.1 listet „Effiziente Implementierung des Domänenmodells", S4.2 stellt das Gegenteil fest.

**Lösungsvorschlag:** In `04-01-Einstieg.md` den irreführenden Punkt ersetzen durch: „Domänenmodell priorisiert Lesbarkeit; Effizienz wird über algorithmische Optimierungen (Alpha-Beta) kompensiert"

#### [KQS-03] Verwaiste Szenarien Z01/Z02 ohne Qualitätsziel und Strategie

**Konflikttyp:** K4 — Verwaiste Szenarien  
**Schwere:** 🟡 Warnung  
**Betroffene Dateien:**
- `10-02-Qualitaetsszenarien.md` — Z01, Z02 (Zuverlässigkeit)
- `01-02-Qualitaetsziele.md` — kein Qualitätsziel für Zuverlässigkeit

**Lösungsvorschlag:** Ergänzendes Qualitätsziel „Robuster Umgang mit Fehlbedienung (Zuverlässigkeit)" aufnehmen, oder die Szenarien als nicht zielgebunden kennzeichnen.

#### [KQS-04] Prioritätsumkehr: Spielstärke hat mehr Szenarien als höher priorisierte Ziele

**Konflikttyp:** K3 — Inkonsistente Priorisierung  
**Schwere:** 🟢 Hinweis

**Befund:** Spielstärke (Priorität 4) hat 4 Szenarien, Analysierbarkeit (Priorität 1) hat 3. Erklärenden Satz ergänzen.

#### [KQS-05] Szenario P01 nicht eindeutig zugeordnet

**Konflikttyp:** K4  
**Schwere:** 🟢 Hinweis

**Befund:** P01 beschreibt inhaltlich Änderbarkeit, ist aber als „Portabilität" gekennzeichnet.

#### [KQS-06] Messbarkeitsdefizit bei Szenario W02 und W03

**Konflikttyp:** K5  
**Schwere:** 🟢 Hinweis

**Befund:** W02 und W03 enthalten nur qualitative Akzeptanzkriterien („unverzüglich", „ohne Umwege").

---

### Strategie ↔ Entscheidungen (S4 ↔ S9)

#### [KSE-01] Bitboard-Entscheidung widerspricht strategischem Grundprinzip

**Konflikttyp:** K1 — Direkter Widerspruch  
**Schwere:** 🔴 Kritisch  
**Betroffene Dateien:**
- `04-02-Aufbau.md` — „bewusst bessere Verständlichkeit angestrebt, auf Kosten von Effizienz"
- `09-03-Brettrepraesentation.md` — Entscheidung für Bitboards mit explizitem Effizienz-Primat

**Lösungsvorschlag:** In `04-02-Aufbau.md` eine Ausnahme für die interne Brettrepräsentation dokumentieren, mit Verweis auf ADR 09-03.

#### [KSE-02] Bitboard-Entscheidung widerspricht OO-Domänenmodell-Ansatz

**Konflikttyp:** K1 — Direkter Widerspruch  
**Schwere:** 🔴 Kritisch  
**Betroffene Dateien:**
- `04-01-Einstieg.md` — „Explizites, objektorientiertes Domänenmodell"
- `09-03-Brettrepraesentation.md` — Entscheidung gegen OO-Modell

**Lösungsvorschlag:** In `04-01-Einstieg.md` den Eintrag differenzieren: „Objektorientiertes Domänenmodell an den Modulgrenzen; intern leistungsoptimierte Brettrepräsentation"

#### [KSE-03] Strategie nicht aktualisiert nach ADR 09-03

**Konflikttyp:** K3 — Veraltete Strategie  
**Schwere:** 🔴 Kritisch  
**Betroffene Dateien:**
- `04-01-Einstieg.md`, `04-02-Aufbau.md` — kein Verweis auf ADR 09-03
- `09-03-Brettrepraesentation.md` — strategisch hochrelevante Entscheidung

**Lösungsvorschlag:** In `04-02-Aufbau.md` Absatz zur Brettrepräsentation ergänzen. In `04-01-Einstieg.md` Effizienz-Tabelle um Bitboard-Verweis ergänzen.

#### [KSE-04] ADR 09-03 konterkariert Qualitätsziel „Experimentierplattform"

**Konflikttyp:** K1  
**Schwere:** 🟡 Warnung

**Befund:** ADR nennt „hohe Einstiegshürde für neue Entwickler". Milderung: öffentliche Schnittstellen bleiben.

#### [KSE-05] Redundanz bei XBoard-Protokoll (S4 ↔ S9)

**Konflikttyp:** K2 — Redundanz  
**Schwere:** 🟢 Hinweis  
**Befund:** Querverweis vorhanden. **Gutes Alignment, kein Handlungsbedarf.**

#### [KSE-06] Redundanz bei Unveränderlichkeit (S4 ↔ S9)

**Konflikttyp:** K2 — Redundanz  
**Schwere:** 🟢 Hinweis  
**Befund:** Rollenverteilung (Strategie = „Was", ADR = „Warum") eingehalten. **Gutes Alignment.**

#### [KSE-07] Fehlende ADR für Minimax/Alpha-Beta-Algorithmus-Wahl

**Konflikttyp:** K4 — Strategie ohne Entscheidungsgrundlage  
**Schwere:** 🟡 Warnung

**Befund:** Grundlegende Architekturentscheidung ohne ADR. Alternativen (MCTS, Negamax) nicht dokumentiert.

#### [KSE-08] ADR 09-03 ohne Rückverweis auf negativ betroffene Qualitätsziele

**Konflikttyp:** K3  
**Schwere:** 🟡 Warnung

**Befund:** ADR referenziert nur Effizienz und Spielstärke, nicht die negativ betroffenen Ziele Analysierbarkeit und Änderbarkeit.

---

### Constraint-Compliance (S2 ↔ S4/S8/S9)

#### [KRC-01] Bitboards widerspricht Designprinzip „Verständlichkeit vor Effizienz"

**Konflikttyp:** K4  
**Schwere:** 🔴 Kritisch  
**Betroffene Dateien:** `04-02-Aufbau.md`, `09-03-Brettrepraesentation.md`

#### [KRC-02] Domänenmodell beschreibt 2D-Array, Entscheidung wählt Bitboards

**Konflikttyp:** K1  
**Schwere:** 🔴 Kritisch  
**Betroffene Dateien:** `08-02-Domaenenmodell.md`, `09-03-Brettrepraesentation.md`

**Lösungsvorschlag:** `08-02-Domaenenmodell.md` aktualisieren: 2D-Array-Passage durch Bitboard-Referenz ersetzen.

#### [KRC-03] Bitboards untergraben OO-Domänenmodell-Ansatz für Analysierbarkeit

**Konflikttyp:** K4  
**Schwere:** 🟡 Warnung

#### [KRC-04] Bitboard-Terminologie verletzt Konvention deutscher Bezeichner

**Konflikttyp:** K3  
**Schwere:** 🟡 Warnung  
**Betroffene Dateien:** `02-03-Konventionen.md`, `09-03-Brettrepraesentation.md`

**Lösungsvorschlag:** Konvention um Ausnahme für etablierte Fachtermini der Schachprogrammierung ergänzen.

#### [KRC-05] Bitboard-Komplexität potentiell inkompatibel mit CheckStyle

**Konflikttyp:** K3  
**Schwere:** 🟡 Warnung  
**Betroffene Dateien:** `02-03-Konventionen.md`, `09-03-Brettrepraesentation.md`

---

### Kontext ↔ Bausteine (S3 ↔ S5)

#### [KKB-01] Computergegner ohne Entsprechung in S5

**Konflikttyp:** K1  
**Schwere:** 🟡 Warnung

**Lösungsvorschlag:** Im technischen Kontext explizit vermerken, dass der XBoard Client sowohl menschliche Gegner als auch andere Engines vermittelt.

#### [KKB-02] Endspiele ohne Erwähnung in S5

**Konflikttyp:** K1  
**Schwere:** 🟢 Hinweis

**Lösungsvorschlag:** In `05-01-Ebene-1.md` einen Absatz „Nicht realisierte Schnittstellen" ergänzen.

#### [KKB-03] Terminologie: „Eröffnungen" (S3, Plural) vs. „Eröffnung" (S5, Singular)

**Konflikttyp:** K3  
**Schwere:** 🟢 Hinweis

#### [KKB-04] Remisangebote im Kontext versprochen, in S5 als nicht unterstützt gelistet

**Konflikttyp:** K4  
**Schwere:** 🟡 Warnung

**Lösungsvorschlag:** Im fachlichen Kontext den betreffenden Satz anpassen: „Weitergehende Interaktionen wie Remisangebote sind denkbar, werden aber in der aktuellen Umsetzung nicht unterstützt."

#### [KKB-05] Bausteinsicht referenziert nur technischen Kontext, nicht den fachlichen

**Konflikttyp:** K3  
**Schwere:** 🟢 Hinweis

---

### Sichten-Konsistenz (S5 ↔ S6 ↔ S7)

#### [KSV-01] Eröffnungs-Subsystem hat kein Deployment-Mapping

**Konflikttyp:** K3 + K2  
**Schwere:** 🟡 Warnung

**Befund:** S5 definiert das Subsystem, S6 nutzt es aktiv, aber S7 zeigt nur die Variante ohne Eröffnungsbibliothek.

**Lösungsvorschlag:** Zweites Deployment-Szenario mit Eröffnungsbibliothek ergänzen.

#### [KSV-02] Namensinkonsistenz: „Eröffnung" vs. „Eröffnungsbibliothek"

**Konflikttyp:** K1  
**Schwere:** 🟢 Hinweis

#### [KSV-03] Ebene-2-Module ohne explizite Laufzeitdarstellung

**Konflikttyp:** K5 + K3  
**Schwere:** 🟢 Hinweis

**Lösungsvorschlag:** In `06-01-Zugermittlung.md` die Module Zugsuche und Stellungsbewertung namentlich nennen.

#### [KSV-04] Laufzeitszenario zeigt Eröffnungsbibliothek nur als Negativfall

**Konflikttyp:** K6  
**Schwere:** 🟢 Hinweis

#### [KSV-05] Verteilungssicht operiert auf gröberer Granularität

**Konflikttyp:** K5  
**Schwere:** 🟢 Hinweis

**Lösungsvorschlag:** In `07-01-Infrastruktur-Windows.md` explizit machen, dass alle Subsysteme im selben Artefakt enthalten sind.

---

### Konzepte ↔ Entscheidungen (S8 ↔ S9)

#### [KKE-01] Domänenmodell beschreibt 2D-Array, Entscheidung wählt Bitboards

**Konflikttyp:** K1 — Direkter Widerspruch  
**Schwere:** 🔴 Kritisch  
**Betroffene Dateien:** `08-02-Domaenenmodell.md`, `09-03-Brettrepraesentation.md`

**Lösungsvorschlag:** Die 2D-Array-Passage in `08-02-Domaenenmodell.md` entfernen und durch Bitboard-Referenz ersetzen.

#### [KKE-02] Domänenmodell Figur-auf-Feld-Semantik inkompatibel mit Bitboards

**Konflikttyp:** K1  
**Schwere:** 🟡 Warnung

**Lösungsvorschlag:** Erklärenden Absatz zur Beziehung zwischen fachlichem Modell und interner Repräsentation ergänzen.

#### [KKE-03] Entscheidung „Kein DI-Framework" in Konzept-Sektion statt in Entscheidungen

**Konflikttyp:** K2 — Falsche Zuordnung  
**Schwere:** 🟡 Warnung

**Lösungsvorschlag:** Eigenständige Entscheidung `09-04-DI-Framework.md` im ADR-Format anlegen.

#### [KKE-04] Entscheidung gegen Logging-Framework in Konzept-Sektion

**Konflikttyp:** K2  
**Schwere:** 🟢 Hinweis

#### [KKE-05] Bitboard-Entscheidung ohne querschnittliches Konzept

**Konflikttyp:** K5  
**Schwere:** 🟡 Warnung

**Lösungsvorschlag:** Neues Konzept `08-08-Brettrepraesentation.md` in S8 anlegen.

#### [KKE-06] Testkonzept referenziert OO-Modell ohne Hinweis auf Bitboard-Interna

**Konflikttyp:** K1  
**Schwere:** 🟢 Hinweis

---

### Risiken ↔ Qualität (S11 ↔ S1/S10)

#### [KRQ-01] Qualitätsziel „Analysierbarkeit" ohne Risikobetrachtung

**Konflikttyp:** K1 — Blinder Fleck  
**Schwere:** 🟡 Warnung

**Befund:** Das höchstpriorisierte Qualitätsziel hat keinen korrespondierenden Risikoeintrag.

#### [KRQ-02] Qualitätsziel „Änderbarkeit" ohne Risikobetrachtung

**Konflikttyp:** K1  
**Schwere:** 🟡 Warnung

#### [KRQ-03] Effizienz-Risiko nur implizit in R3

**Konflikttyp:** K2 — Unmitigiertes Qualitätsrisiko  
**Schwere:** 🟡 Warnung

**Befund:** Szenarien E01 und E02 definieren harte Zeitgrenzen (5s/10s), die nicht systematisch abgesichert werden.

#### [KRQ-04] Aufwandsreduktion (R2) gefährdet Spielstärke-Szenarien

**Konflikttyp:** K3  
**Schwere:** 🟢 Hinweis

#### [KRQ-05] Zuverlässigkeitsszenarien ohne Risikoeintrag

**Konflikttyp:** K4  
**Schwere:** 🟢 Hinweis

#### [KRQ-06] Risikobewertung inkonsistent mit Qualitätspriorität

**Konflikttyp:** K5 — Inkonsistente Priorisierung  
**Schwere:** 🟡 Warnung

**Befund:** Alle drei Risiken adressieren QZ3–QZ5, keines die beiden Top-Qualitätsziele QZ1/QZ2.

---

## Fazit

Die DokChess arc42-Dokumentation ist **strukturell vollständig** — alle 12 Sektionen sind vorhanden und inhaltlich substantiell gefüllt. Die Stärken liegen in der klaren Bausteinsicht, den gut strukturierten ADRs und der lückenlosen Abdeckung aller Qualitätsziele durch Szenarien.

Das **zentrale Problem** ist die nachträglich hinzugefügte Bitboard-Entscheidung (ADR 09-03), die tiefgreifende Auswirkungen auf die Dokumentationskonsistenz hat: Sie widerspricht dem strategischen Grundprinzip „Verständlichkeit vor Effizienz" (S4), dem Domänenmodell (S8), den deutschen Bezeichner-Konventionen (S2) und fehlt als Querverweis in S4. Von den insgesamt 6 kritischen sektionsübergreifenden Konflikten gehen **alle 6** auf ADR 09-03 zurück.

**Priorisierter Handlungsplan:**

1. **Sofort:** Lösungsstrategie (S4) und Domänenmodell (S8) an die Bitboard-Entscheidung anpassen
2. **Kurzfristig:** Technische Schulden dokumentieren (S11), Baustein-Mapping in S7, Ein-/Ausgaben in S3
3. **Mittelfristig:** Querverweise in S8, Nebenläufigkeitskonzept, Glossar-Ergänzungen, Qualitätsbaum textuell

---

## Statistik

| Kategorie | Kritisch (🔴) | Empfehlung/Warnung (🟡) | Hinweis (🟢) | Gesamt |
|---|---|---|---|---|
| Sektions-Reviews | 7 | 30 | 25 | 62 |
| Konfliktanalysen | 6 | 19 | 14 | 39 |
| **Gesamt** | **13** | **49** | **39** | **101** |
