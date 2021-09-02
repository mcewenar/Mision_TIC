#1.Dado un numero entero, determinar si ese numero corresponde al
#codigo ASCII de una vocal minuscula. Ayuda: utilice la funcion
#chr(<numero>) de Python que retorna el caracter ASCII
#correspondiente al numero entero en el cual se evalue la funcion.
#2. Dada una cadena de longitud 1, determine si el codigo ASCII de
#primera letra de la cadena es par o no. Ayuda: utilice la funcion
#ord(<caracter>) de Python que retorna el codigo ASCII de una
#cadena de longitud 1.
#3. Dado un caracter, construya un programa en Python para determinar
#si el caracter es un dgito o no.

#4. Dado un numero real x, construya una funcion que permita
#determinar si el numero es positivo, negativo o cero. Para cada caso
#de debe imprimir el texto que se especica a continuacion:
#Positivo: \El numero x es positivo"
#Negativo: \El numero x es negativo"
#Cero (0): \El numero x es el neutro para la suma"
#5. Dado el centro y el radio de un círculo, determinar si un punto de R2
#pertenece o no al interior del círculo.
#6. Dadas tres longitudes positivas, determinar si con esas longitudes se
#puede construir un triangulo.

#Resolución:

#1. 

#def ascii(x):
#    return chr(x)
#while True:
#    while True:
#        try:
#            num = int(input("Ingrese un número del 97 al 122, o 241: "))
#            break
#        except ValueError:
#            print("Dato errado")
#    if (num >= 97 and num <=122) or num==241:
#        print(ascii(num))
#        print("Fue un placer")
#        cont = input("¿Desea continuar? ")
#        if cont == "sí" or cont == "si":
#            continue
#        elif cont=="no" or cont == "No":
#            print("Hasta luego")
#            break
#        else:
#            print("Dato erróneo")
#    else:
#        print("fuera de rango. Inténtalo nuevamente")

#print("-------2--------")

#def codasci(codigo):
#    return ord(codigo)
#
#
#def par_impar(x):
#    num=codasci(x)
#    if num % 2 == 0:
#        return "Es par"
#    else:
#        return "es impar"
#
#while True:
#    num = input("Ingrese un caracter: ")
#    if len(num) != 1:
#        print("Número con carácteres inadecuado")
#    else: 
#        print(par_impar(num))
#        print("Inténtalo nuevamente")

#print("-------3-------")

#def esDigit(x):
#    if len(x) == 1:
#        if ord(x) >= 48 and ord(x) <= 57: #if x.isnumeric():
#            return "Es un dígito"
#        else:
#            return "No es un dígito"
#    else:
#        return "String fuera de rango"
#print(esDigit(input("Ingrese un dato: ")))




#4.
#print("---------4---------")
#def numero_real(x):
#    if x >0:
#        return "Positivo: \El número " + str(x) + " es positivo."
#    elif x<0:   
#        return "Negativo: \El número " + str(x) + " es negativo."
#    else: 
#        return "Cero (0): \El número " + str(x) + " es el neutro para la suma."
#
#print(numero_real(-5))
#print(numero_real(79))
#print(numero_real(0))

#print("-----5-----")
#def PuntoCirculo(x,y):
    #(x-h)**2 + (y-k)**2 = r**2
    #c(h,k)=c(5,-3). r=5
#    if (x-4)**2 + (y-2)**2 == 9**2:
#        return "Pertenece al círculo"
#    else:
#        return "No pertenece al círculo"
#print(PuntoCirculo(float(input("Ingresa punto x: ")),float(input("Ingresa punto y: "))))

#print("----6----")

#def triangulo(a,b,c):
#    return "Se puede construir un triángulo" if a+b > c and  a + c > b and b + c > a else "No se puede construir un triángulo"

#print(triangulo(float(input("Ingrese lado a: ")),float(input("Ingrese lado b: ")),float(input("Ingrese lado c: "))))

#print("-----Reto ajeno-----")
#j1=0
#j2=0
#while True:
#    x=True
#    jugador1 = input("Ingrese la lista de carácteres1: ")
#    jugador2 = input("Ingrese la lista de carácteres2: ")
#    for d in list(jugador1): 
#        for t in list(jugador2):
#            if ord(t) in range(48,58) or ord(d) in range(48,58): #isnumeric() soluciona el chorrero de código
#                x=False
#    if x==False:
#        print("No se permiten números. Inténtalo de nuevo")
#    elif jugador1.isupper() and jugador2.isupper():
#        maquina = input("Ingrese los valores de juego: ")
#        for j in list(maquina):
#            if ord(j) in range(48,58):
#                print("No se permiten números. Inténtalo de nuevo")
#                break
#        if maquina.isupper():
#            for i in maquina:
#                if jugador1.find(i) != -1:
#                    j1+=1
#                if jugador2.find(i) != -1:
#                    j2+=1
#    
#                if j1 > j2:
#                    print("P",end="")
#                elif j1 < j2:
#                    print("S",end="")
#                elif j1==j2:
#                    print("E",end="")
#            print()
#        else:
#            print("No se permite ingresar minúsculas. Inténtelo de nuevo")
#    else:
#        print("No se permite ingresar minúsculas. Inténtelo de nuevo")
#       
            

#Entrada 1:
#HBKM
#MFZK
#EOBZYFYUFRRCHGO
#Salida1: EEPEESSSSSSSSSS

#Entrada 2:
#J1: NFWRK
#J2: BCROF
#Máquina: UYZSKFCMOMWFPHREVKTPDRJ
#Salida1: EEEEPPEESSEEEEEEEPPPPPP
