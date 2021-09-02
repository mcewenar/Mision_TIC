#Distancia de ese valor al origen
#Forma ternaria:
#IMPORTANTE
def valorAbsolutoPlus(x):
    valor = x if x>= 0 else -x
    return valor
x=float(input("Elige un número: "))
print("El valor absoluto de "+str(x)+ " es:",valorAbsolutoPlus(x))


#Forma más compactada
def valorAbsolutoPlusPlus(x):
    return x if x>= 0 else -x
x=float(input("Elige un número: "))
print("El valor absoluto de "+str(x)+ " es:",valorAbsolutoPlusPlus(x))


def valorAbsoluto(x):
    if x >= 0:
        valor = x
    else:
        valor = -x
    return valor
x=float(input("Elige un número: "))
print("El valor absoluto de "+str(x)+ " es:",valorAbsoluto(x))

