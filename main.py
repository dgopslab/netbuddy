def zeige_menue():
    print("netBuddy")
    print()
    print("1 - IPv4-Subnetz berechnen")
    print("2 - Übungsmodus")
    print("3 - Routing-Tabelle prüfen")
    print("4 - Beenden")

def main():
    zeige_menue()
    auswahl = input("Bitte wähle eine Option aus: ")

    print()    
    if auswahl == "4":
        print("Programm beendet.")
    else:
        print(f"Du hast Option {auswahl} gewählt.")

main()
