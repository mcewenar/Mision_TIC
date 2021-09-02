import modulo as md
print ("Las funciones de 'modulo' son:", dir(md))
x = 12
y = 34
print ("La suma es: ", md.sum1(x,y))
print ("La multiplicacion es: ", md.mul1(x,y))

#Para usar un paquete se debe importar el modulo sys y agregar #el directorio del paquete creado con sys.path.append e importar #cada modulo con from.

#paquetes
import sys #1)
#agregar el directorio del paquete creado con sys.path.append 
sys.path.append
#3-(20)
from comprimir import aZip #3
from comprimir import aRar
from comprimir import aTar
print('modulos:', dir(aZip))
aZip.crear_zip("archivo1")
aRar.crear_rar("archivo2")
aTar.crear_tar("archivo3")