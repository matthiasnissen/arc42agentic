# Zugsuche

## 5.7 Zugsuche (Blackbox)

### Zweck/Verantwortlichkeit

Das Modul ermittelt zu einer Stellung den unter bestimmten Bedingungen optimalen Zug.
Theoretisch gäbe es im Schach einen generell optimalen Zug.
Die hohe Anzahl der möglichen Züge und die damit verbundene schier unglaubliche Anzahl zu bewertender Spielsituationen macht es in der Praxis aber unmöglich, ihn zu bestimmen.
Gängige Algorithmen wie der Minimax begnügen sich daher damit, den “Spielbaum” nur bis zu einer bestimmten Tiefe zu explorieren.

### Schnittstellen

Das Modul stellt seine Funktionalität über die Schnittstelle *de.dokchess.engine.suche.Suche* zur Verfügung.

Der Minimax-Algorithmus liegt in der Klasse *de.dokchess.engine.suche.MinimaxAlgorithmus* vor.
Die Klasse *MinimaxParalleleSuche* nutzt den Algorithmus und implementiert gleichzeitig die Schnittstelle *Suche*.
Sie untersucht mehrere Teilbäume parallel; wenn sie einen besseren Zug findet erhält der Aufrufer eine Nachricht onNext über das Observer-Pattern.
Den Abschluss der Suche signalisiert die Suche über die Nachricht *onComplete*.

![Schnittstelle Suche, Klassen MinimaxAlgorithmus und MinimaxParalleleSuche](../images/Abb09_14_Schnittstellen_Zugsuche.png)

| Methode | Kurzbeschreibung |
| --- | --- |
| zugSuchen | Startet eine Suche nach einem Zug für die angegebene Stellung. Liefert nach und nach bessere Züge als Ereignisse an den übergebenen Observer. Das Ende der Suche (keinen besseren Zug mehr gefunden) wird ebenfalls an den Observer signalisiert. |
| sucheAbbrechen | Bricht die aktuelle Suche ab. |
| schliessen | Schließt die Suche vollständig. Anschließend dürfen keine Züge mehr damit ermittelt werden. |
| *Tabelle: Methoden der Schnittstelle Suche* | |

| Methode | Kurzbeschreibung |
| --- | --- |
| setSpielregeln | Setzt eine Implementierung der Spielregeln über Dependency Injection, [→ 5.3 Spielregeln (Blackbox)](05-03-Spielregeln.md) |
| setBewertung | Setzt die Bewertungsfunktion, anhand derer die Stellungen bei Erreichen der maximalen Suchtiefe bewertet werden. [→ 5.8 Stellungsbewertung (Blackbox)](05-08-Stellungsbewertung.md) |
| setTiefe | Setzt die maximale Suchtiefe in Halbzügen, d.h. bei 4 zieht jeder Spieler zweimal. |
| ermittleBestenZug | Ermittelt zur übergebenen Stellung den optimalen Zug gemäß Minimax und vorgegebener Stellungsbewertung bei fester Suchtiefe. Die Methode blockiert und ist deterministisch. |
| *Tabelle: Methoden der Klasse MinimaxAlgorithmus* | |

### Ablageort / Datei

Die Implementierung liegt unterhalb der Pakete *de.dokchess.engine.suche…*
