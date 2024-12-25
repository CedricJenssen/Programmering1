#Metode 1
def omkrets(lengde, bredde):
    return lengde * bredde

print(omkrets(3, 6))

#Metode 2
def beregn_omkrets(lengde, bredde):
    omkrets = (lengde * bredde)
    return omkrets

omkrets = beregn_omkrets(3, 6)

print(omkrets)