#Reto 3: Cambio a retornar

#Considere el software que se ejecuta en una máquina expendedora. Una de las tareas que debe realizar es determinar cuánto cambio 
#debe entregarle al cliente luego de que paga. Escriba una función que recibe la cantidad de dinero (en pesos) a dar como cambio al 
#cliente y retorne un mensaje con la cantidad de monedas de cada denominación que deben ser entregadas, 
# teniendo en cuenta que el cambio se debe otorgar con la menor cantidad de monedas posible.
#La máquina cuenta con monedas de 500, 200, 100 y 50 pesos, y el cambio total se entregará con monedas de estas denominaciones. 
#El mensaje retornado DEBE seguir el siguiente formato: “A,B,C,D” (sin espacios intermedios) donde A, B, C y D son la cantidad de monedas de 500, 
#200, 100 y 50, respectivamente.
#Su solución debe tener una función de acuerdo con la siguiente especificación:
#•	Nombre de la función: calcular_cambio
#Si lo requiere, puede agregar funciones adicionales.
#Descripción de parámetros: (MEJORADO)

#->Str es lo que no retorna






def devuelta(cambio):
        devolver = []
        denominaciones=[500,200,100,50,10,5]
        for d in denominaciones:
            A = cambio//d
            devolver.append(A)
            cambio = cambio%d
            if A != 0:
                print("Se entregaron {0} billetes de ".format(A),"$"+str(d))
        print("Sobró $" + str(cambio))
c=int(input("Ingrese un valor"))
devuelta(c)

#FORMA DISTINTA:
#def calcularCambio(valor:int):
#    monedas = [500, 200, 100, 50, 10, 5] # LISTA VALORES TIPO INT
#    devuelta = {500: 0, 200:0, 100:0, 50:0, 10:0, 5:0} # DICCIONARIO 
#    for mon in monedas: # RECORRE LA LISTA 
#        if valor//mon >= 1:
#            devuelta[mon] = valor//mon # INGRESA AL VALOR DE LA LISTA Y SOBREESCRIBE LOS ELEMENTOS PREDEFINIDOS
#            valor -= (valor//mon)*mon
        
#    for llave, valores in devuelta.items():
#        if devuelta[llave] != 0:
#            print("Monedas de", llave, ":", valores)
#    print("Sobró $" + str(valor))
