#Mi mamá me manda a comprar, por una aplicación, P panes a $ 300 cada uno, M bolsas
#de leche a $ 3300 cada una y H huevos a $ 350 cada uno. Hacer un
#programa que me diga las vueltas (o lo que quedo debiendo).

def tienda(dinero: int):
    pedido=0
    lista=[]
    lista2=[]
    productos = {"panes":300, "bolsas de leche":3300, "huevos":350, "Butifarras":400}
    for i in range(len(productos)):
        while True:
            try:
                articulo = int(input("Elige la cantidad de "+ str(list(productos.keys())[i])+": ")) #Convierte en lista y la indexa
                break
            except ValueError:
                print("Dato erróneo")
        if articulo != 0:
            pedido += productos.get(list(productos.keys())[i])*articulo
            lista.append(productos.get(list(productos.keys())[i])*articulo)
            lista2.append(list(productos.keys())[i])
    lista.append(lista2)
    lista.append(dinero - pedido)
    return lista

while True:
    while True:
        try:
            dinero = int(input("Ingresa dinero disponible: "))
            break
        except ValueError:
            print("Dato erróneo")
    if dinero <=0:
        print("Ingreso erróneo")
        dinero = int(input("Ingresa dinero disponible: "))
    else:
        saldo=tienda(dinero)
        if saldo[len(saldo)-1] < 0:
            print("Fondos insuficientes. Inténtalo de nuevo.")
        else:
            for i in range(len(saldo)-2):
                print("Usted compró",str(saldo[i])+" pesos en",end=" ")
                print(saldo[len(saldo)-2][i])
            print("Saldo restante:",str(saldo[len(saldo)-1])+" pesos")
            print("\n¡Vuelva pronto!\n")
    

