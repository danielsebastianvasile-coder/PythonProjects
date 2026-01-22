import math_operations as mo

while True:
    try:
        a = float(input("Introdu primul număr: "))
        b = float(input("Introdu al doilea număr: "))

        print("\n--- REZULTATE ---")
        print("Adunare:", mo.adunare(a, b))
        print("Scădere:", mo.scadere(a, b))
        print("Înmulțire:", mo.inmultire(a, b))
        print("Împărțire:", mo.impartire(a, b))
        break

    except ValueError:
        print("Eroare: trebuie să introduci numere valide!\n")

    except ZeroDivisionError as e:
        print("Eroare:", e)
        print("Încearcă din nou.\n")
