# Qualitätsszenarien

## 10.2 Qualitätsszenarien

Die Anfangsbuchstaben der Bezeichner (IDs) der Szenarien in der folgenden Tabelle  stehen jeweils für das übergeordnete Qualitätsmerkmal, W beispielsweise für Wartbarkeit.
Diese Bezeichner finden auch im [Qualitätsbaum](10-01-Qualitaetsbaum.md) Verwendung.
Nicht immer lassen sich die Szenarien eindeutig einem Merkmal zuordnen.
Sie treten daher mitunter mehrmals im Qualitätsbaum auf.

| ID | Szenario |
| --- | --- |
| W01 | Jemand mit Grundkenntnissen in UML und Schach möchte einen Einstieg in die Architektur von DokChess finden. Lösungsstrategie und Entwurf erschließen sich ihr oder ihm innerhalb von 15 Minuten. |
| W02 | Ein Architekt, der arc42 anwenden möchte, sucht zu einem beliebigen Kapitel des Template einen konkreten Beispielinhalt und findet ihn unverzüglich in der Dokumentation. |
| W03 | Eine erfahrene Java-Entwicklerin sucht die Implementierung eines im Entwurf beschriebenen Moduls. Sie findet sie ohne Umwege oder fremde Hilfe im Quelltext. |
| W04 | Ein Entwickler implementiert eine neue Stellungsbewertung. Er kann sie ohne Änderung und ohne Übersetzung vorhandenen Codes in bestehende Strategien integrieren. |
| W05 | Eine Entwicklerin implementiert eine figurenzentrierte Bitboard-Repräsentation der Spielsituation. Der Aufwand dazu beträgt inklusive des Austauschs der bestehenden, feldzentrierten Darstellung durch die neue maximal eine Woche. |
| K01 | Ein Benutzer will DokChess mit einem Schach-Frontend verwenden, das ein von der Lösung implementiertes Kommunikationsprotokoll unterstützt. Das Einbinden erfordert keinerlei Programmieraufwand, die Konfiguration innerhalb des Frontend ist innerhalb von zehn Minuten durchgeführt und getestet. |
| F01 | In einer Spielsituation hat die Engine einen oder mehrere regelkonforme Züge zur Auswahl. Sie antwortet mit einem dieser Züge. |
| F02 | Ein schwacher Spieler zieht in einer Partie gegen die Engine eine Figur ungedeckt und frei von Sinn auf ein von der Engine angegriffenes Feld. Die Engine im Anschluss am Zug nimmt die „eingestellte“ Figur. |
| F03 | Der Engine eröffnet sich eine Springergabel, um Dame oder Turm zu gewinnen. Die Engine gewinnt Dame (bzw. Turm) gegen Springer. |
| F04 | In einer Partie ergibt sich für die Engine ein Matt in zwei Zügen. Die Engine zieht sicher zum Sieg. |
| E01 | Während einer Partie antwortet die Engine auf gegnerische Züge innerhalb von fünf Sekunden mit einem Zug. |
| E02 | Eine in ein grafisches Frontend integrierte Engine spielt schwarz, der menschliche Spieler zieht an. Die Engine antwortet innerhalb von maximal zehn Sekunden mit ihrem ersten Zug, der Benutzer erhält spätestens nach fünf Sekunden eine Rückmeldung, dass die Engine „denkt“. |
| Z01 | Der Engine wird im Spielverlauf ein unzulässiger Gegenzug präsentiert. Die Engine lehnt den Zug ab, erlaubt im Anschluss die Eingabe eines anderen Zugs und spielt fehlerfrei weiter. |
| Z02 | Der Engine wird zum Spielbeginn eine unzulässige Stellung präsentiert. Die Engine erkennt die Situation und beendet das Spiel. |
| P01 | Eine Java-Programmiererin will DokChess mit einem Schach-Frontend verwenden, welches das Einbinden von Engines erlaubt, aber keines der implementierten Protokolle unterstützt. Sie kann das neue Protokoll ohne Änderung am bestehenden Code implementieren und die Engine anschließend wie gewohnt einbinden. |
