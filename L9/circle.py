# circle.py
import math


def aria_cercului(r):
    if r <= 0:
        raise ValueError("Raza trebuie să fie pozitivă!")
    return math.pi * r * r


def circumferinta_cercului(r):
    if r <= 0:
        raise ValueError("Raza trebuie să fie pozitivă!")
    return 2 * math.pi * r
