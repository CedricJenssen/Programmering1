import random

#Tom liste for resultat
resultat = []

#Input som brukeren skriver antall spillere
spillere=int(input("Hvor mange spillere?"))
print(f"Spillere: {(spillere)}")

#Bruker range(3) for tre kast
for x in range(3):
    x = (random.randrange(0, 60))
    resultat.append(x)

#Resultatene blir lagt til i listen og resultatet printet ut, result.clear for hver spiller som skal kaste neste.
if spillere == 1:
    print(f"Sluttscore: {sum(resultat)}")
elif spillere == 2:
    print(f"Spiller en: {sum(resultat)}")
    resultat.clear()
    for x in range(3):
        x = (random.randrange(0, 60))
        resultat.append(x)
    print(f"Spiller to: {sum(resultat)}")
elif spillere == 3:
    print(f"Spiller en: {sum(resultat)}")
    resultat.clear()
    for x in range(3):
        x = (random.randrange(0, 60))
        resultat.append(x)
    print(f"Spiller to: {sum(resultat)}")
    resultat.clear()
    for x in range(3):
        x = (random.randrange(0, 60))
        resultat.append(x)
    print(f"Spiller tre: {sum(resultat)}")
else:
    print("For mange spillere!")
    
