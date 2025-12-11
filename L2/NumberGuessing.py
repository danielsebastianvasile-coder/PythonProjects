import random

def number_guessing():
    secret = random.randint(1, 20)
    attempts = 5

    print("Ghiceste numarul (intre 1 si 20). Ai 5 incercari!")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Incercarea {attempt}: "))

            if guess < 1 or guess > 20:
                raise ValueError("Te rog introdu un numar intre 1 si 20.")

            if guess == secret:
                print("Corect! Ai ghicit numarul! 🎉")
                return
            elif guess < secret:
                print("Prea mic!")
            else:
                print("Prea mare!")

        except ValueError as err:
            print(f"Eroare! {err}")
            continue

    print(f"Ai pierdut! Numarul corect era: {secret}")

number_guessing()
