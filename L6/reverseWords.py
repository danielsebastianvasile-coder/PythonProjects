def reverse_words(sentence):

    if not isinstance(sentence, str):
        raise ValueError("Inputul trebuie să fie un șir de caractere.")

    words = sentence.strip().split()

    reversed_words = words[::-1]

    return " ".join(reversed_words)



while True:
    try:
        sentence = input("Introdu o propoziție (sau 'exit' pentru ieșire): ")

        if sentence.lower() == "exit":
            print("Program oprit 👋")
            break

        rezultat = reverse_words(sentence)
        print("Rezultat:", rezultat)

    except ValueError as e:
        print("Eroare:", e)
    except Exception as e:
        print("A apărut o eroare neașteptată:", e)
