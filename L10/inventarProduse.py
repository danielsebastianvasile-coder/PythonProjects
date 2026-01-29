
inventar = {}


def adauga_produs(nume, cantitate):
    try:
        cantitate = int(cantitate)
        if cantitate < 0:
            print("Eroare: cantitatea nu poate fi negativa!")
            return
        if nume in inventar:
            inventar[nume] += cantitate
        else:
            inventar[nume] = cantitate
        print(f"Produsul '{nume}' a fost adaugat/actualizat cu cantitatea {cantitate}.")
    except ValueError:
        print("Eroare: cantitatea trebuie sa fie un numar intreg!")

def cauta_produs(nume):
    if nume in inventar:
        print(f"Produsul '{nume}' exista. Cantitate: {inventar[nume]}")
    else:
        print(f"Eroare: produsul '{nume}' nu exista in inventar!")

def actualizeaza_cantitate(nume, cantitate):
    try:
        cantitate = int(cantitate)
        if cantitate < 0:
            print("Eroare: cantitatea nu poate fi negativa!")
            return
        if nume in inventar:
            inventar[nume] = cantitate
            print(f"Cantitatea produsului '{nume}' a fost actualizata la {cantitate}.")
        else:
            print(f"Eroare: produsul '{nume}' nu exista in inventar!")
    except ValueError:
        print("Eroare: cantitatea trebuie sa fie un numar intreg!")

# --- Program principal ---
while True:
    print("\n--- MENIU INVENTAR ---")
    print("1. Adauga produs")
    print("2. Cauta produs")
    print("3. Actualizeaza cantitate")
    print("4. Afiseaza inventar")
    print("5. Iesire")

    alegere = input("Alege o optiune (1-5): ")

    if alegere == "1":
        nume = input("Introdu numele produsului: ")
        cant = input("Introdu cantitatea: ")
        adauga_produs(nume, cant)

    elif alegere == "2":
        nume = input("Introdu numele produsului de cautat: ")
        cauta_produs(nume)

    elif alegere == "3":
        nume = input("Introdu numele produsului: ")
        cant = input("Introdu noua cantitate: ")
        actualizeaza_cantitate(nume, cant)

    elif alegere == "4":
        if inventar:
            print("\nInventar complet:")
            for produs, cantitate in inventar.items():
                print(f"{produs}: {cantitate}")
        else:
            print("Inventarul este gol.")

    elif alegere == "5":
        print("Programul se inchide. La revedere!")
        break

    else:
        print("Eroare: optiune invalida! Incearca din nou.")
