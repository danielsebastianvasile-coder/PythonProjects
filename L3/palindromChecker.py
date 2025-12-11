def is_palindrome(word):

    cleaned_word = word.replace(" ", "").lower()
    return cleaned_word == cleaned_word[::-1]

while True:
    try:
        cuvant = input("Introdu un cuvant (sau 'exit' pentru a iesi): ").strip()

        if cuvant.lower() == 'exit':
            print("Program terminat.")
            break

        if not cuvant.isalpha():
            raise ValueError("Trebuie sa introduci doar litere.")

        if is_palindrome(cuvant):
            print(f"'{cuvant}' este palindrom.")
        else:
            print(f"'{cuvant}' nu este palindrom.")

    except ValueError as ve:
        print(f"Eroare: {ve}. Incearca din nou.")
    except Exception as e:
        print(f"A aparut o eroare neasteptata: {e}. Incearca din nou.")
