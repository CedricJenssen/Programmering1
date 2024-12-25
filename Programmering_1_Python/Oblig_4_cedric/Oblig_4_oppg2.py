class Filmer:
    def __init__(self, filmtittel, utgivelsesår, score):
        self.filmtittel = filmtittel
        self.utgivelsesår = utgivelsesår
        self.score = score

    def film_informasjon(self):
        return (f"{self.filmtittel} was released in {self.utgivelsesår} and currently has a score of {self.score}")



inception = Filmer("Inception", 2010, 8.8)
the_martian = Filmer("The Martian", 2015, 8.0)
joker = Filmer("Joker", 2019, 8.4)

print(f"{inception.filmtittel} was released in {inception.utgivelsesår} and currently has a score of {inception.score}")
print(f"{the_martian.filmtittel} was released in {the_martian.utgivelsesår} and currently has a score of {the_martian.score}")
print(f"{joker.filmtittel} was released in {joker.utgivelsesår} and currently has a score of {joker.score}\n")



print(f"{inception.film_informasjon()}")
print(f"{the_martian.film_informasjon()}")
print(f"{joker.film_informasjon()}")

