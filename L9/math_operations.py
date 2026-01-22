# math_operations.py

def adunare(a, b):
    return a + b


def scadere(a, b):
    return a - b


def inmultire(a, b):
    return a * b


def impartire(a, b):
    if b == 0:
        raise ZeroDivisionError("Nu se poate împărți la zero!")
    return a / b
