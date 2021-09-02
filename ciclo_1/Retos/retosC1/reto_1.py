#En una planta de tratamiento de agua potable, le adicionan cada día, tres elementos químicos de corrección: 
#kilos de floculante en el tanque B, kilos de cal en el tanque C y litros de cloro en el tanque de salida, 
#siguiendo la siguiente proporción: si al número de kilos de cal le resto 4, me da el doble de los kilos de floculante. 
#Además, si sumo los kilos de cal y de floculante, esto me da 5 veces el número de litros de cloro que requiere. 
#Dado el número de kilos de floculante que se va a emplear, el programa debe calcular los restantes suministros, 
#siguiendo la proporción definida.

#Además, dependiendo del día de la semana, el consumo de agua de la población varia, por lo cual la formulación 
#del día se ha tipificado en 4 categorías, según la cantidad de cloro: uno, si el cloro es hasta 20 litros, 
#inclusive; dos, si el cloro esta entre 20 y 30 litros, inclusive; tres si el cloro esta entre 30 y 50 litros 
#inclusive y cuatro si requiere más de 50 litros.

#Entrada al programa: un numero entero que determina el número de kilos de floculante.

#Salida: primera línea: 3 números enteros separados por un espacio, que indican el número de kilos de floculante, 
#el número de kilos de cal y el número de litros de cloro. Segunda línea, la categoría del cloro añadido, 
#una de las palabras uno, dos, tres o cuatro según corresponda.

#Ejemplo:
#Entrada     Salida

#45           45 94 27
#             dos


#def planta_tratamiento(kg_floculante: int):
#    kg_cal: int = int(2*kg_floculante + 4)
#    litros_cloro: int = int((kg_cal + kg_floculante)/5)
#    if litros_cloro <= 20:
#        cantidad = "uno"
#    elif litros_cloro > 20 and litros_cloro <= 30:
#        cantidad = "dos"
#    elif litros_cloro > 30 and litros_cloro <= 50:
#        cantidad = "tres"
#    else:
#        cantidad = "cuatro"
    #print(kg_floculante,kg_cal,litros_cloro)
    #print(cantidad) PRIMERA FORMA MÁS BÁSICA
#    return kg_cal, litros_cloro, cantidad

#floculante = int(input("Ingrese los kilogramos de floculante: "))

#Forma 1 de desempaquetar la tupla:
#print(type(planta_tratamiento(floculante)))
#cal,litros,cant=planta_tratamiento(floculante)
#print(floculante,cal,litros,"\n"+cant)

#Forma 2 de desempaquetar la tupla:
#tupla_planta = planta_tratamiento(floculante)
#print(floculante,tupla_planta[0],tupla_planta[1],"\n"+str(tupla_planta[2]))


#Otra forma:
def planta_tratamiento(kg_floculante: int):
    kg_cal: int = int(2*kg_floculante + 4)
    litros_cloro: int = int((kg_cal + kg_floculante)/5)
    if litros_cloro <= 20:
        cantidad = "uno"
    elif litros_cloro > 20 and litros_cloro <= 30:
        cantidad = "dos"
    elif litros_cloro > 30 and litros_cloro <= 50:
        cantidad = "tres"
    else:
        cantidad = "cuatro"
    return [kg_cal, litros_cloro, cantidad]

floculante = int(input("Ingrese los kilogramos de floculante: " " "))
print(floculante,planta_tratamiento(floculante)[0],planta_tratamiento(floculante)[1],"\n"+str(planta_tratamiento(floculante)[2]))