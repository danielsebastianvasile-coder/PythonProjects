while True:
    try:
        n = int(input("Introdu numarul de documente: "))

        if n <= 0:
            raise ValueError

        documents = []
        for i in range(n):
            doc = input(f"Documentul {i}: ").strip()
            if not doc:
                raise ValueError
            documents.append(doc)

        index = {}

        for i, doc in enumerate(documents):
            # ignoram majusculele
            doc = doc.lower()

            # eliminam punctuatia de baza (pastram cratima)
            for p in ".,!?;:":
                doc = doc.replace(p, "")

            words = doc.split()

            for word in words:
                if word not in index:
                    index[word] = {i}
                else:
                    index[word].add(i)

        print("Index inversat:")
        print(index)
        break

    except ValueError:
        print("Eroare! Introdu date valide.")

