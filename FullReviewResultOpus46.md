# arc42 Dokumentations-Review

## Gesamtübersicht

| Sektion | Status | Befunde |
|---------|--------|---------|
| 1. Einführung und Ziele | 🟡 | Qualitätsziele unscharf formuliert, Stakeholder-Tabelle weicht vom arc42-Template ab, Endbenutzer fehlen |
| 2. Randbedingungen | 🟡 | Konsequenzen und Freiheitsgrade nicht dokumentiert, Tippfehler |
| 3. Kontextabgrenzung | 🟡 | Fachliche Ein-/Ausgaben nicht systematisch, Mapping fachlich↔technisch fehlt |
| 4. Lösungsstrategie | 🔴 | Inkonsistente Benennung „Attraktive" vs. „Akzeptable" Spielstärke gegenüber S1 |
| 5. Bausteinsicht | 🟡 | Begründung der Zerlegung fehlt, Endspiel-Schnittstelle aus S3 nicht erwähnt |
| 6. Laufzeitsicht | 🟡 | Nur ein Szenario, Fehler-/Ausnahmefälle und Eröffnungstreffer fehlen |
| 7. Verteilungssicht | 🟡 | Motivation fehlt, kein Baustein-Mapping, nur Windows dokumentiert |
| 8. Querschnittliche Konzepte | 🟡 | Vermischung von Konzepten und Entscheidungen in 8.1 und 8.6, fehlende Rückverweise |
| 9. Architekturentscheidungen | 🟡 | ADRs für Reactive Extensions, Algorithmuswahl etc. fehlen |
| 10. Qualitätsanforderungen | 🟡 | Qualitätsbaum nur als Bild, Szenarien nicht explizit strukturiert |
| 11. Risiken und techn. Schulden | 🔴 | Technische Schulden fehlen vollständig, keine Priorisierung |
| 12. Glossar | 🟡 | Zentrale Begriffe „Stellung" und „Spielbaum" fehlen |

## Sektions-Reviews

### Sektion 1: Einführung und Ziele

| ID | Schwere | Titel |
|---|---|---|
| S01-01 | 🟢 | Redundante Überschriftenebenen in allen drei Dateien |
| S01-02 | 🟢 | Fehlender Verweis auf Anforderungsdokumente |
| S01-03 | 🟡 | Treibende Kräfte / Business-Ziele nicht explizit herausgearbeitet |
| S01-04 | 🟡 | Qualitätsziele nicht ausreichend messbar formuliert |
| S01-05 | 🟡 | Stakeholder-Tabelle weicht vom arc42-Template ab |
| S01-06 | 🟡 | Fehlende Stakeholder-Gruppe: Endbenutzer (Schachspieler) |

#### [S01-01] Redundante Überschriftenebenen in allen drei Dateien

**Schwere:** 🟢 Hinweis
**Datei:** `arc-doc/01-Einfuehrung-und-Ziele/01-01-Aufgabenstellung.md`, `01-02-Qualitaetsziele.md`, `01-03-Stakeholder.md`
**Kriterium:** Formale Struktur

**Befund:** Alle drei Dateien enthalten eine `#`-Überschrift (z. B. `# Aufgabenstellung`) gefolgt von einer `##`-Überschrift mit identischem bzw. nummeriertem Inhalt (`## 1.1 Aufgabenstellung`). Diese Dopplung ist redundant, da die Sektionsnummer bereits durch die Dateistruktur gegeben ist.

**Änderungsvorschlag:**
> Jeweils die `#`-Überschrift entfernen und die `##`-Überschrift als Hauptüberschrift beibehalten, oder die `##`-Überschrift entfernen und die `#`-Überschrift mit Nummerierung versehen (z. B. `# 1.1 Aufgabenstellung`).

---

#### [S01-02] Fehlender Verweis auf Anforderungsdokumente

**Schwere:** 🟢 Hinweis
**Datei:** `arc-doc/01-Einfuehrung-und-Ziele/01-01-Aufgabenstellung.md`
**Kriterium:** Formale Prüfung – Verweise auf existierende Anforderungsdokumente

**Befund:** Es existiert kein Verweis auf weiterführende Anforderungsdokumente (z. B. ein Backlog, eine Feature-Liste oder ein Requirements-Dokument). Für ein Demonstrationsprojekt wie DokChess ist das tolerierbar, aber ein expliziter Hinweis, dass keine separaten Anforderungsdokumente existieren, würde die Vollständigkeit der Sektion verbessern.

**Änderungsvorschlag:**
> Am Ende des Abschnitts „Wesentliche Features" folgenden Satz ergänzen:
>
> _Eine separate, ausführlichere Anforderungsdokumentation existiert für DokChess nicht. Die hier aufgeführten Features stellen den vollständigen funktionalen Umfang dar._

---

#### [S01-03] Treibende Kräfte / Business-Ziele nicht explizit herausgearbeitet

**Schwere:** 🟡 Empfehlung
**Datei:** `arc-doc/01-Einfuehrung-und-Ziele/01-01-Aufgabenstellung.md`
**Kriterium:** Inhaltliche Prüfung – Business-Ziele und treibende Kräfte

**Befund:** Die Business-Ziele (Lehr- und Anschauungszweck) sind im Fließtext unter „Was ist DokChess?" eingebettet, aber nicht als eigenständiger Aspekt hervorgehoben. Arc42 empfiehlt, die treibenden Kräfte explizit herauszuarbeiten, damit Leser sofort erkennen, warum das System existiert.

**Änderungsvorschlag:**
> Einen zusätzlichen Unterabschnitt oder eine explizite Einleitung ergänzen:
>
> ```markdown
> ### Treibende Kräfte
>
> DokChess wurde primär als Anschauungsmaterial für Architekturdokumentation,
> -entwurf und -bewertung konzipiert. Es soll in Workshops, Seminaren und
> Fachbüchern eingesetzt werden. Eine möglichst hohe Spielstärke ist dabei
> nachrangig gegenüber Verständlichkeit und Erweiterbarkeit.
> ```

---

#### [S01-04] Qualitätsziele nicht ausreichend messbar formuliert

**Schwere:** 🟡 Empfehlung
**Datei:** `arc-doc/01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md`
**Kriterium:** Inhaltliche Prüfung – Konkretheit und Messbarkeit der Qualitätsziele

**Befund:** Mehrere Qualitätsziele verwenden unscharfe Formulierungen, die für sich allein nicht messbar sind: „erschließen sich … rasch", „leicht implementiert", „mit angemessenem Aufwand", „stark genug", „rasch". Der Verweis auf Sektion 10 mildert dies ab, da dort Szenarien definiert werden. Dennoch sollten die Qualitätsziele selbst konkreter gefasst sein, damit die Tabelle auch ohne Sektion 10 aussagekräftig ist.

**Änderungsvorschlag:**
> Die Tabelle um eine Spalte „Messkriterium" erweitern oder die Formulierungen präzisieren, z. B.:
>
> | Qualitätsziel | Motivation und Erläuterung | Messkriterium |
> | --- | --- | --- |
> | Zugängliches Beispiel (Analysierbarkeit) | … | Ein Entwickler kann die Struktur innerhalb von 1 Stunde verstehen |
> | Schnelles Antworten auf Züge (Effizienz) | … | Antwortzeit < 10 Sekunden pro Zug in typischen Mittelspielpositionen |

---

#### [S01-05] Stakeholder-Tabelle: Spaltenstruktur weicht vom arc42-Template ab

**Schwere:** 🟡 Empfehlung
**Datei:** `arc-doc/01-Einfuehrung-und-Ziele/01-03-Stakeholder.md`
**Kriterium:** Formale Prüfung – Stakeholder-Tabelle mit Rolle, Name/Beschreibung und Erwartungen

**Befund:** Die Tabelle verwendet die Spalten „Wer?" und „Interesse, Bezug". Das arc42-Template sieht die Spalten „Rolle", „Kontakt" und „Erwartungshaltung" vor. Die aktuelle Struktur vermischt Rollen und konkrete Personen/Organisationen in derselben Spalte, ohne klare Unterscheidung.

**Änderungsvorschlag:**
> Tabelle umstrukturieren:
>
> | Rolle | Kontakt | Erwartungshaltung |
> | --- | --- | --- |
> | Softwarearchitekt:innen | (diverse Leser:innen) | Wollen ein Gefühl bekommen, wie Architekturdokumentation aussehen kann |
> | Entwickler:innen | (diverse Leser:innen) | Suchen Anregungen zur Implementierung einer Schach-Engine |
> | Autor / Initiator | Stefan Zörner | Benötigt Beispiele für Buch, Workshops und Vorträge |
> | Schulungsunternehmen | oose Innovative Informatik | Nutzt DokChess als Schulungsmaterial |

---

#### [S01-06] Fehlende Stakeholder-Gruppe: Endbenutzer (Schachspieler)

**Schwere:** 🟡 Empfehlung
**Datei:** `arc-doc/01-Einfuehrung-und-Ziele/01-03-Stakeholder.md`
**Kriterium:** Inhaltliche Prüfung – Vollständigkeit der Stakeholder-Gruppen

**Befund:** Schachspieler:innen, die DokChess tatsächlich zum Spielen nutzen, fehlen in der Stakeholder-Tabelle. Da in der Aufgabenstellung explizit „Partien, die Gelegenheitsspielern Freude bereiten" erwähnt wird, sind diese als Stakeholder zu berücksichtigen.

**Änderungsvorschlag:**
> Folgenden Eintrag in die Stakeholder-Tabelle aufnehmen:
>
> | Schachspieler:innen (Gelegenheitsspieler) | Erwarten akzeptable Spielstärke, regelkonformes Verhalten und flüssige Interaktion über das Schach-Frontend |

---

### Sektion 2: Randbedingungen

| ID | Schwere | Titel |
|---|---|---|
| S02-01 | 🟡 | Fehlende Konsequenzen der Randbedingungen |
| S02-02 | 🟡 | Fehlende Darstellung der Freiheitsgrade |
| S02-03 | 🟢 | Tippfehler „Schulungsunternehmenin" |
| S02-04 | 🟡 | Fehlende Design- und Entwicklungseinschränkungen |
| S02-05 | 🟢 | Fehlende einleitende Übersicht zur Sektion |

#### [S02-01] Fehlende Konsequenzen der Randbedingungen

**Schwere:** 🟡 Empfehlung
**Datei:** Alle drei Dateien der Sektion
**Kriterium:** Werden die Konsequenzen der Constraints erläutert?

**Befund:** Die Tabellen enthalten jeweils die Spalten „Randbedingung" und „Erläuterungen, Hintergrund". Hintergrund und Motivation werden gut beschrieben, jedoch fehlt eine explizite Darstellung der Konsequenzen für die Architektur.

**Änderungsvorschlag:**
> Ergänze in jeder Tabelle eine dritte Spalte **„Konsequenzen"** oder füge unter jeder Tabelle einen Absatz hinzu, der die architektonischen Auswirkungen zusammenfasst.

---

#### [S02-02] Fehlende Darstellung der Freiheitsgrade

**Schwere:** 🟡 Empfehlung
**Datei:** Alle drei Dateien der Sektion
**Kriterium:** Ist klar, wo die Architekten Freiheitsgrade haben und wo nicht?

**Befund:** Die Randbedingungen beschreiben, was eingeschränkt ist, aber es wird nicht explizit gemacht, wo die Architekten Gestaltungsspielraum haben.

**Änderungsvorschlag:**
> Ergänze am Ende der Sektion einen Abschnitt „Freiheitsgrade", der die nicht eingeschränkten Entscheidungsbereiche auflistet (z.B. Architekturstil, Bibliothekenwahl, interne Datenstrukturen).

---

#### [S02-03] Tippfehler in organisatorischen Randbedingungen

**Schwere:** 🟢 Hinweis
**Datei:** `arc-doc/02-Randbedingungen/02-02-Organisatorisch.md`
**Kriterium:** Formale Korrektheit

**Befund:** Im Zeitplan-Eintrag ist „Schulungsunternehmenin" zusammengeschrieben statt „Schulungsunternehmen in".

**Änderungsvorschlag:**
> Ersetze `Schulungsunternehmenin` durch `Schulungsunternehmen in`.

---

#### [S02-04] Fehlende Design- und Entwicklungseinschränkungen im technischen Abschnitt

**Schwere:** 🟡 Empfehlung
**Datei:** `arc-doc/02-Randbedingungen/02-01-Technisch.md`
**Kriterium:** Werden Design- und Entwicklungseinschränkungen erfasst?

**Befund:** Die technischen Randbedingungen konzentrieren sich auf Hardware, Betriebssystem, Programmiersprache und Fremdsoftware. Explizite Design-Einschränkungen fehlen — etwa Offline-Fähigkeit und Verzicht auf eine Datenbank.

**Änderungsvorschlag:**
> Ergänze in der Tabelle zusätzliche Zeilen für Offline-Betrieb und fehlende externe Datenbank.

---

#### [S02-05] Fehlende einleitende Übersicht zur Sektion

**Schwere:** 🟢 Hinweis
**Datei:** Alle drei Dateien der Sektion
**Kriterium:** Formale Vollständigkeit

**Befund:** Es fehlt eine kurze einleitende Beschreibung, die die drei Kategorien von Randbedingungen einordnet.

**Änderungsvorschlag:**
> Ergänze am Anfang einen kurzen Einleitungstext, der die Kategorien (technisch, organisatorisch, Konventionen) einordnet.

---

### Sektion 3: Kontextabgrenzung

| ID | Schwere | Titel |
|---|---|---|
| S03-01 | 🟡 | Fachliche Ein-/Ausgaben nicht systematisch spezifiziert |
| S03-02 | 🟡 | Datenflüsse bei Eröffnungen und Endspielen nicht beschrieben |
| S03-03 | 🟡 | Kein explizites Mapping fachlich ↔ technisch |
| S03-04 | 🟢 | Endspiele im technischen Kontext nur als Negativabgrenzung |
| S03-05 | 🟡 | Keine Qualitätsanforderungen an externe Schnittstellen |
| S03-06 | 🟢 | Konsistenz mit Bausteinsicht gegeben (kein Befund) |

#### [S03-01] Fachliche Ein-/Ausgaben nicht systematisch spezifiziert

**Schwere:** 🟡 Empfehlung
**Datei:** `arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md`
**Kriterium:** Werden alle Kommunikationspartner mit fachlichen Ein-/Ausgaben spezifiziert?

**Befund:** Für den menschlichen Gegner werden beispielhaft Züge und Remisangebote als Austauschdaten genannt. Für die Fremdsysteme Eröffnungen und Endspiele fehlt eine explizite Angabe. Eine begleitende Tabelle der Kommunikationspartner mit ihren Ein-/Ausgaben fehlt vollständig.

**Änderungsvorschlag:**
> Nach dem Diagramm eine Tabelle ergänzen:
>
> | Kommunikationspartner | Fachliche Eingabe | Fachliche Ausgabe |
> |---|---|---|
> | Menschlicher Gegner | Züge, Remisangebote, Aufgabe | Züge, Remisangebote |
> | Computergegner | Züge, Remisangebote, Aufgabe | Züge, Remisangebote |
> | Eröffnungsbibliothek | Aktuelle Stellung | Eröffnungszug (optional) |
> | Endspielbibliothek | Aktuelle Stellung | Bewertung, optimaler Zug |

---

#### [S03-02] Datenflüsse bei Eröffnungen und Endspielen nicht beschrieben

**Schwere:** 🟡 Empfehlung
**Datei:** `arc-doc/03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md`
**Kriterium:** Werden Datenflüsse im fachlichen Kontext gezeigt?

**Befund:** Die Abschnitte zu Eröffnungen und Endspielen beschreiben den Zweck, aber nicht die konkreten Datenflüsse.

**Änderungsvorschlag:**
> Im Abschnitt "Eröffnungen" ergänzen: „DokChess übergibt die aktuelle Spielstellung an die Eröffnungsbibliothek und erhält – sofern vorhanden – einen geeigneten Eröffnungszug zurück."

---

#### [S03-03] Kein explizites Mapping zwischen fachlichem und technischem Kontext

**Schwere:** 🟡 Empfehlung
**Datei:** `arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md`
**Kriterium:** Gibt es ein Mapping zwischen fachlichen Ein-/Ausgaben und technischen Kanälen?

**Befund:** Der technische Kontext stellt kein explizites Mapping zu den fachlichen Kommunikationspartnern aus Abschnitt 3.1 her.

**Änderungsvorschlag:**
> Am Anfang von Abschnitt 3.2 eine Mapping-Tabelle ergänzen:
>
> | Fachlicher Partner | Technischer Kanal | Protokoll/Format |
> |---|---|---|
> | Menschlicher Gegner / Computergegner | XBoard Client | XBoard-Protokoll (Stdin/Stdout) |
> | Eröffnungsbibliothek | Polyglot Opening Book | Binäres Dateiformat (lesend) |
> | Endspielbibliothek | — (nicht implementiert) | — |

---

#### [S03-04] Endspiele im technischen Kontext nur als Negativabgrenzung

**Schwere:** 🟢 Hinweis
**Datei:** `arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md`
**Kriterium:** Werden ALLE externen Schnittstellen auch im technischen Kontext abgebildet?

**Befund:** Endspiele werden lediglich als nicht implementiert vermerkt, ohne potenzielle technische Schnittstelle zu skizzieren. Für eine bewusste Designentscheidung ist die Dokumentation akzeptabel.

---

#### [S03-05] Keine Qualitätsanforderungen an externe Schnittstellen

**Schwere:** 🟡 Empfehlung
**Datei:** `arc-doc/03-Kontextabgrenzung/03-02-Technischer-Kontext.md`
**Kriterium:** Werden Qualitätsanforderungen an externen Schnittstellen beachtet?

**Befund:** Der technische Kontext beschreibt weder Performanz- noch Verfügbarkeitsanforderungen der externen Schnittstellen.

**Änderungsvorschlag:**
> Im Abschnitt „XBoard Client" ergänzen: „Die Kommunikation erfolgt synchron über Stdin/Stdout. DokChess muss innerhalb der vom Frontend vorgegebenen Bedenkzeit antworten."

---

### Sektion 4: Lösungsstrategie

| ID | Schwere | Titel |
|---|---|---|
| S04-01 | 🔴 | Inkonsistente Bezeichnung „Attraktive Spielstärke (Attraktivität)" vs. „Akzeptable Spielstärke (Funktionale Eignung)" in S1 |
| S04-02 | 🟡 | Fehlende schließende Klammer im Querverweis |
| S04-03 | 🟢 | Fehlende organisatorische Entscheidungen |
| S04-04 | 🟢 | Grammatikfehler „geeigneter" → „geeigneten" |

#### [S04-01] Inkonsistente Bezeichnung des Qualitätsziels „Spielstärke"

**Schwere:** 🔴 Kritisch
**Datei:** `arc-doc/04-Loesungsstrategie/04-01-Einstieg.md`
**Kriterium:** Konsistenz mit Qualitätszielen aus Sektion 1.2

**Befund:** In der Zuordnungstabelle wird das Qualitätsziel als **„Attraktive Spielstärke (Attraktivität)"** bezeichnet. In `01-02-Qualitaetsziele.md` heißt es jedoch **„Akzeptable Spielstärke (Funktionale Eignung)"**. Sowohl der Name als auch das zugeordnete Qualitätsmerkmal weichen voneinander ab.

**Änderungsvorschlag:**
> In `04-01-Einstieg.md` die Bezeichnung an S1.2 angleichen:
>
> | Akzeptable Spielstärke (Funktionale Eignung) | - Integration von Eröffnungsbibliotheken → **(d)** <br> - Implementierung des Minimax-Algorithmus und einer geeigneten Stellungsbewertung, → **(e)** <br> - Integrationstests mit Schachaufgaben für taktische Motive und Mattsituationen |

---

#### [S04-02] Fehlende schließende Klammer im Querverweis

**Schwere:** 🟡 Empfehlung
**Datei:** `arc-doc/04-Loesungsstrategie/04-02-Aufbau.md`
**Kriterium:** Formale Korrektheit der Verweise

**Befund:** Fehlende schließende Klammer `)` bei kombinierten Querverweisen auf Sektion 5 und Konzept 8.1.

---

#### [S04-03] Fehlende organisatorische Entscheidungen

**Schwere:** 🟢 Hinweis
**Datei:** `arc-doc/04-Loesungsstrategie/` (gesamte Sektion)
**Kriterium:** Dokumentation relevanter organisatorischer Entscheidungen

**Befund:** Die Lösungsstrategie enthält keine Angaben zu organisatorischen Aspekten (Entwicklungsprozess, Build-Werkzeuge). Für ein Beispielprojekt nachvollziehbar.

---

#### [S04-04] Grammatikfehler in Tabellenzelle

**Schwere:** 🟢 Hinweis
**Datei:** `arc-doc/04-Loesungsstrategie/04-01-Einstieg.md`
**Kriterium:** Formale Qualität

**Befund:** „einer **geeigneter** Stellungsbewertung" — korrekt wäre „einer **geeigneten** Stellungsbewertung".

---

### Sektion 5: Bausteinsicht

| ID | Schwere | Titel |
|---|---|---|
| S05-01 | 🟡 | Fehlende Begründung der Zerlegung auf Ebene 1 |
| S05-02 | 🟢 | Tippfehler „Püft" in Spielregeln |
| S05-03 | 🟡 | Endspiel-Schnittstelle aus S3 nicht erwähnt |
| S05-04 | 🟡 | Interne Schnittstellen nur implizit dokumentiert |
| S05-05 | 🟢 | Vage Source-Code-Verweise mit Auslassungszeichen |
| S05-06 | 🟢 | Fehlende Qualitäts-/Leistungsmerkmale (optional) |

#### [S05-01] Fehlende Begründung der Zerlegung auf Ebene 1

**Schwere:** 🟡 Empfehlung
**Datei:** `arc-doc/05-Bausteinsicht/05-01-Ebene-1.md`
**Kriterium:** Whitebox Gesamtsystem — Begründung der Zerlegung

**Befund:** Die Ebene 1 beschreibt die vier Subsysteme und ihre Abhängigkeiten, liefert aber keine Begründung, *warum* das System in genau diese vier Bausteine zerlegt wurde.

**Änderungsvorschlag:**
> Nach dem Diagramm einen Absatz „Begründung der Zerlegung" einfügen, der die fachliche Motivation der Aufteilung erklärt.

---

#### [S05-02] Tippfehler in Spielregeln-Schnittstellenbeschreibung

**Schwere:** 🟢 Hinweis
**Datei:** `arc-doc/05-Bausteinsicht/05-03-Spielregeln.md`
**Kriterium:** Formale Qualität

**Befund:** In der Methodentabelle steht bei `aufSchachPruefen` „Püft" statt „Prüft".

---

#### [S05-03] Endspiel-Schnittstelle aus Sektion 3 nicht in Bausteinsicht erwähnt

**Schwere:** 🟡 Empfehlung
**Datei:** `arc-doc/05-Bausteinsicht/05-01-Ebene-1.md`
**Kriterium:** Konsistenz mit Sektion 3

**Befund:** Der fachliche Kontext (S3.1) nennt „Endspiele" als externes Fremdsystem. In der Bausteinsicht fehlt jegliche Erwähnung dieser bewusst nicht umgesetzten Schnittstelle.

**Änderungsvorschlag:**
> Am Ende von `05-01-Ebene-1.md` einen Abschnitt „Bewusst nicht umgesetzte Schnittstellen" ergänzen, der auf die Endspiel-Entscheidung verweist.

---

#### [S05-04] Interne Schnittstellen zwischen Subsystemen nur implizit dokumentiert

**Schwere:** 🟡 Empfehlung
**Datei:** `arc-doc/05-Bausteinsicht/05-01-Ebene-1.md`
**Kriterium:** Beschreibung wichtiger interner Schnittstellen

**Befund:** Die Abhängigkeiten zwischen den vier Subsystemen werden im Diagramm als gestrichelte Pfeile dargestellt, die Art dieser Abhängigkeiten (welche Schnittstelle genutzt wird) wird auf Ebene 1 nicht beschrieben.

**Änderungsvorschlag:**
> Eine Tabelle der internen Abhängigkeiten ergänzen:
>
> | Von | Nach | Schnittstelle |
> | --- | --- | --- |
> | XBoard-Protokoll | Spielregeln | `Spielregeln` (Interface) |
> | XBoard-Protokoll | Engine | `Engine` (Interface) |
> | Engine | Spielregeln | `Spielregeln` (Interface) |
> | Engine | Eröffnung | `Eroeffnungsbibliothek` (Interface, optional) |

---

### Sektion 6: Laufzeitsicht

| ID | Schwere | Titel |
|---|---|---|
| S06-01 | 🟡 | Fehlende Fehler- und Ausnahmeszenarien |
| S06-02 | 🟡 | Fehlendes Szenario für Eröffnungsbibliothek-Treffer |
| S06-03 | 🟢 | Ebene-2-Bausteine nicht explizit in Szenarien benannt |
| S06-04 | 🟢 | Matt-/Patt-Situation als Szenario fehlt |

#### [S06-01] Fehlende Fehler- und Ausnahmeszenarien

**Schwere:** 🟡 Empfehlung
**Datei:** `arc-doc/06-Laufzeitsicht/06-01-Zugermittlung.md`
**Kriterium:** Werden bei Bedarf Fehler- und Ausnahmeszenarien beschrieben?

**Befund:** Die Laufzeitsicht enthält kein Szenario für Fehlerfälle (ungültige Züge, Matt/Patt, fehlende Eröffnungsbibliothek).

**Änderungsvorschlag:**
> Ergänzung eines Szenarios „Ungültiger Zug", das zeigt, wie das XBoard-Protokoll-Subsystem über die Spielregeln den Zug validiert und bei Ungültigkeit eine Fehlermeldung sendet.

---

#### [S06-02] Fehlendes Szenario für Eröffnungsbibliothek-Treffer

**Schwere:** 🟡 Empfehlung
**Datei:** `arc-doc/06-Laufzeitsicht/06-01-Zugermittlung.md`
**Kriterium:** Werden die wichtigsten Use Cases als Szenarien dargestellt?

**Befund:** Das vorhandene Szenario zeigt explizit den Fall, dass die Eröffnungsbibliothek keinen Treffer liefert. Der komplementäre Pfad — ein Treffer — fehlt, obwohl er architekturrelevant ist (Zugsuche und Stellungsbewertung werden übersprungen).

---

#### [S06-03] Ebene-2-Bausteine der Engine nicht explizit in Szenarien benannt

**Schwere:** 🟢 Hinweis
**Datei:** `arc-doc/06-Laufzeitsicht/06-01-Zugermittlung.md`
**Kriterium:** Werden sowohl kleine als auch große Bausteine in Szenarien eingesetzt?

**Befund:** Das Sequenzdiagramm operiert ausschließlich auf Ebene-1-Subsystemen. Die Ebene-2-Module „Zugsuche" und „Stellungsbewertung" werden nicht namentlich genannt.

**Änderungsvorschlag:**
> Im Fließtext die Ebene-2-Bausteine explizit benennen: „…durchsucht die **Zugsuche** den Spielbaum und verwendet dabei die **Stellungsbewertung**…"

---

### Sektion 7: Verteilungssicht

| ID | Schwere | Titel |
|---|---|---|
| S07-01 | 🟡 | Fehlende Motivation für Verteilungsstruktur |
| S07-02 | 🟡 | Kein explizites Baustein-Mapping auf Infrastruktur |
| S07-03 | 🟡 | Nur Windows-Deployment dokumentiert |
| S07-04 | 🟡 | Deployment-Variante mit Eröffnungsbibliothek fehlt |
| S07-05 | 🟢 | Keine Qualitäts-/Performance-Merkmale |
| S07-06 | 🟢 | Fehlende Entwicklungs-/Testumgebung |

#### [S07-01] Fehlende Motivation für die Verteilungsstruktur

**Schwere:** 🟡 Empfehlung
**Datei:** `arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md`
**Kriterium:** Beschreibung der Motivation für die gewählte Deployment-Struktur

**Befund:** Es wird beschrieben, *wie* DokChess verteilt wird, aber nicht *warum* diese Deployment-Struktur gewählt wurde.

---

#### [S07-02] Kein explizites Mapping der Bausteine auf Infrastruktur-Elemente

**Schwere:** 🟡 Empfehlung
**Datei:** `arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md`
**Kriterium:** Mapping von Software-Bausteinen auf Hardware-/Infrastruktur-Elemente

**Befund:** Es wird nicht explizit gesagt, dass alle vier Subsysteme innerhalb des einen Jar auf demselben Rechner in derselben JVM laufen.

**Änderungsvorschlag:**
> Ergänzen: „Sämtliche Subsysteme aus der Bausteinsicht — XBoard-Protokoll, Spielregeln, Engine und Eröffnung — sind im Artefakt *DokChess.jar* zusammengefasst und laufen innerhalb einer einzigen JVM-Instanz."

---

#### [S07-03] Nur Windows-Deployment dokumentiert

**Schwere:** 🟡 Empfehlung
**Datei:** `arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md`
**Kriterium:** Dokumentation verschiedener Umgebungen

**Befund:** Da DokChess Java-basiert und plattformunabhängig ist, fehlt ein Hinweis auf Deployment unter Linux/macOS.

---

#### [S07-04] Deployment-Variante mit Eröffnungsbibliothek fehlt

**Schwere:** 🟡 Empfehlung
**Datei:** `arc-doc/07-Verteilungssicht/07-01-Infrastruktur-Windows.md`
**Kriterium:** Vollständigkeit der Infrastrukturdarstellung

**Befund:** Die Variante mit Eröffnungsbibliothek (Polyglot-Datei) wird nirgends dargestellt.

---

### Sektion 8: Querschnittliche Konzepte

| ID | Schwere | Titel |
|---|---|---|
| S08-01 | 🟡 | Fehlende Rückverweise von Konzepten zu Bausteinen (S5) |
| S08-02 | 🟡 | Vermischung von Konzept und Entscheidung in 8.1 (Abhängigkeiten) |
| S08-03 | 🟡 | Vermischung von Konzept und Entscheidung in 8.6 (Logging) |
| S08-04 | 🟢 | Querschnittlichkeit von 8.3 (Benutzungsoberfläche) unklar |
| S08-05 | 🟢 | Fehlender Verweis auf Code-Beispiele/Tests in 8.4 und 8.5 |

#### [S08-02] Vermischung von Konzept und Entscheidung in 8.1 (Abhängigkeiten)

**Schwere:** 🟡 Empfehlung
**Datei:** `arc-doc/08-Konzepte/08-01-Abhaengigkeiten.md`
**Kriterium:** Werden Konzepte von Entscheidungen abgegrenzt?

**Befund:** Das Konzept beschreibt den DI-Ansatz (HOW), enthält aber auch die Entscheidung, kein DI-Framework zu verwenden (WHAT). Diese Entscheidung wäre in Sektion 9 besser aufgehoben.

**Änderungsvorschlag:**
> Den Entscheidungsteil als eigenständigen ADR in Sektion 9 auslagern und in 8.1 nur einen Verweis setzen.

---

#### [S08-03] Vermischung von Konzept und Entscheidung in 8.6 (Logging)

**Schwere:** 🟡 Empfehlung
**Datei:** `arc-doc/08-Konzepte/08-06-Logging.md`
**Kriterium:** Werden Konzepte von Entscheidungen abgegrenzt?

**Befund:** 8.6 beschreibt weniger ein Logging-Konzept als die bewusste Entscheidung, auf Logging zu verzichten. Das ist primär eine Architekturentscheidung.

---

### Sektion 9: Architekturentscheidungen

| ID | Schwere | Titel |
|---|---|---|
| S09-01 | 🟡 | Zeitliche Diskrepanz Untersuchung (2011) vs. ADR-Status (2026) |
| S09-02 | 🟡 | Fehlende ADRs für Reactive Extensions, Algorithmuswahl, Polyglot-Format |
| S09-03 | 🟢 | Uneinheitliche Benennung der Konsequenz-Kategorien |
| S09-04 | 🟢 | Redundanzprüfung mit Sektion 4 — kein Befund |

#### [S09-01] Zeitliche Diskrepanz zwischen Untersuchung und ADR-Status

**Schwere:** 🟡 Empfehlung
**Datei:** `arc-doc/09-Entscheidungen/09-01-Anbindung.md`
**Kriterium:** Nachvollziehbarkeit / Zeitstempel

**Befund:** Die Untersuchung der Frontends ist mit „Stand 2011" datiert, der ADR-Status jedoch mit „2026-03-10". Für Leser ist unklar, ob die Entscheidung 2011 getroffen und 2026 nur formalisiert wurde.

**Änderungsvorschlag:**
> Im Context-Abschnitt ergänzen: „Die Untersuchung wurde 2011 durchgeführt. Die Ergebnisse wurden bei der Formalisierung als ADR (2026) auf Aktualität geprüft und als weiterhin gültig bewertet."

---

#### [S09-02] Fehlende ADRs für weitere architekturrelevante Entscheidungen

**Schwere:** 🟡 Empfehlung
**Datei:** `arc-doc/09-Entscheidungen/` (Verzeichnis)
**Kriterium:** Relevanz — Werden alle architekturrelevanten Entscheidungen dokumentiert?

**Befund:** Mehrere fundamentale Architekturansätze aus Sektion 4 haben keine ADRs:
- **Reactive Extensions** für nebenläufige Zugermittlung
- **Polyglot Opening Book** als Eröffnungsbibliotheksformat
- **Dependency Injection** als Kompositionsmechanismus

**Änderungsvorschlag:**
> Für mindestens die Entscheidung „Reactive Extensions für nebenläufige Zugermittlung" einen eigenen ADR anlegen.

---

### Sektion 10: Qualitätsanforderungen

| ID | Schwere | Titel |
|---|---|---|
| S10-01 | 🟡 | Qualitätsbaum ausschließlich als Bild ohne textuelle Alternative |
| S10-02 | 🟡 | Szenarien ohne explizite Strukturierung nach Quelle/Stimulus/Metrik |
| S10-03 | 🟢 | Kürzel-Legende nur teilweise aufgelöst |

#### [S10-01] Qualitätsbaum ausschließlich als Bild ohne textuelle Alternative

**Schwere:** 🟡 Empfehlung
**Datei:** `arc-doc/10-Qualitaetsanforderungen/10-01-Qualitaetsbaum.md`
**Kriterium:** Qualitätsübersicht soll strukturiert als Tabelle, Liste oder Mindmap vorliegen

**Befund:** Der gesamte Qualitätsbaum ist ausschließlich als PNG-Bild eingebettet. Es existiert keine textuelle Repräsentation. Falls das Bild nicht darstellbar ist, geht die Information verloren.

**Änderungsvorschlag:**
> Ergänze unterhalb des Bildes eine textuelle Darstellung als Tabelle mit den Spalten: Qualitätsmerkmal, Untermerkmal, Szenarien, Qualitätsziel.

---

#### [S10-02] Szenarien ohne explizite Strukturierung

**Schwere:** 🟡 Empfehlung
**Datei:** `arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md`
**Kriterium:** Qualitätsszenarien sollen Kontext, Quelle/Stimulus und Metrik enthalten

**Befund:** Die Szenarien sind als zweispaltige Tabelle (ID, Szenario) mit Fließtext dokumentiert. Die Bestandteile (Akteur, Aktion, Akzeptanzkriterium) sind implizit vorhanden, aber nicht explizit strukturiert.

---

#### [S10-03] Kürzel-Legende nur teilweise aufgelöst

**Schwere:** 🟢 Hinweis
**Datei:** `arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md`
**Kriterium:** Szenarien sollen eindeutig Qualitätsmerkmalen zugeordnet sein

**Befund:** Nur „W" = Wartbarkeit wird explizit erklärt. K, F, E, Z und P bleiben unerklärt.

**Änderungsvorschlag:**
> Ersetze den Erklärungssatz durch: „**W** = Wartbarkeit, **K** = Kompatibilität, **F** = Funktionale Eignung, **E** = Effizienz, **Z** = Zuverlässigkeit, **P** = Portabilität (Übertragbarkeit)."

---

### Sektion 11: Risiken und technische Schulden

| ID | Schwere | Titel |
|---|---|---|
| S11-01 | 🔴 | Technische Schulden fehlen vollständig |
| S11-02 | 🟡 | Keine Priorisierung der Risiken |
| S11-03 | 🟡 | Keine tabellarische Übersicht aller Risiken |
| S11-04 | 🟡 | Risikoquellen zu einseitig |
| S11-05 | 🟢 | Bekannte Probleme nicht als solche dokumentiert |
| S11-06 | 🟢 | Gute Querverweise zu anderen Sektionen (positiv) |

#### [S11-01] Technische Schulden fehlen vollständig

**Schwere:** 🔴 Kritisch
**Datei:** `arc-doc/11-Risiken/` (alle Dateien)
**Kriterium:** Werden technische Schulden identifiziert?

**Befund:** Die Sektion dokumentiert ausschließlich Risiken. Technische Schulden werden nirgends erfasst. Dabei liefert die Dokumentation selbst Hinweise auf bewusst eingegangene Schulden: 50-Züge-Regel nicht implementiert, Stellungswiederholung nicht implementiert, keine Endspieldatenbanken.

**Änderungsvorschlag:**
> Eine neue Datei `11-04-Technische-Schulden.md` anlegen mit einer Tabelle bewusst eingegangener technischer Schulden (50-Züge-Regel, Stellungswiederholung, fehlende Endspieldatenbanken, fehlende Eröffnungsbibliothek-Anbindung).

---

#### [S11-02] Keine Priorisierung der Risiken

**Schwere:** 🟡 Empfehlung
**Datei:** `arc-doc/11-Risiken/` (alle Dateien)
**Kriterium:** Sind die Risiken nach Priorität geordnet?

**Befund:** Die drei Risiken sind durchnummeriert, aber es fehlt eine explizite Priorisierung nach Eintrittswahrscheinlichkeit und/oder Schadenshöhe.

---

#### [S11-04] Risikoquellen zu einseitig

**Schwere:** 🟡 Empfehlung
**Datei:** `arc-doc/11-Risiken/` (alle Dateien)
**Kriterium:** Wurden verschiedene Perspektiven berücksichtigt?

**Befund:** Alle Risiken konzentrieren sich auf Machbarkeit der Kernentwicklung. Es fehlen Risiken zu externen Abhängigkeiten (XBoard-Protokoll, Polyglot-Format) und zum Veralten der Dokumentation.

---

### Sektion 12: Glossar

| ID | Schwere | Titel |
|---|---|---|
| S12-01 | 🟡 | Zentraler Domänenbegriff „Stellung" fehlt |
| S12-02 | 🟡 | Begriff „Spielbaum" fehlt |
| S12-03 | 🟢 | Konsistenz mit Domänenmodell — „Zug"/„Feld" fehlen |
| S12-04 | 🟢 | FEN-Eintrag: unvollständiger Wikipedia-Verweis |
| S12-05 | 🟢 | „Schach960" ohne Bezug zur Dokumentation |
| S12-06 | 🟢 | Spaltenbezeichnung „Erklärung" statt „Definition" |

#### [S12-01] Zentraler Domänenbegriff „Stellung" fehlt im Glossar

**Schwere:** 🟡 Empfehlung
**Datei:** `arc-doc/12-Glossar/12-02-Begriffe.md`
**Kriterium:** Begriffsauswahl — domänenspezifische Begriffe

**Befund:** „Stellung" ist ein zentrales Konzept im Domänenmodell und wird in der gesamten Dokumentation durchgängig verwendet. Für Wenig- oder Gelegenheitsspieler ist dieser Begriff nicht selbstverständlich.

**Änderungsvorschlag:**
> Eintrag ergänzen: „Stellung — Beschreibung der aktuellen Spielsituation auf dem Brett. Umfasst die Position aller Figuren, die Information, wer am Zug ist, ob noch Rochaden möglich sind und ob en passant geschlagen werden kann."

---

#### [S12-02] Begriff „Spielbaum" fehlt im Glossar

**Schwere:** 🟡 Empfehlung
**Datei:** `arc-doc/12-Glossar/12-02-Begriffe.md`
**Kriterium:** Begriffsauswahl — technische Begriffe

**Befund:** „Spielbaum" wird in der Lösungsstrategie und der Bausteinsicht verwendet, ohne im Glossar definiert zu sein. Er ist ein Fachbegriff aus der Spieltheorie/Informatik.

---

## Sektionsübergreifende Konflikte

| Konfliktdimension | Status | Befunde |
|---|---|---|
| Qualitätsstrang (S1 ↔ S4 ↔ S10) | 🟡 | Namensinkonsistenz „Spielstärke", Widerspruch „effizientes Domänenmodell", verwaiste Szenarien Z01/Z02 |
| Strategie ↔ Entscheidungen (S4 ↔ S9) | 🟡 | Reactive Extensions, Minimax-Wahl, Polyglot-Format und DI ohne ADR |
| Constraint-Compliance (S2 ↔ S4/S8/S9) | 🟡 | ADR-Überschriften auf Englisch, ASCII-Transliteration statt UTF-8 in ADRs |
| Kontext ↔ Bausteine (S3 ↔ S5) | 🟡 | Endspiele ohne Baustein-Gegenstück, Remisangebote in S3 erwähnt aber in S5 ausgeschlossen |
| Sichten-Konsistenz (S5 ↔ S6 ↔ S7) | 🟡 | Eröffnung ohne Deployment-Szenario, Ebene-2-Bausteine nicht namentlich in S6, kein Baustein-Mapping in S7 |
| Konzepte ↔ Entscheidungen (S8 ↔ S9) | 🟡 | Verzicht auf DI-Framework und Logging-Framework sind Entscheidungen in S8 statt S9 |
| Risiken ↔ Qualität (S11 ↔ S1/S10) | 🟡 | Höchstpriorisierte Ziele (Analysierbarkeit, Änderbarkeit) ohne Risikobetrachtung |

### 1. Qualitätsstrang (S1 ↔ S4 ↔ S10)

| ID | Schwere | Titel |
|---|---|---|
| KQS-01 | 🟡 | Inkonsistente Benennung des Qualitätsziels „Spielstärke" (S1: „Akzeptable/Funktionale Eignung" vs. S4: „Attraktive/Attraktivität") |
| KQS-02 | 🟡 | Widerspruch zur Effizienz des Domänenmodells: S4-01 nennt „Effiziente Implementierung", S4-02 sagt „Lesbarkeit vor Effizienz" |
| KQS-03 | 🟡 | Verwaiste Szenarien Z01/Z02 (Zuverlässigkeit) — kein zugehöriges Qualitätsziel in S1 |
| KQS-04 | 🟢 | Leichte Prioritätsumkehr: Funktionale Eignung (Prio 4) hat 4 Szenarien, Interoperabilität (Prio 3) nur 1 |

### 2. Strategie ↔ Entscheidungen (S4 ↔ S9)

| ID | Schwere | Titel |
|---|---|---|
| KSE-01 | 🟡 | Reactive Extensions: Technologieentscheidung in S4 gesetzt, aber kein ADR in S9 |
| KSE-02 | 🟢 | Minimax-/Alpha-Beta-Algorithmuswahl ohne Entscheidungsdokumentation |
| KSE-03 | 🟢 | Polyglot Opening Book Format ohne Entscheidungsdokumentation |
| KSE-04 | 🟢 | Dependency Injection als Architekturansatz ohne Entscheidungsdokumentation |

### 3. Constraint-Compliance (S2 ↔ S4/S8/S9)

| ID | Schwere | Titel |
|---|---|---|
| KRC-01 | 🟡 | ADR-Strukturelemente in englischer Sprache (Status, Context, Decision, Consequences) — Konvention KC-3 fordert Deutsch |
| KRC-02 | 🟡 | ASCII-Transliteration statt UTF-8-Umlaute in ADRs (z.B. „Qualitaetsziel" statt „Qualitätsziel") |

### 4. Kontext ↔ Bausteine (S3 ↔ S5)

| ID | Schwere | Titel |
|---|---|---|
| KKB-01 | 🟡 | Endspiele im fachlichen Kontext als externer Partner dargestellt, aber ohne Entsprechung in Bausteinsicht |
| KKB-02 | 🟡 | Remisangebote im fachlichen Kontext erwähnt, in Bausteinsicht explizit als nicht unterstützt aufgeführt |
| KKB-03 | 🟢 | Terminologie-Unterschied: „Eröffnungen" (S3) vs. „Eröffnung" (S5) vs. „Eröffnungsbibliothek" (Interface) |
| KKB-04 | 🟢 | Bausteinsicht referenziert nur technischen Kontext (S3.2), nicht fachlichen Kontext (S3.1) |

### 5. Sichten-Konsistenz (S5 ↔ S6 ↔ S7)

| ID | Schwere | Titel |
|---|---|---|
| KSV-01 | 🟡 | Eröffnungs-Subsystem ohne aktives Laufzeit- und Deployment-Szenario |
| KSV-02 | 🟡 | Granularitäts-Mismatch: Ebene-2-Verhalten in S6 ohne Benennung der Ebene-2-Bausteine |
| KSV-03 | 🟡 | Verteilungssicht ohne explizites Baustein-zu-Infrastruktur-Mapping |
| KSV-04 | 🟢 | Bezeichnung „Eröffnungsbibliothek" vs. Subsystem-Name „Eröffnung" |
| KSV-05 | 🟢 | Nur ein Laufzeitszenario deckt nicht alle Subsystem-Interaktionen ab |

### 6. Konzepte ↔ Entscheidungen (S8 ↔ S9)

| ID | Schwere | Titel |
|---|---|---|
| KKE-01 | 🟡 | Verzicht auf DI-Framework als Entscheidung in S8 dokumentiert statt als ADR in S9 |
| KKE-02 | 🟡 | Verzicht auf Logging-Framework als Entscheidung in S8 dokumentiert statt als ADR in S9 |
| KKE-03 | 🟢 | Ausschließliche Verwendung von Runtime Exceptions ohne Entscheidungsgrundlage |

### 7. Risiken ↔ Qualität (S11 ↔ S1/S10)

| ID | Schwere | Titel |
|---|---|---|
| KRQ-01 | 🟡 | Höchstpriorisiertes Qualitätsziel „Analysierbarkeit" ohne Risikobetrachtung |
| KRQ-02 | 🟢 | Qualitätsziel „Änderbarkeit" ohne Risikobetrachtung |
| KRQ-03 | 🟢 | Effizienz in R3 nur implizit adressiert — keine eigene Maßnahme |
| KRQ-04 | 🟢 | Zuverlässigkeitsszenarien Z01/Z02 implizieren nicht dokumentierte Risiken |
| KRQ-05 | 🟡 | Risikoabdeckung invers zur Qualitätsziel-Priorisierung (Prio 1–2 ohne Risiko, Prio 3–5 mit Risiko) |

---

## Konfliktkarte

| Sektion | Involviert in Konflikten |
|---|---|
| S5 — Bausteinsicht | 9 |
| S9 — Entscheidungen | 9 |
| S4 — Lösungsstrategie | 6 |
| S1 — Einführung/Ziele | 6 |
| S10 — Qualitätsanforderungen | 6 |
| S8 — Konzepte | 5 |
| S11 — Risiken | 5 |
| S3 — Kontextabgrenzung | 4 |
| S6 — Laufzeitsicht | 4 |
| S7 — Verteilungssicht | 3 |
| S2 — Randbedingungen | 2 |

---

## Zusammenfassung

| Kategorie | Anzahl |
|---|---|
| 🔴 Kritische Befunde | 2 |
| 🟡 Warnungen / Empfehlungen | 48 |
| 🟢 Hinweise | 38 |

### Handlungsempfehlungen

1. **Terminologie in S4 an S1 angleichen** (🔴 S04-01): In `04-01-Einstieg.md` „Attraktive Spielstärke (Attraktivität)" zu „Akzeptable Spielstärke (Funktionale Eignung)" korrigieren, um Konsistenz mit den Qualitätszielen herzustellen.

2. **Technische Schulden in S11 dokumentieren** (🔴 S11-01): Eine Datei `11-04-Technische-Schulden.md` anlegen, die bewusst eingegangene Schulden erfasst (50-Züge-Regel, Stellungswiederholung, fehlende Endspieldatenbank).

3. **Widerspruch „effizientes Domänenmodell" in S4 auflösen** (🟡 KQS-02): Die Strategietabelle widerspricht der eigenen Aussage „Lesbarkeit vor Effizienz" — den Eintrag in `04-01-Einstieg.md` präzisieren.

4. **Entscheidungen aus S8 in S9 überführen** (🟡 KKE-01/02, S08-02/03): Verzicht auf DI-Framework und Logging-Framework als eigenständige ADRs in Sektion 9 dokumentieren.

5. **ADR für Reactive Extensions anlegen** (🟡 KSE-01): Eine weitreichende Technologieentscheidung mit klaren Alternativen, die bisher nur in S4 als Fakt beschrieben wird.

6. **ADR-Sprache auf Deutsch umstellen** (🟡 KRC-01/02): Englische Strukturüberschriften und ASCII-Transliteration in den ADRs an die übrige deutschsprachige Dokumentation anpassen.

7. **Risikobetrachtung für höchstpriorisierte Qualitätsziele ergänzen** (🟡 KRQ-01/05): Analysierbarkeit und Änderbarkeit haben keine Risikobetrachtung — zumindest eine bewusste Einschätzung dokumentieren.

8. **Fachlichen Kontext nachziehen** (🟡 KKB-01/02): Endspiele als nicht implementiert kennzeichnen, Remisangebote als nicht unterstützt markieren.