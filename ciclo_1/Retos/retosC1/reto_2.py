#Reto 2: Grupo P21
#Disponible desde: Monday, 14 de June de 2021, 00:00
#Número máximo de ficheros: 1
#Tipo de trabajo: Individual
#En la asamblea ordinaria de un conjunto residencial, van a elegir el consejo de administración, 
# a partir de dos planchas: plancha 1 y plancha 2; cada plancha va a tener n candidatos, que se identifican 
# por una letra única. Ud va a elaborar el programa para el escrutinio. Los votos solo contienen una letra 
# que identifica a uno de los candidatos, cualquiera sea su plancha, recuerde puede haber votos en blanco también. 
# El programa va a incrementar un contador cada que se procese un voto por la plancha 1 y va a incrementar su propio 
# contador para la plancha 2, excepto que sea un voto en blanco.
#
#Entradas:
#
#línea 1: serie de las letras que identifican los integrantes de la plancha 1.
#
#Línea 2: algo similar para la plancha 2.
#
#Línea 3: serie de muchas letras, una por cada voto.
#
#Las letras se ingresan juntas, es decir sin espacios entre ellas
#
# 
#
#Salida:
#
#una de las letras P, N, I, se imprime cada vez que se lee públicamente el voto. Imprime la letra P si la plancha 
# 1 tiene en ese momento mas votos que la plancha 2; Imprime N si la plancha 2 tiene en ese momento mas votos que la plancha 1; 
# imprime la letra I, si en ese momento hay empate.
#
#Ejemplo:
#
#
#ENTRADA 1:
#ADFBC
#KLMNP

#AXDDMNMCSSDFMPBLNBPHRANB
#SALIDA 1:
#PPPPPPIPPPPPPPPPIPIIIPIP

#ENTRADA 2:
#YAV

#FXS

#ASDFXCVTREASDBVBCVCVFAS

#SALIDA 2:
#PIINNNNNNNINNNIIIPPPPPP

#FORMA LARGA Y MÁS COMPLETA:

#def escrutinio(p1,p2,es):
#    up1=p1.upper()
#    up2=p2.upper()
#    ues=es.upper()
#    lista=[]
#    s1=0
#    s2=0
#    for i in ues:
#        if up1.find(i) != -1:
#            s1+=1
#        if up2.find(i) != -1:
#            s2+=1
#
#        if s1>s2:
#            lista.append("P")
#        elif s1<s2:
#            lista.append("N")
#        else:
#            lista.append("I")
#    return "".join(lista)
#
#
#while True:
#    bandera = True
#    plancha1=input("Ingrese los candidatos de la plancha 1: ")
#    plancha2= input("Ingrese los candidatos de la plancha 2: ")
#    for d in plancha1:
#        for f in plancha2:
#            if f == d:
#                bandera = False
#                break
#    if bandera == False:
#        print("No se permite ingresar los mismos candidatos. Inténtalo nuevamente")
#
#    else:
#        votos=input("Ingrese serie de muchas letras: ")
#        print(escrutinio(plancha1,plancha2,votos))

#ENTRADA 1:
#ADFBC
#KLMNP

#AXDDMNMCSSDFMPBLNBPHRANB
#SALIDA 1:
#PPPPPPIPPPPPPPPPIPIIIPIP

#ENTRADA 2:
#YAV

#FXS

#ASDFXCVTREASDBVBCVCVFAS

#SALIDA 2:
#PIINNNNNNNINNNIIIPPPPPP

#FORMA  PRINCIPAL.
plancha1=input("Ingrese los candidatos de la plancha 1: ")
plancha2= input("Ingrese los candidatos de la plancha 2: ")
votos=input("Ingrese serie de muchas letras: ")
s1=0
s2=0
for i in votos:
    if plancha1.find(i) != -1:
        s1+=1
    if plancha2.find(i) != -1:
        s2+=1
    if s1>s2:
        print("P",end="")
    elif s1<s2:
        print("N",end="")
    else:
        print("I",end="")
print()
#OTRA FORMA:
##a=input("1")
#b=input("2")
#c=input("3")
#plancha1=0
#plancha2=0
#for i in c:
#    if i in a:
#        plancha1+=1
#    if i in b:
#        plancha2+=1
#    
#    if plancha1 == plancha2:
#        print("I",end="")
#    elif plancha1 < plancha2:
#        print("N",end="")
#    elif plancha1 > plancha2:
#        print("P",end="")

#a=input("1")
#b=input("2")
#c=input("3")
#plancha1=0
#plancha2=0
#for i in range(len(c)):
#    for j in range(len(a)):
#        if a[j] == c[i]:
#            plancha1+=1
#        if b[j] == c[i]:
#            plancha2+=1
#    if plancha1 == plancha2:
#        print("I",end="")
#    elif plancha1 < plancha2:
#        print("N",end="")
#    elif plancha1 > plancha2:
#        print("P",end="")

