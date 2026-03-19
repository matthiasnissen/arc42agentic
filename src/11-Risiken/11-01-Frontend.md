# Anbindung Frontend

## 11.1 Risiko: Anbindung an das Frontend schlägt fehl

Es liegt keinerlei Wissen über die Anbindung einer Engine an ein vorhandenes Schach-Frontend vor.
Vorhandene Open Source Engines sind in C programmiert und werden als ausführbare Programme (unter Windows z.B. *.exe) geliefert.
Da wir DokChess in Java entwickeln, taugen sie nur bedingt zur Inspiration.
Über Kommunikationsprotokolle ist überhaupt nichts bekannt.

Falls es uns nicht gelingt, eine funktionierende Anbindung zu realisieren, können wir die Lösung nicht mit bestehenden Frontends verwenden.
Damit fehlt nicht nur ein wichtiges Feature ([vgl. Aufgabenstellung](../01-Einfuehrung-und-Ziele/01-01-Aufgabenstellung.md)), sondern die Lösung ist als Ganzes, insbesondere auch als Fallbeispiel, unglaubwürdig.

### Eventualfallplanung

Wir könnten ein einfaches textuelles User-Interface realisieren, um mit der Engine zu interagieren.
Aufwändiger wäre die Implementierung eines eigenen grafischen Frontends (siehe auch [Risiko 11.2](11-02-Aufwand.md)).

### Risikominderung

Durch einen Proof of concept erreichen wir hier frühestmöglich Sicherheit.
