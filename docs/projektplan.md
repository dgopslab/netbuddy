# Projektplan

## Projektidee

NetBuddy ist ein kleines Lern-Tool für Netzwerktechnik. Es entsteht während meiner Umschulung zum Fachinformatiker für Systemintegration und verbindet Python mit Themen aus dem ITT-Netzwerkunterricht.

Der erste Schwerpunkt liegt auf IPv4-Subnetting. Danach sollen ein Übungsmodus und ein einfacher Routing-Tabellen-Modus dazukommen.

## Problem

Viele Netzwerkaufgaben wirken am Anfang komplizierter, als sie eigentlich sind.

Typische Stolperstellen sind:

- CIDR-Schreibweise verstehen
- Subnetzmasken ableiten
- Netzwerkadresse und Broadcast unterscheiden
- nutzbare Host-Adressen erkennen
- Routing-Tabellen richtig lesen
- Longest Prefix Match anwenden

Dazu kommt: Viele Rechner im Internet liefern zwar Ergebnisse, erklären aber nicht wirklich den Weg dahin. Fürs Lernen reicht das nicht.

## Ziel

NetBuddy soll Aufgaben nicht nur berechnen, sondern die Lösung verständlich erklären.

Das Projekt soll am Ende für drei Dinge nützlich sein:

1. Ich kann selbst Subnetting und Routing besser üben.
2. Mitschüler können das Tool zum Lernen verwenden.
3. Das Projekt zeigt auf GitHub, wie ich Python auf ein echtes FISI-Thema anwende.

## Zielgruppe

Die Zielgruppe sind vor allem FISI-Umschüler und Anfänger in der Netzwerktechnik.

Das Tool soll bewusst nicht für erfahrene Netzwerkadmins optimiert sein. Es soll nicht möglichst viele Spezialfälle abdecken, sondern Grundlagen sauber erklären.

## Erste Version

Die erste Version soll ein einfaches Konsolenprogramm sein.

Geplante Funktionen:

- Menü anzeigen
- IPv4-Netz im CIDR-Format entgegennehmen
- Eingabe prüfen
- Netzwerkdaten berechnen
- Ergebnisse übersichtlich ausgeben
- kurze Erklärung zur Berechnung anzeigen

## Abgrenzung

NetBuddy ist am Anfang kein Netzwerk-Scanner.

Das Programm greift nicht aktiv ins Netzwerk ein und benötigt keine Admin-Rechte. Es berechnet und erklärt Netzwerkgrundlagen. Das ist bewusst so gewählt, weil ich aktuell auf einem Leihgerät ohne Admin-Rechte arbeite und das Projekt trotzdem sauber umsetzbar bleiben soll.

## Technische Umsetzung

Geplant ist Python als Konsolenprogramm.

Für die erste Umsetzung kann das eingebaute Modul `ipaddress` genutzt werden. Zusätzlich sollen wichtige Schritte selbst erklärt werden, damit das Programm nicht nur wie ein Taschenrechner wirkt.

## Erfolgskriterium

Das Projekt ist erfolgreich, wenn eine Person mit wenig Vorwissen ein Netz wie `192.168.5.0/27` eingeben kann und danach besser versteht, was Netzwerkadresse, Broadcast, Hostbereich und CIDR-Präfix bedeuten.
