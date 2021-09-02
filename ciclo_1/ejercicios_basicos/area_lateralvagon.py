#Hallar el area lateral de un vagon con 2 ruedas

#Problema (continuacion)
#1 Establezca el modelo matematico (funcion matematica) que permita
#calcular el area lateral del vagon.

#2 Escriba una funcion en Python que implemente la funcion
#anteriormente modelada, en la cual se invoque la constante
#matematica π del modulo math.
from math import pi
def area_vagon():
    return (3*6) + (2*pi*(2**2)) #Valores de las variables vienen dadas por defecto, pues no se dan el ejercicio, así que los asumo yo

print(area_vagon())

#-------------------------------------------------------------------OTRO----------------------------------------------------------------------------
#Establezca el modelo matematico (funcion matematica) que permita
#calcular el area lateral del carro.

#2 Escriba una funcion en Python que implemente la funcion matematica
#previamente modelada, en la cual se utilice la composicion de las
#funciones de suma de numeros reales, area circulo y area rectangulo
#codificadas previamente.
print("-------2--------")
def area_rectangulo(b1,a1,b2,a2):
    rectangulo = (b1*a1)+(b2*a2)
    return rectangulo
    

def area_circulo(r1,r2):
    circulo = (pi*(r1**2)) + (pi*(r2**2))
    return circulo


def area_carro(b1,a1,b2,a2,r1,r2):
    carro = area_rectangulo(b1,a1,b2,a2) + area_circulo(r1,r2)
    return carro

#print(area_carro(area_rectangulo(2,3,4,2),area_circulo(3,6)))
print(area_carro(2,3,4,2,3,6))