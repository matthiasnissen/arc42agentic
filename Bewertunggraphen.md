# Bewertung der arc42-Wissensgraphen

Geprüft wurden die drei Graphen in `.arc42-graph_demo_results/` (`FullReviewRunGPT61Sol`, `FullReviewRunOpus55`, `FullReviewRunSonnet55`). Sie entstanden im Zuge der Full-Reviews im Graph-Modus mit dem überarbeiteten Skill [.agents/skills/arc42-knowledge-graph/SKILL.md](.agents/skills/arc42-knowledge-graph/SKILL.md) und dessen Skripten. Bewertet wurden Vorgabentreue, Korrektheit und Vollständigkeit gegenüber `arc-doc/`. Die Ordnernamen fließen nicht in die Bewertung ein.

Dies ist die zweite Generation. Die erste, vor der Einführung von `schema.json`, `build_graph.py` und `validate_graph.py` erzeugte Generation steht gekürzt am Ende (Abschnitt 6).

Vorgehen:
- Alle drei Graphen und Manifeste wurden mit `validate_graph.py` gegen `schema.json` und `arc-doc/` geprüft.
- Mit einem Scorecard (Soll-Zahlen je Entitätstyp und Relation aus `arc-doc/`, neun Widerspruchsfakten) wurden Umfang und Treue verglichen.
- Auffällige Bereiche wurden gegen die Quellen geprüft: Bausteinhierarchie, Evidence-Vergabe, Manifest, `contains`, `deployed_on`.

Einschränkungen: Die Soll-Zahlen und Widerspruchsfakten sind DokChess-spezifisch und nicht auf andere Dokumentationen übertragbar. Je Modell liegt nur ein Lauf vor.

## 1. Gemeinsame Basis

| Prüfpunkt | GPT61Sol | Opus55 | Sonnet55 |
|---|---|---|---|
| Schemafehler / Warnungen | 0 / 0 | 0 / 0 | 0 / 0 |
| Hinweise (Knoten ohne semantische Kante) | 55 | 12 | 13 |
| Manifest: Quelldateien / Kanten des Graphen im Manifest | 40 / 458 von 458 | 40 / 614 von 614 | 40 / 557 von 557 |
| `explicit`-Kanten mit Verweistext | 100 % | 100 % | 100 % |
| ID-Konvention eingehalten | ja | ja | ja |
| Zielname „Attraktive Spielstärke“ auf Qualitätsziel normalisiert | ja | ja | ja |
| `defines_term_for` ausschließlich `inferred` | ja | ja | ja |
| Risiko-Priorität „nicht angegeben“ (Doku bewertet nicht) | ja | ja | ja |
| ADR-Status als Enumerationswert `accepted` | ja | ja | ja |

Alle drei Graphen sind schemakonform und vollständig im Manifest. Die in der ersten Generation häufigen Verstöße (falsch `explicit` markierte Glossarkanten, Status mit Datum, unvollständiges Manifest, Signaturverstöße) sind bei allen verschwunden. Das ist im Wesentlichen die Wirkung von `schema.json` und der Prüfung durch `build_graph.py`.

## 2. Umfang

| Kennzahl | GPT61Sol | Opus55 | Sonnet55 |
|---|---:|---:|---:|
| Knoten / Kanten | 159 / 458 | 164 / 614 | 158 / 557 |
| Semantische Kanten (ohne `member_of`) | 95 | 232 | 200 |
| davon `explicit` / `inferred` / `structural` | 81 / 11 / 3 | 125 / 97 / 10 | 115 / 74 / 11 |
| Relationstypen verwendet (von 22) | 17 | 19 | 19 |
| Entitätstypen verwendet (von 19) | 17 | 17 | 18 |
| `StrategyApproach` | 24 | 28 | 23 |
| `Requirement` | 8 | 8 | 6 |
| `InternalInterface` | 6 | 6 | 5 |
| `BuildingBlock` | 7 | 8 | 8 |
| `Mitigation` | 0 | 0 | 2 |
| `addresses` (Tabelle 4.1 ergibt 18) | 18 | 25 | 27 |
| `contains` (Soll 7) | 3 | 7 | 7 |
| `constrains` | 4 | 21 | 16 |
| `affects` | 5 | 18 | 17 |
| `mitigates` | 0 | 7 | 3 |
| `defines_term_for` (24 Begriffe) | 8 | 28 | 24 |
| Ø Länge `description` | 229 | 224 | 228 |

## 3. Scorecard gegen `arc-doc/`

| | GPT61Sol | Opus55 | Sonnet55 |
|---|---:|---:|---:|
| Soll-Treffer (Knoten und Kanten, 25 Punkte) | 21 | 24 | 24 |
| Widerspruchsfakten | 9 von 9 | 9 von 9 | 9 von 9 |
| Abweichungen | `BuildingBlock` 7 statt 8, `concretizes` 12 statt 13, `contains` 3 statt 7, `based_on` 1 statt 2 | `based_on` 4 statt 2 | `InternalInterface` 5 statt mindestens 6 |

Alle drei Graphen enthalten die Widerspruchsfakten (FIDE-Umfang, 50-Züge-Regel, „keine Konsequenz“ in 11.2, Z02, 8.4 zu Stellung und Buchzug, F01, Effizienz-/Lesbarkeitsansätze, ADR „Stand 2011“). Die Fakten stehen bei GPT61Sol zum Teil in einem Knoten gebündelt, etwa die Validierung in `s08-concept-validation`.

## 4. Bewertung je Graph

### Opus55: breiteste Abdeckung

**Vorgabentreue: hoch.**
- Alle Pflichtattribute gesetzt, Evidence korrekt: Glossarkanten `inferred`, `constrains` überwiegend `inferred` und damit ehrlich gekennzeichnet.
- Beide Whitebox-Ebenen sind als `BuildingBlock` vorhanden, `contains` bildet die Hierarchie vollständig ab (7 von 7).
- Das Manifest enthält alle 614 Kanten.

**Korrektheit: hoch.** `addresses`: 18 explizite Kanten entsprechen Tabelle 4.1, 7 weitere sind als `inferred` markiert. `concretizes` (13) und `deployed_on` (4) stimmen mit dem Qualitätsbaum und dem Verteilungsdiagramm überein.

**Vollständigkeit: höchste der drei.** 8 Requirements je Feature, 6 interne Schnittstellen, 28 Strategieansätze, alle Widerspruchsfakten vorhanden. Es fehlen `Mitigation`-Knoten, die Maßnahmen stecken in den `mitigates`-Kanten. Schwächen: Mit 97 `inferred`-Kanten (42 %) ist der spekulative Anteil am höchsten. Dazu zählen 16 `inferred`-Kanten bei `constrains`, die für Konflikt-Agenten Prüfhinweise, aber keine Belege sind. `based_on` hat 4 statt 2 Kanten.

### Sonnet55: sauberste Evidence, kleinere Lücken

**Vorgabentreue: hoch.**
- 18 von 19 Entitätstypen, 19 von 22 Relationstypen. Als einziger Graph mit `Mitigation`-Knoten (2).
- Beide Whitebox-Ebenen vorhanden, `contains` vollständig (7 von 7).
- Manifest vollständig, Evidence-Anteil `inferred` mit 37 % niedriger als bei Opus55.

**Korrektheit: hoch.** `deployed_on` hat 7 Kanten, weil alle Bausteine auf das JAR zeigen. Davon sind 5 `explicit` und 2 `inferred` (Zugsuche, Stellungsbewertung als Teile der Engine). Das ist plausibel und ehrlich gekennzeichnet.

**Vollständigkeit: hoch, aber gröber.** Nur 6 Requirements (zusammengefasste Features), 5 interne Schnittstellen statt 6 (XBoard und Main fehlt) und nur 3 `realizes`-Kanten.

### GPT61Sol: sehr konservativ, hohe Präzision, geringe Dichte

**Vorgabentreue: mittel bis hoch.** Der Graph ist inzwischen schemakonform und kein Volltextarchiv mehr. Die Extraktion ist aber sehr zurückhaltend.
- Nur 95 semantische Kanten, davon fast alle `explicit` (81). Es gibt keine spekulativen Zuordnungen und nur 11 `inferred`-Kanten (12 %).
- Keine `mitigates`-Kanten und keine `Mitigation`-Knoten. Die Maßnahmen stehen nur als Text im Risiko.
- Das Whitebox-Element „DokChess Ebene 1“ fehlt. Dadurch hat `contains` nur 3 Kanten (nur Engine-Ebene), und die Hierarchie System → Bausteine ist nicht strukturell vorhanden.
- `based_on` nur 1 statt 2 (8.3 zu ADR 9.1 fehlt), `concretizes` 12 statt 13.
- Nur 8 von 24 Glossarbegriffen sind per `defines_term_for` verknüpft.

**Korrektheit: hoch.** Alle vorhandenen Kanten stimmen mit den Quellen überein. `addresses` entspricht exakt den 18 Zuordnungen aus Tabelle 4.1.

**Vollständigkeit: mittel.** Entitäten sind weitgehend vollständig (Soll-Typen bis auf einen Baustein erreicht), die Querbeziehungen aber dünn. Konflikt-Agenten müssen mehr aus dem Text nachschlagen. Der Review-Bericht räumt das selbst ein und wertet fehlende Kanten nicht als Beleg fehlender Dokumentation.

## 5. Ranking

| Rang | Graph | Vorgaben | Korrektheit | Vollständigkeit | Kurzbegründung |
|---|---|---|---|---|---|
| 1 | **Opus55** | hoch | hoch | hoch | Höchste Abdeckung, vollständige Hierarchie, 24 von 25 Soll-Punkten, alle Widerspruchsfakten. Abzug: hoher `inferred`-Anteil (42 %). |
| 2 | **Sonnet55** | hoch | hoch | mittel bis hoch | Ebenfalls 24 von 25, sauberste Evidence, als einziger mit `Mitigation`. Abzug: gröbere Requirements, eine Schnittstelle fehlt, weniger `realizes`. |
| 3 | **GPT61Sol** | mittel bis hoch | hoch | mittel | Präzise und rein explizit, aber dünn: Whitebox Ebene 1 fehlt, `contains`, `mitigates`, `constrains` kaum vertreten, 21 von 25 Soll-Punkten. |

Der Abstand zwischen Platz 1 und 2 ist klein. Die Abdeckung von Opus55 geht auf Kosten eines höheren spekulativen Anteils. Wer rein belegte Kanten bevorzugt, kommt eher zu Sonnet55 oder zu GPT61Sol. Für Review-Agenten ist die Dichte wichtiger, solange `inferred` als Vorbehalt gekennzeichnet bleibt.

Auffällig: GPT61Sol hat den dünnsten Graphen, in der Review-Bewertung dennoch die am besten kalibrierten Befunde (siehe [BewertungReviewResults.md](BewertungReviewResults.md)). Die Graphqualität bestimmt das Review-Ergebnis also nicht allein.

## 6. Vergleich mit der ersten Generation

| | Erste Generation | Zweite Generation |
|---|---|---|
| Opus | 646 Kanten, 38 `defines_term_for` falsch `explicit`, 3 Signaturverstöße, Manifest ohne `member_of`, Ebene `0` | 614 Kanten, alle Verstöße behoben, Manifest vollständig, Hierarchie vollständig |
| Sonnet | 570 Kanten, Whitebox-Knoten fehlten, Status mit Datum, keine Delta-Keys | 557 Kanten, Whitebox-Knoten vorhanden, Status `accepted`, 24 von 25 Soll-Punkten |
| GPT | Volltextarchiv: nur `references` und `member_of`, 40 `Document`-Knoten außerhalb des Vokabulars, 4 Strategieansätze | Typisierte Kanten (17 Relationstypen), keine `Document`-Knoten, 24 Strategieansätze; weiterhin dünn bei Querbeziehungen |

Ranking der ersten Generation: Opus, Sonnet, GPT. Das Ranking der zweiten Generation ändert nur die Abstände: GPT hat am meisten aufgeholt, Opus und Sonnet sind auf gleichem Niveau.

## 7. Empfohlene Nachbesserungen

- **Opus55:** Spekulative `constrains`- und `affects`-Kanten prüfen und, wo schwach begründet, entfernen. `based_on` auf die zwei belegten Kanten zurückführen. `Mitigation`-Knoten ergänzen.
- **Sonnet55:** Requirements je Feature aufspalten, die Schnittstelle „XBoard und Main“ ergänzen, `realizes` für ADR 9.1 zu Standard-Ein-/Ausgabe nachtragen.
- **GPT61Sol:** Whitebox „DokChess Ebene 1“ und `contains` zu den Blackboxen ergänzen, `mitigates` und `Mitigation` aus den Risikotexten ableiten, `based_on` 8.3 → ADR 9.1 und die fehlende `concretizes`-Kante nachziehen.
- **Skill und Validator:** Ein Info-Hinweis bei auffällig dünnen Graphen (wenig `contains`, wenig `inferred`, `mitigates` fehlt komplett bei vorhandenen Risiken) würde GPT61Sol-artige Lücken früh sichtbar machen.
