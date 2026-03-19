# Validierung

## 8.4 Plausibilisierung und Validierung

DokChess ist, vereinfacht ausgedrückt, ein Algorithmus, es antwortet auf Züge des Gegners mit eigenen Zügen. Für die Überprüfung von Eingaben sind zwei Kanäle relevant: das XBoard-Protokoll für interaktive Benutzereingaben des Gegners sowie Eröffnungsbibliotheken in Form von Dateien.

Eingaben, die über das XBoard-Protokoll eingehen, werden vom entsprechenden Subsystem geparst. Unbekannte oder nicht implementierte Kommandos meldet DokChess mit dem XBoard-Kommando “Error” an den Client zurück.

Im Falle eines Zugkommandos wird mit Hilfe des Spielregeln-Subsystem überprüft, ob der Zug regelkonform ist. Unzulässige Züge meldet DokChess mit dem XBoard-Kommando “Illegal move” an den Client zurück.
Bei Verwendung eines grafischen Frontends sollte dieser Fall nicht auftreten, da diese typischerweise nur gültige Züge absetzen. Der Fall ist eher für die Interaktion per Kommandozeile relevant ([→ 8.3 „Benutzungsoberfläche“](08-03-Benutzungsoberflaeche.md)).

Beim Aufbau einer Stellung überprüft DokChess die Einhaltung des Protokolls, nicht aber, ob die Position zulässig ist. Im Extremfall kann das dazu führen, dass das Engine-Subsystem im Spielverlauf Fehler wirft (z.B. wenn man keine Könige auf das Brett stellt).

Bei den Eröffnungsbibliotheken prüft DokChess lediglich, ob es die Datei öffnen und einlesen kann. Im Fehlerfall (konkret z.B.: Datei nicht gefunden) wird eine Exception geworfen ([→ 8.5](08-05-Fehlerbehandlung.md)).
Beim Einlesen quittiert das Eröffnung-Subsystem von ihm erkannte Probleme (z.B. ungültiges Format) ebenfalls mit einem Laufzeitfehler.
Inhaltlich prüft es die Bibliothek jedoch nicht. Falls beispielsweise unzulässige Züge für eine Stellung hinterlegt sind, wird das nicht erkannt. Für die Qualität der Bibliothek ist der Anwender selbst verantwortlich (siehe [→ 3. Kontextabgrenzung](../03-Kontextabgrenzung/03-01-Fachlicher-Kontext.md)).
Im Extremfall antwortet die Engine mit einem ungültigen Zug.
