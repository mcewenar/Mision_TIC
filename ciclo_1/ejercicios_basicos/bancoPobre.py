class Billete:
    def __init__(self):
        self.__valor = 0
        self.__cantidad = 0
    def asignarValor(self,v):
        self.__valor = v
    def asignarCantidad(self,c):
        self.__cantidad = c
    def verValor(self):
        return self.__valor
    def verCantidad(self):
        return self.__cantidad

class Sistema(Billete):
    def __init__(self):
        Billete.__init__(self)
        #super().__init__() OTRA FORMA DE HERENCIA
        self.objetos_Billete = []
        self.totalidad_cajero = 0
        
        
    def devuelta(self,cambio):
        resta = self.cantidadCajero()
        cambio1 = 0
        papeles = 0
        if cambio > resta:
            print("Su petición supera el dinero disponible de la caja. Por favor ingrese una suma inferior.")
            print("Nuestro banco pobre tan solo tiene $"+str(resta))

        else:
            resta = resta - cambio
            for d in self.objetos_Billete:
                if cambio >= 0:
                    div = cambio//d.verValor()
                    if div > d.verCantidad():
                        papeles = d.verCantidad()
                    else:
                        papeles = div
                    cambio1 = cambio % d.verValor()
                    cambio -= d.verValor()*papeles
                    if papeles != 0:
                        print("Se entregó {0} billete(s) de".format(papeles),"$"+str(d.verValor()))

            if papeles != 0:   
                print("Sobró $" + str(cambio1))
                print("Nuestro banco pobre ahora tan solo tiene $"+str(resta))
            else:
                print("No es posible hacer la transacción")
            
        print()
        print("Fue un placer. Vuelva pronto.\n\n")
            
            
        
    def cantidadCajero(self):
        for f in self.objetos_Billete:
            self.totalidad_cajero += f.verCantidad() * f.verValor()
        return self.totalidad_cajero
    
    def crearBilletes(self,v,c):
        billetico = Billete()
        billetico.asignarValor(v)
        billetico.asignarCantidad(c)
        nuevo_billete = self.objetos_Billete.append(billetico)
        return nuevo_billete
        
        
def main():
    denominaciones = [500,200,100,50,10]
    sis = Sistema()
    while True:
        while True:
            try:
                opcion = int(input("Ingrese la opción que desea: \nElige 1. Para retirar dinero.\nElige 2. para agregar billetes (Opción no válida para clientes). "))
                break
            except ValueError:
                print("Dato inválido. Por favor ingresa nuevamente")
        if opcion == 1:
            while True:
                try:
                    Dinero = int(input("Ingrese el valor que desea retirar: "))
                    break
                except ValueError:
                    print("Dato inválido. Por favor ingresa nuevamente")
            sis.devuelta(Dinero)
        elif opcion == 2:
            while True:
                try:
                    for v in denominaciones:
                        c = int(input("Ingrese la cantidad de billetes de $"+ str(v)+": "))
                        sis.crearBilletes(v,c)
                    print("Se ha ingresado los billetes satisfactoriamente")
                    break
                except:
                    print("Dato erróneo. Inténtalo nuevamente")
                    continue
        else:
            print("Valor erróneo")
            continue

main()



#FORMA INEFICIENTE
#class Billete:
#    def __init__(self):
#        #self.__valor = 0 #Idealmente quería agregar objetos (billete, cantidad) al diccionario llamado caja.
#        #self.__cantidad = 0
#        self.caja = {"A":[500,0],"B":[200,0],"C":[100,0],"D":[50,0],"E":[10,0]} #Clave:[Valor de billete,Cantidad de billete]
#    def verCantidad(self): #Pendiente de terminar
#        return self.__valor
#    def verValor(self):
#        return self.__cantidad
#    def asignarValor(self,a):
#        self.__valor = a;
#    def asignarCantidad(self,i,b):
#        self.caja[i][1] = self.caja[i][1] + b


#    def devuelta(self,cambio):
#        papeles = 0
#        resta = self.cantidadCajero()
#        if cambio > resta:
#            print("Su petición supera el dinero disponible de la caja. Por favor ingrese una suma inferior.")
#            print("Nuestro banco pobre tan solo tiene $"+str(self.cantidadCajero()))
#        else:
#            resta = resta - cambio
#            for d in self.caja:
#                if cambio >= 0:
#                    A = cambio//self.caja[d][0]
#                    if A > self.caja[d][1]:
#                        papeles = self.caja[d][1]
#                    else:
#                        papeles = A
#                    cambio1 = cambio%self.caja[d][0]
#                    cambio -= self.caja[d][0]*papeles
#                    if papeles != 0:
#                        print("Se entregó {0} billete(s) de ".format(papeles),"$"+str(self.caja[d][0]))
#            print("Sobró $" + str(cambio1))
#            print("Nuestro banco pobre ahora tan solo tiene $"+str(resta))
#        print()
#        print("Fue un placer. Vuelva pronto.\n\n")
        
#    def cantidadCajero(self):
#        totalidad_cajero = 0
#        for f in self.caja:
#            totalidad_cajero += self.caja[f][0] * self.caja[f][1]
#        return totalidad_cajero

#def main():
#    billetes = Billete()
#    while True:
#        try:
#            opcion = int(input("Ingrese la opción que desea: \nElige 1. Para retirar dinero.\nElige 2. para agregar billetes (Opción no válida para clientes). "))
#            if opcion == 1:
#                Dinero = int(input("Ingrese el valor que desea retirar: "))
#                billetes.devuelta(Dinero)
#            elif opcion == 2:
#                for i in billetes.caja:
#                    p = int(input("Ingrese la cantidad de billetes de $"+ str(billetes.caja.get(i)[0])+": "))
#                    billetes.asignarCantidad(i,p)
#                print("Se ha ingresado los billetes satisfactoriamente")
#            else:
#                print("Valor erróneo")

#        except ValueError:
#            print("Dato inválido. Por favor ingresa nuevamente")

#main()