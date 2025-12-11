def grading_system():
    while True:
        try:
            score = float(input("Introdu scorul procentual (0-100): "))

            if score < 0 or score > 100:
                raise ValueError("Scorul trebuie sa fie intre 0 si 100.")

            if score >= 90:
                grade = "A"
            elif score >= 80:
                grade = "B"
            elif score >= 70:
                grade = "C"
            elif score >= 60:
                grade = "D"
            else:
                grade = "F"

            print(f"Nota corespunzatoare este: {grade}")
            break

        except ValueError as err:
            print(f"Eroare! {err}\nReincearca...\n")

grading_system()
