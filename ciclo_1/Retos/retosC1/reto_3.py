#Una tienda de celulares, va a determinar el modelo estrella, definido como aquel que se vende más veces de forma 
#seguida en un período de una semana. Para el efecto identifican con un número de un solo dígito, a 10 modelos preferidos. 
#En el sistema se registra el número que identifica a los modelos que se ha vendido, y en el orden que ocurren 
#(los números quedan separados por un espacio en blanco).
#
#Su tarea es hacer el programa para el conteo de modelos vendidos, es decir, muestre en un renglón los datos de la entrada, 
#separados por un espacio (cuando un modelo se vende varias veces en forma seguida, se muestra el número del modelo una sola vez) 
#y en el segundo renglón muestre el número de veces seguidas que ocurrieron las ventas de ese modelo.

#Entrada: 4 4 0 4 5 5 5 7
#Salida:  4 0 4 5 7
#         2 1 1 3 1
#ant=""
#n=1
#lista2=[]
#lista1=[]
#lista_sep = input("Ingrese lista separada por espacios: ").split()
#for act in lista_sep:
#    if act == ant:
#        n+=1
#        lista2.pop()
#        lista2.append(n)
#    else:
#        n=1
#        lista1.append(act)
#        lista2.append(n)
#    ant=act
#print(*lista1,sep=" ")
#print(*lista2,sep=" ")
##Forma larga de impresión:
#for j in lista1:
#    print(j,end=" ")
#print()
#for i in lista2:
#    print(i,end=" ")

#Forma abreviada: 
#print(*lista)


#Otra forma:
#entrada = input('')
#listaString = entrada.split()
#
#numeros= [int(x) for x in listaString] 
#
#noRepetidos=numeros.copy()
#
#def elminirDuplicados(x: list)-> None:
#  i:int =0
#  for _ in range(len(x)-1):
#    if x[i]==x[i+1]:
#        del x[i]
#    else:
#      i+=1
#  
#print("Antes:",noRepetidos)
#elminirDuplicados(noRepetidos) 
#print("Después:",noRepetidos)
#
#for i in noRepetidos:
#  print(i, end=" ")
#
#
#print("")
#contador=0
#aux = numeros[0]
#
#for i in range(len(numeros)):
#  if aux == numeros[i]:
#    contador+=1
#
#  else:    
#    print(contador, end=" ")
#    contador=1
#    aux=numeros[i]
##
#
#
#if aux==numeros[len(numeros)-1]:
#      print(contador, end=" ")
#
#
#
#
#
##VERSION MANUEL 1
#lista_llamadas = input("ingrese lista: ").split(" ")
#M = 0 
#H = 0
#anterior = ""
#LIST_MH = []
#LIST_VARMH = []
#for i in range(len(lista_llamadas)):
#    var = lista_llamadas[i]
#    if var ==  anterior and anterior == "M":
#        M+=1
#    elif var == anterior and anterior == "H":
#        H+=1
#    elif var == "H"  : 
#        LIST_VARMH.append(str(M))
#        LIST_MH.append("H")
#        H = 1 
#    elif var == "M" :
#        LIST_VARMH.append(str(H))
#        LIST_MH.append("M")
#        M = 1
#    if i+1== len(lista_llamadas) and var == "H": 
#        LIST_VARMH.append(str(H))
#    elif  i+1== len(lista_llamadas) and var == "M":
#        LIST_VARMH.append(str(M))
#    anterior = var
#
#LIST_VARMH.pop(0)
#print(" ".join(LIST_MH))
#print(" ".join(LIST_VARMH))
#
#
## VERSION MANUEL 2 
#lista_llamadas = input("ingrese lista: ").split(" ")
#lista_llamadas.append("")
#anterior, M = "",0
#LIST_MH,LIST_VARMH = [],[]
#for i in range(len(lista_llamadas)):
#    var = lista_llamadas[i]
#    if var!=anterior:
#        LIST_VARMH.append(str(M))
#        LIST_MH.append(var)
#        M=1
#    else: M+=1
#    anterior = var  
#LIST_VARMH.pop(0)
#LIST_MH.pop()
#print(" ".join(LIST_MH) + "\n" +  " ".join(LIST_VARMH))
#
#
#
#
# #VERSION 3
#resultado = []
#producto = input()
#producto = producto.split()
#bandera = True
#i = 0
#contador = 1
#lista = []
#while bandera:
#    if i + 1 == len(producto):
#        bandera = False
#        lista.append(producto[i])
#        resultado.append(contador)
#    elif producto[i] == producto[i+1]:
#        i += 1  
#        contador += 1
#    else:
#        lista.append(producto[i])
#        resultado.append(contador)
#        contador = 1
#        i += 1
#print(lista)
#print(resultado)
#
#
#
#
#
## VERSION 4
#cadena = input("ingrese cadena: ")
#instrucciones =[]
#apariciones =[]
#reff=cadena[0]
#cont=0
#instrucciones.append(reff)
#for i in range(len(cadena)):
#    if(cadena[i] != " "):
#        if(cadena[i]==reff):cont+=1
#        else:
#            reff=cadena[i]
#            instrucciones.append(reff)
#            apariciones.append(str(cont))
#            cont=1
#apariciones.append(str(cont))
#print(' '.join(instrucciones))
#print(' '.join(apariciones))

