try:
    principal = float(input("Introdu principalul (suma initiala): "))
    rata = float(input("Introdu rata anuala a dobanzii (ex: 5, 6, 10): "))
    timp = float(input("Introdu timpul in ani: "))

    dobanda = (principal * rata * timp) / 100

    print(f"Dobanda calculata este: {dobanda}")
except ValueError:
    print("Te rog introdu valori numerice corecte!")
