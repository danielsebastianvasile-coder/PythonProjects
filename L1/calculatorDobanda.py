while True:
    try:
        principal = float(input("Introdu principalul (suma initiala): "))
        rata = float(input("Introdu rata anuala a dobanzii (ex: 5, 6, 10): "))
        timp = float(input("Introdu timpul in ani: "))

        dobanda = (principal * rata * timp) / 100

        print(f"Dobanda calculata este: {dobanda}")
        break  # iesim din loop dacă totul e corect

    except ValueError:
        print("Eroare! Te rog introdu valori numerice corecte.\nReincearca...\n")
