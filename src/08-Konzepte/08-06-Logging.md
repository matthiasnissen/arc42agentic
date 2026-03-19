# Protokollierung

## 8.6 Logging, Protokollierung, Tracing

Für Verbesserungen und Erweiterungen von DokChess durch Dritte sind die vorhandenen Analysemöglichkeiten von Interesse, insbesondere bei Fehlverhalten.

Die Funktionalität selbst lässt sich gut mit Unit-Tests überprüfen.
Das gilt insbesondere für die korrekte Implementierung der Spielregeln, für die Spielweise der Engine ([→ 8.7 „Testbarkeit“](08-07-Testbarkeit.md)) und auch für eigene Erweiterungen.

Innerhalb von DokChess gibt es daher keine feinkörnigen Logging-Ausgaben; Lösungen wie log4j kommen nicht zum Einsatz.
Auf diese Weise wird eine Abhängigkeit zu einer Fremdbibliothek, die sich durch den ganzen Quelltext ziehen würde, vermieden und der Code nicht durch diesen Aspekt verschmutzt.

Für die Kommunikation zwischen Client und DokChess über das XBoard-Protokoll besteht neben der interaktiven Bedienung über eine Shell ([→ 8.3 Benutzungsoberfläche](08-03-Benutzungsoberflaeche.md)) oft die Möglichkeit, den Client die Konversation protokollieren zu lassen. Gängige Schachfrontends erlauben dies über das Schreiben von Log-Dateien und/oder die simultane Anzeige eines Protokollfensters während des Spiels. Das folgende Bild zeigt diese Funktionalität exemplarisch für Arena.

![Protokollfenster zum XBoard-Protokoll in Arena](../images/Abb09_23_ProtokollfensterArena.png)

Solche Werkzeuge sind von unschätzbarem Wert, wenn die Engine hängt und unklar ist, was auf dem XBoard-Protokoll gelaufen ist. Aufgrund ihrer Verfügbarkeit wurde auf die Implementierung eines Kommunikationsprotokoll-Tracings innerhalb von DokChess verzichtet.
