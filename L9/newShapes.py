import math


class Shape:
    def area(self):
        # Metodă care trebuie implementată în clasele copil
        raise NotImplementedError("Metoda area() trebuie implementată în subclase.")


class Circle(Shape):
    def __init__(self, radius):
        # Validare date
        if radius <= 0:
            raise ValueError("Raza cercului trebuie să fie pozitivă.")

        self.radius = radius

    def area(self):
        # Formula ariei cercului
        return math.pi * self.radius ** 2

    def __str__(self):
        # Afișare obiect
        return f"Circle with radius {self.radius} has area {self.area():.2f}"


class Rectangle(Shape):
    def __init__(self, width, height):
        # Validare date
        if width <= 0 or height <= 0:
            raise ValueError("Lățimea și înălțimea trebuie să fie pozitive.")

        self.width = width
        self.height = height

    def area(self):
        # Formula ariei dreptunghiului
        return self.width * self.height

    def __str__(self):
        # Afișare obiect
        return f"Rectangle with width {self.width} and height {self.height} has area {self.area()}"


# ---------------- PROGRAM PRINCIPAL ----------------
try:
    circle = Circle(5)
    rectangle = Rectangle(10, 4)

    print(circle)
    print(rectangle)w

except ValueError as e:
    print("Eroare:", e)
