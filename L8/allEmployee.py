class Employee:
    def __init__(self, name, salary):
        # Validare date de intrare
        if not name:
            raise ValueError("Numele nu poate fi gol.")
        if salary <= 0:
            raise ValueError("Salariul trebuie să fie pozitiv.")

        self.name = name
        self.salary = salary

    def get_details(self):
        # Metodă din clasa de bază
        return f"Employee: {self.name}, Salary: {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, department):
        # Apelăm constructorul clasei părinte
        super().__init__(name, salary)

        if not department:
            raise ValueError("Departamentul nu poate fi gol.")

        self.department = department

    def get_details(self):
        # Suprascriere metodă (override)
        return f"Manager: {self.name}, Salary: {self.salary}, Department: {self.department}"


# ---------------- PROGRAM PRINCIPAL ----------------

employees = []

while True:
    print("\n--- MENIU ANGAJAȚI ---")
    print("1. Adaugă angajat")
    print("2. Adaugă manager")
    print("3. Afișează toți angajații")
    print("4. Ieșire")

    try:
        option = int(input("Alege o opțiune: "))

        if option == 1:
            try:
                name = input("Nume angajat: ")
                salary = float(input("Salariu: "))
                emp = Employee(name, salary)
                employees.append(emp)
                print("Angajat adăugat cu succes!")
            except ValueError as e:
                print("Eroare:", e)

        elif option == 2:
            try:
                name = input("Nume manager: ")
                salary = float(input("Salariu: "))
                department = input("Departament: ")
                mgr = Manager(name, salary, department)
                employees.append(mgr)
                print("Manager adăugat cu succes!")
            except ValueError as e:
                print("Eroare:", e)

        elif option == 3:
            if not employees:
                print("Nu există angajați.")
            else:
                print("\n--- LISTĂ ANGAJAȚI ---")
                for emp in employees:
                    # Polimorfism: se apelează metoda corectă automat
                    print(emp.get_details())

        elif option == 4:
            print("Aplicația s-a închis.")
            break

        else:
            print("Opțiune invalidă.")

    except ValueError:
        print("Te rog introdu un NUMĂR valid pentru opțiune!")
