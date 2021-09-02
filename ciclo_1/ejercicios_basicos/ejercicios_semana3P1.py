#1. Desarrollar un programa que imprima el cuadrado del numero que el
#usuario ingresa mientras que el numero ingresado no sea negativo.

#2 Desarrollar un programa que dado un numero entero positivo n
#calcule e imprima (separados por espacios) n=2//2 si es par o 3n +1 si es
#impar. El programa debe repetir el proceso con el numero resultado
#de dicha operacion mientras este sea diferente de 1. Por ejemplo para
#el numero 3 debe imprimir 10 5 16 8 4 2 1.

#3 En 2022 el paíss A tendría una población de 25 millones de habitantes
#y el país B de 18.9 millones. Las tasas de crecimiento anual de la
#población serán de 2% y 3% respectivamente. Desarrollar un
#programa que imprima el a~no en que la poblacion del pas B superara
#a la de A.
#J.

#Diseñar una funcion que permita calcular el epsilon de la maquina. El
#epsilon de maquina es el numero decimal mas peque~no que sumado
#a 1 se puede representar de manera precisa en la maquina (que no es
#redondeado), es decir, retorna un valor diferente de 1, este da una idea
#de la precision o numero de cifras reales que pueden ser almacenadas
#en la maquina. La idea es realizar un ciclo en el cual se realiza la
#operacion 1 +  para potencias de 2 desde  = 20 y continuando con
#potencias decrecientes de 2
#􀀀
# = 2􀀀1;  = 2􀀀2;  = 2􀀀3;  = 2􀀀4; : : :
#
#hasta obtener que el resultado de la suma 1 +  no se altere.

#1.
#cuadrado = int(input("Ingrese un número natural: "))
#while cuadrado >= 0:
#    print(cuadrado, "al cuadrado es:", cuadrado**2)
#    cuadrado = int(input("Ingrese un número natural: "))
#print("Número negativo")


#2. 
#def numeroPositivo(N):
#    lista=[]
#    n=N
#    while n != 1:
#        if n%2==0:
#            n=n//2
#        else: 
#            n=3*n+1
#        lista.append(n)
#    return lista
#N=int(input("Ingresa un número: "))
#for i in numeroPositivo(N):
#    print(i,end=" ")

#i=0
#b=18e6
#a=25e6
#while a > b:
#    a+=a*0.02
#    b+=b*0.03
#    i+=1
#print(i-1,"años.","Valor poblacional actual a:",a,"; valor poblacional actual b",b)

#5.
#def numeroMinimo():
#    Xo=1.0
#    Xi= Xo/2.0
#    while Xi>0:
#        Xo = Xi
#        Xi = Xo / 2.0
#    return Xo
#print("El m ́ınimo n ́umero positivo", end = " ")
#print("en esta m ́aquina es:", numeroMinimo())


#1.Imprimir un listado con los numeros del 1 al 100 cada uno con su
#respectivo cuadrado.
#
#2. Imprimir un listado con los numeros impares desde 1 hasta 999 y
#seguidamente otro listado con los numeros pares desde 2 hasta 1000.
#
#3. Imprimir los numeros pares en forma descendente hasta 2 que son
#menores o iguales a un numero natural n  2 dado.
#
#4. Imprimir los numeros de 1 hasta un numero natural n dado, cada uno
#con su respectivo factorial.
#
#5. Calcular el valor de 2 elevado a la potencia n.
#
#6. Leer un numero natural n, leer otro dato de tipo real x y calcular xn.
#
#7. Dise~ne un programa que muestre las tablas de multiplicar del 1 al 9.

#1. 
#n=100
#for i in range(n+1):
#    print(i, "elevado al cuadrado es:",i**2)

#2.
#for i in range(1,1000,2):
#    print("Impar:",i)
#print("Parte 2")
#for d in range(2,1001,2):
#    print("Par:",d)

#3. FORMA HECHA POR MÍ
#n=int(input("Ingresa un número: "))
#for i in range(n,1,-1):
#    if i % 2 == 0:
#        print(i,end=" ")
#print()  
##Hecha por el profesor
##n=15
##vs: npp    (numero par prox   14)
#if n % 2 !=0: # significa que n es impar; halla en numero impar <= n
#  npp = n-1
#else:  #n es par
#  npp=n #inicialice npp
#
#for i in range(npp, 1, -2):
#  print(i, end=' ')

#4.
#def factorial(n):
#    x=1
#    for i in range(1,n+1):
#        x*=i
#    return x
#
#n = int(input("Ingrese un número: "))
#for i in range(1,n+1):
#    print(i,"factorial de:",factorial(i))

#5. 
#def elevado(n):
#    producto=1
#    for i in range(1,n+1):
#        producto*=2
#    return producto
#
#n=8
#print("2 elevado a la", n,"es",elevado(n))
#def elevado(n):
#    return 2**n
#
#n=8
#print("2 elevado a la", n,"es",elevado(n))


#for i in range(1,10):
#    print(i,":",end="")
#    for j in range(1,10):
#        prod= i*j
#        print("\t",prod,end="")
#    print()

#Disenar una funcion que permita calcular una aproximacion de la
#funcion exponencial alrededor de 0 para cualquier valor x E R,
#utilizando los primeros n terminos de la serie de Maclaurin
from math import pi
def factorial(n):
    x=1
    for i in range(1,n+1):
        x*=i
    return x


def McLaurin(x,n):
    acum=0.0
    sig=1.
    for i in range(n+1):
        num=x**(2*i+1)
        den=factorial(2*i+1)
        ter=sig*num/den
        acum += ter
        sig=sig*(-1)
    return acum

angulo = float(input("Seno: Ingrese ángulo en grados y punto: "))
rad = angulo*pi/180.
res=McLaurin(rad,10)
print(res)

#ESTO DE SUCESIONES ME QUEDA PENDIENTE