while True:
    try:
        numar = int(input("Introdu un numar intreg: "))
        break
    except ValueError:
        print("Te rog introdu doar cifre!")

if numar%2==0:
    print(f"{numar} este par.")
else:
    print(f"{numar} este impar.")
