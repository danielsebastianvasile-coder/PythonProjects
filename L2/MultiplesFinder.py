def multiples_finder():
    try:
        x = int(input("Introdu numarul x: "))
        y = int(input("Introdu numarul y: "))

        if x == 0:
            raise ValueError("x nu poate fi 0 (nu exista multipli pentru 0).")

        print(f"Multiplii lui {x} mai mici decat {y} sunt:")

        found = False
        for i in range(x, y, x):
            print(i)
            found = True

        if not found:
            print("Nu exista multiplii ai lui x mai mici decat y.")

    except ValueError as err:
        print(f"Eroare! {err}")

multiples_finder()
