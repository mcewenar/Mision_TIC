#Los proveedores de equipo de cómputo, normalmente identifican los bienes que tienen para la venta en un catálogo 
#mediante parejas <código_estandar:valor> en formato JSON.
#
#Una empresa va a adquirir varios equipos de cómputo de varias marcas (servidores, estaciones de trabajo, computadores de escritorio, 
#portátiles, tabletas, enrutadores, switches, Access points), para todas sus sedes. Y hace una licitación 
#publicando una relación de los equipos que requiere, identificados mediante de códigos estándar de una letra.
#
#Uno de los proveedores de equipo requiere un programa para cruzar la lista de equipos solicitados por licitación 
#contra su propio catalogo ya que quiere saber cuáles equipos puede ofrecer y cuál sería el valor total de la oferta, 
#si de cada equipo se compra una unidad.
#
#Entrada:
#
#Línea1: parejas <código_estandar:valor> en formato JSON del catálogo del proveedor y linea2: relación total de letras que 
#identifican los equipos solicitados por licitación. En este caso los equipos se identifican por letras del alfabeto, separados por espacio.
#
#Salida:
#
#Línea 1: valor total de los equipos solicitados y que el proveedor puede ofrecer, representado por un número entero.
#
#linea2: relación de códigos que identifican los equipos que el proveedor puede ofrecer y que son solicitados en la licitación.

#Ejemplo:

#Entrada:
#{"v": 45, "s": 32, "c": 45, "g": 29, "z": 45, "d": 46}
#s v c d y f t
#
#Salida: 
#168
#s v c d

import json
def Inventario(proveedor: str,licit: str):
    dic_relacionados = {}
    lista_licit: list = licit.split()
    dict_data: dict = json.loads(proveedor)
    for i in lista_licit:
        if i in dict_data:
            dic_relacionados.update({i:dict_data.get(i)})
    total = totalValorCruzado(dic_relacionados)
    return total," ".join(list(dic_relacionados.keys()))

def totalValorCruzado(dict_cruz: dict):
    total = 0
    for i in dict_cruz.values():
        total+=i
    return total

def main():
    total,coincidencias=Inventario(input("Enter dict supplier: "),input("Enter enterprise list: "))
    print(total)
    print(coincidencias)
if __name__ == "__main__":
    main()