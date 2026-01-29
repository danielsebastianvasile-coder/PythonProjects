def suma_din_fisier(nume_fisier):
    suma = 0
    try:
        with open(nume_fisier, "r") as fisier:
            for linie in fisier:
                try:
                    numar = float(linie.strip())
                    suma += numar
                except ValueError:
                    print(f"Valoare invalida ignorata: {linie.strip()}")
        return suma

    except FileNotFoundError:
        print("Eroare: fisierul nu exista!")
        return None
    except IOError:
        print("Eroare: problema la citirea fisierului!")
        return None


# --- Program principal ---
while True:
    nume_fisier = input("Introdu numele fisierului: ")
    rezultat = suma_din_fisier(nume_fisier)

    if rezultat is not None:
        print("Suma numerelor din fisier:", rezultat)
        break
    else:
        print("Incearca din nou.\n")
