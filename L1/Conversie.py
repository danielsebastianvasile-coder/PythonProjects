while True:
    try:
        user_input = input("Introdu temperatura in grade Celsius: ")
        user_input = user_input.replace(',', '.')
        celsius = float(user_input)
        fahrenheit = celsius * 9/5 + 32
        print("Temperatura in Fahrenheit este:", fahrenheit)
        break
    except ValueError:
        print("Trebuie introdus un numar valid! Mai incearca:(")

