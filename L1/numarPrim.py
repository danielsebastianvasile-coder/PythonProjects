while True:
    try:
        numar = int(input("Introdu un numar intreg: "))
        break
    except ValueError:
        print("Te rog introdu doar un numar intreg!")

if numar <= 1:
    print("Numarul NU este prim.")
else:
    este_prim = True
    for i in range(2, int(numar ** 0.5) + 1):
        if numar % i == 0:
            este_prim = False
            break

    if este_prim:
        print("Numarul este prim.")
    else:
        print("Numarul nu este prim.")
