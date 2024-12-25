#Lager en liste med bøkene
tolkien = ['The Hobbit', 'Farmer Giles of Ham', 'The Fellowship of the Ring', 'The Two Towers', 'The Return of the King', 'The Adventures of Tom Bombadil', 'Tree and Leaf']
print(tolkien[0])
print(tolkien[1])
print(tolkien[5])
print(tolkien[6])

#Legger til to bøker
tolkien.append('The Silmarillion')
tolkien.append('Unfinished Tales')

#Gir bøkene under et nytt navn
tolkien[2] = 'Lord of The Rings: The Fellowship of the Ring'
tolkien[3] = 'Lord of The Rings: The Two Towers'
tolkien[4] = 'Lord of The Rings: The Return of the King'

#sorterer listen og printer den
tolkien.sort()
print(f"\nSortert liste: {tolkien}")


tom_liste = []

#Legger til bøkene i den tomme listen og printer den ut
tom_liste = [x for x in tolkien if "Lord of The Rings:" in x]
print(tom_liste)

#Printer ut bøkene med for løkker
for books in tolkien:
  if "Lord of the Rings:" in books:
    tom_liste.append(books)
print(tom_liste)

for books in range(len(tom_liste)):
    print(tom_liste[books])
