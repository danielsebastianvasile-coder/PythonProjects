def run_length_encoding(text):

    if not isinstance(text, str):
        raise ValueError("Inputul trebuie să fie un șir de caractere.")

    if text == "":
        raise ValueError("Șirul nu poate fi gol.")

    result = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result += text[i - 1] + str(count)
            count = 1

    result += text[-1] + str(count)

    return result


while True:
    try:
        text = input("Introdu un text (sau 'exit' pentru ieșire): ")

        if text.lower() == "exit":
            print("Program oprit 👋")
            break

        rezultat = run_length_encoding(text)
        print("Rezultat RLE:", rezultat)

    except ValueError as e:
        print("Eroare:", e)
    except Exception as e:
        print("A apărut o eroare neașteptată:", e)
