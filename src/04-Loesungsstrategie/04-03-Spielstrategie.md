# Spielstrategie

## 4.3 Spielstrategie

Für die Integration von Eröffnungsbibliotheken wurde das Dateiformat „Polyglot Opening Book“ implementiert ([→ Bausteinsicht 5.5 “Eröffnung“](../05-Bausteinsicht/05-05-Eroeffnung.md)), DokChess antwortet dadurch zu Beginn mit „Buchwissen“.

Für die Spielstrategie im weiteren Partieverlauf ist ein klassischer [Minimax­-Algorithmus](https://de.wikipedia.org/wiki/Minimax-Algorithmus) mit fester Suchtiefe im Spielbaum verantwortlich.
Dessen Basis-Implementierung ist nicht nebenläufig, die Bewertung einer Stellung an einem Terminalknoten im Spielbaum basiert ausschließlich auf dem Material ([→ Bausteinsicht Ebene 2, 5.6 “Engine“](../05-Bausteinsicht/05-06-Ebene-2-Engine.md)). Diese einfachen Implementierungen erfüllen unter den gegebenen Randbedingungen bereits die Qualitätsszenarien.

Eine [Alpha­-Beta­-Suche](https://de.wikipedia.org/wiki/Alpha-Beta-Suche) illustriert den einfachen Austausch von Algorithmen. Spielstärke und/oder Effizienz verbessern sich durch die bei gleicher Rechenzeit tiefere Suche im Baum erheblich. Die unveränderlichen Datenstrukturen in DokChess erleichtern auch das Implementieren nebenläufiger Algorithmen; ein paralleler Minimax ist ebenfalls als Beispiel enthalten.
