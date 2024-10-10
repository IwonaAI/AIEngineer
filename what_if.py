favourite_movies = [
    {
        "title": "Purple hearts",
        "year": 2022,
        "rating": 6.7,
        "stars": ["Sofia Carson", "Nicolas Galitzine"],
        "description": "W tym romantycznym dramacie szukająca sławy piosenkarka Cassie (Sofia Carson) i były komandos z trudną przeszłością Luke (Nicholas Galitzine) decydują się na małżeństwo z rozsądku.",
    },
    {
        "title": "Requiem for a dream",
        "year": 2000,
        "rating": 7.8,
        "stars": ["Jennifer Connely", "Jared Leto", "Ellen Burstyn"],
        "description": "Wstrząsająca opowieść o czwórce bohaterów z Brooklynu, którzy w pogoni za realizacją swoich marzeń odbywają podróż w głąb piekła uzależnień",
    },
    {
        "title": "Kamerdyner",
        "year": 2018,
        "rating": 6.5,
        "stars": ["Sebastian Fabijański", "Marianna Zydek", "Janusz Gajos", "Adam Woronowicz"],
        "description": "Kaszubski chłopiec, po śmierci matki zostaje przygarnięty przez arystokratkę Gerdę von Krauss pochodzącą z majętnego pruskiego rodu. Dorasta w pałacu. Rówieśniczką Mateusza jest córka Kraussów Marita. Między młodymi rodzi się miłość. ",
    },
    {
        "title": "The wolf of Wall Street",
        "year": 2013,
        "rating": 7.7,
        "stars": ["Leonardo DiCaprio", "Margot Robbie", "Matthew McConaughey"],
        "description": "Jordan Belfort był złotym dzieckiem świata amerykańskich finansów. Szybki i oszałamiający sukces przyniósł mu fortunę, władzę i poczucie bezkarności. Pokusy czaiły się wszędzie, a Belfort lubił im ulegać i robił to w wielkim stylu.",
    },
]

my_movie_new = favourite_movies[0]

for movie in favourite_movies:
    if movie["year"] > my_movie_new["year"]:
        my_movie_new = movie

print(my_movie_new["title"])


stars_by_movies = ""
for movie in favourite_movies:
   for star in movie["stars"]:
    stars_by_movies += star + ",\n"
stars_by_movies += "\n_\n\n"
print(stars_by_movies)











   


