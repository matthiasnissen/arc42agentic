# 09-01 Frontend-Anbindung

## Status

Accepted (2026-03-10)

## Context

Als zentrale Anforderung muss DokChess mit vorhandenen Schach-Frontends zusammenarbeiten. Die Architekturentscheidung betrifft die Frage, wie die Engine an diese Frontends angebunden wird.

Es existieren verschiedene grafische Oberflaechen fuer Schachprogramme. Je nachdem, welches Kommunikationsprotokoll genutzt wird, kann DokChess mit unterschiedlichen Frontends zusammenarbeiten. Das hat direkten Einfluss auf Interoperabilitaet und auf die Anpassbarkeit an zukuenftige Schach-Software.

Relevante Einflussfaktoren:

- Betrieb der Frontends zumindest auf Windows-Desktop-Betriebssystemen
- Unterstuetzung frei verfuegbarer Frontends
- Bevorzugung etablierter (Schach-)Standards ([-> 2.3 Konventionen](../02-Randbedingungen/02-03-Konventionen.md))
- Massgeblich betroffene Qualitaetsmerkmale ([-> 1.2 Qualitaetsziele](../01-Einfuehrung-und-Ziele/01-02-Qualitaetsziele.md))
- Qualitaetsziel: Bestehende Frontends nutzen (Interoperabilitaet)
- Qualitaetsziel: Einladende Experimentierplattform (Aenderbarkeit)
- Risiko: Anbindung an das Frontend schlaegt fehl ([-> 11.1](../11-Risiken/11-01-Frontend.md))

Annahme:

- Die Untersuchung weniger verfuegbarer Frontends fuehrt zu allen relevanten Integrationsoptionen.

Betrachtete Alternativen:

- Option 1: UCI Protocol (Universal Chess Interface, [Details](https://www.chessprogramming.org/UCI))
- Option 2: XBoard Protocol (auch WinBoard/Chess Engine Communication Protocol, [Details](https://www.chessprogramming.org/Chess_Engine_Communication_Protocol))

Untersuchte Frontends (Stand 2011):

- Arena Chess GUI (frei verfuegbar, Windows)
- Fritz for Fun (kommerziell, Windows)
- WinBoard/XBoard (Open Source, Windows, Mac OS X, Linux/*nix)

Beide Protokolle sind textbasiert; die Kommunikation erfolgt ueber stdin/stdout. Das Frontend startet die Engine jeweils in einem separaten Prozess.

| | Arena 3 | Fritz for Fun | Winboard/XBoard |
| --- | --- | --- | --- |
| UCI-Protokoll | Ja | Ja | - |
| XBoard-Protokoll | Ja | - | Ja |
| *Tabelle: Protokolle und Frontends* | | | |

## Decision

DokChess implementiert das **XBoard-Protokoll** als primaeres Kommunikationsprotokoll.

Die Entscheidung fiel zugunsten von XBoard, weil damit neben Windows auch weitere Betriebssysteme (insbesondere Mac OS X und Linux) mit frei verfuegbaren Frontends unterstuetzt werden koennen. Das bevorzugte Frontend unter Windows ist Arena; Arena unterstuetzt beide Protokolle.

Die Struktur von DokChess bleibt so ausgelegt, dass alternative Protokolle (z.B. UCI) spaeter ergaenzt werden koennen, ohne die Engine selbst zu veraendern ([-> 5.1](../05-Bausteinsicht/05-01-Ebene-1.md)).

## Consequences

Positive Konsequenzen:

- Breitere Interoperabilitaet mit frei verfuegbaren Frontends ueber mehrere Betriebssysteme.
- Niedrige Einstiegshuerde fuer Nutzer durch freie Werkzeuge.
- Gute Debugging-Unterstuetzung durch das bevorzugte Frontend Arena.
- Erweiterbarkeit bleibt erhalten: zusaetzliche Protokolle koennen spaeter hinzugefuegt werden.

Negative Konsequenzen:

- UCI wird initial nicht nativ umgesetzt; UCI-spezifische Integrationen sind zunaechst nicht direkt verfuegbar.
- Die Bewertung der Integrationsoptionen basiert auf einer begrenzten Menge betrachteter Frontends.

Neutrale/Folgen fuer die Weiterentwicklung:

- Die Kommunikationsschnittstelle muss stabil gehalten werden, damit spaetere Protokollerweiterungen ohne Eingriffe in die Engine moeglich bleiben.
