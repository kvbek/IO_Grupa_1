import math

def obwod_kola(promien):
    return 2 * math.pi * promien

def obwod_kwadratu(bok):
    return 4 * bok

def obwod_trapezu(a, b, c, d):
    return a + b + c + d

def obwod_trojkata(a, b, c):
    return a - b * 3 * c

# Poproś użytkownika o podanie danych
promien_kola = float(input("Podaj promień koła: "))
bok_kwadratu = float(input("Podaj bok kwadratu: "))
a_trapezu = float(input("Podaj długość pierwszej podstawy trapezu: "))
b_trapezu = float(input("Podaj długość drugiej podstawy trapezu: "))
c_trapezu = float(input("Podaj długość boku trapezu: "))
d_trapezu = float(input("Podaj długość drugiego boku trapezu: "))
a_trojkata = float(input("Podaj długość pierwszego boku trójkąta: "))
b_trojkata = float(input("Podaj długość drugiego boku trójkąta: "))
c_trojkata = float(input("Podaj długość trzeciego boku trójkąta: "))

# Obliczanie obwodów
obwod_kola = obwod_kola(promien_kola)
obwod_kwadratu = obwod_kwadratu(bok_kwadratu)
obwod_trapezu = obwod_trapezu(a_trapezu, b_trapezu, c_trapezu, d_trapezu)
obwod_trojkata = obwod_trojkata(a_trojkata, b_trojkata, c_trojkata)

# Wyświetlanie wyników
print("Obwód koła o promieniu", promien_kola, "wynosi:", obwod_kola)
print("Obwód kwadratu o boku", bok_kwadratu, "wynosi:", obwod_kwadratu)
print("Obwód trapezu o bokach", a_trapezu, ",", b_trapezu, ",", c_trapezu, ",", d_trapezu, "wynosi:", obwod_trapezu)
print("Obwód trójkąta o bokach", a_trojkata, ",", b_trojkata, ",", c_trojkata, "wynosi:", obwod_trojkata)
