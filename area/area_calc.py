import math

def pole_kwadratu(bok):
    return bok ** 2

def pole_trojkata(podstawa, wysokosc):
    return podstawa*wysokosc/2

def pole_trapezu(podstawa1, podstawa2, wysokosc):
    return podstawa1+podstawa2*wysokosc/2

def pole_kola(promien):
    return math.pi*promien**2