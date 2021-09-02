#Reto 4: Hora de llegada de vuelo:


#Una agencia de viajes necesita informar a sus clientes la hora de llegada de sus vuelos. Se conoce la hora de partida del vuelo 
#(en horas, minutos y segundos) y la duración del vuelo (en horas, minutos y segundos).
#Cree una función que retorne la hora de llegada del vuelo en una cadena con el formato “HH:mm:ss” donde HH es la hora, 
#mm los minutos y ss los segundos de la hora de llegada del vuelo. 
#La hora está dada en formato de 24 horas. Si alguno de los 3 números de la respuesta es menor a 10, 
#sólo se necesita un dígito ('7' en lugar de '07').
#Su solución debe tener una función de acuerdo con la siguiente especificación:
#•	Nombre de la función: calcular_horario_llegada
#Si lo requiere, puede agregar funciones adicionales.
#Descripción de parámetros:


def calcular_horario_llegada(hsalida, msalida, ssalida, duracionH, duracionM, duracionS):
    segundos =  (ssalida + duracionS)
    minutos = (msalida + duracionM) + segundos//60
    hora = (hsalida + duracionH) + minutos//60
    segundos %= 60
    minutos %= 60
    hora %= 24
    return str(hora)+":"+str(minutos)+":"+str(segundos)

    
print(calcular_horario_llegada(23, 32, 4, 7, 30, 15))




#ejercicio 2
#Escenario
#La tarea es preparar un código simple para evaluar o encontrar el tiempo final de un periodo de tiempo dado,
#expresándolo en horas y minutos. Las horas van de 0 a 23 y los minutes de 0 a 59.
#El resultado debe ser mostrado en la consola.

#Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16.
#No te preocupes si tu código no es perfecto, está bien si acepta una hora invalida,
#lo más importante es que el código produzca una salida correcta acorde a la entrada dada.
#Datos de Prueba
#Entrada de muestra:
#12
#17
#59

#Salida esperada: 13:16


#Entrada de muestra:
#23
#58
#642

#Salida esperada: 10:40


#Entrada de muestra:
#0
#1
#2939

#Salida esperada: 1:0

#Prueba el código cuidadosamente. Pista: utilizar el operador % puede ser clave para el éxito.

hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# coloca tu código aqui
# calcula los minutos y los convierte a una cadena
minutos=str((min+dura)%60)
# calcula los minutos totales y luego lo convierte a horas para luego convertirlo a una cadena
horas=str(((hora*60 + min + dura)//60) % 24)
print("Hora: "+horas+":"+minutos)
