def count_words_in_file(filename):
    """
    Citește un fișier text și returnează
    numărul total de cuvinte din fișier.
    """
    if not isinstance(filename, str):
        raise ValueError("Numele fișierului trebuie să fie un șir de caractere.")

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    # Împărțim textul în cuvinte (elimină automat spațiile multiple)
    words = content.split()

    return len(words)


# Buclă infinită
while True:
    try:
        filename = input("Introdu numele fișierului (sau 'exit' pentru ieșire): ")

        if filename.lower() == "exit":
            print("Program oprit 👋")
            break

        result = count_words_in_file(filename)
        print("Număr total de cuvinte:", result)

    except FileNotFoundError:
        print("Eroare: Fișierul nu există.")
    except ValueError as e:
        print("Eroare:", e)
    except Exception as e:
        print("A apărut o eroare neașteptată:", e)
