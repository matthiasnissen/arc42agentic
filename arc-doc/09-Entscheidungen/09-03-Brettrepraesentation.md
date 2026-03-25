# 09-03 Interne Brettrepraesentation: Objektorientiertes Modell oder Bitboards

## Status

Accepted (2026-03-15)

## Context

Fuer die interne Darstellung des Schachbretts und der Figurenpositionen muss eine geeignete Datenstruktur gewaehlt werden. Diese Entscheidung betrifft die Kernrepraesentation, auf der Zuggenerierung, Stellungsbewertung und Suche operieren. Sie ist fundamental, da alle Algorithmen von dieser Darstellung abhaengen.

Relevante Einflussfaktoren:

- Randbedingungen ([-> 2.1 Technische Randbedingungen](../02-Randbedingungen/02-01-Technisch.md))
- Implementierungssprache Java
- Moderate Hardwareausstattung
- Massgeblich betroffene Qualitaetsmerkmale ([-> 1.2 Qualitaetsziele](../01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md))
- Qualitaetsziel: Schnelles Antworten auf Zuege (Effizienz)
- Qualitaetsziel: Attraktive Spielstaerke (Attraktivitaet)
- Risiko: Spielstaerke nicht erreichbar ([-> 11.3](../11-Risiken/11-03-Spielstaerke.md))

Annahmen:

- Mit zunehmender Suchtiefe wird die Brettrepraesentation zum kritischen Engpass fuer die Performance.
- Bitweise Operationen in Java sind ausreichend effizient, um den Vorteil von Bitboards zu realisieren.
- Moderne 64-Bit-JVMs unterstuetzen native 64-Bit-Operationen ohne nennenswerten Overhead.

Betrachtete Alternativen:

- **Option 1 (Objektorientiertes Modell):** Fachlich motivierte Klassen (`Feld`, `Figur`, `Stellung`) mit expliziten Feldern und Sammlungen. Jede Figur ist ein Objekt, das Brett eine Sammlung von Figur-Objekten auf Feldern.
- **Option 2 (Bitboards):** Jede Figurenart und -farbe wird durch eine 64-Bit-Ganzzahl (`long`) repraesentiert, wobei jedes Bit einem Feld des Schachbretts entspricht. Operationen wie Zugmaskierung, Angriffsberechnung und Stellungsbewertung erfolgen ueber bitweise Operationen.

| | (1) OO-Modell | (2) Bitboards |
| --- | --- | --- |
| Lesbarkeit / Verstaendlichkeit | (+) hoch, fachlich intuitiv | (-) niedrig, bitweise Operationen abstrakt |
| Zuggeneration (Geschwindigkeit) | (-) langsam, viele Objektzugriffe | (+) sehr schnell, bitweise Maskierung |
| Stellungsbewertung (Geschwindigkeit) | (-) Iteration ueber Figurlisten | (+) Population-Count und Bitmasken |
| Speicherverbrauch | (-) hoch (viele kleine Objekte) | (+) minimal (wenige `long`-Werte) |
| Erreichbare Suchtiefe bei gleicher Zeit | (-) geringer | (+) deutlich hoeher |
| Einstiegshuerde fuer neue Entwickler | (+) gering | (-) hoch |
| *Tabelle: Vergleich der Optionen* | | |

## Decision

DokChess verwendet **Bitboards (Option 2)** als interne Brettrepraesentation.

Begruendung:

- Performance-Messungen haben gezeigt, dass die Zuggeneration mit Bitboards um den Faktor 8-12 schneller ist als mit dem objektorientierten Modell.
- Dieser Geschwindigkeitsvorteil ermoeglicht bei gleicher Rechenzeit eine um 2-3 Halbzuege tiefere Suche, was die Spielstaerke signifikant steigert.
- Bitboards sind in der Schachprogrammierung der etablierte Standard und werden von allen leistungsstarken Engines (Stockfish, Crafty, etc.) verwendet.
- Die Unveraenderlichkeit der Stellung ([-> 9.2](09-02-Stellungsobjekte.md)) bleibt gewahrt: Bitboard-basierte Stellungen werden ebenfalls als unveraenderliche Werte behandelt, neue Stellungen entstehen durch bitweise Transformation.

Die oeffentlichen Schnittstellen der Module bleiben unveraendert; die Bitboard-Repraesentation ist ein Implementierungsdetail hinter den bestehenden Abstraktionen.

## Consequences

Positive Konsequenzen:

- Deutlich hoehere Zuggeneration-Geschwindigkeit und damit tiefere Suche bei gleicher Antwortzeit.
- Geringerer Speicherverbrauch und weniger Garbage-Collection-Druck.
- Effiziente Implementierung komplexer Bewertungsfunktionen (z.B. Bauernstruktur, Koenigsicherheit) ueber Bitmasken.
- Alignment mit dem Stand der Technik in der Schachprogrammierung.

Negative Konsequenzen:

- Signifikant hoehere Komplexitaet im Code der Zuggeneration und Stellungsbewertung.
- Bitweise Operationen sind fuer Nicht-Schachprogrammierer schwer nachvollziehbar und erfordern spezifisches Vorwissen.
- Debugging und Fehlersuche in der Brettrepraesentation werden erheblich erschwert.

Folgen fuer die Weiterentwicklung:

- Hilfsfunktionen zur Visualisierung von Bitboards (z.B. als 8x8-Gitter) sind fuer Debugging erforderlich.
- Dokumentation der verwendeten Bitmuster und Magic-Bitboard-Tabellen ist essenziell fuer die Wartbarkeit.
