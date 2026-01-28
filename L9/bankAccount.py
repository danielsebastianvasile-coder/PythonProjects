class BankAccount:
    def __init__(self, initial_balance=0):
        # Atribut privat (encapsulation)
        self._balance = initial_balance

    def deposit(self, amount):
        # Verificăm dacă suma este pozitivă
        if amount <= 0:
            raise ValueError("Suma depusă trebuie să fie pozitivă.")

        self._balance += amount
        print(f"Depunere reușită! Sold curent: {self._balance} lei")

    def withdraw(self, amount):
        # Verificăm dacă suma este pozitivă
        if amount <= 0:
            raise ValueError("Suma retrasă trebuie să fie pozitivă.")

        # Verificăm dacă există suficient sold
        if amount > self._balance:
            raise ValueError("Fonduri insuficiente pentru retragere.")

        self._balance -= amount
        print(f"Retragere reușită! Sold curent: {self._balance} lei")

    def get_balance(self):
        # Returnăm soldul (fără acces direct la atribut)
        return self._balance


# ---------------- PROGRAM PRINCIPAL ----------------

# Instanțierea unui cont bancar
account = BankAccount()

while True:
    print("\n--- MENIU CONT BANCAR ---")
    print("1. Depunere bani")
    print("2. Retragere bani")
    print("3. Afișare sold")
    print("4. Ieșire")

    try:
        option = int(input("Alege o opțiune: "))

        if option == 1:
            try:
                amount = float(input("Introdu suma de depus: "))
                account.deposit(amount)
            except ValueError as e:
                print("Eroare:", e)

        elif option == 2:
            try:
                amount = float(input("Introdu suma de retras: "))
                account.withdraw(amount)
            except ValueError as e:
                print("Eroare:", e)

        elif option == 3:
            print(f"Soldul curent este: {account.get_balance()} lei")

        elif option == 4:
            print("Aplicația s-a închis. O zi bună!")
            break

        else:
            print("Opțiune invalidă. Alege între 1 și 4.")

    except ValueError:
        print("Te rog introdu un NUMĂR valid pentru opțiune!")
