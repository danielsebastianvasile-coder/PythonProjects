def reverse_lines(input_file, output_file):

    if not isinstance(input_file, str) or not isinstance(output_file, str):
        raise ValueError("Numele fișierelor trebuie să fie șiruri de caractere.")

    with open(input_file, "r", encoding="utf-8") as fin:
        lines = fin.readlines()

    with open(output_file, "w", encoding="utf-8") as fout:
        for line in lines:

            reversed_line = line.rstrip("\n")[::-1]
            fout.write(reversed_line + "\n")


while True:
    try:
        input_file = input("Introdu fișierul de intrare (sau 'exit' pentru ieșire): ")

        if input_file.lower() == "exit":
            print("Program oprit 👋")
            break

        output_file = input("Introdu fișierul de ieșire: ")

        reverse_lines(input_file, output_file)
        print("Fișier creat cu succes:", output_file)

    except FileNotFoundError:
        print("Eroare: Fișierul de intrare nu există.")
    except ValueError as e:
        print("Eroare:", e)
    except Exception as e:
        print("A apărut o eroare neașteptată:", e)
