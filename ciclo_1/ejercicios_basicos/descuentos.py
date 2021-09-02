#Una tienda tiene las siguientes promociones
#Si un cliente lleva mas de 5 productos del mismo tipo le realizan
#un descuento del 5%. Si lleva mas de 10 productos del mismo tipo
#le realizan un descuento del 10%. Si lleva mas de 20 productos
#del mismo tipo le realizan un descuento del 20%. Construya un
#programa que dado el numero de productos y el precio de cada
#producto determine el valor a pagar por el cliente.
def pago(n,precio):
    if n <= 5:
        valor = n*precio 
    elif 5 < n <= 10:
        valor = n * precio * 0.95
    elif 10 < n <= 20:
        valor = n * precio * 0.90
    else: valor = n*precio * 0.80
    return valor

print(pago(8,3000))

def pago_final(n, precio):
    if n <= 5:
        valor = n * precio
    elif n <= 10:
        valor = n * precio * 0.95
    elif n <= 20:
        valor = n * precio * 0.90
    else:
        valor = n * precio * 0.80
    return valor
print(pago_final(8,3000))
print(pago_final(4,10000))
print(pago_final(8,10000))
print(pago_final(15,10000))
print(pago_final(25,10000))