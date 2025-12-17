while True:
    try:
        input_str = input("Introdu valori separate prin virgula: ")

        values = tuple(int(x.strip()) for x in input_str.split(","))

        if len(values) == 0:
            raise ValueError

        search_value = int(input("Introdu valoarea de cautat: "))

        print("Tupla:", values)

        if search_value in values:
            index = values.index(search_value)
            print(f"{search_value} se regaseste in tupla la indexul {index}.")
        else:
            print(f"{search_value} NU se regaseste in tupla.")

        break

    except ValueError:
        print("Eroare! Introdu doar numere intregi separate prin virgula.")

