filmer = [
    {"name" : "Inception", "year" : 2010, "rating" : 8.7},
    {"name" : "Inside Out", "year" : 2015, "rating" : 8.1},
    {"name" : "Con Air", "year" : 1997, "rating" : 6.9}
]

def add_movie(name, year, rating=5.0):
    print(f"{name} - {year} has a rating of {rating}")
    filmer.append({"name": name, "year": year, "rating": rating})
    return filmer

add_movie("No Time to Die", 2021, 7.6)
add_movie("Snatch", 2000, 8.3)
add_movie("Oldboy", 2003, 8.4)
add_movie("Reservoir Dogs", 1992)
print(filmer)


ratings = [8.7, 8.1, 6.9, 7.6, 8.3, 8.4, 5.0]

def average_rating():
    avg_value = sum(ratings) / len(filmer)
    return avg_value

avg_value = average_rating()
print(f"The average rating is: {avg_value}")



def print_filmer_2003(filmer, year):
    for film in filmer:
        if film["year"] >= year:
            print(film)
    
print_filmer_2003(filmer, 2003)

def file(filmer, movie_titles):
    with open("movie_titles.txt", "w") as file:
        file.write(str(filmer))

file(filmer, "movie_titles.txt")

