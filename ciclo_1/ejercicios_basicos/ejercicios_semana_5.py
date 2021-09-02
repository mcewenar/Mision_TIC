#1. Desarrollar un algoritmo que imprima de manera ascendente los
#valores (todos del mismo tipo) de un diccionario.

#2. Desarrollar un algoritmo que verique si todas las clave:valor de
#un diccionario se encuentran en otro diccionario.

#3. Desarrollar una funcion que reciba dos diccionarios como parametros
#y los mezcle, es decir, que se construya un nuevo diccionario con las
#llaves de los dos diccionarios; si hay una clave repetida en ambos
#diccionarios, se debe asignar el valor que tenga la clave en el
#primer diccionario.

#4. Desarrollar un programa que dada una listas de personas, cada
#persona representada como el siguiente ejemplo:
#f"nombres":"Pedro Julio", "apellidos":"Tristan Merchan",
#"edad":101g, imprima los nombres y apellidos de las personas que
#estan en un rango de edades.

#1.
#dicc = {"a":5,"b":3,"c":6,"d":2,"e":1,"f":4}
#for i in dicc:
#    for j in dicc:
#        if dicc[i] < dicc[j]:
#            #Forma rápida
#            dicc[i],dicc[j]=dicc[j],dicc[i]
#
#            #Forma larga: (ANALIZAR)
#            #tem=dicc[i]
#            #dicc[i]=dicc[j]
#            #dicc[j]=tem
#print(dicc)

#2. Desarrollar un algoritmo que verifique si todas las clave:valor de un diccionario se encuentran en otro diccionario.
#De dicc 1 en dicc 2
#bandera:bool=True
#dicc1={"a":5,"b":3,"c":6,"d":2,"e":1,"f":4}
#dicc2={"a":69,"b":3,"c":6,"d":2,"e":1,"f":4}
#for k1 in dicc1:
#    print(k1,"-->",dicc1[k1])
#    if k1 in dicc2 and dicc1[k1] in list(dicc2.values()):
#        bandera=True
#    else:
#        bandera=False
#        break
#print(bandera)
#
#
#print(dicc1==dicc2)
##De dicc 2 en dicc 1
#for llaveB in dicc2:  
#  if llaveB not in dicc1:
#    bandera=False
#    break
#  elif dicc1.get(llaveB) != dicc2.get(llaveB):
#    bandera=False
#    break
#print(bandera)

#3.
#def diccionarios(dict1:dict,dict2:dict):
#    dict3={}
#    print(type(dict1),type(dict2))
#    for k in dict2:
#        if k in dict1:
#            dict1[k]=dict2.get(k)
#    dict3.update(dict1)
#    dict3.update(dict2)
#    print(dict3) 
#diccionarios({"a":5,"b":3,"c":6,"d":9,"e":1,"f":2},{"g":69,"b":20,"h":45,"d":21,"i":8,"f":22})

#4.
#dicc=[{"nombres":"Juan", "apellidos":"Tristán Merchan",
#"edad":50},{"nombres":"Andrés", "apellidos":"Arango",
#"edad":25},{"nombres":"Pedro Julio", "apellidos":"Ortega",
#"edad":101},{"nombres":"Carlos", "apellidos":"Segura",
#"edad":68},{"nombres":"David", "apellidos":"Fernandez",
#"edad":65}]
#print("Nombre y apellido:")
#for i in range(len(dicc)):
#    if dicc[i]["edad"] >= 18 and dicc[i]["edad"] <= 65:
#        print(dicc[i]["nombres"],dicc[i]["apellidos"])


#5. Dado el archivo de texto files/SalesJan2009.csv, procese el archivo para obtener las compras realizadas en un país dado. Ejemplo:
#Input: United Kingdom. Output: 100

#ruta="C:\\Users\\dmcew\\proy_programacion\\Mision_TIC\\ciclo_1\\ejercicios_basicos\\Manejo_Archivos\\files\\SalesJan2009.csv"
#atributo='Country'
#vrCountry = input('Ingrese '+ atributo +': ') # United Kingdom
#vrPayment_Type = input('Enter payment type: ') #Mastercard
#with open(ruta, "r",encoding="utf-8") as f:
#    data = f.readline() #Localiza el encabezado: Transaction_date,Product,Price,Payment_Type,Name,City,State,Country,Account_Created,Last_Login,Latitude,Longitude
#    #print(data) (muestra ese encabezado del archivo csv.)
#
#    #FORMA DE DETECTAR EN QUÉ PARTE DEL CSV SE LOCALIZA LA POSICIÓN DEL PAÍS QUE SE DESEA SOLICITAR. Country posición 7.
#    llaves = data.split(',') #data es una cadena y se convierte a lista, separado por split, delimitado por comas.
#    pos = llaves.index(atributo) #Encuentra la posición en la que se encuentra el país
#    pos1= llaves.index("Payment_Type")
#    #print(pos)
#    n1=0 #contador
#    for linea in f: #lee linea x linea
#        #print(linea) #imprime línea por línea del archivo csv.
#        vals = linea.split(',') #cada línea se convierte en una lista
#        if vrCountry == vals[pos] and vrPayment_Type == vals[pos1]: #vals es una lista (comparo cadenas) con la posición 7 donde se encuentra el País.
#            print("Nombre de personas que pagan con Mastercard y son de UK:",vals[4])
#            n1+=1 #contador
#print("Número de compras total:",n1)
#print(llaves) #Muestra el encabezado convertido en lista

#6. Dado el archivo de texto files/SalesJan2009.csv, procese el archivo para obtener las compras realizadas con un medio de pago dado.
#Ejemplo: Input: Visa: Input: 521

#path="C:\\Users\\dmcew\\proy_programacion\\Mision_TIC\\ciclo_1\\ejercicios_basicos\\Manejo_Archivos\\files\\SalesJan2009.csv"
#payment_type = input("Enter payment method: ")
#with open(path,"r",encoding="utf-8") as f:
#    bandera = False
#    header = f.readline()
#    ky = header.split(",")
#    position = ky.index("Payment_Type") #Position 3
#    counter = 0
#    for i in f: #f contiene todo el archivo. i representa cada cadena por línea
#        lista_payment = i.split(",")
#        if payment_type == lista_payment[position]:
#            #print(*lista_payment[4])
#            counter+=1
#            bandera = True
#print(counter) if bandera else print("No existe")
#Forma del profesor:
#with open(path, "r", encoding="utf-8") as f: 
#  cabecera = f.readline() #retorna una cadena
#  campos=cabecera.split(',')#retorna una lista
#  i = list(range(len(campos)))#coleccion 0, 1, 2, 3, ... len()
#  dict1 = dict([(k,v) for k, v in zip(i, campos)])
#  print(dict1)
#  pos = int(input('ingrese llave del campo deseado: '))# 3
#  atributo = str(dict1.get(pos)) #atributo='Payment_Type'
#  vrAtri = input('Ingrese '+ atributo +': ') #Visa
#  n=0
#  for linea in f: #linea va tomando una linea de f a la vez
#    val = linea.split(',') #linea, val es lista de cadenas
#    if vrAtri == val[pos]: #Comparacion de strings
#      n+=1
##ya se cerro el arch
#print('Nro de compras con ', vrAtri,'= ',n)
#

#7. Imprima los nombres completos (nombre y apellidos) de las personas que practican el deporte ingresado por el usuario.
#import json
#data="""{"jadiazcoronado":{
#        "nombres": "Juan Antonio",
#        "apellidos": "Díaz Coronado",
#        "edad":19,
#        "colombiano":true,
#        "deportes":["Fútbol","Ajedrez","Gimnasia"]
#        },
#        "dmlunasol":{
#        "nombres": "Dorotea Maritza",
#        "apellidos": "Luna Sol",
#        "edad":25,
#        "colombiano":false,
#        "deportes":["Baloncesto","Ajedrez","Gimnasia"]
#        },
#        "dmcewena":{
#        "nombres": "David McEwen",
#        "apellidos": "McEwen Arango",
#        "edad":26,
#        "colombiano":true,
#        "deportes":["Baloncesto","Ajedrez","Gimnasia"]}}"""
#
##IMPORTANTÍSIMO:

#7. Imprima los nombres completos (nombre y apellidos) de las personas que practican el deporte ingresado por el usuario.
#path="C:\\Users\\dmcew\\proy_programacion\\Mision_TIC\\ciclo_1\\ejercicios_basicos\\Manejo_Archivos\\files\\Semana5Exercise-json.json"
#with open(path, "w",encoding="utf-8") as write_file:
#    json.dump(data,write_file) #dump
#    
#    #Dumps asigna a un string y lo convierte a JSON.Se usa por fuera del with
#    #Para asignar a un string: .dumps (!= a dump)
#
#with open(path,"r",encoding="utf-8") as read_file:
#    json_string=json.load(read_file)
#    #data2=json.loads(data1) #.Load deserializa el objeto .json guardado
#    #data2=json.loads(data1)
#data1=json.loads(json_string)
#print(data1) #Deserializado el archivo, tipo . Lo convierte a Python
#print()
#print()
#
#deportes=input("Enter sport: ")
#for i in data1:
#    if deportes in data1[i].get("deportes"):
#        print(data1[i].get("nombres"),data1[i].get("apellidos"))

#ESTRATEGIA DEL PROFESOR:
#estrategia: leer cada item del diccionario dat y voy a buscar 'Futbol' entre dat[deportes]
#for kk, vv in dat.items(): #coleccion de 2 entradas y cada entrada es un dicci q tiene k, v
#a=data1.values()
##print(type(a), a)
#for vv in data1.values():
##  lis_deportes= vv['deportes']
#  lis_deportes= vv.get('deportes')
#  if deporte in lis_deportes:
#    print(vv['nombres'], vv['apellidos'])
#print('fin')
# for vv in data1.values()
# for kk in data1.keys()

#8. Imprima los nombres completos (nombre y apellidos) de las personas que esten en un rango de edades dado por el usuario.
#with open(path,"w",encoding="utf-8") as write_file:
#    json.dump(data,write_file) #El proceso de transformar datos en series de bytes para ser enviados por una red o ser guardados como archivo
##    se conoce como serializacion. Los archivos JSON se pueden serializar. La librera json expone el metodo dump() 
##    para escribir datos en un archivo. Si se tiene el siguiente diccionario
#with open(path,"r",encoding="utf-8") as read_file:
#    json_string=json.load(read_file) #El siguiente codigo carga el objeto JSON a la variable data y luego imprime uno de los registros del objeto JSON data,
#   #Se usa dentro de la indentación de with
#data1=json.loads(json_string) #Es posible cargar un archivo de JSON desde un string. En el siguiente codigo se crea un string (en dos lineas por espacio, para esto se encierra
##entre tres comillas simples '''), luego se carga el objeto JSON a la
##variable data y por ultimo esta se imprime
#
#rango = list(map(int,input("Enter range: ").split()))
#for i in data1:
#    age = data1[i].get("edad")
#    if age >= rango[0] and age <= rango[1]:
#        print(data1[i].get("nombres"),data1[i].get("apellidos"))

#Cree un JSON de deportes como sigue:
#{
#"Ajedrez":["jadiazcoronado",...,"dmlunasol"],
#"Futbol":["jadiazcoronado",...],
#"Gimnasia":["jadiazcoronado,...,"dmlunasol"],
#...
#"Baloncesto":[...,"dmlunasol"]
#}

#PENDIENTE: PEDIR CITA HOY (FORMA DIOS)
#newDict = {}
#cont=0
#newList = []
#for i in data1:
#    
#    if data1[i].get("deportes")[cont] in data1[i].get("deportes"):
#        newList.append(i)
#    
#    cont+=1
#    for j in data1[i].get("deportes"):
#        newDict.update({j:newList})
#print(newDict)
#from pprint import pprint
#
#deporte1 = {
#  "Ajedrez":["gasparov","fabioCasas"],
#  "Gimnasia":["GilbertoSerna","dmlunasol"],
#  'Natacion':['LilianaObando', 'MarthaAcevedo', 'LorenaUribe'],
#  'Tenis':['MiachaelJackson','dmcewena',"mcardona"],
#  "Ciclismo":["LinaBuitrago","Bibiana","RubielMartinez"],
#  "Boxeo":["JuanOrtega","MannyPacquiao","MikeTy"],
#  "Lol":["CamiloSaldarriaga","CristianoRonaldo","LeonelMessi"]
#}
#deporte2 = {
#  "Pingpon":['abc', 'xyz', 'pqr', 'rst'],
#  "Ajedrez":["jadiazcoronado",'fabioCasas',"dmlunasol"],
#  "Futbol":["jadiazcoronado",'RubenAmaya'],
#  "Gimnasia":['GilbertoSerna',"dmlunasol"],
#  'Ciclismo':['ALU','LinaBuitrago','Bibiana','RubielMartinez'],
#  "Baloncesto":["dmlunasol",'plo','rFrancoA','OrlandoLuna'],
#  "Lol":["CamiloSaldarriaga","CristianoRonaldo","LeonelMessi"]
#}
#
##9. Desarrolle un programa que lea dos archivos JSON, y encuentre los
##componentes clave:valor que son iguales en ambos. Genere un nuevo
##archivo JSON con las coincidencias exactas entre los dos archivos.
#path1="C:\\Users\\dmcew\\proy_programacion\\Mision_TIC\\ciclo_1\\ejercicios_basicos\\Manejo_Archivos\\files\\Semana5ExerciseDeportes1-json.json"
#path2="C:\\Users\\dmcew\\proy_programacion\\Mision_TIC\\ciclo_1\\ejercicios_basicos\\Manejo_Archivos\\files\\Semana5ExerciseDeportes2-json.json"
#def serializacion(archiv1,archiv2):
#    with open(archiv1,"w",encoding="utf-8") as wfile1, open(archiv2,"w",encoding="utf-8") as wfile2:
#        json.dump(deporte1,wfile1)
#        json.dump(deporte2,wfile2)
#def deserializacion(archivo1,archivo2):
#    with open(archivo1,"r",encoding="utf-8") as rfile1,open(archivo2,"r",encoding="utf-8") as rfile2:
#        data2=json.load(rfile1)
#        data3=json.load(rfile2)
#    return data2,data3
#def semejanzas(archivos):
#    newDict = {}
#    dicc1=archivos[0]; dicc2=archivos[1]
#    for k1 in dicc1:
#        #print(k1,"-->",dicc1[k1])
#        if k1 in dicc2 and dicc1[k1] in list(dicc2.values()):
#            newDict[k1]=dicc1[k1]  
#    serializacionResultante(newDict)
#    return newDict
#def serializacionResultante(file):
#    path3="C:\\Users\\dmcew\\proy_programacion\\Mision_TIC\\ciclo_1\\ejercicios_basicos\\Manejo_Archivos\\files\\Semana5ExerciseDeportesResultante-json.json"
#    with open(path3,"w",encoding="utf-8") as wfile1:
#        json.dump(file,wfile1)
#
#serializacion(path1,path2)
#archivos = deserializacion(path1,path2)
#pprint(archivos[0])
#print()
#pprint(archivos[1])
#print("Diccionario de semejanzas: ",semejanzas(archivos))



#10. Desarrolle un programa que lea un archivo JSON, en el cual se
#encuentran las notas de los estudiantes del curso. Cada llave
#corresponde al código de cada estudiante, y su valor es una lista con
#las notas obtenidas en las actividades del curso. Se debe generar un
#nuevo archivo JSON que para uno de los estudiantes solo guarde el
#promedio de las notas obtenidas.
#import json
#from pprint import pprint
#path1="C:\\Users\\dmcew\\proy_programacion\\Mision_TIC\\ciclo_1\\ejercicios_basicos\\Manejo_Archivos\\files\\CalificacionesJSON-semana5.json"
#notas = {
#    'David McEwen':[2.5,3.6,4.5,2.1,4.6],
#    'María Rivera':[3.5,1.0,4.6,4.5,3.0],
#    'Manuel Cely':[2.0,3.0,4.0,5.0,3.5],
#    'Juan José Acevedo':[2.5,1.5,4.0,4.1,2.9],
#    'Daniela Gómez':[3.1,3.2,2.6,4.1,4.3],
#    'Daniel Miranda':[1.0,4.0,2.5,1.3,0.9],
#    'Natalia Pérez':[1.0,2.0,3.9,1.5,2.2]
#}
#def pasoArchivoJSON(path,notas):
#    fileJSON=json.dumps(notas)
#    with open(path,"w",encoding="utf-8") as writeF:
#        json.dump(fileJSON,writeF)
#
#def loadJSON(path):
#    with open(path1,"r",encoding="utf-8") as rfile:
#        str1 = json.load(rfile)
#    notstr = json.loads(str1)
#    return notstr
#def StudentsAvg(jsonStudents):
#    newDict = {}
#    for i in jsonStudents:
#        cont=0
#        countN = len(jsonStudents[i])
#        for j in jsonStudents[i]:
#            cont+=j
#        newDict[i]=cont/countN
#    serializacionAVRG(newDict)
#    return newDict
#
#def serializacionAVRG(notes):
#    path2="C:\\Users\\dmcew\\proy_programacion\\Mision_TIC\\ciclo_1\\ejercicios_basicos\\Manejo_Archivos\\files\\Semana5ExerciseAverageStudents-json.json"
#    with open(path2,"w",encoding="utf-8") as wfile1:
#        json.dump(notes,wfile1)
#
#def main():
#    pasoArchivoJSON(path1,notas)
#    studentsDict=loadJSON(path1)
#    pprint(studentsDict)
#    pprint(StudentsAvg(studentsDict))
#main()


#11. Desarrollar un programa que lea un archivo JSON que contiene una
#serie de cadenas de carácteres en minúscula, cada una con su propia
#llave. 
#Estas llaves tienen una codificación, a forma de encriptación, en
#donde las vocales están descritas como otros símbolos: $ en vez de a,
# # en vez de e, * en vez de i, ¬ en vez de o, y + en vez de u. Una vez
#leído el archivo, realice una desencriptación de todas las cadenas, es
#decir, convierta los símbolos a sus vocales correspondientes (si la
#cadena de entrada es "h¬l$", la cadena resultante sería "hola"), y
#guarde el resultado en un nuevo archivo JSON.



#import json
#values = {"$":"a","#":"e","*":"i","¬":"o","+":"u","h¬l$":"hola"}
#cipher={'n¬mbr#':['s$r$', 'm$r*n'],'#st+d*¬s':['s*c¬l¬g*$','n+tr*c*¬n'],'#mpr#s$s':['h¬sp*t$l','cl*n*c$'],'c+mpl#$ñ¬s':['#n#r¬','01']}
#lista=[]
#for k, v in cipher.items():  #k, v son tipo string, procesa un item encriptado
#  for kq in values: #for in. leo diccio en equivalencias
#    k = k.replace(kq, values[kq]) # desencripta las claves. string.replace(oldvalue, newvalue, count)
#    for i in range(len(v)):#for mas int  ... 0, 1
#      v[i] = v[i].replace(kq,values[kq]) #desencripta valores
#  n_item =[(k, v)]
#  lista.extend(n_item)
#sali=dict(lista)
#print(sali)

#REPASAR. HECHO POR EL PROFESOR
#lista=[]
#for k, v in cipher.items():  #k, v son string type, proceso un item encriptado
#  for kq, vq in values.items(): #for in leo diccoin equivalencias
#    k = k.replace(kq, vq) # desencripta las claves 
#    for i in range(len(v)):#for mas int  ... 0, 1
#      v[i] = v[i].replace(kq,vq) #desencripta valores
#  n_item =[(k, v)]
#  lista.extend(n_item)
#sali=dict(lista)


#Importante:
#El manejo de excepciones, si se quiere uno para cada tipo de excepcion
#(opcional), tiene la siguiente forma:
#try:
  #codigo que puede generar alguna excepcion a manejar
#except Exception_name1: # Primer tipo de excepcion
  #codigo que maneja la excepcion Exception_name1
#except Exception_name2: # Segundo tipo de excepcion (opcional)
  #codigo que maneja la excepcion Exception_name2
#...
#except Exception_nameN: # N-esimo tipo de excepcion (opcional)
  #codigo que maneja la excepcion Exception_nameN
#else: #opcional
  #codigo extra por si no se presenta una excepcion
#finally:
  #Codigo que se ejecuta al final sí o sí


#try => except => else => finally
#try:
#  num = int(input("Ingrese un numero "))
#  re = 100/num
#except:
#  print("Algo esta mal")
#else:
#  print("El resultado es ",re)
#finally:
#  print("El programa termina!")

#12. Capture la excepcion que evita que el usuario acceda a posiciones que
#no se encuentran detenidas en la lista dada y muestre el mensaje
#Intenta acceder una posicion que no esta en el arreglo:
#lista = [1, 2, 3, 4]
#try:
#  lista[5]
##Capture one type of exception
#except Exception as e: #This say the exception type without commit it
#  print(e, "\n","Catch error type", type(e))
#Si se ejecuta sin el manejo de la excepción se produce la siguiente
#salida:
#IndexError Traceback (most recent call last)
#<ipython-input-42-64245f71fd49> in <module>
#1 lista = [1, 2, 3, 4]
#----> 2 lista[5]
#IndexError: list index out of range

#Capture la excepción para evitar que un programador sume una
#cadena de texto a un número y muestre el mensaje
#Los tipos de datos no cuadran para hacer la operación:
#def operar(a, b):
#  return a+b
#def main():
#      try:
#        a = int(input())
#        b = 'hola'
#      except Exception as e:
#        print(e, type(e))
#      except ValueError:
#        print("B parameter is not a real number")
#      else:
#        operar(a, b)
#main()

#13. 
#Capture la excepcion cuando se trata de obtener una llave que no se
#encuentra en un diccionario y muestre el mensaje
#Intenta acceder una llave que no esta en el diccionario:

#def main():
#      try:
#        dict = {'James': 'Java', 'Dennis' : 'C', 'Das':'Python'}
#        print(dict['Ada'])
#      except Exception as e: #KeyError
#        print(e,"type:", type(e))
#main()
#SI NO SÉ QUÉ TIPO DE ERROR USAR, LO PUEDO ATRAPAR CON EL CÓDIGO DE ARRIBA














