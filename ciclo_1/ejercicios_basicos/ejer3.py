#Reto 2: Índice de masa corporal

#Cree una función que pueda calcular el índice de masa corporal (BMI) de una persona.
#La fórmula para calcular el BMI es la siguiente: 
#BMI = peso/(altura^2)
#En esta fórmula el peso está en kilogramos y la altura en metros. Tenga en cuenta que el peso y altura que reciban su función, 
#van a estar en libras y pulgadas respectivamente, ya que su función será usada en los Estados Unidos.
#Recuerde que:
#•	1 libra corresponde a 0.45kg.
#•	1 pulgada corresponde a 0.025 metros.
#El valor de retorno debe estar redondeado a dos decimales. 
#Su solución debe tener una función de acuerdo con la siguiente especificación:
#•	Nombre de la función: calcular_BMI
#Si lo requiere, puede agregar funciones adicionales. 
#Descripción de parámetros:

desire = 1
def mass_index(peso,alt):
    peso *= 0.45
    alt *= 0.025
    bmi = peso/(alt**2)
    return bmi

while desire:
    try:
        peso = float(input("Ingrese el peso (lb): "))
        alt = float(input("Ingrese la altura (In): "))
        c=mass_index(peso,alt)
        print("Tu índice de masa muscular (IMM) es de " + str(round(c,2)))
    except ValueError:
        print("No se admiten carácteres. Inténtalo de nuevo")
        
    
    desire = input("¿Desea salir? ")
    if desire == "No" or desire == "NO" or desire == "no":
        continue
    elif desire == "Sí" or desire == "Si" or desire == "SÍ" or desire == "sí" or desire == "Sí" or desire == "si": 
        desire = 0
    else:
        print("Dato erróneo. Inténtalo nuevamente")
print("Hasta pronto")
