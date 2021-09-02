#IMPORTANTE:
import json
from pprint import pprint #Pretty print
#El proceso de transformar datos en series de bytes para ser enviados por
#una red o ser guardados como archivo se conoce como serializacion. Los
#archivos JSON se pueden serializar. La librera json expone el metodo
#dump() para escribir datos en un archivo. Si se tiene el siguiente
#diccionario
data = {
'cientifico': {
1: "Alan Mathison Turing", #.dump lo pasa el 1 a str, pues JSON sólo permite cadena de carácteres
"edad": "41"
}}
print(data,"Archivo normal")
with open("C:\\Users\\dmcew\\proy_programacion\\Mision_TIC\\ciclo_1\\ejercicios_basicos\\Manejo_Archivos\\files\\data_file.json", "w") as write_file:
    json.dump(data, write_file) #JSON: COMILLAS DOBLES, CUYAS CLAVES ÚNICAMENTE PERMITEN CARÁCTERES

with open("C:\\Users\\dmcew\\proy_programacion\\Mision_TIC\\ciclo_1\\ejercicios_basicos\\Manejo_Archivos\\files\\data_file.json", "r") as write_file:
    print(write_file.read(),type(write_file),"1")


print("-----------2-----------")
#SERIALIZACIÓN
#Es posible especificar el tamaño de la indentación para estructuras
#anidadas. El siguiente programa establece que la indentacion se realiza a 4
#espacios y se imprime en forma de arbol expandido hacia la derecha.
json_string = json.dumps(data, indent=5)
print(json_string,type(json_string),"2") #Lo pasa a sintaxis JSON y, casteado a str

#Deserialización (de JSON a Python):
#El siguiente codigo carga el objeto JSON a la variable data y luego
#imprime uno de los registros del objeto JSON data, así

#Es posible cargar un archivo de JSON desde un archivo de la siguiente
#manera
with open("C:\\Users\\dmcew\\proy_programacion\\Mision_TIC\\ciclo_1\\ejercicios_basicos\\Manejo_Archivos\\files\\data_file.json", "r") as read_file:
    data = json.load(read_file)
    print(data["cientifico"],"3") #Lo pasa a sintaxis Python


#Es posible cargar un archivo de JSON desde un string. En el siguiente
#codigo se crea un string (en dos lineas por espacio, para esto se encierra
#entre tres comillas simples '''), luego se carga el objeto JSON a la
#variable data y por ultimo esta se imprime
json_string = '''{"cientifico":
{"nombre":"Alan Mathison Turing", "edad": "41"}}'''
data = json.loads(json_string)
print(data,"4")


strjson = '''{
"boolean1": null,
"diccionario": {"papa": 2000, "arroz": 5000},
"intValue": 0, "myList": [],
"myList2":["info1", "info2"],
"littleboolean": false, "myEmptyList": null,
"text1": null, "text2": "hello", "value1": null,
"value2": null}'''
data = json.loads(strjson)
pprint(data) #Imprime lindo 
#Imprime a sintaxis PY.

print("------Indexaciones------")
print(data["text2"], type(data["text2"]))
print(data["text1"], type(data["text1"]))
print(data["intValue"], type(data["intValue"]))
print(data["myList"], type(data["myList"]))
print(data["myList2"], type(data["myList2"]))
print(data["diccionario"], type(data["diccionario"]))
print(data["myList2"][1])
print(data["diccionario"]["papa"])

print("---------3---------")
#Existe un recurso en lnea gratuito llamado JSONPlaceholder para practicar
#peticiones que se pueden realizar en formato JSON. Para realizar una
#peticion se utiliza la librera request as
import json
import requests
#Para leer un archivo JSON de una url especca, se utiliza la instruccion
#response = requests.get("https://github.com/")
#y se carga con
#c=json.loads(response.text)
#print(c)
response = requests.get("https://jsonplaceholder.typicode.com/todos")
pendientes = json.loads(response.text)
#imprime el json cargado
#pprint(pendientes)


#Al procesar los registros del JSON de pendientes cargados se observa
#que cada registro posee un usuario userId, un identicador de pendiente
#id, un ttulo de tarea especco title y un estado completed que indica
#si la tarea ha sido realizada o no.
#Con la siguiente instruccion se obtienen los dos registros iniciales del
#JSON:
#pendientes[:2]

#Salida:
#[{'completed': False,
#'id': 1,
#'title': 'delectus aut autem',
#'userId': 1},
#{'completed': False,
#'id': 2,
#'title': 'quis ut nam facilis et officia qui',
#'userId': 1}]


#Es posible observar que hay varios usuarios cada uno con un identicador
#unico y cada tarea tiene un estado que indica si la tarea se completo o no.
#Procesaremos este archivo para obtener cuantas tareas ha completado
#cada usuario y establecer los usuarios que mas tareas han completado.
#Esto se puede hacer en tres fases:
#1 Contar cuantas tareas han completado los usuarios.
#2 Ordenar el conteo de tareas pendientes que se han completado.
#3 Escoger los usuarios que tienen el mismo numero de tareas maximo.Es posible observar que hay varios usuarios cada uno con un identicador
#unico y cada tarea tiene un estado que indica si la tarea se completo o no.
#Procesaremos este archivo para obtener cuantas tareas ha completado
#cada usuario y establecer los usuarios que mas tareas han completado.
#Esto se puede hacer en tres fases:
#1 Contar cuantas tareas han completado los usuarios.
#2 Ordenar el conteo de tareas pendientes que se han completado.
#3 Escoger los usuarios que tienen el mismo numero de tareas maximo.

#La primera parte lleva un conteo de tareas completadas por usuario:
pendientes_por_usuario= {}
# Lleva un conteo de los pendientes
# que ha completado cada usuario
for pendiente in pendientes:
    if pendiente["completed"]:
        if pendiente["userId"] in pendientes_por_usuario:
            pendientes_por_usuario[pendiente["userId"]] += 1
        else:
            pendientes_por_usuario[pendiente["userId"]] = 1

#Segunda parte:
#La segunda parte ordena el diccionario de pendientes por usuario por su
#conteo de tareas*:
# ordena por id los usuarios
items_ordenados = sorted(pendientes_por_usuario.items(), #sorted(iterable, key=key, reverse=reverse) Optional. A Boolean. False will sort ascending, True will sort descending. Default is False
key=lambda x: x[1], reverse=True) #Parecido a la función arrow
maximas_tareas_completadas = items_ordenados[0][1]


#La tercera parte obtiene las personas con el numero de tareas maximas
usuarios = []
for usuario, num_tareas_completas in items_ordenados:
    if num_tareas_completas == maximas_tareas_completadas:
        usuarios.append(str(usuario))
    else:
        break
usuarios_con_max = " y ".join(usuarios)
print("los usuarios", usuarios_con_max)
print("han completado ", maximas_tareas_completadas, "tareas")
#La salida de este codigo completo es la siguiente
#los usuarios 5 y 10
#han completado 12 tareas


#Es posible ltrar las tareas de los usuarios que han hecho la mayor cantidad
#de pendientes completados y escribirlas en un archivo json. Para esto nos
#apoyaremos de la funcion filter que determina a traves de una funcion
#que retorna un booleano si incluir al elemento en la lista de salida o no
def filtro(pendiente):
    esta_completa = pendiente["completed"]
    esta_en_el_maximo_conteo = str(pendiente["userId"]) in usuarios
    return esta_completa and esta_en_el_maximo_conteo
with open("C:\\Users\\dmcew\\proy_programacion\\Mision_TIC\\ciclo_1\\ejercicios_basicos\\Manejo_Archivos\\files\\tareas_filtradas.json", "w") as archivo_salida:
    tareas_filtradas = list(filter(filtro, pendientes)) #The filter() function returns an iterator were the items are filtered through a
    #function to test if the item is accepted or not. Filter(function, iterable)
    json.dump(tareas_filtradas, archivo_salida, indent=2)

#Una parte de la salida anterior nos muestra tareas con completed=True
#[{'completed': True, 'id': 81, 'title': 'suscipit qui totam', 'userId': 5},
#{'completed': True,
#'id': 83,
#'title': 'quidem at rerum quis ex aut sit quam',
#'userId': 5},
#{'completed': True, 'id': 85, 'title': 'et quia ad iste a', 'userId': 5},
#{'completed': True, 'id': 86, 'title': 'incidunt ut saepe autem',
#'userId': 5},
#{'completed': True,
#'id': 87,
#'title': 'laudantium quae eligendi consequatur quia et vero autem',
#'userId': 5},
#{'completed': True, 'id': 89, 'title': 'sequi ut omnis et', 'userId': 5},