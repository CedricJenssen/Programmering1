#Bruker tredje siffer i range-funksjon for å lage en intervall på 2 så bare oddetallene blir printet.
for value in range(9,101,2):
    print(value)

#Counter starter på 9
counter = 9
#counter er mindre eller lik 101
while counter <=101:
    print(counter)
    #taller øker med to for hver runde
    counter += 2