import math

def objetosc_szescianu(krawedz):
    return krawedz ** 3

def objetosc_walca(promien, wysokosc):
    return math.pi*promien*2*wysokosc

def objetosc_kuli(promien):
    return 4/3*math.pi*promien**3

szescian_krawedz = int(input("Podaj długość krawędzi sześcianu: "))
walec_dl = int(input("Podaj długość promienia walca: "))
walec_wys = int(input("Podaj wysokość walca: "))
kula_promien = int(input("Podaj długość promienia kuli: "))

print(f"Objętość sześcianu wynosi {objetosc_szescianu(szescian_krawedz)}.\n" 
+ f"Objętość walca wynosi {objetosc_walca(walec_dl, walec_wys)}.\n"
+ f"Objętość kuli wynosi {objetosc_kuli(kula_promien)}.")