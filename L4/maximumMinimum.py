while True:
    try:
        input_str = input("Introdu o lista de numere separate prin virgula: ")

        numbers = [int(x.strip()) for x in input_str.split(",")]

        if len(numbers) == 0:
            raise ValueError("Lista este goala.")

        print("Lista introdusa:", numbers)
        print("Minimul:", min(numbers))
        print("Maximul:", max(numbers))
        break

    except ValueError:
        print("Eroare! Introdu doar numere intregi separate prin virgula.")

