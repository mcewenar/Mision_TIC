def buscar_parcial(str,ch,n):
    if n > 0:
        return (str[n-1] == ch) or buscar_parcial(str,ch,n-1)
    else:
        return False
def buscar(str,ch):
    return buscar_parcial(str,ch,len(str))


print(buscar("Erase una vez","f")) #Funciona
print("----2----")

def f(n): #Números pares e impares con recursión
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        return f(n-2)
print(f(15))
print("---3---")

def g(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return g(n-3)
print(g(13))
print("---4---")
def h(n,m): #Suma de 2 números con recursión
    if m == 0:
        return n
    else:
        return h(n+1,m-1)
print(h(2, 3)); print(h(8, 5)); print(h(6, 6))

print("---ejercicio1---")
#Disene un modelo matematico que permita calcular la funcion producto,
#es decir, que reciba dos (2) numeros naturales y retorne la multiplicacion
#del primer numero por el segundo.
#No se pueden utilizar los operadores de multiplicacion ni de division (ni
#entera ni real).
#Codifique el modelo matematico utilizando el lenguaje Python.

def producto(m,n):
    if n==0:
        return 0
    else:
       return m + producto(m,n-1)
        
print(producto(8,5))


print("----5----")
def potencia(b, n):
    if n == 0:
        return 1
    else:
        return potencia(b,n-1) * b
base = float(input("Por favor digite la base: "))
exp = int(input("Por favor digite el exponente: "))
print(base, "^", exp, "=", potencia(base, exp))