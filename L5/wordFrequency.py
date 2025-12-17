while True:
    try:
        text = input("Introdu un text: ")

        if not text.strip():
            raise ValueError("Textul este gol.")

        text = text.lower()

        for p in ".,!?;:":
            text = text.replace(p, "")

        words = text.split()

        if len(words) == 0:
            raise ValueError("Nu exista cuvinte valide.")

        freq = {}
        for word in words:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1

        print("Frecventa cuvintelor:")
        print(freq)
        break

    except ValueError:
        print("Eroare! Introdu un text valid.")
