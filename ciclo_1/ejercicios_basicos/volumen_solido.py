#Problema (continuacion)
#1 Establezca el modelo matematico (funcion matematica) que permita
#calcular el volumen del solido anteriormente mostrado.

#2 Escriba una funcion en Python que implemente la funcion
#anteriormente modelada, en la cual se invoque la constante
#matematica π del modulo math.

#3 Para los valores r1 = 3, h = 9/2 y r2 = 4, calcule (a mano o con
#calculadora) el volumen del s ́olido y comp ́arelo con el resultado
#obtenido a partir de la evaluacion de la funcion anteriormente
#implementada. ¿Que pasa si se invoca la funci ́on con los mismos
#valores, pero h se calcula como la expresi ́on h = 9//2?

#Solución:
#1. Modelo matemático:

# _esfera + v_cono = v_total.
#revisión bibliográfica:

#v_esfera = 4/3πr³
#v_cono = = 1/3hπr²
#v_total = 4/3 πr³ + 1/3hπr²

#2.
from math import pi
r_esfera = 4
r_cono = 3
h=4.5
def total():
    return ((4/3)*pi*(r_esfera**3))+((1/3)*h*pi*(r_cono**2))

    
print(total())