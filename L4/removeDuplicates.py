while True:
    try:
        input_str = input("Introdu o lista de numere separate prin virgula: ")

        numbers = [int(x.strip()) for x in input_str.split(",")]

        if len(numbers) == 0:
            raise ValueError

        unique_numbers = []
        for num in numbers:
            if num not in unique_numbers:
                unique_numbers.append(num)

        print("Lista fara duplicate:", unique_numbers)
        break

    except ValueError:
        print("Eroare! Introdu doar numere intregi separate prin virgula.")

