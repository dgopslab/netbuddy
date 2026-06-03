# NetBuddy

NetBuddy ist ein kleines Python-Projekt aus meiner Umschulung zum Fachinformatiker für Systemintegration.

Das Ziel ist simpel: Netzwerkthemen verständlicher machen. Gerade IPv4, Subnetting, Routing-Tabellen und später auch IPv6 sind Themen, bei denen viele am Anfang hängen bleiben. NetBuddy soll nicht nur Ergebnisse ausspucken, sondern Schritt für Schritt zeigen, warum diese Ergebnisse entstehen.

## Warum ich das Projekt baue

In der Umschulung behandeln wir aktuell IPv4, IPv6, Subnetting und Routing-Tabellen. Mir ist aufgefallen, dass viele Aufgaben nicht schwer sind, weil die Rechnung unmöglich ist, sondern weil der Ablauf unklar bleibt.

NetBuddy soll genau da helfen:

* Was bedeutet `/24`, `/27` oder `/30`?
* Wie komme ich von der CIDR-Schreibweise zur Subnetzmaske?
* Wo liegen Netzwerkadresse und Broadcast?
* Welche IPs sind nutzbar?
* Warum gewinnt bei Routing-Tabellen die spezifischere Route?
* Wie kann man solche Aufgaben üben, ohne jedes Mal komplett neu anzufangen?

## Geplante Funktionen

### IPv4-Subnetting

* Netzwerk im CIDR-Format eingeben
* Netzwerkadresse anzeigen
* Subnetzmaske anzeigen
* Broadcast-Adresse anzeigen
* erste und letzte nutzbare Host-Adresse anzeigen
* Anzahl nutzbarer Hosts berechnen
* kurze Erklärung zur Berechnung ausgeben

### Übungsmodus

* kleine Subnetting-Aufgaben erzeugen
* Lösung erst auf Wunsch anzeigen
* Aufgaben so formulieren, dass sie auch für Mitschüler nutzbar sind

### Routing-Tabellen

* Ziel-IP eingeben
* mehrere Routen vergleichen
* erklären, welche Route gewinnt
* Longest Prefix Match verständlich machen

### Später möglich

* IPv6-Grundlagen
* gespeicherte Übungsaufgaben
* einfache Auswertung von falschen Antworten
* Export von Aufgaben und Lösungen

## Beispiel

Eingabe:

```text
192.168.5.0/27
```

Ausgabe:

```text
Netzwerkadresse: 192.168.5.0
Subnetzmaske: 255.255.255.224
Broadcast-Adresse: 192.168.5.31
Erste nutzbare IP: 192.168.5.1
Letzte nutzbare IP: 192.168.5.30
Nutzbare Hosts: 30
```

Erklärung:

```text
/27 bedeutet:
27 Bits sind für das Netz reserviert.
5 Bits bleiben für Hosts übrig.
2^5 = 32 Adressen insgesamt.
Davon fallen Netzwerkadresse und Broadcast weg.
Also bleiben 30 nutzbare Host-Adressen.
```

## Lernziele

Mit NetBuddy übe ich zwei Dinge gleichzeitig:

1. Netzwerktechnik besser verstehen
2. Python sinnvoll für ein echtes Thema einsetzen

Dabei geht es mir nicht darum, sofort ein perfektes Tool zu bauen. Ich möchte das Projekt Schritt für Schritt erweitern und dabei sauber dokumentieren, was ich lerne.

## Aktueller Stand

Das Projekt befindet sich im Aufbau.

Die erste Version konzentriert sich auf ein einfaches Konsolenmenü und die Berechnung von IPv4-Subnetzen.

