#Printer meny med valgmulighetene og gir dem et referanse nr
def menu():
    print("[1]Bukse")
    print("[2]T-skjorte")
    print("[3]Sokker")
    print("[4]Hatter")
    print("[5]Hansker")
    print("[8]Print pakkelisten")
    print("[9]Fjern")
    print("[0]Avslutt program")

#Tom liste hvor valgene blir oppbevaret
pakkeliste = []
menu()

#Lager while loop med if statements
#Continue blir brukt for at loopen skal fortsette etter valg og vil spørre om input igjen
#Break blir brukt for å avslutte loopen

while True:
    valg = int(input("Hva vil du ha med deg?\n:"))
    if valg == 1:
        pakkeliste.append("Bukse")
        print("Bukse lagt til i pakkelisten")
        continue
    elif valg == 2:
        pakkeliste.append("T-Skjorte")
        print("T-skjorte lagt til i pakkelisten")
        continue
    elif valg == 3:
        pakkeliste.append("Sokker")
        print("Sokker lagt til i pakkelisten")
        continue
    elif valg == 4:
        pakkeliste.append("Hatter")
        print("Hatt lagt til i pakkelisten")
        continue
    elif valg == 5:
        pakkeliste.append("Hansker")
        print("Hansker lagt til i pakkelisten")
        continue
    elif valg == 9:
        pakkeliste.pop()
        print("Siste valg ble fjernet fra pakkelisten")
        continue
    elif valg == 8:
        print(pakkeliste)
        svar = input("Er pakkelisten ferdig?")
        if svar == "Ja" or "ja":
            break
        elif svar == "Nei" or "nei":
            continue
        else:
            print("Prøv på nytt")
    elif valg == 0:
        break

print("Pakkelisten din er ferdig")
print(pakkeliste)