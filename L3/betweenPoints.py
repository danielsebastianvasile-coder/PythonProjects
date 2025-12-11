import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

while True:
    try:
        print("Introdu coordonatele primului punct (x1, y1) sau 'exit' pentru a iesi:")
        x1_input = input("x1: ").strip()
        if x1_input.lower() == 'exit':
            break
        y1_input = input("y1: ").strip()
        if y1_input.lower() == 'exit':
            break

        print("Introdu coordonatele celui de-al doilea punct (x2, y2):")
        x2_input = input("x2: ").strip()
        if x2_input.lower() == 'exit':
            break
        y2_input = input("y2: ").strip()
        if y2_input.lower() == 'exit':
            break

        x1 = float(x1_input)
        y1 = float(y1_input)
        x2 = float(x2_input)
        y2 = float(y2_input)

        dist = distance(x1, y1, x2, y2)
        print(f"Distanta dintre punctele ({x1}, {y1}) si ({x2}, {y2}) este {dist:.4f}")

    except ValueError:
        print("Eroare: Trebuie sa introduci un numar valid. Incearca din nou.")
    except Exception as e:
        print(f"A aparut o eroare neasteptata: {e}. Incearca din nou.")

print("Program terminat.")
