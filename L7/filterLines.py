def filter_lines(input_file, output_file, keyword):

    if not isinstance(input_file, str) or not isinstance(output_file, str):
        raise ValueError("Numele fișierelor trebuie să fie șiruri de caractere.")

    if not isinstance(keyword, str) or keyword.strip() == "":
        raise ValueError("Cuvântul cheie trebuie să fie un șir valid.")

    with open(input_file, "r", encoding="utf-8") as fin:
        lines = fin.readlines()

    with open(output_file, "w", encoding="utf-8") as fout:
        for line in lines:
            if keyword in line:
                fout.write(line)


while True:
    try:
        input_file = input("Introdu fișierul de intrare (sau 'exit' pentru ieșire): ")

        if input_file.lower() == "exit":
            print("Program oprit 👋")
            break

        keyword = input("Introdu cuvântul cheie: ")
        output_file = input("Introdu fișierul de ieșire: ")

        filter_lines(input_file, output_file, keyword)
        print("Fișier creat cu succes:", output_file)

    except FileNotFoundError:
        print("Eroare: Fișierul de intrare nu există.")
    except ValueError as e:
        print("Eroare:", e)
    except Exception as e:
        print("A apărut o eroare neașteptată:", e)
