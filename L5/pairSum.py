while True:
    try:
        input_str = input("Introdu o lista de numere intregi separate prin virgula: ")
        numbers = [int(x.strip()) for x in input_str.split(",")]

        if len(numbers) < 2:
            raise ValueError("Lista trebuie sa contina cel putin doua numere.")

        target = int(input("Introdu valoarea tinta: "))

        pairs = set()

        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    a = min(numbers[i], numbers[j])
                    b = max(numbers[i], numbers[j])
                    pairs.add((a, b))

        print("Perechi unice care dau suma tinta:")
        print(pairs)
        break

    except ValueError:
        print("Eroare! Introdu doar numere intregi valide.")

