import nmap
import ipaddress
import re
import time

def start():
    # Hier heb ik de range staan van de poorten je kunt hierin alle getallen invullen tot het maximum van 65535.
    port_range = re.compile("([0-9]+)-([0-9]+)")
    port_min = 0
    port_max = 65535

    # Hieronder staat een while loop waarin je een ip address invuld.
    # De regel van ip_scan is van de module ipaddress en bekijkt of de input een geldig ip adres is.
    while True:
        ip_input = input("Enter the ip address you want to scan:  ")
        try:
            ip_scan = ipaddress.ip_address(ip_input)
            print("Valid ip, you may continue.")
            break
        except:
            print("IP address invalid, please try again.")

    # Hieronder kun je aangeven welke poorten je zou willen scannen.
    # Er word gekeken of de aangegeven range voldoet aan de eisen van regex.
    # Daarna worden het eerste en laatste getal in een groep geplaatst om parameters te kunnen aangeven in het volgende stuk.
    while True:
        print("Please enter the range of ports you want to scan. (example 20-80)")
        port_input = input("Enter port range (range = 0 t/m 65535): ")
        range_valid = port_range.search(port_input.replace("",""))
        if range_valid:
            port_min = int(range_valid.group(1))
            port_max = int(range_valid.group(2))
            break

    # Hieronder word de scan uitgevoerd door middel van een loop.
    # Er word gevraagd aan het ip adres wat de status van de poorten in de aangegeven range is.
    # Daarna word de poort uitgeprint en de status erbij gezet.
    nm = nmap.PortScanner()
    for port in range(port_min, port_max + 1):
        try:
            result = nm.scan(ip_input, str(port))
            port_status = (result['scan'][ip_input]['tcp'][port]['state'])
            print(f"Port {port} is {port_status}")
        except:
            print(f"Can't scan port {port}.")
    print("All requested ports are scanned.")
    another_scan()

    # Hier wacht het programma 3 seconden voor dat die verder gaat met restart.
    time.sleep(3)


# Hier kun je aangeven of je het programma wil afsluiten of opnieuw wil scannen.
def another_scan():
    restart = input("Would you like to scan another IP address? type yes, if not type no.      ")
    restart = str(restart)
    if (restart == "yes"):
        start()

    if (restart == "no"):
        exit()
    
    else:
        print("Error please type in yes or no all lower case letters.")
        another_scan()

start()
