# Lernnotizen

Hier sammle ich kurze Notizen zu den Netzwerkthemen, die ich für NetBuddy brauche.

Die Notizen sind nicht als fertiges Lehrbuch gedacht. Sie sollen mir helfen, die Themen selbst sauber zu verstehen und später im Programm verständlich zu erklären.

## IPv4

Eine IPv4-Adresse besteht aus 32 Bits.

Meist sieht man sie in dieser Schreibweise:

```text
192.168.5.10

Die Adresse besteht aus vier Blöcken. Jeder Block kann Werte von 0 bis 255 haben.
```
## CIDR

CIDR ist die Schreibweise mit dem Schrägstrich, zum Beispiel:

192.168.5.0/24

Die Zahl hinter dem Schrägstrich sagt, wie viele Bits für den Netzanteil verwendet werden.

Beispiel:
```text
/24

Das bedeutet:

24 Bits Netzanteil
8 Bits Hostanteil

IPv4 hat insgesamt 32 Bits.

Also:

32 - 24 = 8 Hostbits
```
## Hostbits

Die Hostbits bestimmen, wie viele Adressen in einem Netz möglich sind.

Beispiel bei /27:
```text
32 - 27 = 5 Hostbits
2^5 = 32 Adressen

Bei normalen IPv4-Netzen fallen davon zwei Adressen weg:

Netzwerkadresse
Broadcast-Adresse

Also:

32 - 2 = 30 nutzbare Host-Adressen
```
## Netzwerkadresse

Die Netzwerkadresse beschreibt das Netz selbst.

Beispiel:
```text
192.168.5.0/27

Hier ist:

192.168.5.0

die Netzwerkadresse.

Diese Adresse wird nicht an ein Gerät vergeben.
```
## Broadcast-Adresse

Die Broadcast-Adresse ist die letzte Adresse im Netz.

Bei:

192.168.5.0/27

ist die Broadcast-Adresse:

192.168.5.31

Auch diese Adresse wird nicht an ein normales Gerät vergeben.

Longest Prefix Match

Beim Routing kann eine Ziel-IP zu mehreren Routen passen.

Dann gewinnt die Route mit dem längsten Präfix.

Beispiel:
```text
192.168.5.0/24
192.168.5.0/27
0.0.0.0/0

Für die Ziel-IP:

192.168.5.25

passt mehr als eine Route.

Die Route mit /27 ist am genauesten und gewinnt deshalb.
```
