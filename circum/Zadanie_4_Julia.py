import math

def obwod_kola(promien) -> float:
    try:
        return 2 * math.pi * promien if promien > 0 else print("Promień musi być większy od 0!")
    except ValueError and TypeError:
        print("Promień musi być wartością liczbową!")

def obwod_kwadratu(bok) -> float:
    try:
        return 4 * bok if bok > 0 else print("Bok musi być większy niz 0!")
    except ValueError and TypeError:
        print("Bok musi być wartością liczbową!")

def obwod_trapezu(a, b, c, d) -> float:
    try:
        return a + b + c + d if all([bok > 0 for bok in locals().values()]) else print("Kazdy bok musi być większy niz 0!")
    except ValueError and TypeError:
        print("Kazdy z boków musi być wartością liczbową!")

def obwod_trojkata(a, b, c) -> float:
    try:
        return a + b + c if all([bok > 0 for bok in locals().values()]) else print("Kazdy bok musi być większy niz 0!")
    except ValueError and TypeError:
        print("Kazdy z boków musi być wartością liczbową!")

# Poproś użytkownika o podanie danych
'''
promien_kola = float(input("Podaj promień koła: "))
bok_kwadratu = float(input("Podaj bok kwadratu: "))
a_trapezu = float(input("Podaj długość pierwszej podstawy trapezu: "))
b_trapezu = float(input("Podaj długość drugiej podstawy trapezu: "))
c_trapezu = float(input("Podaj długość boku trapezu: "))
d_trapezu = float(input("Podaj długość drugiego boku trapezu: "))
a_trojkata = float(input("Podaj długość pierwszego boku trójkąta: "))
b_trojkata = float(input("Podaj długość drugiego boku trójkąta: "))
c_trojkata = float(input("Podaj długość trzeciego boku trójkąta: "))
'''
# Obliczanie obwodów
'''
obwod_kola = obwod_kola(promien_kola)
obwod_kwadratu = obwod_kwadratu(bok_kwadratu)
obwod_trapezu = obwod_trapezu(a_trapezu, b_trapezu, c_trapezu, d_trapezu)
obwod_trojkata = obwod_trojkata(a_trojkata, b_trojkata, c_trojkata)
'''
# Wyświetlanie wyników
'''
print("Obwód koła o promieniu", promien_kola, "wynosi:", obwod_kola)
print("Obwód kwadratu o boku", bok_kwadratu, "wynosi:", obwod_kwadratu)
print("Obwód trapezu o bokach", a_trapezu, ",", b_trapezu, ",", c_trapezu, ",", d_trapezu, "wynosi:", obwod_trapezu)
print("Obwód trójkąta o bokach", a_trojkata, ",", b_trojkata, ",", c_trojkata, "wynosi:", obwod_trojkata)
'''

# Test obwodu kwadratu
print(obwod_kwadratu(-5))
assert obwod_kwadratu(-5) == None, "Bok kwadratu musi byc wiekszy od 0"
assert obwod_kwadratu(5) == 20, "Błędny wynik!"
assert obwod_kwadratu("x") == None, "Bok kwadratu musi mieć wartość liczbową!"
assert obwod_kwadratu("5") == None, "Bok kwadratu musi mieć wartość liczbową!"

# Test obwodu kola
assert obwod_kola(-5) == None, "Promień musi byc wiekszy od 0"
assert int(obwod_kola(5)) == 31, "Błędny wynik!"
assert obwod_kola("x") == None, "Promień musi mieć wartość liczbową!"
assert obwod_kola("5") == None, "Promień musi mieć wartość liczbową!"

# Test obwodu trojkata
assert obwod_trojkata(-5, 6, 7) == None, "Bok kwadratu musi byc wiekszy od 0"
assert obwod_trojkata(5, 6, 7) == 18, "Błędny wynik!"
assert obwod_trojkata("x", 6, 7) == None, "Bok kwadratu musi mieć wartość liczbową!"
assert obwod_trojkata("5", 6, 7) == None, "Bok kwadratu musi mieć wartość liczbową!"

# Test obwodu trapezu
assert obwod_trapezu(-5, 6, 7, 8) == None, "Bok kwadratu musi byc wiekszy od 0"
assert obwod_trapezu(5, 6, 7, 8) == 26, "Błędny wynik!"
assert obwod_trapezu("x", 6, 7, 8) == None, "Bok kwadratu musi mieć wartość liczbową!"
assert obwod_trapezu("5", 6, 7, 8) == None, "Bok kwadratu musi mieć wartość liczbową!"
