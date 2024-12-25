#Printer spørsmål
print("Hva er meningen med livet?")
#Henter user input i integer
answer = int(input())

#If statement for å finne ut om svaret er feil eller riktig. Elif for et nytt alternativ.
if(answer == 42):
    print("Det stemmer, meningen med livet er 42!")
elif(answer>=30 and answer<=50):
    print("Nærme, men feil.")
else:
    print("FEIL!")
