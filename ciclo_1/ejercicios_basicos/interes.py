#Si pido prestados P cantidad de pesos para pagarlos en dos meses, si
#el interes del prestamo es del 3%. ¿Cuanto se debe pagar al final del
#segundo mes si el interes es compuesto mensualmente?.

#Revisión bibliográfica:
#ecuación:
#Capital final = C0 x (1+Ti) ^t

#(^t = elevado por el periodo de tiempo)
#CO es el capital inicial, Ti es la tasa de interés anual y t es el tiempo que dura la inversión.
#Utilizando el ejemplo anterior, el primer año el resultado de 110 euros se obtendría de esta forma:
#Capital final= 100 X (1 + 0,10/1) ^ 1 = 110
#En el segundo año, la fórmula se aplicaría así:
#110 x (1+ 0,10/1) ^ 1 = 121
#Como puede verse, el capital inicial va variando ya que se van sumando los intereses obtenidos, por lo que el total va aumentando cada año.


#Dinero = capital inicial
#**t elevado por período de tiempo
#ti tasa de interés anual/mensual. Toca dividirlo entre meses y 100
def interes(dinero,t,ti):
    ti=ti/12
    return dinero * ((1+(ti/100))**t)
while True:
    print("Bienvenido/a, esta es una calculadora de interés compuesto mensual")
    while True:
        try:
            dinero = float(input("Ingresa el monto: "))
            tiempo = int(input("Ingresa los meses: "))
            t_interes = float(input("Ingresa el interés % POR CADA MES: "))
            break
        except ValueError:
            print("Dato erróneo. Inténtalo nuevamente")

    if (t_interes > 0 and t_interes <= 100) and (tiempo > 0) and (dinero > 0):
        print("Al cabo de "+str(tiempo)+" meses, se tiene que pagar " + str(round(interes(dinero,tiempo,t_interes),2))+" pesos")
        principal = input("¿Desea reiniciar?")
        while True:
            if principal == "SI" or principal == "Si" or principal == "sI" or principal == "SÍ" or principal == "Sí" or principal == "sí" or principal == "Sí" or principal == "si" or principal == "sí":
                continue
            elif principal == "NO" or principal == "No" or principal == "nO" or principal == "no":
                print("¡Hasta luego!")
                break
            else:
                print("Dato erróneo")
                principal = input("¿Desea reiniciar?")
        break
    else:
        print("Valores erróneos")
    