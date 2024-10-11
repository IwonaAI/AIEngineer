favourite_books = [
    {
    "title": "Siła emocji",
    "author": "Thibaut Meurisse",
    "year": 2023,
    "is_published_after_2000": True,
    "characters": ["Frank", "Bob", "Ashley", "Mia"],
    },
    {
        "title": "Nie czekaj już dłużej",
        "author": "Alina Adamowicz",
        "year": 2024,
        "is_published_after_2000": True,
        "characters": ["Laura", "Beata", "Patrycja", "Kasia"],
        }
]
# for book in favourite_books:
  #  print(book["title"])

# for book in favourite_books:
  #  print(book["author"])

# if favourite_books[0]["is_published_after_2000"]==True:
  #  print(favourite_books[0]["title"])

# if favourite_books[0]["is_published_after_2000"] == True:
  #   print("Książka " + (favourite_books[0]["title"]) + " jest opublikowana po 2000 roku")
# elif favourite_books[0]["is_published_after_2000"] == False:
  #  print("Książka " + (favourite_books[0]["title"]) + " nie jest opublikowana po 2000 roku")

# if favourite_books[1]["is_published_after_2000"] == True:
  #   print("Książka " + (favourite_books[1]["title"]) + " jest opublikowana po 2000 roku")
# elif favourite_books[1]["is_published_after_2000"] == False:
  #   print("Książka " + (favourite_books[1]["title"]) + " nie jest opublikowana po 2000 roku")


# if favourite_books[0]["is_published_after_2000"] != False:
  #  print("Książka " + (favourite_books[0]["title"]) + " jest opublikowana po 2000 roku")

# if favourite_books[0]["year"] >= 2000:
  # print("Książka " + (favourite_books[0]["title"]) + " jest opublikowana po 2000 roku")
# elif favourite_books[0]["year"] <= 2000:
  # print("Książka " + (favourite_books[0]["title"]) + " nie jest opublikowana po 2000 roku")

# if favourite_books[1]["year"] >= 2000:
  # print("Książka " + (favourite_books[1]["title"]) + " jest opublikowane po 2000 roku")
# elif favourite_books[1]["year"] <= 2000:
  # print("Książka " + (favourite_books[1]["title"]) + " nie jest opublikowane po 2000 roku")

for book in favourite_books:
  if book["is_published_after_2000"] == True:
    print("Książka " + (book["title"]) + " jest opublikowana po 2000 roku")
  else:
      print("Książka " + (book["title"]) + " nie jest opublikowana po 2000 roku")




