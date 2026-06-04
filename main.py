def zeige_menue():
    print("netBuddy")
    print()
    print("1 - IPv4-Subnetz berechnen")
    print("2 - Übungsmodus")
    print("3 - Routing-Tabelle prüfen")
    print("4 - Beenden")

def main():
    while True:
        zeige_menue()
        auswahl = input("Bitte wähle eine Option aus: ")

        print()
        if auswahl == "1":
            print("IPv4-Subnetzrechner wird gestartet.")
            print()
        elif auswahl == "2":
            print("Übungsmodus wird gestartet.")
            print()
        elif auswahl == "3":
            print("Routing-Tabelle wird geprüft.")
            print()
        elif auswahl == "4":
            print("Programm beendet.")
            print()
            break
        else:
            print("Ungültige Auswahl.")
            print()

main()
