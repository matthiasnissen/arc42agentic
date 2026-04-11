# arc42 Branch-Review

## Überblick

**Branch:** `Konflikt/ADR`
**Basis:** `origin/main`
**Geänderte Dateien:** 1
**Betroffene Sektionen:** S9 (Architekturentscheidungen)

## Geänderte Dateien

| Datei | Änderungstyp | Sektion |
|---|---|---|
| `arc-doc/09-Entscheidungen/09-03-Brettrepraesentation.md` | Added | Sektion 9 |

## Gesamtübersicht

| Sektion | Status | Befunde |
|---------|--------|---------|
| 9. Architekturentscheidungen | 🔴 | Neue ADR formal einwandfrei, aber unaufgelöster Widerspruch zur Lösungsstrategie (S4) |

| Konfliktdimension | Status | Befunde |
|---|---|---|
| Strategie ↔ Entscheidungen (S4 ↔ S9) | 🔴 | Zwei direkte Widersprüche: „Lesbarkeit vor Effizienz" und „OO-Domänenmodell" vs. Bitboards |
| Konzepte ↔ Entscheidungen (S8 ↔ S9) | 🔴 | Domänenmodell beschreibt 8×8-Array, ADR entscheidet für Bitboards; Testbarkeit/Debugging fehlen |
| Constraint-Compliance (S2 ↔ S9) | 🟡 | Lehr-Intention, Teamzugänglichkeit und deutsche Bezeichner in Spannung mit Bitboards |

## Sektions-Reviews

### Sektion 9: Architekturentscheidungen

**Formale Prüfung:** Alle Pflichtabschnitte des Nygard-ADR-Formats sind vorhanden und korrekt strukturiert. Stilistisch konsistent mit den bestehenden ADRs 09-01 und 09-02.

#### [S09-01] Widerspruch zur Lösungsstrategie — „Lesbarkeit vor Effizienz"

**Schwere:** 🔴 Kritisch
**Datei:** `arc-doc/09-Entscheidungen/09-03-Brettrepraesentation.md`
**Kriterium:** Konsistenz mit Lösungsstrategie (Sektion 4)

**Befund:** Die Lösungsstrategie in `arc-doc/04-Loesungsstrategie/04-02-Aufbau.md` formuliert zweifach explizit „bewusst eine bessere Verständlichkeit angestrebt, auf Kosten von Effizienz". Die neue ADR entscheidet das exakte Gegenteil: Effizienz vor Lesbarkeit. Die ADR mildert dies durch Beibehaltung öffentlicher Schnittstellen ab, adressiert aber den strategischen Widerspruch nicht.

**Änderungsvorschlag:** Im ADR-Abschnitt **Decision** ergänzen:

> Diese Entscheidung weicht bewusst vom in der Lösungsstrategie ([→ 4.2](../04-Loesungsstrategie/04-02-Aufbau.md)) formulierten Grundsatz „Lesbarkeit vor Effizienz" ab. Der Grundsatz gilt weiterhin für die öffentlichen Schnittstellen und das fachliche Domänenmodell. Die Bitboard-Repräsentation betrifft ausschließlich die interne Implementierung. In der Lösungsstrategie sollte diese Differenzierung nachgetragen werden.

---

#### [S09-02] Performance-Messungen ohne Quellenangabe

**Schwere:** 🟡 Empfehlung
**Datei:** `arc-doc/09-Entscheidungen/09-03-Brettrepraesentation.md`
**Kriterium:** Nachvollziehbarkeit der Entscheidungsbegründung

**Befund:** Konkrete Zahlen (Faktor 8–12, 2–3 Halbzüge) ohne Verweis auf Messmethodik oder Prototyp. ADR 09-02 verweist zum Vergleich auf einen konkreten Prototypvergleich.

**Änderungsvorschlag:** Den Satz ergänzen:

> Performance-Messungen in einem Prototypvergleich (Perft-Test, Tiefe 6, Startstellung) haben gezeigt, dass …

---

#### [S09-03] Fehlender Verweis aus Sektion 4 auf dieses ADR

**Schwere:** 🟡 Empfehlung
**Datei:** `arc-doc/04-Loesungsstrategie/04-02-Aufbau.md`
**Kriterium:** Querverweisstruktur

**Befund:** Die bestehenden ADRs 09-01 und 09-02 werden aus S4 referenziert. Für die neue ADR 09-03 fehlt ein entsprechender Verweis.

**Änderungsvorschlag:** In `arc-doc/04-Loesungsstrategie/04-02-Aufbau.md` ergänzen:

> Für die interne Brettrepräsentation wurde aus Effizienzgründen von diesem Grundsatz abgewichen ([→ Entscheidung 9.3](../09-Entscheidungen/09-03-Brettrepraesentation.md)).

---

## Konfliktanalyse

### 1. Strategie ↔ Entscheidungen (S4 ↔ S9)

#### [KSE-01] Strategie „Lesbarkeit vor Effizienz" vs. Bitboard-Entscheidung

**Konflikttyp:** K1 — Direkter Widerspruch
**Schwere:** 🔴 Kritisch
**Betroffene Dateien:**
- `arc-doc/04-Loesungsstrategie/04-02-Aufbau.md` — „bewusst eine bessere Verständlichkeit angestrebt, auf Kosten von Effizienz"
- `arc-doc/09-Entscheidungen/09-03-Brettrepraesentation.md` — Entscheidung für Bitboards, „Lesbarkeit: (-) niedrig"

**Beschreibung:** Die Lösungsstrategie formuliert als bewusstes Entwurfsprinzip, dass bei den zentralen Datenstrukturen (Stellung, Spielsituation) **Lesbarkeit vor Effizienz** geht. Dies wird in `04-02-Aufbau.md` gleich zweifach betont. ADR 09-03 trifft die exakt gegenteilige Abwägung: Bitboards werden **wegen** ihrer Performance gewählt (Faktor 8–12), obwohl ihre Lesbarkeit als niedrig und die Einstiegshürde als hoch eingestuft wird.

**Lösungsvorschlag:** Strategie in `04-02-Aufbau.md` aktualisieren:

> *Für die interne Brettrepräsentation wurde von diesem Grundsatz abgewichen: Hier kommen Bitboards zum Einsatz, deren Performance-Vorteil (Faktor 8–12 bei der Zuggeneration) die Spielstärke signifikant steigert. Die öffentlichen Schnittstellen bleiben fachlich motiviert und objektorientiert; die Bitboard-Repräsentation ist ein Implementierungsdetail hinter den bestehenden Abstraktionen ([→ Entscheidung 9.3](../09-Entscheidungen/09-03-Brettrepraesentation.md)).*

---

#### [KSE-02] Strategie „OO-Domänenmodell" vs. Bitboard-Repräsentation

**Konflikttyp:** K1 — Direkter Widerspruch
**Schwere:** 🔴 Kritisch
**Betroffene Dateien:**
- `arc-doc/04-Loesungsstrategie/04-01-Einstieg.md` — „Explizites, objektorientiertes Domänenmodell" für Analysierbarkeit
- `arc-doc/09-Entscheidungen/09-03-Brettrepraesentation.md` — `long`-Werte statt Klassen

**Beschreibung:** Die Lösungsstrategie nennt ein „explizites, objektorientiertes Domänenmodell" als zentralen Architekturansatz für das Qualitätsziel „Zugängliches Beispiel (Analysierbarkeit)". ADR 09-03 ersetzt die interne Repräsentation durch Bitboards (`long`-Werte mit bitweiser Maskierung). Zusätzlich wird die Annahme aus ADR 09-02 — „Ein fachliches Objektmodell ist effizient genug implementierbar" — durch ADR 09-03 implizit widerlegt.

**Lösungsvorschlag:** In `04-01-Einstieg.md` differenzieren:

> `Explizites, objektorientiertes Domänenmodell auf Schnittstellenebene; intern nutzt die Brettrepräsentation performanceoptimierte Bitboards ([→ Entscheidung 9.3](../09-Entscheidungen/09-03-Brettrepraesentation.md))`

---

#### [KSE-03] Strategielücke: Bitboards nicht in S4 reflektiert

**Konflikttyp:** K3 — Veraltete/unvollständige Strategie
**Schwere:** 🟡 Warnung
**Betroffene Dateien:**
- `arc-doc/04-Loesungsstrategie/04-01-Einstieg.md` — Tabelle listet nur Reactive Extensions, Alpha-Beta, „Effiziente Implementierung"
- `arc-doc/04-Loesungsstrategie/04-03-Spielstrategie.md` — erwähnt tiefere Suche nur durch Alpha-Beta

**Beschreibung:** ADR 09-03 ist strategisch hochrelevant (2–3 Halbzüge tiefere Suche), fehlt aber in der Strategietabelle und in der Spielstrategie.

**Lösungsvorschlag:** In `04-01-Einstieg.md` bei „Schnelles Antworten auf Züge (Effizienz)" ergänzen:

> `- Bitboard-basierte Brettrepräsentation für performante Zuggeneration`

In `04-03-Spielstrategie.md` ergänzen:

> *Ein weiterer wesentlicher Faktor für die erreichbare Suchtiefe ist die interne Brettrepräsentation auf Basis von Bitboards ([→ Entscheidung 9.3](../09-Entscheidungen/09-03-Brettrepraesentation.md)).*

---

#### [KSE-04] Spannung mit Qualitätsziel „Einladende Experimentierplattform"

**Konflikttyp:** K1 — Indirekter Widerspruch
**Schwere:** 🟡 Warnung
**Betroffene Dateien:**
- `arc-doc/04-Loesungsstrategie/04-01-Einstieg.md` — „Einladende Experimentierplattform (Änderbarkeit)"
- `arc-doc/09-Entscheidungen/09-03-Brettrepraesentation.md` — „Einstiegshürde: (-) hoch"

**Beschreibung:** Bitboards stehen in Spannung zum Ziel einer einladenden Experimentierplattform. Die Schnittstellen-Abstraktion mildert dies teilweise.

**Lösungsvorschlag:** In der ADR unter „Consequences" dokumentieren:

> *Die höhere Einstiegshürde steht in Spannung zum Qualitätsziel „Einladende Experimentierplattform". Experimente an Stellungsbewertung oder Zugauswahl können über die bestehenden Abstraktionen erfolgen, ohne Bitboard-Details zu kennen. Für Experimente an der Zuggeneration selbst ist Bitboard-Wissen erforderlich.*

---

### 2. Konzepte ↔ Entscheidungen (S8 ↔ S9)

#### [KKE-01] Domänenmodell beschreibt 8×8-Array, ADR entscheidet für Bitboards

**Konflikttyp:** K1 — Direkter Widerspruch
**Schwere:** 🔴 Kritisch
**Betroffene Dateien:**
- `arc-doc/08-Konzepte/08-02-Domaenenmodell.md` — „intern als zweidimensionales Array (8 × 8) implementiert"
- `arc-doc/09-Entscheidungen/09-03-Brettrepraesentation.md` — „DokChess verwendet Bitboards als interne Brettrepräsentation"

**Beschreibung:** Das Domänenmodell-Konzept beschreibt die Klasse `Stellung` explizit als zweidimensionales 8×8-Array mit `null` für unbesetzte Felder. Die ADR entscheidet für 64-Bit-`long`-Werte (Bitboards). Leser erhalten widersprüchliche Informationen.

**Lösungsvorschlag:** In `08-02-Domaenenmodell.md` aktualisieren:

> Die Klasse *Stellung* stellt die aktuelle Situation auf dem Brett dar. Die Figurenpositionen werden intern über Bitboards repräsentiert — jede Figurenart und -farbe als 64-Bit-Wert (`long`), wobei jedes Bit einem Feld entspricht ([→ Entscheidung 9.3](../09-Entscheidungen/09-03-Brettrepraesentation.md)).

---

#### [KKE-02] Debugging-Konzept für Bitboards fehlt

**Konflikttyp:** K5 — Fehlende Konzeptbeschreibung
**Schwere:** 🟡 Warnung
**Betroffene Dateien:**
- `arc-doc/09-Entscheidungen/09-03-Brettrepraesentation.md` — „Debugging und Fehlersuche werden erheblich erschwert"
- `arc-doc/08-Konzepte/08-05-Fehlerbehandlung.md` — behandelt nur Runtime Exceptions und XBoard

**Beschreibung:** Die ADR fordert Visualisierungs-Hilfsfunktionen für Bitboards. Das Fehlerbehandlungskonzept adressiert dies nicht.

**Lösungsvorschlag:** In `08-05-Fehlerbehandlung.md` ergänzen:

> ### Debugging der Brettrepräsentation
>
> Da die interne Brettrepräsentation auf Bitboards basiert ([→ Entscheidung 9.3](../09-Entscheidungen/09-03-Brettrepraesentation.md)), sind bitweise kodierte Stellungen für Menschen nicht direkt lesbar. Hilfsfunktionen visualisieren einzelne Bitboards als 8×8-Gitter und erleichtern so die Fehlersuche in Zuggenerierung und Stellungsbewertung.

---

#### [KKE-03] Teststrategie für Bitboard-Korrektheit fehlt

**Konflikttyp:** K5 — Fehlende Konzeptbeschreibung
**Schwere:** 🟡 Warnung
**Betroffene Dateien:**
- `arc-doc/09-Entscheidungen/09-03-Brettrepraesentation.md` — „Signifikant höhere Komplexität im Code"
- `arc-doc/08-Konzepte/08-07-Testbarkeit.md` — beschreibt nur FEN-basierte Tests

**Beschreibung:** FEN-basierte Tests prüfen nur das externe Verhalten. Bitboard-Korrektheit (Bitmaskierung, Magic-Bitboard-Tabellen, Population-Count) erfordert zusätzliche Teststrategien.

**Lösungsvorschlag:** In `08-07-Testbarkeit.md` ergänzen:

> ### Testen der Bitboard-Repräsentation
>
> Die Bitboard-basierte Brettrepräsentation ([→ Entscheidung 9.3](../09-Entscheidungen/09-03-Brettrepraesentation.md)) erfordert neben den fachlichen Tests über FEN auch gezielte Tests auf Bit-Ebene: Verifikation einzelner Bitmasken, Korrektheit der Magic-Bitboard-Tabellen sowie Grenzfälle bei bitweisen Transformationen.

---

#### [KKE-04] Figur/Feld-Objektmodell vs. Bitmasken-Realität

**Konflikttyp:** K1 — Direkter Widerspruch
**Schwere:** 🟢 Hinweis
**Betroffene Dateien:**
- `arc-doc/08-Konzepte/08-02-Domaenenmodell.md` — `Figur` als eigenständiges Objekt mit `Farbe` und `Art`
- `arc-doc/09-Entscheidungen/09-03-Brettrepraesentation.md` — Figuren als Bitmasken pro Typ und Farbe

**Lösungsvorschlag:** Im Domänenmodell klarstellen, dass die fachlichen Klassen als Schnittstellenkonzepte gelten und die interne Repräsentation über Bitboards erfolgt.

---

### 3. Constraint-Compliance (S2 ↔ S9)

#### [KRC-01] Bitboards vs. Lehr-Intention der Java-Constraint

**Konflikttyp:** K4 — Implizite Verletzung
**Schwere:** 🟡 Warnung
**Betroffene Dateien:**
- `arc-doc/02-Randbedingungen/02-01-Technisch.md` — Constraint „Java" mit Begründung: „Einsatz als Beispiel in Java-lastigen Seminaren"
- `arc-doc/09-Entscheidungen/09-03-Brettrepraesentation.md` — „Bitweise Operationen sind für Nicht-Schachprogrammierer schwer nachvollziehbar"

**Beschreibung:** Der Java-Constraint wird technisch eingehalten, aber die dokumentierte Intention (zugängliches Lehrbeispiel) wird durch die Bitboard-Komplexität konterkariert.

**Lösungsvorschlag:** In der ADR dokumentieren, wie der Seminar-Einsatz erhalten bleibt, z.B. durch Beibehaltung der OO-Variante als alternative, lehrfreundliche Implementierung.

---

#### [KRC-02] Hohe Einstiegshürde vs. Team mit Workshop-Teilnehmern

**Konflikttyp:** K2 — Organisatorische Constraint-Verletzung
**Schwere:** 🟡 Warnung
**Betroffene Dateien:**
- `arc-doc/02-Randbedingungen/02-02-Organisatorisch.md` — Team: „unterstützt durch Interessierte aus Workshops und Seminaren"
- `arc-doc/09-Entscheidungen/09-03-Brettrepraesentation.md` — „Einstiegshürde für neue Entwickler: (-) hoch"

**Beschreibung:** Workshop-Teilnehmer ohne Spezialkenntnisse werden vom Verständnis einer Kernkomponente faktisch ausgeschlossen.

**Lösungsvorschlag:** Mitigationsmaßnahmen in der ADR ergänzen (ausführliche Kommentierung, Visualisierungshilfen, unveränderte Schnittstellen-Abstraktionen).

---

#### [KRC-03] Bitboard-Terminologie vs. Konvention für deutsche Bezeichner

**Konflikttyp:** K3 — Konventions-Verletzung
**Schwere:** 🟡 Warnung
**Betroffene Dateien:**
- `arc-doc/02-Randbedingungen/02-03-Konventionen.md` — „Verwendung deutscher Bezeichner für Klassen, Methoden etc."
- `arc-doc/09-Entscheidungen/09-03-Brettrepraesentation.md` — Durchgehend englische Begriffe: „Bitboards", „Magic-Bitboard-Tabellen", „Population-Count"

**Beschreibung:** Die Konvention verlangt deutsche Bezeichner. Für Bitboard-Konzepte existieren keine etablierten deutschen Übersetzungen.

**Lösungsvorschlag:** Namenskonvention für Bitboard-Begriffe festlegen, englische Fachbegriffe ohne deutsche Entsprechung im Glossar aufnehmen.

---

#### [KRC-04] Potenzielle CheckStyle-Konflikte durch Bitboard-Code

**Konflikttyp:** K3 — Konventions-Verletzung
**Schwere:** 🟢 Hinweis
**Betroffene Dateien:**
- `arc-doc/02-Randbedingungen/02-03-Konventionen.md` — „Java Coding Conventions, geprüft mit CheckStyle"
- `arc-doc/09-Entscheidungen/09-03-Brettrepraesentation.md` — Magic-Bitboard-Tabellen mit hexadezimalen Konstanten

**Lösungsvorschlag:** CheckStyle-Ausnahmen für Bitboard-Module in der ADR unter „Folgen für die Weiterentwicklung" dokumentieren.

---

## Zusammenfassung

| Kategorie | Anzahl |
|---|---|
| 🔴 Kritische Befunde | 4 |
| 🟡 Warnungen / Empfehlungen | 9 |
| 🟢 Hinweise | 2 |

### Handlungsempfehlungen

1. **Lösungsstrategie (S4) aktualisieren** — `04-02-Aufbau.md` und `04-01-Einstieg.md` müssen die bewusste Abweichung vom Prinzip „Lesbarkeit vor Effizienz" für die interne Brettrepräsentation dokumentieren. *(Löst KSE-01, KSE-02, KSE-03, S09-01, S09-03)*
2. **Domänenmodell (S8) aktualisieren** — `08-02-Domaenenmodell.md` beschreibt ein 8×8-Array, das durch Bitboards ersetzt wurde. Zwingend korrigieren. *(Löst KKE-01, KKE-04)*
3. **ADR 09-03 erweitern** — Strategische Abweichung im Decision-Abschnitt adressieren, Performance-Messungen belegen, Mitigationsmaßnahmen für Lehr-Charakter und Zugänglichkeit dokumentieren. *(Löst S09-02, KSE-04, KRC-01, KRC-02, KRC-03)*
4. **Konzepte ergänzen** — Debugging-Konzept für Bitboards in `08-05-Fehlerbehandlung.md` und Teststrategie in `08-07-Testbarkeit.md` aufnehmen. *(Löst KKE-02, KKE-03)*