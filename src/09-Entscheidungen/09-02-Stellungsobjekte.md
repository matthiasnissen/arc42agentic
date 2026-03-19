# 09-02 Stellungsobjekte: veraenderlich oder unveraenderlich

## Status

Accepted (2026-03-10)

## Context

Spielsituationen auf dem Schachbrett (Stellungen) muessen zwischen mehreren DokChess-Modulen ausgetauscht werden. Die zentrale Frage lautet: Soll die Datenstruktur `Stellung` veraenderlich oder unveraenderlich (immutable) sein?

Die Entscheidung wirkt breit, da von der Schnittstelle der Stellung saemtliche Module abhaengen. Eine spaetere Aenderung wuerde das Gesamtsystem betreffen.

Relevante Einflussfaktoren:

- Randbedingungen ([-> 2.1 Technische Randbedingungen](../02-Randbedingungen/02-01-Technisch.md))
- Implementierungssprache Java
- Moderate Hardwareausstattung
- Massgeblich betroffene Qualitaetsmerkmale ([-> 1.2 Qualitaetsziele](../01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md))
- Qualitaetsziel: Einladende Experimentierplattform (Aenderbarkeit)
- Qualitaetsziel: Akzeptable Spielstaerke (Funktionale Eignung)
- Qualitaetsziel: Schnelles Antworten auf Zuege (Effizienz)
- Risiken: Aufwand zu hoch ([-> 11.2](../11-Risiken/11-02-Aufwand.md)), Spielstaerke nicht erreichbar ([-> 11.3](../11-Risiken/11-03-Spielstaerke.md))

Annahmen:

- Ein fachliches Objektmodell (Feld, Figur, Zug, Stellung) ist effizient genug implementierbar.
- Nebenlaeufige Algorithmen sollen kuenftig moeglich sein.

Betrachtete Alternativen:

- **Option 1 (veraenderlich):** Methoden veraendern den Zustand und erlauben z.B. `fuehreZugAus(...)` und `nimmLetztenZugZurueck()`.
- **Option 2 (unveraenderlich):** `fuehreZugAus(...)` liefert ein neues `Stellung`-Objekt, das Original bleibt unveraendert.

| | (1) veraenderlich | (2) unveraenderlich |
| --- | --- | --- |
| Implementierungsaufwand | (-) hoeher | (+) geringer |
| Effizienz (Speicherverbrauch) | (+) sparsamer | (-) Bedarf hoeher |
| Effizienz (Zeitverhalten) | (o) neutral | (-) schlechter |
| Eignung fuer nebenlaeufige Algorithmen | (-) schlecht | (+) gut |
| *Tabelle: Vergleich der Optionen* | | |

## Decision

DokChess verwendet fuer `Stellung` die **unveraenderliche Variante (Option 2)**.

Begruendung:

- Einfachere Implementierung ohne Undo-Mechanik fuer den Suchbaum.
- Bessere Eignung fuer nebenlaeufige Ausfuehrung.
- Effizienznachteile wurden vorab geprueft: In einem Prototypvergleich (Mattsuche, Minimax, Matt in 3) lag die unveraenderliche Variante bei ca. 30 Prozent laengerer Laufzeit, aber weiterhin innerhalb der geforderten Grenzen.

## Consequences

Positive Konsequenzen:

- Geringerer Implementierungsaufwand in der Suchlogik, da kein explizites Rueckgaengigmachen von Zuegen erforderlich ist.
- Robustere Grundlage fuer spaetere Nebenlaeufigkeit.
- Klarere Nutzungssemantik: alte Stellungen bleiben als Werte erhalten.

Negative Konsequenzen:

- Hoeherer Speicherbedarf durch haeufiges Erzeugen neuer Stellungen.
- Mehr Last auf Garbage Collector und potentiell schlechteres Zeitverhalten.
- Gemessener Effizienznachteil gegenueber Option 1 (im Prototyp ca. 30 Prozent laenger).

Folgen fuer die Weiterentwicklung:

- Performance-Optimierungen bleiben relevant (effizientes Kopieren, spaeter Parallelisierung).
- Der gewaehlte Ansatz wurde mit DokChess 2.0 durch einen parallelen Minimax bereits teilweise adressiert.
