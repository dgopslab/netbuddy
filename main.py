def zeige_menue():
    print("netBuddy")
    print()
    print("1 - IPv4-Subnetz berechnen")
    print("2 - Übungsmodus")
    print("3 - Routing-Tabelle prüfen")
    print("4 - Beenden")

def starte_subnetzrechner():
    print("IPv4-Subnetzrechner wird gestartet.")
    print()    
    cidr = input("Bitte gib ein Netzwerk im CIDR-Format ein, z. B. 192.168.5.0/24: ").strip()
    print()

    ip_teile = cidr.split("/")

    if len(ip_teile) != 2:
        print("Ungültiges CIDR-Format. Bitte verwende z. B. 192.168.5.0/24.")
    else:
        ip_adresse = ip_teile[0]
        praefix = ip_teile[1]
        print(f"Du hast eingegeben:\nIP-Adresse: {ip_adresse}\nPräfix: {praefix}")

def starte_uebungsmodus():
    print("Übungsmodus wird gestartet.")
    print()

def pruefe_routing_tabelle():
    print("Routing-Tabelle wird geprüft.")
    print()

def main():
    while True:
        zeige_menue()
        auswahl = input("Bitte wähle eine Option aus: ")

        print()
        if auswahl == "1":
            starte_subnetzrechner()
        elif auswahl == "2":
            starte_uebungsmodus()
        elif auswahl == "3":
            pruefe_routing_tabelle()
        elif auswahl == "4":
            print("Programm beendet.")
            print()
            break
        else:
            print("Ungültige Auswahl.")
            print()


main()
