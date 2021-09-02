#def reverse(num):
#    reverse=0
#    bandera = True
#    while bandera: 
#        reverse=reverse*10+num%10
#        num=num//10
#        if num == 0: bandera = False
#    return reverse
#print(reverse(123456))


#Forma recursiva:
#def reverse(num, rever=0): #Rever guarda el último dígito
#    print(type(num))
#    if num==0:
#        return rever
#    else:
#        return reverse(num//10, rever*10 + num%10)
#
#print(reverse(123456))

#1.Piense que está bien para que esté bien.
#2. Siempre se es el primero y el último.
#3. Un problema es simple o se puede dividir en problemas que se pueden solucionar siguiendo las tres máximas del profesor Jonatan Gómez.



#def sumar_parcial(L,n):
#    if n > 0:
#        return L[n-1] + sumar_parcial(L,n-1) #sumar_parcial lo único que hace es rellamar la función las veces que represente la longitud de la lista. Hasta l
#        #L[n-1] suma la última posición con la posición n-1
#        #return L[n-1] + sumar_parcial(L,n-1) 
#    else:
#        return 0
#def sumar_lista(L):
#    return sumar_parcial(L,len(L))
#print(sumar_lista([1,2,3,4,5,6,7,8,9]))


#Diseñe un modelo matemático que permita calcular la funcion producto,
#es decir, que reciba dos (2) numeros naturales y retorne la multiplicacion
#del primer numero por el segundo.
#No se pueden utilizar los operadores de multiplicacion ni de division (ni
#entera ni real).
#Codifique el modelo matematico utilizando el lenguaje Python.


#Una función f : A ! B se dice recursiva si y sólo si f está definida por
#casos (mediante un predicado sobre los argumentos), en donde al menos
#uno de los casos se define usando la misma función f y los argumentos, y
#al menos uno de los otros casos se define usando solamente los
#argumentos sin involucrar la función f .
#Aquellos casos en los cuales se invoca a la misma funcion se llaman casos
#recursivos, y aquellos casos en los cuales no interviene la funcion se
#denominan casos base.
#Nota:
#def producto(m,n):
#    if n==0:
#        return 0
#    else:
#       return m + producto(m,n-1)
#        
#print(producto(8,5))
#
#
#def buscar_parcial(str,ch,n):
#    if n > 0:
#        return (str[n-1] == ch) or buscar_parcial(str,ch,n-1)
#    else:
#        return False
#def buscar(str,ch):
#    return buscar_parcial(str,ch,len(str))
#print(buscar("erase una vez","z"))

#Suma
#def h(n,m):
#    if m == 0:
#        return n
#    else:
#        return h(n+1,m-1)
#
#print(h(5,6))


#def fibo(n):
#    if n == 0:
#        return 0
#    elif n == 1:
#        return 1
#    return fibo(n - 1) + fibo(n - 2)
#print(fibo(12))
