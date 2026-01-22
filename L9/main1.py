from circle import aria_cercului, circumferinta_cercului
from rectangle import aria_dreptunghiului, perimetru_dreptunghiului

while True:
    try:
        r = float(input("Introdu raza cercului: "))
        l = float(input("Introdu lungimea dreptunghiului: "))
        w = float(input("Introdu lățimea dreptunghiului: "))

        print("\n--- REZULTATE ---")
        print("Aria cercului:", aria_cercului(r))
        print("Circumferința cercului:", circumferinta_cercului(r))
        print("Aria dreptunghiului:", aria_dreptunghiului(l, w))
        print("Perimetrul dreptunghiului:", perimetru_dreptunghiului(l, w))
        break

    except ValueError as e:
        print("Eroare:", e)
        print("Încearcă din nou.\n")
