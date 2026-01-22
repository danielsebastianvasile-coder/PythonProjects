# rectangle.py

def aria_dreptunghiului(lungime, latime):
    if lungime <= 0 or latime <= 0:
        raise ValueError("Lungimea și lățimea trebuie să fie pozitive!")
    return lungime * latime


def perimetru_dreptunghiului(lungime, latime):
    if lungime <= 0 or latime <= 0:
        raise ValueError("Lungimea și lățimea trebuie să fie pozitive!")
    return 2 * (lungime + latime)
