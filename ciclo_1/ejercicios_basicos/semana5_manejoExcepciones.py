#def division(a, b):
#    try:
#        coc = a//b
#        res = a % b
#        return(coc, res)
#
#    except ZeroDivisionError: #No incluye error ValueError
#        print("Error en la division de", a, "entre", b)
#def main():
#    try:
#        num = int(input("digite el dividendo: "))
#        div = int(input("digite el divisor: "))
#        print(division(num, div))
#        
#    except ValueError:
#        print("El valor digitado no es un numero.")
#    finally:
#        print("Bye")
        
    
#main()

#try:
#    num = int(input("Ingrese un numero "))
#    re = 100/num
#except:
#    print("Algo esta mal")
#else:
#    print("El resultado es ",re)
#finally:
#    print("El programa termina!")


#IMPORTANTE.
#Para determinar el tipo de excepcion se puede utilizar una lnea de codigo:
#try:
#    num = int(input("Ingrese un numero: "))
#    re = 100/num # Generar excepcion si se digito 0
#    print(re)
#except Exception as e:
#    print(e, "\n", type(e))


#Para el siguiente codigo se lanza y se atrapa una excepcion
def division(a, b):
    if b == 0:
        raise ValueError("Error de division por cero")
    else:
        coc = a // b
        res = a % b
    return(coc, res)
try:
    print(division(10, 0))
except Exception as e:
    print(e, "\n", type(e))