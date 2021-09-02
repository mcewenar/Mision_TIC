def variable_argument(var1, *vari): #Se utiliza *nombre var quedando nombre var como tupla. Si sólo hay un parámetro, ignora el segundo parámetro
    print('salida:'+ str(var1))
    for var in vari: #Sólo sirve si hay dos parámtros
        print(var)
variable_argument(60)
variable_argument(100, 90, 67, 23, 10) #Toma el primer parámetro (100) y los demás los mete en una tupla
#Esto ayuda a evitar errores de parámetros


#Es posible enviar parejas llave=valor como argumentos a una funcion con
#**nombre var , la variable nombre var queda denida como diccionario.
from pprint import pprint
def informar(**var): #Convierte las variables=valor a un diccionario
    pprint(var)
    for key, value in var.items():
        pprint("%s == %s" %(key,value)) #Ojo a esto
informar(nombre="Poseidón",edad=6000,ciudad="Olimpo",estilo="Jabalina") #Positional argument


print("----2----")
def unir_listas(lista1, lista2):
    lista1.extend(lista2)
avengers = ['Tony', 'Natalia', 'Steve']
nuevos_avengers = ['Thor', 'Peter']
unir_listas(avengers, nuevos_avengers)

#No necesita un return, pues la listas son globales, aun así se modifican
print(avengers)


print("-----3----, sin parámetros ni return")
print("No recomendable")
avengers = ['Tony', 'Natalia', 'Steve']
nuevos_avengers = ['Thor', 'Peter']
def unir_listas():
    avengers.extend(nuevos_avengers)

unir_listas()
#No necesita un return, pues la listas son globales, aun así se modifican,
#El return es indispensable con variables con local scope.
print(avengers)


print("---4---")
def func(a):
    a *= 10
    print('En la funcion a=',a)
a = 45
func(a)
print('En el programa principal a=',a)
#Recordar los ámbitos: Global y local

#En el siguiente ejemplo, el valor de avengers del programa principal no
#cambia debido a la asignacion que se esta realizando dentro de la funcion
#a la variable lista (click aqu para ver paso a paso):
def no_limpia_lista(lista):
    lista = []  #se crea una copia, lo cual guarda un diferente espacio RAM, por tanto, no se modifica el valor original
    #lista.copy() También crea una copia
avengers = ['Tony', 'Natalia', 'Steve']
no_limpia_lista(avengers)
print(avengers)

print("----5----")
#En python hay dos tpos basicos de alcance de las variables:
#Variables locales
#Variables globales
#Para entender este concepto, se usaran los decretos expedidos por
#gobiernos locales y nacionales como smil. Un decreto expedido por la
#alcalda de Bogota tiene alcance solo para los habitantes de la capital pero
#no para los del resto del pas. Un decreto expedido por la presidencia de
#Colombia tiene alcance en el pas (incluida Bogota) pero no en otros
#países.
def func():
    a=12
print('Variable local:', a)
a=10
func()
print ('Variable del cuerpo principal:',a)

#Cuando se usa la palabra global antes de una variable, dentro de una
#funcion, se indica que dicha variable tiene alcance global y que cualquier
#operacion que le hagamos dentro de la funcion puede modicar el valor de
#la variable global (click aqu para analizar el codigo):
print("---tener en cuenta")

#De esta manera, con la palabra global se puede cambiar el valor de una
#variable global dentro de una funcion:
k=5
def func():
    global k
    k=k+7
    print("La variable k tiene alcance global:",k)
    k=10
func()
print ("Valor de la variable global k fuera de la funcion:",k)

print("-----6-----")
x = "sorprendente"
print(x)
def myfunc():
    global x
    x = "fantástico"
    print(x)
print("Antes Python era " + x)
myfunc() #A partir de acá lo modifica permanentemente
print("Ahora Python es " + x)
print("Ahora Python es " + x)


print("---7---")
#Se modica el archivo main.py para usar la funcion dir con el modulo
#modulo:
#import modulo
#print ("Las funciones de modulo son:", dir(modulo))

#Cuando se utiliza import, python buscara el modulo en la siguiente forma:
#El directorio actual
#La variable de entorno PYTHONPATH
#Para ver informacion sobre las rutas usadas por Python para import:
import sys
for p in sys.path:
    print(p)