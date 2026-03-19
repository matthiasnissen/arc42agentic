# Aufbau

## 4.2 Der Aufbau von DokChess

DokChess ist als Java-Programm mit main-Routine realisiert. Es zerfällt grob in folgende Teile:

- eine Implementierung der Schachregeln
- die eigentliche Engine, welche die Züge ermittelt
- die Anbindung an eine grafische Benutzeroberfläche über das XBoard-Protokoll
- einen Adapter für ein konkretes Eröffnungsbibliotheksformat (Polyglot Opening Book)

Diese Zerlegung ermöglicht es, Dinge wie das Kommunikationsprotokoll oder das Eröffnungsbibliotheksformat bei Bedarf auszutauschen. Alle Teile sind durch Schnittstellen abstrahiert, die Implementierungen werden per Dependency Injection zusammengesteckt ([→ 5. Bausteinsicht](../05-Bausteinsicht/05-01-Ebene-1.md), [→ Konzept 8.1 „Abhängigkeiten zwischen Modulen"](../08-Konzepte/08-01-Abhaengigkeiten.md).
Die Zerlegung erlaubt es weiterhin die Software, allen voran die Schachalgorithmen, leicht automatisiert zu testen ([→ Konzept 8.7 „Testbarkeit“](../08-Konzepte/08-07-Testbarkeit.md)).

Die Interaktion zwischen Algorithmen­Teilen erfolgt über den Austausch fachlich motivierter Datenstrukturen, realisiert als Klassen (*Figur*, *Zug*, … [→ Konzept 8.2 „Schach­Domänenmodell“](../08-Konzepte/08-02-Domaenenmodell.md)).
Hier wurde bewusst eine bessere Verständlichkeit angestrebt, auf Kosten von Effizienz.
Gleichwohl erreicht DokChess eine akzeptable Spielstärke, wie ein Durchspielen der entsprechenden Szenarien zeigt ([→ 10. Qualitätsszenarien](../10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md)).

Zentrales Element beim Entwurf der Datenstrukturen ist die Spielsituation: Welche Figuren gerade wo stehen und was sonst noch zur Stellung dazu gehört (z. B. wer am Zug ist).
Auch hier ging bei der Implementierung der fachlich motivierten Klasse dazu Lesbarkeit vor Effizienz.
Ein wichtiger Aspekt dabei: Wie alle anderen fachlichen Klassen ist auch sie unveränderlich ([→ Entscheidung 9.2 „Sind Stellungsobjekte veränderlich oder nicht?“](../09-Entscheidungen/09-02-Stellungsobjekte.md)).
