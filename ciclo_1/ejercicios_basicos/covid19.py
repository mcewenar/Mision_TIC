#El número de contagiados de Covid-19 en el país de NuncaLandia se
#duplica cada día. Hacer un programa que diga el número total de
#personas que se han contagiado cuando pasen D días a partir de hoy,
#si el número de contagiados actuales es C.

def covid(c,n):
    p = c*(2**n - 1)
    return p
c=int("Cantidad de infectados: ") #Número de infectadoso inicial
n=int("Número de días") #Número de días
print("Población infectada después de ",n," días = ",covid(c,n))