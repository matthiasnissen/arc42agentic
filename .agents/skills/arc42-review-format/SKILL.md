---
name: arc42-review-format
description: "Gemeinsame Ausgabeformate und Review-Modi für arc42-Review-Agenten. Definiert Befund-Templates für Sektions-Reviews und Konfliktanalysen, sowie Vollständig- und Delta-Modi. Use when: arc42 Review formatieren, Befund-Format, Konflikt-Format, Review-Modus, Sektions-Review, Konfliktanalyse."
---

# arc42 Review-Format

Dieses Skill definiert die gemeinsamen Formate und Modi für alle arc42-Review-Agenten. Es gibt zwei Agent-Typen mit jeweils eigenen Varianten: **Sektions-Review-Agenten** und **Konfliktanalyse-Agenten**.

## Review-Modi

### Sektions-Review Modi

Jeder Sektions-Agent unterstützt zwei Modi, abhängig vom Aufrufkontext:

**Vollständig-Modus (Standard)**
Wenn du OHNE spezifischen Änderungskontext aufgerufen wirst → prüfe alle Dateien der Sektion vollständig.

**Delta-Modus (Branch-Review)**
Wenn der Aufrufer **geänderte Dateien und/oder Diffs** mitliefert → prüfe NUR diese Änderungen:
- Lies nur die genannten geänderten Dateien vollständig
- Prüfe nur die Änderungen gegen die untenstehenden Kriterien
- Lies unveränderte Dateien der Sektion nur als Kontext, wenn zum Verständnis der Änderung nötig
- Kennzeichne jeden Befund klar als änderungsbezogen

### Konfliktanalyse Modi

Jeder Konflikt-Agent unterstützt zwei Modi:

**Vollständig-Modus (Standard)**
Wenn du OHNE spezifischen Änderungskontext aufgerufen wirst → prüfe alle Konfliktdimensionen vollständig.

**Delta-Modus (Branch-Review)**
Wenn der Aufrufer **geänderte Dateien und/oder Diffs** mitliefert:
- Lies trotzdem ALLE relevanten Dateien aus den beteiligten Sektionen (beide Seiten der Beziehung werden für Konfliktprüfung benötigt)
- Fokussiere die Analyse darauf, ob die **Änderungen neue Konflikte einführen** oder bestehende verschärfen
- Melde nur Konflikte, die durch die Änderungen verursacht oder beeinflusst wurden
- Kennzeichne jeden Befund als änderungsbezogen

## Ausgabeformate

### Sektions-Review: Befund-Format

Für jede Abweichung in einem Sektions-Review:

~~~markdown
### [Befund-ID] Titel

**Schwere:** 🔴 Kritisch / 🟡 Empfehlung / 🟢 Hinweis
**Datei:** [pfad/zur/datei.md](pfad/zur/datei.md#L12) (Zeilenanker der Fundstelle)
**Kriterium:** Welches arc42-Kriterium verletzt ist
**Zitat:** „wörtliche Textstelle aus der Datei“

**Befund:** Beschreibung des Problems

**Änderungsvorschlag:**
> Konkreter Text, der eingefügt oder geändert werden soll.
> Direkt übernehmbar formuliert.
~~~

### Konfliktanalyse: Befund-Format

Jeder Konflikt-Agent gibt zunächst seine **agenten-spezifische Übersichtsmatrix** aus (z.B. Zuordnungsmatrix, Schnittstellenvergleich, etc.), gefolgt von den einzelnen Konflikten in diesem Format:

~~~markdown
### [PREFIX-nn] Titel

**Konflikttyp:** K1/K2/K3/...
**Schwere:** 🔴 Kritisch / 🟡 Warnung / 🟢 Hinweis
**Betroffene Dateien:**
- `datei1.md` — betroffene Aussage
- `datei2.md` — widersprüchliche Aussage

**Beschreibung:** Worin genau der Konflikt besteht

**Lösungsvorschlag:** Konkreter Vorschlag zur Auflösung des Konflikts
~~~

Das PREFIX wird vom jeweiligen Konflikt-Agenten definiert (z.B. KQS, KKB, KRC, KSE, KSV, KKE, KRQ).

## Gemeinsame Regeln

- Schlage bei jedem Befund eine **KONKRETE, direkt übernehmbare Änderung** vor
- Berücksichtige, dass die Dokumentation auf **Deutsch** verfasst ist
- Befund-IDs müssen eindeutig und fortlaufend nummeriert sein

### Schweregrad kalibrieren

- 🔴 **Kritisch** nur, wenn zwei Textstellen der Dokumentation sich belegbar widersprechen oder eine Zusicherung nachweislich nicht erfüllt wird. Beides ist mit wörtlichen Zitaten zu belegen.
- 🟡 **Empfehlung/Warnung** für fehlende oder unscharfe Angaben, bei denen kein Widerspruch vorliegt (z. B. fehlende Messbedingungen, fehlende Begründung, „beispielsweise“-Formulierungen).
- 🟢 **Hinweis** für optionale Verbesserungen und Verdachtsfälle ohne Beleg.
- Eine Lücke im Graphen oder eine fehlende Kante ist kein Beleg für fehlende Dokumentation; prüfe im Zweifel die Quelle.
- Fordere neue ADRs, Risiken oder Szenarien nur, wenn die Dokumentation selbst eine Entscheidung, ein Risiko oder eine Zusage enthält, die dort fehlt. Ein Konzept darf Regeln samt Begründung enthalten.

### Belege und Vorschläge

- Jeder Befund nennt eine **Zitat-Zeile** mit wörtlich übernommenem Text und, wo möglich, einen Zeilenanker (`#L<n>`) der Fundstelle. Gekürzte Zitate werden mit `[…]` markiert; Paraphrasen stehen nicht in Anführungszeichen.
- Erfinde keine Zahlenwerte, Schwellen, Zuständigkeiten oder Termine. Fehlt eine Entscheidung, setze `TODO` oder kennzeichne den Wert ausdrücklich als Vorschlag zur Abstimmung.
- Mehrere Befunde mit derselben Ursache sind miteinander zu verknüpfen („Siehe auch …“) und werden im Zusammenfassungsblock als eine Ursache ausgewiesen.
- Fertige Berichte lassen sich mit `python3 <skill-ordner>/scripts/check_review.py <bericht.md> --doc <doku-pfad>` prüfen (Summen, Befund-IDs, Links, Zeilenanker, wörtliche Zitate).

## Verwandte Skills

- **`arc42-doc-layout`**: Struktur-Erkennung und Delegations-Protokoll für verschiedene Dokumentations-Layouts (Multi-Folder, Flat-Files, Single-File). Muss von Orchestratoren geladen werden, damit Section-Agenten korrekte Dateipfade oder Inline-Content erhalten.
