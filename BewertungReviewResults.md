# Bewertung der sechs arc42-Reviews zu `arc-doc/`

Bewertet wurden die sechs Vollreviews im Workspace-Root: je drei im Graph-Modus (`FullReviewResultGraph*.md`) und im Datei-Modus (`FullReviewResultFiles*.md`) von Opus 5.5, GPT 6.1 Sol und Sonnet 5.5. Das Ranking beruht ausschließlich auf dem Inhalt, nicht auf den Dateinamen. Kriterien sind Korrektheit, Vollständigkeit und Exaktheit. Die Nachvollziehbarkeit fließt in die Exaktheit ein. Zusätzlich wird geprüft, ob der Graph-Modus gegenüber dem Datei-Modus einen Vorteil bietet. Die zugehörigen Graphen stehen in [Bewertunggraphen.md](Bewertunggraphen.md).

**Vorgehen.** Die Kernaussagen wurden gegen die Quelldateien in `arc-doc/` geprüft. Zusätzlich liefen Skriptprüfungen (`check_review.py` im Skill `arc42-review-format`):
- Befund-IDs eindeutig, Schweregrade und Summen konsistent mit der Zusammenfassung,
- lokale Links vorhanden, `#L`-Zeilenanker innerhalb der Dateilänge,
- Zitate in Anführungszeichen wörtlich in `arc-doc/` auffindbar.

Reproduzierbar mit `python3 .agents/skills/arc42-review-format/scripts/check_review.py FullReviewResult*.md --doc arc-doc --gold dokchess`. Die Zuordnung der Hauptbefunde (`--gold`) ist eine Stichwortsuche und wurde von Hand gegengeprüft.

**Einschränkungen.**
- Je Modell und Modus liegt ein Lauf vor.
- Die Referenzbefunde sind DokChess-spezifisch und stammen aus meiner eigenen Lektüre von `arc-doc/`, nicht aus einer unabhängigen Quelle.
- Die Läufe unterscheiden sich nicht nur im Modus, sondern auch im Zeitpunkt, in den Agentenfassungen und durch die Streuung der Modelle.
- Aufwand und Laufzeit wurden nicht gemessen.

## Referenzbasis: Was in `arc-doc/` tatsächlich stimmt

**Echte Hauptbefunde**

- **A, FIDE-Regeln:** [01-01](arc-doc/01-Einfuehrung-und-Ziele/01-01-Aufgabenstellung.md) verspricht „Vollständige Implementierung der FIDE-Schachregeln“. [05-03](arc-doc/05-Bausteinsicht/05-03-Spielregeln.md) nennt 50-Züge-Regel und Stellungswiederholung als nicht implementiert. [11-02](arc-doc/11-Risiken/11-02-Aufwand.md) behauptet dazu „keine [Konsequenzen] bezüglich der Korrektheit“.
- **B, Z02 gegen 8.4:** [10-02](arc-doc/10-Qualitaetsanforderungen/10-02-Qualitaetsszenarien.md) Z02 verlangt, dass die Engine eine unzulässige Stellung erkennt und das Spiel beendet. [08-04](arc-doc/08-Konzepte/08-04-Validierung.md) sagt, die Zulässigkeit der Position werde nicht geprüft. Fehler können erst später im Spielverlauf auftreten.
- **C, Buchzüge gegen F01:** [08-04](arc-doc/08-Konzepte/08-04-Validierung.md) sagt, die Bibliothek werde inhaltlich nicht geprüft, und „im Extremfall antwortet die Engine mit einem ungültigen Zug“. F01 sichert unbedingt einen regelkonformen Zug zu.

**Weitere belegte Einzelbefunde**

- **Alpha-Beta fehlt in 5.7:** [04-01](arc-doc/04-Loesungsstrategie/04-01-Einstieg.md) und [04-03](arc-doc/04-Loesungsstrategie/04-03-Spielstrategie.md) nennen Alpha-Beta. [05-07](arc-doc/05-Bausteinsicht/05-07-Zugsuche.md) kennt nur `MinimaxAlgorithmus` und `MinimaxParalleleSuche`.
- **E01/E02 überlappen:** E01 fordert fünf Sekunden für jeden Zug, E02 zehn Sekunden für den ersten Zug. Die Abgrenzung fehlt.
- **E02 „denkt“-Rückmeldung:** Sie ist nirgends als Verhalten beschrieben.
- **W05 gegen ADR 9.2:** Der Austausch der Brettrepräsentation in einer Woche passt nicht zu „Eine spätere Änderung würde das Gesamtsystem betreffen“.
- **Materialbewertung gegen F04:** [04-03](arc-doc/04-Loesungsstrategie/04-03-Spielstrategie.md) beschreibt nur Materialbewertung und behauptet trotzdem, die einfachen Implementierungen erfüllten die Szenarien. F04 verlangt ein Matt in zwei.
- **Weitere Befunde:** Remisangebote in S3 gegen S5.2, Zielname „Attraktive Spielstärke“, fehlendes `setSuche` in [05-04](arc-doc/05-Bausteinsicht/05-04-Engine.md), eine geschützte Methode im Blackbox-Diagramm von 5.7, Linktexte der ADR-Verweise, mehrere Tippfehler, „Fisher“ gegen „Fischer“ in [00-00](arc-doc/00-Ueberblick/00-00-Overview.md), Bibliotheksabfrage in S6 gegen S7.

**Nachweislich falsche Aussagen in den Reviews**

- **Englischer Fließtext in ADR 09-01:** Der Text ist deutsch, nur ohne Umlaute geschrieben. Englisch sind lediglich die Überschriften. Behauptet in [FullReviewResultFilesOpus55.md](FullReviewResultFilesOpus55.md).
- **Eröffnungsbibliothek hängt an der Zugsuche:** Im Diagramm 5.6 hängt sie am Engine-Port, nicht an der Zugsuche. Ebenfalls in [FullReviewResultFilesOpus55.md](FullReviewResultFilesOpus55.md).

Die übrigen fünf Reviews enthalten keine nachweislich falsche Aussage.

## Abdeckung der Hauptbefunde

| Review | A FIDE | B Z02 gegen 8.4 | C Buchzug gegen F01 | Schweregrad-Kalibrierung |
|---|---|---|---|---|
| [FullReviewResultGraphOpus55.md](FullReviewResultGraphOpus55.md) | kritisch (S11-02, mit 1.1 verknüpft) | kritisch (KRQ-01) | kritisch als fehlendes Risiko, mit Bezug zu F01 (S11-01, KRQ-01) | 3 von 6 kritischen Befunden überhöht (S03-01, S10-01, S10-02) |
| [FullReviewResultGraphGPT61Sol.md](FullReviewResultGraphGPT61Sol.md) | kritisch (S01-01) | kritisch (KRQ-01) | kritisch als Widerspruch zu F01 (KRQ-04) | sehr gut: genau A, B und C sind kritisch, Abstufungen sind begründet |
| [FullReviewResultGraphSonnet55.md](FullReviewResultGraphSonnet55.md) | nur Warnung („Spannung“, S11-03) | kritisch (S8-01) | kritisch als fehlendes Risiko (S11-01, KRQ-01) | B und C dreifach als kritisch gezählt, Spielstärke (S10-01) überhöht |
| [FullReviewResultFilesOpus55.md](FullReviewResultFilesOpus55.md) | kritisch (KRQ-03) | nur Warnung, als Risikolücke (KRQ-05) | nur Warnung | Spielstärke (S10-01) überhöht |
| [FullReviewResultFilesGPT61Sol.md](FullReviewResultFilesGPT61Sol.md) | kritisch (KRQ-01) | fehlt | fehlt | gut |
| [FullReviewResultFilesSonnet55.md](FullReviewResultFilesSonnet55.md) | nur Warnung | kritisch, aber nur als Risikolücke (S11-01) | kritisch, aber nur als Risikolücke (S11-01) | Spielstärke (S10-01) überhöht, A nur Warnung bei kritischer Risikolücke |

## Nebenbefunde

| Nebenbefund | Opus Graph | Opus Datei | GPT Graph | GPT Datei | Sonnet Graph | Sonnet Datei |
|---|---|---|---|---|---|---|
| Alpha-Beta fehlt in 5.7 | ja | nein | nein | nein | nein | nein |
| E01/E02 überlappen | ja | nein | nein | ja | ja | ja |
| E02 „denkt“-Rückmeldung nicht beschrieben | nein | nein | nein | ja | teilweise | ja |
| W05 gegen ADR 9.2 | ja | nein | teilweise | nein | ja | nein |
| Zielname „Attraktive Spielstärke“ | ja | ja | ja | ja | ja | ja |
| Remisangebote (S3 gegen S5.2) | ja | ja | ja | ja | ja | ja |
| Tippfehler, „Fisher“, ADR-Linktitel | ja | nein | nein | nein | nein | nein |
| Materialbewertung gegen F04 | nein | nein | nein | ja | nein | ja |
| Geschützte Methode in 5.7 | nein | nein | nein | nein | nein | ja |
| Treffer von 9 | 6 | 2 | 2 | 5 | 4 | 6 |

Nicht gefunden hat keiner: `setSuche` fehlt in 5.4.

## Kennzahlen und Exaktheit

| Kennzahl | Opus Graph | Opus Datei | GPT Graph | GPT Datei | Sonnet Graph | Sonnet Datei |
|---|---:|---:|---:|---:|---:|---:|
| Befunde | 86 | 75 | 50 | 48 | 58 | 78 |
| kritisch / Warnung / Hinweis | 6 / 72 / 8 | 2 / 63 / 10 | 3 / 39 / 8 | 1 / 42 / 5 | 4 / 50 / 4 | 2 / 66 / 10 |
| Wörter | 10 821 | 7 158 | 6 837 | 6 826 | 4 653 | 13 772 |
| Links, davon fehlend | 134, 0 | 153, 0 | 111, 0 | 122, 0 | 89, 0 | 147, 0 |
| `#L`-Zeilenanker, davon hinter Dateiende | 125, 2 | 50, 0 | 0 | 80, 0 | 0 | 104, 0 |
| Zitate in Anführungszeichen | 180 | 45 | 24 | 17 | 37 | 87 |
| davon ohne wörtliche Entsprechung* | 11 (6 %) | 17 (38 %) | 7 (29 %) | 5 (29 %) | 3 (8 %) | 15 (17 %) |
| Befunde ohne Vorschlag | 0 | 0 | 0 | 0 | 11 | 0 |
| Summen stimmen | ja | ja | ja | ja | ja | ja |

\* Stichproben zeigten typografische Unterschiede, gekürzte Zitate und Paraphrasen in Anführungszeichen. Ein Beispiel ist „jedes XBoard-Frontend“, wo das Original „jedes grafische Frontend, welches das … XBoard-Protokoll unterstützt“ lautet. Die Quote ist daher eine Obergrenze für ungenaue Zitate, taugt aber zum Vergleich.

Opus Graph nennt in Vorschlägen Zahlenwerte, etwa 80 % Gewinnquote oder zwei Personentage, ohne sie als Annahme zu kennzeichnen. GPT Graph setzt in 37 Fällen `TODO`. Sonnet Graph benennt Werte ausdrücklich als Vorschlag zur Abstimmung.

## Ranking

1. **[FullReviewResultGraphOpus55.md](FullReviewResultGraphOpus55.md)**
   - Korrektheit: Keine falsche Aussage, aber drei der sechs kritischen Befunde sind überhöht, und sechs neue ADRs werden gefordert.
   - Vollständigkeit: Die höchste. A, B und C sind abgedeckt, dazu Alpha-Beta in 5.7, W05 gegen ADR 9.2, E01/E02, Tippfehler, „Fisher“ und die Bibliotheksabfrage S6 gegen S7.
   - Exaktheit: Die beste. Zitat-Zeile und Zeilenanker je Befund, 125 Anker mit zwei Abweichungen um eine Zeile, nur 6 % ungenaue Zitate.
   - Schwächen: 86 Befunde mit 72 Warnungen (Rauschen), nicht gekennzeichnete Beispielwerte.
2. **[FullReviewResultGraphGPT61Sol.md](FullReviewResultGraphGPT61Sol.md)**
   - Korrektheit: Die beste. Genau A, B und C sind kritisch. Der Review begründet, warum er fünf Hinweise der Spezialagenten abgestuft hat, und sagt offen, dass fehlende Graphkanten kein Beleg sind.
   - Vollständigkeit: A, B und C vollständig, bei den Nebenbefunden aber nur 2 von 9.
   - Exaktheit: Keine erfundenen Werte (`TODO`), die Verifikation an den Originalen ist benannt. Dafür keine Zeilenanker und 29 % ungenaue Zitate.
3. **[FullReviewResultGraphSonnet55.md](FullReviewResultGraphSonnet55.md)**
   - Deckt B und C ab, A nur als Warnung („Spannung“). Die Aussage in 11.2 („keine Konsequenzen bezüglich der Korrektheit“) wird nicht infrage gestellt.
   - B und C werden als drei kritische Befunde mit derselben Ursache gezählt, die Spielstärke ist überhöht.
   - Zusatzbeobachtungen wie E01/E02 und Bitboard im Glossar sind belegt. Knappe Vorschläge, elf Befunde ohne Vorschlag, keine Zeilenanker.
4. **[FullReviewResultFilesGPT61Sol.md](FullReviewResultFilesGPT61Sol.md)**
   - Sehr sorgfältig und frei von falschen Aussagen, mit einer eigenen guten Beobachtung (Materialbewertung gegen F04) und 80 Zeilenankern.
   - Übersieht aber B und C, die offensichtlichsten Widersprüche.
5. **[FullReviewResultFilesSonnet55.md](FullReviewResultFilesSonnet55.md)**
   - Tief und korrekt in den Details, etwa Ereignisvertrag bei Abbruch und geschützte Methode im Diagramm, mit 104 Zeilenankern.
   - Erfasst B und C nur als Risikolücke in S11 und bewertet den FIDE-Widerspruch nur als Warnung. Überbewertet die Spielstärke-Messbarkeit.
6. **[FullReviewResultFilesOpus55.md](FullReviewResultFilesOpus55.md)**
   - Zwei nachweislich falsche Befunde (englischer Fließtext in 09-01, Eröffnungsbibliothek an der Zugsuche).
   - Behauptet Diagrammprüfung bei den Sektionen, schreibt bei den Konflikten aber, die Diagramme seien nicht ausgewertet. 38 % der Zitate ohne wörtliche Entsprechung. B ist nur eine Warnung, C nur eine Warnung zur fehlenden Prüfung.

Die Plätze 1 und 2 liegen eng beieinander. Wer die Kalibrierung höher gewichtet als die Tiefe, setzt GPT Graph vorn.

## Bietet der Graph-Modus einen Vorteil?

**Kurz:** Ja, bei sektionsübergreifenden Widersprüchen. Bei lokalen Details und bei Zeilenbelegen gibt es keinen Vorteil, teils einen Nachteil. Ein Kostenvorteil ist nicht untersucht.

| Merkmal | Graph-Modus | Datei-Modus | Bewertung |
|---|---|---|---|
| Hauptbefunde A, B, C mindestens als Warnung (3 Modelle × 3) | 9 von 9 | 7 von 9 | Vorteil Graph |
| Hauptbefunde als **kritisch** | 8 von 9 | 4 von 9 | Vorteil Graph |
| davon B als Widerspruch kritisch | 3 von 3 | 0 von 3 | Deutlicher Vorteil Graph |
| davon C kritisch (als Widerspruch oder als fehlendes Risiko) | 3 von 3 | 1 von 3 | Vorteil Graph |
| A (FIDE) kritisch | 2 von 3 | 2 von 3 | gleich |
| Nachweislich falsche Aussagen | 0 | 2 (ein Review) | leichter Vorteil Graph |
| Zitate ohne wörtliche Entsprechung | Opus 6 %, GPT 29 %, Sonnet 8 % | Opus 38 %, GPT 29 %, Sonnet 17 % | Vorteil Graph bei Opus und Sonnet, GPT gleich |
| Nebenbefunde von 9 | 6 / 2 / 4 | 2 / 5 / 6 | modellabhängig, im Mittel gleich (12 gegen 13) |
| Zeilenanker `#L` | Opus 125, GPT 0, Sonnet 0 | Opus 50, GPT 80, Sonnet 104 | Nachteil Graph bei GPT und Sonnet |
| Anteil begründeter kritischer Befunde | 9 von 13 (69 %) | 3 von 5 (60 %) | kein klarer Unterschied |

(Reihenfolge der Modelle in den Zeilen: Opus, GPT, Sonnet.)

**Wo der Vorteil liegt.** B und C sind keine Widersprüche zwischen zwei benachbarten Absätzen. Es steht in 8.4, dass Zulässigkeit und Buchinhalt nicht geprüft werden, und in 10.2 stehen Zusagen (Z02, F01), die genau das voraussetzen. Im Datei-Modus sahen die Agenten die Stellen, stuften sie aber als fehlendes Risiko in S11 oder als Warnung ein oder übersahen den Zusammenhang. Im Graph-Modus enthalten alle drei Graphen den Wortlaut aus 8.4 („nicht aber, ob die Position zulässig ist“, „im Extremfall … ungültigen Zug“) als Beschreibung des Validierungskonzepts, neben den Szenarien Z02 und F01 in der Konfliktdimension `c-rq`. Alle drei Reviews leiten daraus für B einen kritischen Widerspruch ab. Für C stufen GPT einen Widerspruch zu F01 und Opus sowie Sonnet ein kritisches fehlendes Risiko ein. Die plausibelste Erklärung ist also, dass die Extraktion die Einschränkungen im Wortlaut erhält und die Konfliktdimension die zusammengehörigen Entitäten bündelt. Das ist der beabsichtigte Nutzen des Graphen.

**Wo kein Vorteil sichtbar ist.**
- A ist ein Widerspruch zwischen wenigen, gut sichtbaren Stellen. Er wird in beiden Modi gleich häufig gefunden (je 2 von 3 kritisch).
- Lokale Beobachtungen aus einzelnen Texten oder Diagrammen (Materialbewertung gegen F04, geschützte Methode in 5.7, „denkt“-Rückmeldung) fand der Datei-Modus bei GPT und Sonnet öfter. Der Graph fasst Inhalte zusammen, was Details kosten kann. Bei Opus ist es umgekehrt: Der Graph-Review fand sechs statt zwei Nebenbefunde.
- Die Graphdichte bestimmt das Ergebnis nicht allein: Der GPT-Graph ist der dünnste (siehe [Bewertunggraphen.md](Bewertunggraphen.md)), liefert aber die am besten kalibrierten Befunde und findet B und C.

**Nachteile des Graph-Modus.**
- GPT und Sonnet nennen im Graph-Review keine Zeilenanker mehr (80 und 104 im Datei-Review). Die Provenienz im Graphen besteht aus Überschriftenankern. Wer Zeilenbelege will, muss sie verlangen. Opus liefert sie auch im Graph-Modus.
- Der Aufbau erfordert einen zusätzlichen Schritt mit einer Extraktionsdatei von 100 bis 139 KB und Python. Ob sich der Aufwand lohnt, ist offen. Die Läufe messen weder Kosten noch Dauer, und der erwartete Vorteil bei Wiederverwendung des Graphen (wiederholte Reviews, Branch-Review) wurde nicht untersucht.

**Belastbarkeit.** Das Muster bei B und C ist bei drei verschiedenen Modellen gleich, das spricht gegen einen Zufall einzelner Läufe. Mit einem Lauf je Modell und Modus, unterschiedlichen Agentenfassungen und Referenzbefunden aus derselben Quelle ist es aber kein Beleg. Verallgemeinerbar wäre es erst durch Wiederholungsläufe und eine zweite Dokumentation.

**Empfehlung.** Den Graph-Modus für die sektionsübergreifende Konfliktanalyse nutzen, die Sektions-Agenten aber weiterhin bei Bedarf in der Quelle nachlesen lassen. Zeilenanker und Zitat-Zeile je Befund im Review-Format verlangen (siehe `arc42-review-format`), und `check_review.py` als Gegenprobe einsetzen.

## Gesamtbild

Die drei Graph-Reviews liegen vorn, weil sie die kritischen Widersprüche B und C zuverlässiger erfassen und keine nachweislich falsche Aussage enthalten. Der Abstand beruht auf Trefferquote, Kalibrierung und Belegqualität, nicht auf dem Modus allein: Zwischen den Graph-Reviews entscheiden Kalibrierung (GPT) und Tiefe samt Zeilenbelegen (Opus). Offene Schwächen sind überhöhte Schweregrade bei Opus und Sonnet, die zahlreichen Warnungen bei Opus Graph und die fehlenden Zeilenbelege bei GPT Graph und Sonnet Graph.
