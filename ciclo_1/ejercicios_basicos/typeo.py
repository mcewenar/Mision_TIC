#TOCA USAR MANEJO DE EXCEPCIONES


data = int(input("Ingresa un número: "))

if type(data) == int:
    print("es entero")
elif type(data) == float:
    print("es float")
elif type(data) == str:
        print("es string")