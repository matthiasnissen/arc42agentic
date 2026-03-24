# Stellungsbewertung

## 5.8 Stellungsbewertung (Blackbox)

### Zweck/Verantwortlichkeit

Das Modul bewertet eine Stellung aus Sicht eines Spielers.
Ergebnis ist eine Zahl, wobei 0 eine ausgeglichene Situation beschreibt, eine positive Zahl einen Vorteil für den Spieler, eine negative einen Nachteil.
Je höher der Betrag, desto größer der Vor- bzw. Nachteil.
Das Modul ermöglicht es so, Stellungen miteinander zu vergleichen.

### Schnittstellen

Das Modul stellt seine Funktionalität über die Schnittstelle *de.dokchess.engine.bewertung.Bewertung* bereit, *de.dokchess.engine.bewertung.ReineMaterialBewertung* ist eine sehr einfache Implementierung.
Die Schnittstelle enthält Konstanten für typische Bewertungen.

![Schnittstelle Bewertung, Klasse ReineMaterialBewertung](../images/Abb09_15_SchnittstellenBewertung.png)

| Methode | Kurzbeschreibung |
| --- | --- |
| bewerteStellung | Liefert zur gegebenen Stellung eine Bewertung aus Sicht der angegebenen Spielerfarbe. Je höher, desto besser. |
| *Tabelle: Methoden der Schnittstelle Bewertung* | |

### ReineMaterialBewertung

Die Implementierung berücksichtigt ausschließlich die vorhandenen Figuren (Material).
Jede Figurenart enthält einen Wert (Bauer 1, Springer 3, …, Dame 9), die Figuren auf dem Brett werden entsprechend aufsummiert. Eigene Figuren zählen positiv, gegnerische negativ.
Entsprechend ist bei ausgeglichenem Material das Ergebnis 0, verliert man z.B. eine Dame, sinkt der Wert um 9.

### Ablageort / Datei

Die Implementierung liegt unterhalb der Pakete *de.dokchess.engine.bewertung…*

### Offene Punkte

Bei der reinen Materialbewertung spielt es keine Rolle, wo die Figur steht.
Ein Bauer in Startposition ist genau so viel wert, wie einer kurz vor der Umwandlung.
Und ein Springer am Rand entspricht einem Springer im Zentrum.
Hier ist viel Spielraum für Verbesserungen, der bewusst nicht ausgeschöpft wurde, da DokChess ja zum Experimentieren einladen soll.
