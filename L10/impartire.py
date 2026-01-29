
def imparte(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Eroare: nu se poate imparti la zero!"


while True:
    try:
        a = float(input("Introdu primul numar: "))
        b = float(input("Introdu al doilea numar: "))

        rezultat = imparte(a, b)
        print("Rezultat:", rezultat)
        break

    except ValueError:
        print("Eroare: introdu doar numere! Incearca din nou.\n")
