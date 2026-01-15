def is_palindrome(text):

    if not isinstance(text, str):
        raise ValueError("Inputul trebuie să fie un șir de caractere.")


    cleaned_text = text.replace(" ", "").lower()

    return cleaned_text == cleaned_text[::-1]


while True:
    try:
        text = input("Introdu un text (sau 'exit' pentru ieșire): ")

        if text.lower() == "exit":
            print("Program oprit 👋")
            break

        rezultat = is_palindrome(text)
        print("Este palindrom?", rezultat)

    except ValueError as e:
        print("Eroare:", e)
    except Exception as e:
        print("A apărut o eroare neașteptată:", e)
