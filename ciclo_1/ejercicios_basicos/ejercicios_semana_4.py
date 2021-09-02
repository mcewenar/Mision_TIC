#1 Desarrollar un programa que determine si en una lista no existen
#elementos repetidos.
#2 Desarrollar un programa que determine si un elemento de una lista es
#una cadena palndrome. Si la cadena existe debe imprimirla y si no
#existe debe imprimir 'No existe'.
#3 Desarrollar un programa que determine si en una lista se encuentra
#una cadena de caracteres con dos o mas vocales. Si la cadena existe
#debe imprimirla y si no existe debe imprimir 'No existe'.
#4 Desarrollar un programa que determine si una lista es palndrome.
#Una lista es palndrome si el elemento en la posicion i es el mismo de
#la posicion n 􀀀 1 􀀀 i con n la longitud de la lista.

#1.
#def lista_repetida(x):
#    for i in x:
#        
#        if x.count(i) != 1:
#            return "La lista tiene elementos repetidos"
#    return "No tiene elementos repetidos"

#print(lista_repetida([x for x in input("Ingrese el arreglo de carácteres con espacios: ").split()])) #Genera un arreglo de carácteres separados por espacios
#print(lista_repetida(['a', 'g','b','r','e','i','u','c','t','y',"c",'d']))
#def sinRepetidos(lista1):
#      #VE:lista1
#  #VS: bandera: bool
#  nn=len(lista1)
#  print(nn)
#  bandera=True #No existen elementos repetidos; for i es el for externo
#  for i in range(nn): #i es un elemento de la coleccion generada con range, (0, 1, 2, 3, ..nn-2)
#    #print(i,end="")
#    llave = lista1[i] #llave='a', 'g', b,r, ..c,
#    for j in range(i+1,nn): #for interno, hay 2 for anidados Coleccion j=(1, 2, 3, ... nn-1)
#      if lista1[j] == llave:
#        bandera = False
#        break
#  return bandera
#
#lis=['a', 'g','b','r','e','i','u','c','t','y','d',"d"]
#res=sinRepetidos(lis)
#print(res)

#2. 
#Forma rápida:
#metodo replace(old, new, n) sobre cadenas
#ca='aldkfgsj rkdfbdsxscs'
##n: reemplazar n ocurrencias de 's'
#cb=ca.replace('s', '#', 1)
#print(cb)
#a=ca[6];print(a)
#ca[6]='#'

#def esPalindrome(palabra):
#  NN = len(palabra)   
#  long2 = NN // 2  
#  izq = palabra[0:long2] #slice o rebanada, exclueye la pos [long2]
#  der1 = palabra[long2:NN] if NN % 2 == 0 else palabra[long2+1:NN]
#  der = der1[::-1] # reversa el lado derecho
#  res:bool = der == izq  #compara ambas en orden lexicografico
#  return res 
##print(math.ceil(3.2))
#def cadena_palindrome(x):
#  flag = False
#  for frase in x:
#    res = esPalindrome(frase)
#    if res:
#      return "Es palíndrome"
#      flag=True
#  if not flag:
#    return 'No es palíndrome'
#  
#print(cadena_palindrome(["amor a roma","anita atina","al sur de Colombia","anula las alas a la luna", \
#"anulal a sala sal aluna","la tele letal"]))
#lista=["amor a roma","anita atina","al sur de Colombia","anula las alas a la luna", \
#"anulal a sala sal aluna","la tele letal"]
#for frase in lista: #frase es una cadena
#  res=esPalindrome(frase)
#  print(frase,'\t',res)

#3.
#def lista_cadena(frase):
#  vocales = ["a","e","i","o","u"]
#  n=0
#  for vocal in vocales:
#    n+=frase.count(vocal)
#  if n>=2:
#    return frase
#  else:
#    return 'No existe'
#      
#lista = ["amor a roma","anita atina","al sur de Colombia",'p@ssw0rd',"anula las alas a la luna", \
#"anulal a sala sal aluna","la tele letal",'@nit@']
#for i in lista:       
#  print(lista_cadena(i))

#4.

#def lista_palindrome(lista):
#  flag = True
#  N=len(lista)
#  ini = 0; fin = N//2; inc = 1
#  for i in range(ini,fin,inc):
#    if lista[i] != lista[N-1-i]:
#      flag = False
#  return flag
#
#
#print(lista_palindrome(['anita', 'luis', 'hugo', 'hugo', 'luis', 'anita']))
#print(lista_palindrome(['anita', 'luis', 'hugo','paco', 'hugo', 'luis', 'anita']))
#print(lista_palindrome(['anita', 'luis', 'hugo','paco', 'carl', 'luis', 'anita']))



#5. Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista.
#Ejemplo:
#lista1: [1, Hola,-12,True]
#lista2: [11,12,3, Hola0; False]
#salida: [1;True]
#lista1=[1,2,"hola",-12.3,True]
#lista2 = [11,-12.3,"hola",False,"pera"]
#lista3=[]
#for i in lista1:
#  if i not in lista2:
#    lista3.append(i)
#print(lista3)


#6. Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.
#sumatoria = [float(x) for x in input("Arreglo: ").split()]
#print(sum(sumatoria)/len(sumatoria))

#7. Desarrollar un algoritmo que calcule el producto punto de dos arreglos
#de numeros enteros (reales) de igual tama~no. Sean
#v = [v0, v1, ... , vn􀀀1] y w = [w0,w1, . . . ,wn1] dos arreglos, el
#producto de v y w (notado v * w) es el numero:
#v0 * w0 + v1 * w1 + ... + vn1 * wn1.

#lista1 = [2,2,2,2,2]
#lista2 = [3,3,3,3,3]
#producto_punto=0
#for i in lista1:
#    producto_punto+=(lista1[i]*lista2[i])
#print(producto_punto)

#8. Desarrollar un algoritmo que calcule el producto directo de dos arreglos de números reales de igual tamaño. Sean
#v = [v0, v1, . . . , vn-1] y w = [w0,w1, . . . ,wn-1] dos arreglos, el producto directo de v y w (notado v * w) es el vector:
#[v0 * w0, v1 * w1, . . . , vn-1 * wn-1].
#lista1 = [2,2,2,2,2]
#lista2 = [3,3,3,3,3]
#lista3=[]
#producto_punto=0
#for i in lista1:
#    producto_punto=lista1[i]*lista2[i]
#    lista3.append(producto_punto)
#print(lista3)

#Truco:
#dict1 = {"a":"apple","b":"ball","c":"Cat"}
#dict2 = {"c":"Cow","d":"Dog","e":"Elephant"}
#dict3 = {**dict1,**dict2}
#print(dict3)

#9.
#Desarrollar un algoritmo que determine la mediana de un arreglo de
#enteros. La mediana es el numero que queda en la mitad del arreglo
#despues de ser ordenado.


#from math import floor,ceil
#def ordenamiento(lista_arreglo: list):
#    nn=len(lista_arreglo)
#    for i in range(nn-1): # escojo un elemento a la vez y comparo contra los elementos restantes
#        for j in range(i+1,nn):
#            if lista_arreglo[i] > lista_arreglo[j]: # intercambia elementos
#                tem=lista_arreglo[i]
#                lista_arreglo[i]=lista_arreglo[j]
#                lista_arreglo[j]=tem
#    return lista_arreglo
#
#def mediana(A):
#    a: list = ordenamiento(A)
#    print("Lista organizada:",a)
#    if len(a)%2==0:
#        n2=floor(len(a)/2) #Redondea el número menor
#        return (a[n2-1]+a[n2])/2
#    else:
#        return a[ceil(len(a)/2)]
#def main():
#    print("Mediana:",mediana([float(x) for x in input("Arreglo: ").split()]))
#main()
#
##Formas beta:
#print(type(lista_arreglo))
    #for i in range(len(lista_arreglo) - 1): # necesitamos (5 - 1) comparaciones. Empieza con 0
    #    if lista_arreglo[i] > lista_arreglo[i + 1]: # compara elementos adyacentes
    #        lista_arreglo[i], lista_arreglo[i + 1] = lista_arreglo[i + 1], lista_arreglo[i] # si terminamos aquí significa que tenemos que intercambiar los elementos.
    #    elif lista_arreglo[i] == lista_arreglo[i + 1]:
    #        continue
    
    #for i in range(len(lista_arreglo)-1):
    #    if lista_arreglo[i]>lista_arreglo[i+1]:
    #        temp=lista_arreglo[i]
    #        lista_arreglo[i+1]=temp
    #    #print(arreglo)
    ##print("{0} - ok".format(arreglo))

#10. Hacer un algoritmo que deje al nal de un arreglo de numeros todos
#los ceros que aparezcan en dicho arreglo.

#vector original: [1, 6, 0, 7,-3, 8, 0,-2, 11]
#vector salida: [1; 6; 7;􀀀3; 8;􀀀2; 11; 0; 0]
#Ejemplo
#vector original: [0; 11; 36; 10; 0; 17;􀀀23; 81; 0; 0; 12; 11; 0]
#vector salida: [11; 36; 10; 17;􀀀23; 81; 12; 11; 0; 0; 0; 0; 0]

#def matrizCero(lista_arreglo: list):
#    #nn=len(A) #9
#    #llave=0
#    #for i in range(nn):
#    #   if A[i] == llave:
#    #       n=nn-1
#    #       for j in range(i,n):
#    #           A[j]=A[j+1]
#    #       A[n]=llave
#    #return A
#    print(lista_arreglo)
#    nn=len(lista_arreglo) #9
#    for i in range(nn):
#        if lista_arreglo[i] == 0:
#            lista_arreglo.pop(i)
#            lista_arreglo.append(0)
#    return lista_arreglo
#print("Matriz final:",matrizCero([int(x) for x in input("Arreglo: ").split()]))

#11. Desarrollar un algoritmo que permita sumar dos matrices de numeros reales (enteros).
#def sumat(A,B):
#  #VE: A , B
#  nfa=len(A); nca=len(A[0])
#  nfb=len(B); ncb=len(B[0])
#  C=[] # VS: C tamaño nfa x nca
#  if nfa == nfb and nca == ncb:
#    for i in range(nfa): #for ext  coleccion: 0, 1
#      fila = [] #[2, -6, 4]
#      nca = len(A[i])
#      for j in range(nca): #for int   for anidados, coleccion: 0, 1, 2
#        fila.append(A[i][j] + B[i][j])
#      C.append(fila)
#    return C
#  else:
#    print('error: las matrices deberian ser compatibles para la suma')
#    return -1
#A=[[1,-3, 2,4,6,3,7,12,3,7],[4,11,-1,2,23,12,16,56,11,34]] #tamaño 2 x 3
#B=[[1,-3, 2,12,34,56,33,11,33,45],[4,11,-1,32,23,11,45,55,33,17]]
#print(sumat(A,B))

#12. Desarrollar un algoritmo que permita multiplicar dos matrices de números reales (enteros).
#def multiplicarM(X:list,Y:list):
#  nfx=len(X)
#  ncx=len(X[0])
#  nfy=len(Y)
#  ncy=len(Y[0])
#  a=[]
#  for f in range(nfx):
#    a.append([])
#    for c in range(ncy):
#      a[f].append([])
#  res=[]
#  compatibilidad = ncx == nfy
#  if compatibilidad:
#    for i in range(nfx):  # tres for anidados
#    # itera a traves de las columnas de Y , un cambio de i es un cambio de fila anclo la posicion de una fila y recorro cols
#      for j in range(ncy):
#        # itera a traves de las filas de Y, recorro cols
#        for k in range(nfy): #coleccion: 0, 1, ...nfy
#            #res[i][j] += X[i][k] * Y[k][j]
#            pass
#    return res
#  else:
#   return "Matriz incompatible"

#FORMA DEL PROFESOR:
#PV2-multiplicar dos matrices de numeros reales
#ef promat(X,Y): # Tamaño X:  3 x 3       Y:  3 x 4
# res es 3x4          res[i][j] = res[i][j]+    X[i][k] * Y[k][j], para k: desde 0:ncx
# res   = [[0,0,0,0],
#         [0,0,0,0],
#         [0,0,0,0]]      # tamaño 3 x 4, append() para tener un progr generico
# itera a traves de las filas de X
#precondiciones = nca == nfb
# nfx=len(X); ncx=len(X[0])
# nfy=len(Y); ncy=len(Y[0])
# precondicion= ncx ==nfy 
# if precondicion:
#  for i in range(len(X)):  # tres for anidados
#   # itera a traves de las columnas de Y , un cambio de i es un cambio de fila anclo la posicion de una fila y recorro cols
#   for j in range(len(Y[0])):
#       # itera a traves de las filas de Y, recorro cols
#       for k in range(len(Y)): #coleccion: 0, 1, ...nfy
#           res[i][j] += X[i][k] * Y[k][j]
#  return res
# else:
#  print('error: las matrices deben ser compatibles para le producto')
#  return res
## 3x3 matriz
#A = [[12,7,3], #premultiplicando
#    [4 ,5,6],
#    [7 ,8,9]]
## 3x4 matriz       
#B = [[5,8,1,2],  #posmultiplicador
#    [6,7,3,0],
#    [4,5,9,1]]
#res=promat(A,B)  #res[0][0]=12 x 5 + 7 * 6 + 2*4
##print(res)
#for r in res:
#   print(r)
##12 * 5 + 7 * 6 + 3*4
#12 * 8 + 7*7+3*5

#A=[[1,-3, 2,4]] #tamaño 1 x 4
#B=[[1,-3, 2,12,34,56,33,11,33,45], #tamaño 4 x 10
#[4,11,-1,32,23,11,45,55,33,17],
#[3,6,33,5,7,9,33,57,99,22],
#[1,-3, 2,12,34,56,33,11,33,45]]
#print(multiplicarM(A,B))

#13 Desarrollar un programa que sume los elementos de una columna dada de una matriz.
#A=[[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18]]
#mfa=len(A)
#mca=len(A[0])
#result=0
#for i in range(len(A)):
#    print(A[i])
#columnas=int(input("Ingrese las filas: "))
#ColumnasM=columnas-1
#if ColumnasM <= mca and ColumnasM >= 0:
#    for i in range(mfa): #filas 0,1,2
#        result+= A[i][ColumnasM]
#    print(result)
#else:
#    print("Fuera de rango")


#14 Desarrollar un programa que sume los elementos de una fila dada de una matriz.
#A=[[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18]]
#mfa=len(A[0])
#
#result=0
#for i in range(len(A)):
#    print(A[i])
#filas=int(input("Ingrese las filas: "))
#filasM=filas-1
#if filasM <= mfa and filasM >= 0:
#    for i in range(mfa): #filas 0,1,2
#        result+= A[filasM][i]
#    print(result)
#else:
#    print("Fuera de rango")


#15. Desarrollar un algoritmo que determine si una matriz es mágica. Se dice que una matriz cuadrada es mágica si la suma de cada una de
#sus filas, de cada una de sus columnas y de cada diagonal, es igual.

A=[[1,2,3,4,5,6],
  [7,8,9,10,11,12],
  [13,14,15,16,17,18],
  [19,20,21,22,23,24],
  [25,26,27,28,29,30],
  [31,32,33,34,35,36]
]
nf=len(A)
nc=len(A[0])
for i in range(len(A)):
    print(A[i])
mc = nf == nc
if not mc:
    print('numero de filas: ',nf,' ;numero de columnas: ', nc)
    print('La matriz no es cuadrada')
else:
    #Diagonales:
    sumaDiaIzq=0
    sumaDiaDer=0
    for i in range(nf):
        sumaDiaDer+=A[i][i]
        sumaDiaIzq+=A[i][nf-i-1]
        sf=0
    #Suma filas
    for f in range(nf):
        for c in range(nc):
            sf+=A[f][c]
    sf=sf/nf
    #suma por columnas
    sc=0
    for i in range(nf):
        for j in range(nc):
            sc+=A[j][i]
    sc/=nc
    if sumaDiaDer != sumaDiaIzq or sc != sumaDiaIzq or sf != sumaDiaDer:
        print('la matriz no es magica')
    else:
        print("Izq:",sumaDiaIzq,"Der:",sumaDiaDer,". Suma de diagonales iguales.")
        print('la matriz es magica')
        

    
    







