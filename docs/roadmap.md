# Roadmap

## Version 0.1 – Grundgerüst

- [x] Repository anlegen
- [x] README schreiben
- [x] Projektstruktur erstellen
- [x] `main.py` anlegen
- [x] einfaches Konsolenmenü bauen
- [x] Auswahl des Nutzers sinnvoll auswerten

Geplantes Menü:

```text
NetBuddy

1 - IPv4-Subnetz berechnen
2 - Übungsmodus
3 - Routing-Tabelle prüfen
4 - Beenden
```

## Version 0.2 – IPv4-Subnetzrechner
- [ ] IPv4-Netz im CIDR-Format einlesen
- [ ] Eingabe prüfen
- [ ] Netzwerkadresse ausgeben
- [ ] Subnetzmaske ausgeben
- [ ] Broadcast-Adresse ausgeben
- [ ] erste nutzbare Host-Adresse ausgeben
- [ ] letzte nutzbare Host-Adresse ausgeben
- [ ] Anzahl nutzbarer Hosts ausgeben

Beispiel:
```text
Eingabe: 192.168.5.0/27

Netzwerkadresse: 192.168.5.0
Subnetzmaske: 255.255.255.224
Broadcast-Adresse: 192.168.5.31
Erste nutzbare IP: 192.168.5.1
Letzte nutzbare IP: 192.168.5.30
Nutzbare Hosts: 30
```

## Version 0.3 – Erklärmodus
- [ ] Hostbits berechnen
- [ ] Gesamtanzahl der Adressen erklären
- [ ] nutzbare Hosts erklären
- [ ] Sonderfälle wie /31 und /32 später sauber behandeln

Beispiel:
```text
/27 bedeutet:
27 Bits sind Netzanteil.
5 Bits bleiben für Hosts.
2^5 = 32 Adressen insgesamt.
32 - 2 = 30 nutzbare Host-Adressen.
```

## Version 0.4 – Übungsmodus
- [ ] einfache Subnetting-Aufgaben anzeigen
- [ ] Lösung erst auf Wunsch anzeigen
- [ ] mehrere Schwierigkeitsstufen vorbereiten


Mögliche Aufgabentypen:
```text
- Broadcast-Adresse berechnen
- erste nutzbare IP finden
- letzte nutzbare IP finden
- nutzbare Hosts berechnen
- passende Subnetzmaske bestimmen
```

## Version 0.5 – Routing-Tabellen-Modus
- [ ] Ziel-IP eingeben
- [ ] mehrere Routen hinterlegen
- [ ] prüfen, in welchen Netzen die Ziel-IP liegt
- [ ] spezifischste Route bestimmen
- [ ] Longest Prefix Match erklären

Beispiel:
```text
Ziel-IP: 192.168.5.25

Routen:
192.168.5.0/24
192.168.5.0/27
0.0.0.0/0

Beste Route:
192.168.5.0/27

Grund:
Die Ziel-IP passt zu mehreren Routen.
Die Route mit dem längsten Präfix ist am spezifischsten.
Deshalb gewinnt /27.
```
## Version 0.6 – IPv6-Grundlagen
- [ ] IPv6-Adressen erkennen
- [ ] Präfix anzeigen
- [ ] einfache Unterschiede zu IPv4 erklären
- [ ] Hinweis: kein Broadcast bei IPv6
- [ ] typische Präfixe grob erklären
## Später vielleicht
- [ ] Aufgaben aus Datei laden
- [ ] eigene Aufgaben speichern
- [ ] Ergebnis als Textdatei exportieren
- [ ] kleine Tests mit pytest
- [ ] einfache SQLite-Datenbank für Übungsfortschritt
