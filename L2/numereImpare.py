def odd_numbers():
    while True:
        try:
            n = int(input("Introdu un numar n: "))

            if n < 1:
                raise ValueError("n trebuie sa fie un numar pozitiv mai mare sau egal cu 1.")

            print("Numerele impare pana la n sunt:")
            for i in range(1, n + 1, 2):
                print(i, end=" ")
            print()
            break

        except ValueError as err:
            print(f"Eroare! {err} Incearca din nou.")

odd_numbers()
