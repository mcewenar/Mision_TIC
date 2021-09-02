#1. Diseñe una funcion que calcule la cantidad de carne de aves en kilos
#si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6
#kilos, 7 kilos y 1 kilo respectivamente.

def cantidad_pollo(gallinas,gallos,pollitos):
    return gallinas*6 + gallos*7 + pollitos*1

gallinas = int(input("Ingrese cantidad de gallinas: "))
gallos = int(input("Ingrese cantidad de gallos: "))
pollitos = int(input("Ingrese cantidad de pollitos: "))
print(cantidad_pollo(gallinas, gallos, pollitos))