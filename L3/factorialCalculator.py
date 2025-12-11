def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


while True:
    try:
        num = input("Introdu un numar intreg pozitiv (sau 'exit' pentru a iesi): ").strip()

        if num.lower() == 'exit':
            print("Program terminat.")
            break

        n = int(num)

        if n < 0:
            raise ValueError("Numarul trebuie sa fie pozitiv sau zero.")

        print(f"Factorialul lui {n} este {factorial(n)}.")

    except ValueError as ve:
        print(f"Eroare: {ve}. Incearca din nou.")
    except Exception as e:
        print(f"A aparut o eroare neasteptata: {e}. Incearca din nou.")
