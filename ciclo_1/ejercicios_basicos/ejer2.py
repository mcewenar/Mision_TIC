#Reto 1: Área de un triángulo

#El área de un triángulo puede ser calculada cuando se conoce la longitud de sus lados. Teniendo en cuenta que s1, s2 y s3 son las 
#longitudes de los lados del triángulo, se puede calcular el subperímetro s = (s1+s2+s3)/2, y, con este valor, 
#se puede calcular el área del triángulo de la siguiente manera: area = √( s * (s-s1) * (s-s2) * (s-s3) ). 
#Cree una función que recibe la medida de los lados del triángulo y retorna el área de este, redondeada a una cifra decimal. 
#El módulo math puede serle de ayuda para calcular la raíz cuadrada.
#Su solución debe tener una función de acuerdo con la siguiente especificación:

#Nombre de la función: area_triangulo
#Si lo requiere, puede agregar funciones adicionales


import math as p
desire = 1
def area_triangulo(s1,s2,s3):
    s = (s1+s1+s3)/2
    a = p.sqrt(s*(s-s1)*(s-s2)*(s-s3))
    return a

while desire:
    try:
        s1 = float(input("Ingrese el lado 1: "))
        s2 = float(input("Ingrese el lado 2: "))
        s3 = float(input("Ingrese el lado 3: "))
        c=area_triangulo(s1,s2,s3)
        print(round(c,1), "cm al 2")
    except ValueError:
        print("No se admiten carácteres. Inténtelo de nuevo")
    
    desire = input("¿Desea salir? ")
    if desire == "No" or desire == "NO" or desire == "no":
        continue
    elif desire == "Sí" or desire == "Si" or desire == "SÍ" or desire == "sí" or desire == "Sí" or desire == "si": 
        desire = 0
    else:
        print("Dato erróneo. Inténtalo nuevamente")

print("Hasta pronto")



