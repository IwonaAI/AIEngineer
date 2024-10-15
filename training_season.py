#name = input("Podaj swoje imię: ")
#print ("Witaj " + name + "!")

#hrs = input("Podaj liczbę godzin: ")
#hrs = float(hrs)
#rt = input("Podaj stawkę godzinową: ")
#rt = float(rt)
#pay = hrs * rt 
#pay = round(pay, 2)
#print("Wynagrodzenie: " + str(pay))

#celsius = input("Podaj temperaturę w skali Celsjusza: ")
#celsius = float(celsius)
#fahrenheit = ((celsius * 2) + 32)
#print ("Temperatura w skali Fahrenheita to: " + str(fahrenheit))

#hrs = input("Podaj liczbę godzin: ")
#hrs = float(hrs)
#rt = input("Podaj stawkę godzinową: ")
#rt = float(rt)
#if hrs <= 40:
    #pay = hrs * rt
#else:
    #pay = 40 * rt + (hrs -  40) * 1.5 *rt
#pay = round(pay, 2)
#print("Wynagrodzenie: " + str(pay))

try:
    hrs = input("Podaj liczbę godzin: ")
    hrs = float(hrs)
    rt = input("Podaj stawkę godzinową: ")
    rt = float(rt)
    if hrs <= 40:
        pay = hrs *rt
    else:
        pay = rt * 40 + (hrs - 40) * 1.5 * rt
    pay = round(pay, 2)
    print("Wynagrodzenie: " + str(pay))
except: 
    print("Błąd! Podaj wartość numeryczną")

try:
    score = input("Podaj wartość pomiędzy 0.0 a 1.0: ")
    score = float(score)
    if score > 1.0 or score < 0.0:
        print("Podaj poprawną wartość")
    elif score >= 0.9:
        print("5.0")
    elif score >= 0.8:
        print("4,5")
    elif score >= 0.7:
        print("4.0")
    elif score >= 0.6:
        print("3,5")
    elif score >= 0.5:
        print("3.0")
    else:
        print("2.0")
except:
    print("Niepoprawna wartość!")


