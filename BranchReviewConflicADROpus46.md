# arc42 Branch-Review

## Überblick

**Branch:** `Konflikt/ADR`
**Basis:** `main` (origin/main)
**Geänderte Dateien:** 1 (nicht committet)
**Betroffene Sektionen:** Sektion 9 (Entscheidungen)

## Geänderte Dateien

| Datei | Änderungstyp | Sektion |
|---|---|---|
| `src/09-Entscheidungen/09-03-Brettrepraesentation.md` | Added | Sektion 9 |

---

## Sektions-Review

### Sektion 9: Architekturentscheidungen

#### [S09-01] Widerspruch zur Lösungsstrategie: OO-Domänenmodell vs. Bitboards

**Schwere:** 🔴 Kritisch
**Datei:** `src/09-Entscheidungen/09-03-Brettrepraesentation.md`
**Kriterium:** Konsistenz mit Lösungsstrategie (Sektion 4) — keine Widersprüche

**Befund:** ADR 09-03 entscheidet sich für Bitboards als interne Brettrepräsentation. Sektion 4 beschreibt jedoch durchgängig ein objektorientiertes Domänenmodell mit expliziter Priorisierung von Lesbarkeit gegenüber Effizienz:

- `04-01-Einstieg.md` nennt „Explizites, objektorientiertes Domänenmodell" als tragenden Architekturansatz für das Qualitätsziel *Zugängliches Beispiel (Analysierbarkeit)*.
- `04-02-Aufbau.md` formuliert explizit: *„Hier wurde bewusst eine bessere Verständlichkeit angestrebt, auf Kosten von Effizienz"* und *„ging bei der Implementierung der fachlich motivierten Klasse dazu Lesbarkeit vor Effizienz"*.

Die ADR-Entscheidung für Bitboards kehrt dieses Prinzip um (Effizienz vor Lesbarkeit) und steht im direkten Widerspruch zur dokumentierten Lösungsstrategie. Der Satz in der ADR, dass „die oeffentlichen Schnittstellen der Module unveraendert bleiben", mildert den Widerspruch, löst ihn aber nicht auf, da Sektion 4 auch die *Implementierung* als objektorientiert und lesbar beschreibt.

**Änderungsvorschlag:** Entweder (a) Sektion 4 aktualisieren, um die Designentscheidung Bitboards als Performance-Optimierung hinter den OO-Schnittstellen zu reflektieren, oder (b) im Context-Abschnitt der ADR den bestehenden Designansatz aus Sektion 4 als explizite Gegenkraft benennen und in der Decision begründen, warum dieser Ansatz hier bewusst durchbrochen wird. Beispiel für den Context:

> Bisher priorisiert die Lösungsstrategie von DokChess Lesbarkeit vor Effizienz bei der Implementierung des Domänenmodells ([-> 4.2 Aufbau](../04-Loesungsstrategie/04-02-Aufbau.md)). Diese Entscheidung stellt die interne Brettrepräsentation als gezielte Ausnahme von diesem Prinzip zur Diskussion, da die Zuggeneration als kritischer Engpass identifiziert wurde.

---

#### [S09-02] Fehlende Auswirkung auf Qualitätsziel „Analysierbarkeit"

**Schwere:** 🟡 Empfehlung
**Datei:** `src/09-Entscheidungen/09-03-Brettrepraesentation.md`
**Kriterium:** Konsequenzen — werden ALLE Konsequenzen aufgeführt (positive, negative, neutrale)?

**Befund:** Die Consequences-Sektion benennt zwar die höhere Codekomplexität und erschwerteres Debugging, adressiert aber nicht explizit die Auswirkung auf das Qualitätsziel *Zugängliches Beispiel (Analysierbarkeit)* aus Sektion 1.2. Bitboards untergraben dieses Qualitätsziel fundamental — das sollte als Konsequenz klar benannt werden.

**Änderungsvorschlag:** Folgenden Punkt unter „Negative Konsequenzen" ergänzen:

> - Das Qualitaetsziel „Zugaengliches Beispiel (Analysierbarkeit)" wird fuer den Bereich der Brettrepraesentation eingeschraenkt: Der Bitboard-Code ist ohne Schachprogrammier-Vorwissen nicht mehr zugaenglich. Die OO-Schnittstellen der Module kaschieren dies nach aussen.

---

#### [S09-03] Fehlender Bezug auf bestehende Designphilosophie im Context

**Schwere:** 🟡 Empfehlung
**Datei:** `src/09-Entscheidungen/09-03-Brettrepraesentation.md`
**Kriterium:** Kontext — Werden die Kräfte vollständig beschrieben? Werden Spannungen zwischen verschiedenen Aspekten aufgezeigt?

**Befund:** Der Context-Abschnitt listet Randbedingungen, Qualitätsmerkmale und Annahmen auf, benennt aber nicht die bestehende Designphilosophie „Lesbarkeit vor Effizienz" als relevante Gegenkraft. Gerade weil diese ADR eine Abkehr von diesem Prinzip darstellt, müsste die Spannung zwischen Performance-Bedarf und bestehender OO-Designphilosophie explizit im Kontext erscheinen.

**Änderungsvorschlag:** Im Context-Abschnitt unter „Relevante Einflussfaktoren" ergänzen:

> - Bisherige Designphilosophie: Lesbarkeit vor Effizienz bei Implementierung des Domaenenmodells ([-> 4.2 Aufbau](../04-Loesungsstrategie/04-02-Aufbau.md))

---

#### [S09-04] Abschnitt „Folgen fuer die Weiterentwicklung" unvollständig

**Schwere:** 🟢 Hinweis
**Datei:** `src/09-Entscheidungen/09-03-Brettrepraesentation.md`
**Kriterium:** Konsequenzen — Vollständigkeit und Nachvollziehbarkeit

**Befund:** Es fehlt eine Aussage darüber, wie die Bitboard-Entscheidung die in ADR 09-02 beschriebene Immutability-Strategie konkret beeinflusst (z.B. Kopiersemantik bei Bitboards vs. bei OO-Objekten).

**Änderungsvorschlag:** Folgenden Punkt unter „Folgen fuer die Weiterentwicklung" ergänzen:

> - Die Kopiersemantik unveraenderlicher Stellungen ([-> 9.2](09-02-Stellungsobjekte.md)) vereinfacht sich mit Bitboards: Eine neue Stellung entsteht durch bitweise Operationen auf primitiven `long`-Werten statt durch Deep-Copy komplexer Objektgraphen.

---

#### [S09-05] Stilistische Inkonsistenz bei Consequences-Unterüberschriften

**Schwere:** 🟢 Hinweis
**Datei:** `src/09-Entscheidungen/09-03-Brettrepraesentation.md`
**Kriterium:** Konsistenz mit bestehenden ADRs

**Befund:** ADR 09-01 verwendet „Neutrale/Folgen fuer die Weiterentwicklung:" als dritte Consequences-Kategorie, ADR 09-02 verwendet „Folgen fuer die Weiterentwicklung:". ADR 09-03 folgt dem Muster von 09-02. Kein Fehler, aber die Inkonsistenz zu 09-01 fällt auf.

**Änderungsvorschlag:** Kein Änderungsbedarf an 09-03 — gegebenenfalls 09-01 bei Gelegenheit angleichen.

---

## Konfliktanalysen

### Lösungsstrategie (S4) ↔ Entscheidungen (S9)

#### Zuordnungsmatrix

| Strategische Festlegung (S4) | Zugehörige Entscheidung(en) (S9) | Status |
|---|---|---|
| Explizites, objektorientiertes Domänenmodell (04-01, Analysierbarkeit) | ADR 09-03 Bitboards | ❌ Widerspruch |
| Lesbarkeit vor Effizienz bei Datenstrukturen (04-02) | ADR 09-03 Bitboards | ❌ Widerspruch |
| Einladende Experimentierplattform / niedrige Einstiegshürde (04-01, Änderbarkeit) | ADR 09-03 Bitboards | ⚠️ Spannung |
| Einfache Implementierungen erfüllen Qualitätsszenarien (04-03) | ADR 09-03 Bitboards | ⚠️ Spannung |
| Unveränderliche Datenstrukturen (04-02, 04-03) | ADR 09-02 Stellungsobjekte, ADR 09-03 Bitboards | ✅ Aligned |
| XBoard-Protokoll (04-04) | ADR 09-01 Anbindung | ✅ Aligned |
| Effiziente Implementierung des Domänenmodells (04-01, Effizienz) | ADR 09-03 Bitboards | 🔲 Lücke — Strategie nicht aktualisiert |

#### [KSE-01] Direkter Widerspruch: „Lesbarkeit vor Effizienz" vs. Bitboard-Entscheidung

**Konflikttyp:** K1 — Direkter Widerspruch
**Schwere:** 🔴 Kritisch
**Betroffene Dateien:**
- `src/04-Loesungsstrategie/04-02-Aufbau.md` — *„Hier wurde bewusst eine bessere Verständlichkeit angestrebt, auf Kosten von Effizienz"* und *„Auch hier ging bei der Implementierung der fachlich motivierten Klasse dazu Lesbarkeit vor Effizienz"*
- `src/09-Entscheidungen/09-03-Brettrepraesentation.md` — Entscheidung für Bitboards, explizit begründet mit Performance (Faktor 8–12), auf Kosten von Lesbarkeit und Verständlichkeit

**Beschreibung:** Die Strategie formuliert zweimal explizit das Prinzip **„Lesbarkeit vor Effizienz"** für die zentralen Datenstrukturen, insbesondere für die Spielsituation (`Stellung`). Die ADR trifft für exakt diese Datenstruktur die diametral entgegengesetzte Abwägung: Bitboards werden **wegen** ihrer Effizienz gewählt, obwohl die ADR selbst anerkennt, dass Lesbarkeit und Verständlichkeit „niedrig" sind. Der Hinweis, dass die öffentlichen Schnittstellen unverändert bleiben, mildert den Widerspruch nicht vollständig, da die Strategie explizit von der **Implementierung** der fachlich motivierten Klasse spricht.

**Lösungsvorschlag:** Die Strategie in `04-02-Aufbau.md` muss aktualisiert werden, um die differenzierte Abwägung widerzuspiegeln:

> *„Die Interaktion zwischen den Modulen erfolgt über fachlich motivierte Datenstrukturen (Figur, Zug, Stellung), deren **öffentliche Schnittstellen** Verständlichkeit priorisieren. Intern setzt DokChess bei der Brettrepräsentation auf Bitboards, um die für eine attraktive Spielstärke nötige Performance zu erreichen ([→ Entscheidung 9.3](../09-Entscheidungen/09-03-Brettrepraesentation.md)). Diese Optimierung ist hinter den fachlichen Abstraktionen gekapselt."*

---

#### [KSE-02] Widerspruch: „Objektorientiertes Domänenmodell" als Architekturansatz vs. Bitboards

**Konflikttyp:** K1 — Direkter Widerspruch
**Schwere:** 🔴 Kritisch
**Betroffene Dateien:**
- `src/04-Loesungsstrategie/04-01-Einstieg.md` — Qualitätsziel „Zugängliches Beispiel (Analysierbarkeit)" wird durch *„Explizites, objektorientiertes Domänenmodell"* adressiert
- `src/09-Entscheidungen/09-03-Brettrepraesentation.md` — Kernrepräsentation des Domänenmodells ist nicht mehr objektorientiert, sondern bitbasiert

**Beschreibung:** Die Strategie-Tabelle benennt ein „Explizites, objektorientiertes Domänenmodell" als zentralen Architekturansatz für das Qualitätsziel Analysierbarkeit. Die ADR 09-03 ersetzt das Herzstück dieses Modells — die interne Brettrepräsentation — durch `long`-Werte und bitweise Operationen.

**Lösungsvorschlag:** Die Strategie-Tabelle in `04-01-Einstieg.md` sollte den Architekturansatz differenzieren:

> *„Objektorientiertes Domänenmodell an den öffentlichen Schnittstellen (Figur, Zug, Stellung); intern performanceoptimierte Brettrepräsentation über Bitboards, gekapselt hinter den fachlichen Abstraktionen ([→ Entscheidung 9.3](../09-Entscheidungen/09-03-Brettrepraesentation.md))"*

---

#### [KSE-03] Spannung: „Einladende Experimentierplattform" vs. hohe Einstiegshürde durch Bitboards

**Konflikttyp:** K1 — Direkter Widerspruch
**Schwere:** 🟡 Warnung
**Betroffene Dateien:**
- `src/04-Loesungsstrategie/04-01-Einstieg.md` — Qualitätsziel „Einladende Experimentierplattform (Änderbarkeit)"
- `src/09-Entscheidungen/09-03-Brettrepraesentation.md` — „Einstiegshürde für neue Entwickler: hoch"

**Beschreibung:** Die Strategie verfolgt eine „Einladende Experimentierplattform" mit niedriger Einstiegshürde. Die ADR erkennt selbst an, dass Bitboards die Einstiegshürde signifikant erhöhen. Gemildert dadurch, dass Experimentierer auf Modulebene die Bitboard-Interna nicht verstehen müssen — wer jedoch Zuggeneration oder Stellungsbewertung modifizieren will, trifft auf hohe Komplexität.

**Lösungsvorschlag:** In der ADR 09-03 die Auswirkung auf das Qualitätsziel „Einladende Experimentierplattform" explizit adressieren. Ergänzung in „Negative Konsequenzen":

> *„Die hohe Einstiegshürde der Bitboard-Repräsentation steht in Spannung zum strategischen Ziel einer einladenden Experimentierplattform ([→ 4.1](../04-Loesungsstrategie/04-01-Einstieg.md)). Diese Spannung wird gemildert, indem die öffentlichen Schnittstellen (Spielregeln, Engine) weiterhin fachlich motivierte Typen verwenden. Für Experimente an der Zuggeneration selbst werden Hilfsfunktionen zur Bitboard-Visualisierung bereitgestellt."*

---

#### [KSE-04] Spannung: „Einfache Implementierungen erfüllen Qualitätsszenarien" vs. Bitboard-Notwendigkeit

**Konflikttyp:** K3 — Veraltete Strategie
**Schwere:** 🟡 Warnung
**Betroffene Dateien:**
- `src/04-Loesungsstrategie/04-03-Spielstrategie.md` — *„Diese einfachen Implementierungen erfüllen unter den gegebenen Randbedingungen bereits die Qualitätsszenarien."*
- `src/09-Entscheidungen/09-03-Brettrepraesentation.md` — Bitboard-Notwendigkeit impliziert, dass die einfache Implementierung nicht (mehr) ausreicht

**Beschreibung:** Die Strategie behauptet, einfache Implementierungen reichen für die Qualitätsszenarien. Die ADR rechtfertigt Bitboards damit, dass 2–3 Halbzüge tiefere Suche die Spielstärke „signifikant steigert" und referenziert das Risiko „Spielstärke nicht erreichbar" — dies impliziert, dass die bisherige einfache Implementierung für die gewünschte Spielstärke nicht ausreicht.

**Lösungsvorschlag:** Ergänzung in `04-03-Spielstrategie.md`:

> *„Um die Spielstärke über das Basisniveau hinaus zu steigern, setzt DokChess intern auf eine Bitboard-basierte Brettrepräsentation ([→ Entscheidung 9.3](../09-Entscheidungen/09-03-Brettrepraesentation.md)). Diese ermöglicht bei gleicher Rechenzeit eine deutlich tiefere Suche und damit eine signifikant stärkere Spielweise."*

---

#### [KSE-05] Strategielücke: Performance-Optimierung ohne strategische Verankerung

**Konflikttyp:** K3 — Veraltete oder unvollständige Strategie
**Schwere:** 🟡 Warnung
**Betroffene Dateien:**
- `src/04-Loesungsstrategie/04-01-Einstieg.md` — *„Effiziente Implementierung des Domänenmodells"* ohne Konkretisierung
- `src/09-Entscheidungen/09-03-Brettrepraesentation.md` — Fundamentale, strategisch relevante Entscheidung

**Beschreibung:** Die ADR 09-03 verändert die Kernrepräsentation, beeinflusst zwei Qualitätsziele (Effizienz, Spielstärke) und kehrt ein geltendes Designprinzip um. Eine Entscheidung dieser Tragweite sollte in der Strategie explizit verankert sein. Der bestehende Punkt „Effiziente Implementierung des Domänenmodells" ist zu unspezifisch.

**Lösungsvorschlag:** In der Tabelle in `04-01-Einstieg.md` unter „Schnelles Antworten auf Züge (Effizienz)" konkretisieren:

> *„Effiziente Implementierung des Domänenmodells: intern Bitboard-basierte Brettrepräsentation für schnelle Zuggeneration ([→ Entscheidung 9.3](../09-Entscheidungen/09-03-Brettrepraesentation.md))"*

---

### Konzepte (S8) ↔ Entscheidungen (S9)

#### Zuordnungsanalyse

| Element | Sektion | Korrekte Zuordnung? | Bezug |
|---|---|---|---|
| Abhängigkeiten zwischen Modulen | S8 | ✅ Korrekt | — |
| Domänenmodell | S8 | ✅ Korrekt | Enthält aber Implementierungsdetail (→ KKE-01) |
| Benutzungsoberfläche | S8 | ✅ Korrekt | — |
| Validierung | S8 | ✅ Korrekt | — |
| Fehlerbehandlung | S8 | ✅ Korrekt | — |
| Logging | S8 | ✅ Korrekt | — |
| Testbarkeit | S8 | ✅ Korrekt | — |
| Frontend-Anbindung (09-01) | S9 | ✅ Korrekt | — |
| Stellungsobjekte (09-02) | S9 | ✅ Korrekt | Annahme konfligiert mit 09-03 (→ KKE-03) |
| Brettrepräsentation (09-03) | S9 | ✅ Korrekt | Neue ADR, korrekt verortet |

#### [KKE-01] Domänenmodell beschreibt 8×8-Array — durch Bitboards faktisch falsch

**Konflikttyp:** K1 — Direkter Widerspruch
**Schwere:** 🔴 Kritisch
**Betroffene Dateien:**
- `src/08-Konzepte/08-02-Domaenenmodell.md` — *„das intern als zweidimensionales Array (8 x 8) implementiert ist. Falls ein Feld unbesetzt ist, steht null im Array."*
- `src/09-Entscheidungen/09-03-Brettrepraesentation.md` — Entscheidung für Bitboards (64-Bit `long`-Werte) statt OO-Modell mit Arrays

**Beschreibung:** Das Domänenmodell in S8 beschreibt die Klasse `Stellung` mit einem konkreten Implementierungsdetail: einem zweidimensionalen 8×8-Array mit `null` für unbesetzte Felder. Die ADR 09-03 entscheidet sich explizit gegen dieses Modell und für Bitboards. Das Konzept in 08-02 ist damit inhaltlich falsch.

**Lösungsvorschlag:** In `08-02-Domaenenmodell.md` den Satz zur internen Implementierung ersetzen:

> *„Vor allem sind das die Figuren auf dem Brett. Die interne Repräsentation des Bretts erfolgt über Bitboards — 64-Bit-Ganzzahlen, bei denen jedes Bit einem Feld entspricht ([→ Entscheidung 9.3 „Interne Brettrepräsentation"](../09-Entscheidungen/09-03-Brettrepraesentation.md)). Nach außen bleibt die fachliche Schnittstelle (Zugriff über `Feld` und `Figur`) erhalten."*

---

#### [KKE-02] Fehlende Konzeptbeschreibung für Bitboard-Handling in S8

**Konflikttyp:** K5 — Fehlende Konzeptbeschreibung
**Schwere:** 🟡 Warnung
**Betroffene Dateien:**
- `src/09-Entscheidungen/09-03-Brettrepraesentation.md` — *„Hilfsfunktionen zur Visualisierung von Bitboards erforderlich", „Dokumentation der Bitmuster und Magic-Bitboard-Tabellen essenziell"*
- Sektion 8 — kein entsprechendes Konzept vorhanden

**Beschreibung:** Die ADR benennt zwei querschnittliche Notwendigkeiten: (1) Visualisierungshilfsfunktionen für Debugging und (2) Dokumentation der Bitmuster und Magic-Bitboard-Tabellen. Beides betrifft mehrere Module und steht in Spannung zu `08-06-Logging.md`, das „keine feinkörnigen Logging-Ausgaben" vorsieht.

**Lösungsvorschlag:** Das bestehende Konzept `08-06-Logging.md` um einen Abschnitt erweitern oder ein neues Konzept `08-08-Bitboard-Debugging.md` ergänzen:

> *„Mit der Umstellung auf Bitboards als interne Brettrepräsentation ([→ Entscheidung 9.3](../09-Entscheidungen/09-03-Brettrepraesentation.md)) werden Hilfsfunktionen zur Visualisierung bereitgestellt, die einen `long`-Wert als 8×8-Gitter auf der Konsole ausgeben. Diese Funktionen dienen ausschließlich dem Debugging in der Entwicklung und sind nicht als Laufzeit-Logging gedacht."*

---

#### [KKE-03] Annahme in ADR 09-02 durch ADR 09-03 widerlegt

**Konflikttyp:** K1 — Direkter Widerspruch (innerhalb S9)
**Schwere:** 🟡 Warnung
**Betroffene Dateien:**
- `src/09-Entscheidungen/09-02-Stellungsobjekte.md` — Annahme: *„Ein fachliches Objektmodell (Feld, Figur, Zug, Stellung) ist effizient genug implementierbar."*
- `src/09-Entscheidungen/09-03-Brettrepraesentation.md` — Das OO-Modell wird als zu langsam verworfen (Faktor 8–12 langsamer)

**Beschreibung:** ADR 09-02 formuliert als Annahme, dass ein fachliches Objektmodell effizient genug implementierbar ist. ADR 09-03 widerlegt genau diese Annahme durch Performance-Messungen. Die Rückwirkung auf 09-02 ist nicht dokumentiert.

**Lösungsvorschlag:** In `09-02-Stellungsobjekte.md` die Annahme präzisieren:

> *„Ein fachliches Objektmodell (Feld, Figur, Zug, Stellung) ist als Schnittstelle effizient genug. Für die interne Brettrepräsentation wurde diese Annahme revidiert ([→ Entscheidung 9.3](09-03-Brettrepraesentation.md))."*

---

#### [KKE-04] Spannung zwischen „Experimentierplattform" und Bitboard-Komplexität

**Konflikttyp:** K1 — Indirekter Widerspruch
**Schwere:** 🟢 Hinweis
**Betroffene Dateien:**
- `src/08-Konzepte/08-01-Abhaengigkeiten.md` — *„DokChess soll zum Experimentieren und zum Erweitern der Engine einladen"*
- `src/09-Entscheidungen/09-03-Brettrepraesentation.md` — *„Schwer nachvollziehbar fuer Nicht-Schachprogrammierer", „Einstiegshuerde fuer neue Entwickler: hoch"*

**Beschreibung:** Das Abhängigkeitskonzept betont, dass DokChess „zum Experimentieren einladen" soll. Wer die Engine tatsächlich erweitern will (z.B. Stellungsbewertung), muss trotz Interface-Abstraktion mit Bitboard-Interna arbeiten.

**Lösungsvorschlag:** Optional ein ergänzender Satz in `08-01-Abhaengigkeiten.md`:

> *„Für die Erweiterung der Engine-internen Algorithmen (Zuggeneration, Stellungsbewertung) ist Kenntnis der Bitboard-Repräsentation erforderlich ([→ Entscheidung 9.3](../09-Entscheidungen/09-03-Brettrepraesentation.md)). Die Schnittstellen-Abstraktion schützt Anwender auf Modulebene, nicht innerhalb der Engine."*

---

### Randbedingungen (S2) ↔ Compliance (S4/S8/S9)

#### Constraint-Compliance-Matrix

| Constraint (S2) | Kategorie | S9-03 (NEU) | Status |
|---|---|---|---|
| Moderate Hardwareausstattung | Technisch | ✅ | ✅ Konform |
| Betrieb auf Windows Desktop | Technisch | ✅ | ✅ Konform |
| Implementierung in Java | Technisch | ✅ | ✅ Konform |
| Fremdsoftware frei verfügbar | Technisch | ✅ | ✅ Konform |
| Team (inkl. Workshop-Teilnehmer) | Organisatorisch | ⚠️ | 🟡 Spannung |
| Vorgehensmodell (risikogetrieben) | Organisatorisch | ✅ | ✅ Konform |
| Veröffentlichung als Open Source | Organisatorisch | ⚠️ | 🟡 Spannung |
| Kodierrichtlinien (Sun/Oracle, CheckStyle) | Konvention | ⚠️ | 🟡 Prüfung nötig |
| Sprache Deutsch für Bezeichner | Konvention | ⚠️ | 🟡 Spannung |

#### [KRC-01] Bitboard-Entscheidung widerspricht Lösungsstrategie „Lesbarkeit vor Effizienz"

**Konflikttyp:** K4 — Implizite Verletzung
**Schwere:** 🔴 Kritisch
**Betroffene Dateien:**
- `src/04-Loesungsstrategie/04-02-Aufbau.md` — *„Lesbarkeit vor Effizienz"*
- `src/09-Entscheidungen/09-03-Brettrepraesentation.md` — Bitboards priorisieren Effizienz zulasten der Lesbarkeit

**Beschreibung:** Das Designprinzip „Lesbarkeit vor Effizienz" ist direkt abgeleitet aus den organisatorischen Randbedingungen (Team-Zusammensetzung, Open-Source-Veröffentlichung für Lern-/Seminarzwecke). Ein Verstoß gegen die Strategie verletzt implizit auch den Rahmen der Randbedingungen.

**Lösungsvorschlag:** Entweder (a) ADR 09-03 auf Status „Rejected" setzen, oder (b) Lösungsstrategie in `04-02-Aufbau.md` aktualisieren und das Prinzip differenzieren:

> *„Für die öffentlichen Schnittstellen und das Domänenmodell gilt weiterhin Lesbarkeit vor Effizienz. Für die interne Brettrepräsentation wurde eine effizientere, aber komplexere Implementierung gewählt (→ Entscheidung 9.3)."*

---

#### [KRC-02] Bitboards widersprechen Strategieansatz „OO Domänenmodell"

**Konflikttyp:** K4 — Implizite Verletzung
**Schwere:** 🔴 Kritisch
**Betroffene Dateien:**
- `src/04-Loesungsstrategie/04-01-Einstieg.md` — *„Explizites, objektorientiertes Domänenmodell"* für Analysierbarkeit
- `src/09-Entscheidungen/09-03-Brettrepraesentation.md` — Bitboards sind nicht-objektorientiert

**Beschreibung:** DokChess dient gerade als Lehrbeispiel, bei dem auch die Implementierung untersucht wird. Die organisatorische Randbedingung „Team" (Workshop-Teilnehmer) setzt implizit voraus, dass der Code zugänglich bleibt.

**Lösungsvorschlag:** In `04-01-Einstieg.md` ergänzen:

> *„Die interne Brettrepräsentation nutzt Bitboards für Effizienz; die öffentlichen API-Schnittstellen behalten das objektorientierte Domänenmodell bei (→ Entscheidung 9.3)."*

---

#### [KRC-03] Dokumentierte Brettimplementierung in Konzept 8.2 wird ungültig

**Konflikttyp:** K4 — Implizite Verletzung
**Schwere:** 🟡 Warnung
**Betroffene Dateien:**
- `src/08-Konzepte/08-02-Domaenenmodell.md` — *„zweidimensionales Array (8 x 8)"*
- `src/09-Entscheidungen/09-03-Brettrepraesentation.md` — Bitboards ersetzen das 8×8-Array

**Beschreibung:** Überschneidung mit KKE-01. Das Implementierungsdetail in Sektion 8.2 wäre nach Umsetzung der ADR faktisch falsch.

**Lösungsvorschlag:** Siehe KKE-01.

---

#### [KRC-04] Team-Randbedingung vs. erforderliches Spezialwissen für Bitboards

**Konflikttyp:** K2 — Organisatorische Constraint-Verletzung
**Schwere:** 🟡 Warnung
**Betroffene Dateien:**
- `src/02-Randbedingungen/02-02-Organisatorisch.md` — *„Stefan Zörner, unterstützt durch Kollegen, Bekannte und Interessierte aus Workshops und Seminaren"*
- `src/09-Entscheidungen/09-03-Brettrepraesentation.md` — *„Bitweise Operationen sind fuer Nicht-Schachprogrammierer schwer nachvollziehbar"*

**Beschreibung:** Die organisatorische Randbedingung beschreibt ein Team, das Lernende und Einsteiger umfasst. Die ADR führt wissentlich eine Implementierung ein, die ein wesentlicher Teil des definierten Teams nicht mehr ohne Weiteres verstehen kann.

**Lösungsvorschlag:** In der ADR 09-03 Maßnahmen zur Abmilderung verbindlich definieren:

> *„Maßnahmen zur Wahrung der Zugänglichkeit: (1) Ausführliche Inline-Dokumentation aller Bitboard-Operationen. (2) Bereitstellung eines Visualisierungs-Tools für Bitboards. (3) Einführendes Dokument ‚Bitboards in DokChess' als Einstiegshilfe im Projekt-Wiki."*

---

#### [KRC-05] Konventions-Spannung bei deutschen Bezeichnern für Bitboard-Terminologie

**Konflikttyp:** K3 — Konventions-Verletzung
**Schwere:** 🟢 Hinweis
**Betroffene Dateien:**
- `src/02-Randbedingungen/02-03-Konventionen.md` — *„Verwendung deutscher Bezeichner für Klassen, Methoden etc."*
- `src/09-Entscheidungen/09-03-Brettrepraesentation.md` — Begriffe „Bitboards", „Magic-Bitboard-Tabellen"

**Beschreibung:** Die Konvention verlangt deutsche Bezeichner. Bitboard-Terminologie ist stark englischsprachig geprägt. Bei der Implementierung besteht die Gefahr, dass englische Fachbegriffe ohne Eindeutschung als Klassen- oder Methodennamen verwendet werden.

**Lösungsvorschlag:** In der ADR festhalten, dass deutsche Bezeichner gelten, und ein Mapping definieren:

> *„Für die Benennung im Quelltext gelten weiterhin die Konventionen aus Sektion 2.3: Bitboard → Brett64, Magic-Bitboard-Tabellen → MagischeZugtabellen, o.ä. Eine Zuordnungstabelle englischer Bitboard-Fachbegriffe zu deutschen Bezeichnern wird im Glossar gepflegt."*

---

## Zusammenfassung

| Kategorie | Anzahl |
|---|---|
| 🔴 Kritische Befunde | 6 |
| 🟡 Warnungen / Empfehlungen | 9 |
| 🟢 Hinweise | 4 |
| ❌ Sektionsübergreifende Konflikte | 14 |

> **Hinweis:** Die kritischen Befunde S09-01, KSE-01/02, KRC-01/02 und KKE-01 adressieren im Kern **denselben fundamentalen Widerspruch** aus verschiedenen Perspektiven: Die ADR 09-03 invertiert das in der Lösungsstrategie festgeschriebene Designprinzip *„Lesbarkeit vor Effizienz"* und widerspricht dem dokumentierten Domänenmodell, ohne die betroffenen Sektionen mitzuziehen.

### Handlungsempfehlungen

1. **Vor Merge zwingend:** Lösungsstrategie (`04-01-Einstieg.md`, `04-02-Aufbau.md`) aktualisieren — das Prinzip „Lesbarkeit vor Effizienz" differenzieren (öffentliche Schnittstellen vs. interne Repräsentation) und Bitboards als bewusste Ausnahme verankern.
2. **Vor Merge zwingend:** Domänenmodell (`08-02-Domaenenmodell.md`) aktualisieren — die Passage zum *„zweidimensionalen Array (8×8)"* durch die Bitboard-Repräsentation ersetzen.
3. **Vor Merge empfohlen:** In ADR 09-03 den Context um die bestehende Designphilosophie als Gegenkraft ergänzen und in Consequences die Auswirkung auf das Qualitätsziel „Analysierbarkeit" explizit benennen.
4. **Vor Merge empfohlen:** Annahme in ADR `09-02-Stellungsobjekte.md` (*„OO-Modell effizient genug"*) mit Verweis auf ADR 09-03 präzisieren.
5. **Zeitnah:** Konzept für Bitboard-Debugging in Sektion 8 ergänzen und Glossar um Bitboard-Terminologie erweitern.