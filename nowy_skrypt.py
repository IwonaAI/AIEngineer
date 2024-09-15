list_all = list(range(1,101))
liczby_parzyste = [liczba for liczba in list_all if liczba % 2 == 0 ]
print (liczby_parzyste)


oceny = {"Jan": 4, "Anna": 5, "Piotr": 3}
oceny ["Anna"] = 6
print (oceny)

zbior = {10, 20, 30, 40, 50}
liczba = 30
if liczba in zbior: zbior.remove(liczba)
print (zbior)

lista_imion = ["Ala", "Ola", "Ela"]
krotka_imion = tuple(lista_imion)
print(krotka_imion)


lista_liczb = list(range(1,21))
print (lista_liczb)
lista_liczb[2] = 100
lista_liczb[4] = 200
print (lista_liczb)
lista_liczb.extend([15,18,35])
print(lista_liczb)

lista1 = [1,2,3]
lista2 = [4,5,6]
lista_polaczona = lista1+lista2
print(lista_polaczona)


lista = [50,20, 30, 10, 40]
posortowana = sorted(lista)
print(posortowana)

