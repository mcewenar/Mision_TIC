#Ejercicio. RETO UNIVERSIDAD AUNTÓNOMA DE BUCARAMANGA

#Se ha registrado las calificaciones (de 1.0 a 5.0) obtenidas por un estudiante. Escriba un programa en Python 3 que solicite la 
#información y la almacene en una lista y que al final muestre en pantalla el nombre del estudiante, la suma de las notas, 
#la cantidad de notas y el promedio (con un decimal) y si aprobó la asignatura (promedio mínimo de 3.0). El programa 
#debe validar que los números ingresados sean decimales positivos en el rango indicado y, ante un error, mostrar el mensaje: "dato errado,
#intente de nuevo" y solicitar de nuevo el dato. El programa terminará cuando se ingrese la nota 10 o cuando se ingrese el valor cero.

lista_estudiante = []
i=1
def notas_estudiante(datos:list):
    contador = 0
    sumatoria_notas = 0.0
    for t in range(len(datos)):
        if t < len(datos)-1:
            sumatoria_notas += datos[t]
            contador += 1
    estudiante = datos[contador]
    promedio = round(sumatoria_notas/contador,1)
    if promedio < 3.0:
        apro = ". No aprobó la asignatura"
    else:
        apro = ". ¡Aprobó la asignatura!"
    return [estudiante,contador,sumatoria_notas,promedio,apro]
    

nombre = input("Ingrese el nombre del estudiante: ")
while i<=10:
    try:
        u = float(input("Ingrese la nota " + str(i) + ": "))
        if u >=1 and u <= 5:
            lista_estudiante.append(u)
            i+=1
        elif u == 0:
            break
        else: 
            print("Dato errado, intente de nuevo")
    except ValueError:
        print("Dato errado, intente de nuevo")
lista_estudiante.append(nombre)
informacion=notas_estudiante(lista_estudiante)
print("El estudiante",informacion[0],"obtuvo",informacion[1],"notas que suman",str(informacion[2])+". Su calificación final es de",str(informacion[3])+informacion[4])
print("\nHasta pronto")


#FORMA CON MANEJO DE ERRORES:

#class Error(Exception):
#    """Base class for other exceptions"""
#    pass

#class LargerThan5Error(Error):
#  """Number is larger than 5"""
#  pass

#class NegativeNumberError(Error):
#  """The number is negative"""
#  pass


#name = input("Nombre del estudiante: ")

#all_notes = []
#note = 0

#note_number = 1
#i = 0
#while i < 10:
#  try:
#   print('Nota', note_number, end="")
#   print(': ', end="")
#   note = float(input())

#   if note > 5:
#     raise LargerThan5Error

#   elif note < 0:
#     raise NegativeNumberError

#  except LargerThan5Error:
#    print("Dato errado, intente de nuevo.")
#    continue

#  except NegativeNumberError:
#    print("Dato errado, intente de nuevo.")
#    continue

#  except:
#    print("Dato errado, intente de nuevo.")
#    continue

#  if (note == 0):
#    break

#  all_notes.append(note)
#  note_number +=1
#  i += 1

#notes_quantity = len(all_notes)
#note_points = sum(all_notes)

#final_note = note_points / notes_quantity

#print('El estudiante', name, 'obtuvo', notes_quantity, 'notas', 'que suman ', end="")
#print(note_points, end="")
#print(', su calificación final es de ', end="")
#print(round(final_note, 2), end="")

#if final_note > 3:
#  print(', ¡aprobó la asignatura!', end="")

