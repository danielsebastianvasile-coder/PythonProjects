import math

# Citirea numărului pentru calcule matematice
while True:
    try:
        num = int(input("Introdu un număr întreg (>= 0): "))
        if num < 0:
            raise ValueError("Numărul trebuie să fie pozitiv sau zero.")
        break
    except ValueError as e:
        print("Eroare:", e)
        print("Te rog încearcă din nou.\n")

# Citirea unghiului în grade
while True:
    try:
        angle = float(input("Introdu un unghi în grade: "))
        break
    except ValueError:
        print("Eroare: unghiul trebuie să fie un număr real.\n")

# 1. Rădăcina pătrată
try:
    radacina = math.sqrt(num)
except ValueError:
    radacina = "Nu se poate calcula"

# 2. Factorialul
try:
    factorial = math.factorial(num)
except ValueError:
    factorial = "Nu se poate calcula"

# 3. Sinusul (grade -> radiani)
sinus = math.sin(math.radians(angle))

# Afișarea rezultatelor
print("\n--- REZULTATE ---")
print(f"Rădăcina pătrată a {num} este {radacina}")
print(f"Factorialul lui {num} este {factorial}")
print(f"Sinusul unghiului de {angle} grade este {sinus}")
