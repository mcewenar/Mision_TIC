with open("C:\\Users\\dmcew\proy_programacion\\Mision_TIC\\ciclo_1\\ejercicios_basicos\\Manejo_Archivos\\files\\dataProbando.txt","w") as f:
    escritura = "Hola, buenos días. JEJEJ"
    f.write(escritura)
    f.write("\tSobreescrito")
    f.write("\tNo se sobreescribe")
    #print(data)


with open("C:\\Users\\dmcew\proy_programacion\\Mision_TIC\\ciclo_1\\ejercicios_basicos\\Manejo_Archivos\\files\\dataProbando.txt","w",encoding="utf-8") as f:
    escritura = "El comando open (ruta del archivo, 'w') abre el archivo en modo de \
    escritura creando el archivo si no existe (write) o sobreescribiendo el \
    archivo si existe. El siguiente codigo crea el archivo wdata.txt en la \
    carpeta files:"
    f.write(escritura)
    f.write("\t No se sobreescribo")
    f.write("\t No se sobreescribe")

with open("C:\\Users\\dmcew\proy_programacion\\Mision_TIC\\ciclo_1\\ejercicios_basicos\\Manejo_Archivos\\files\\dataProbando.txt","a",encoding="utf-8") as f:
    escritura = "El comando open(ruta del archivo, 'a') abre el archivo en modo de \
    adjuntar creando el archivo si no existe (append ) o escribiendo al nal del \
    archivo si existe. El siguiente codigo escribe al nal del archivo wdata.txt:"
    f.write(escritura)
    f.write("\t NO SE Sobreescribe")
    f.write("\tNo se sobreescribe en el mismo with open")

with open("C:\\Users\\dmcew\proy_programacion\\Mision_TIC\\ciclo_1\\ejercicios_basicos\\Manejo_Archivos\\files\\dataProbando.txt","r",encoding="utf-8") as f:
    data = f.read()
    print(data)


#----------------------------------------------------------------------------2-----------------------------------------------------------
with open("C:\\Users\\dmcew\\proy_programacion\\Mision_TIC\\ciclo_1\\ejercicios_basicos\\Manejo_Archivos\\files\\data1.txt", "r",encoding="utf-8") as f: #Forma de aceptar tildes y muchos carácteres raros
    print(f.read(39)) #Cuántos bytes se van a imprimir
    linea2 = f.read() #El puntero queda ahí
    print(linea2)
    print(f.read(15))


with open("C:\\Users\\dmcew\\proy_programacion\\Mision_TIC\\ciclo_1\\ejercicios_basicos\\Manejo_Archivos\\files\\data1.txt", "r",encoding="utf-8") as f: #Forma de aceptar tildes y muchos carácteres raros
    print("----2----")
    linea1 = f.readline()
    linea2 = f.readline()
    print("Nombre del archivo: ", f.name)
    print(type(f))
    lista = f.readlines()
print(lista)
print(linea1)
print(linea2)


#--------------------------------------------------------3------------------------------------------------------------------------------------------
print("----3----")

with open("C:\\Users\\dmcew\\proy_programacion\\Mision_TIC\\ciclo_1\\ejercicios_basicos\\Manejo_Archivos\\files\\data1.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line, end="")

#---------------------------------------------4----------------------------------------------------------------------------------------------------
values = [1234, 5678, 9012, 3.14159265, False]
with open("C:\\Users\\dmcew\\proy_programacion\\Mision_TIC\\ciclo_1\\ejercicios_basicos\\Manejo_Archivos\\files\\data3.txt", "w+") as f: #Reescribiendo.
    #Si se desea escribir datos que no son cadenas de texto en un archivo es
    #necesario convertir cada dato a string con el comando str() as como
    #se muestra a continuacion.
    for value in values:
        str_value = str(value)
        f.write(str_value)
        f.write("\n")

with open("C:\\Users\\dmcew\\proy_programacion\\Mision_TIC\\ciclo_1\\ejercicios_basicos\\Manejo_Archivos\\files\\data3.txt", "r") as f: 
    print(f.read())
    print(f.tell())
    print(f.seek(11,0)) #Manipula el puntero
    print(f.tell())
print("----------------------4-------------------------")
# Abre el archivo en modo de solo lectura
with open("C:\\Users\\dmcew\\proy_programacion\\Mision_TIC\\ciclo_1\\ejercicios_basicos\\Manejo_Archivos\\files\\data5.txt", "r", encoding="utf-8") as f:
    list_content = f.readlines()
    list_content.insert(1, "Esta es la lnea 1.5: jajaja\n")
# Re-abre el archivo en modo de solo escritura
# para sobreescribir la version anterior de este
with open("C:\\Users\\dmcew\\proy_programacion\\Mision_TIC\\ciclo_1\\ejercicios_basicos\\Manejo_Archivos\\files\\data5.txt", "w", encoding="utf-8") as f:
    contenido = "".join(list_content)
    f.write(contenido)
with open("C:\\Users\\dmcew\\proy_programacion\\Mision_TIC\\ciclo_1\\ejercicios_basicos\\Manejo_Archivos\\files\\data5.txt", "r", encoding="utf-8") as f:
    print(f.read())


print("--------------------5---------------------------")
#Para el directorio files, el siguiente codigo permite caracterizar el
#contenido de archivos y subdirectorios contenidos en este.
import os
entries = os.scandir("C:\\Users\\dmcew\\proy_programacion\\Mision_TIC\\ciclo_1\\ejercicios_basicos\\Manejo_Archivos\\files")
for entry in entries:
    print(entry.name + ", es directorio: "
    + str(entry.is_dir()) + ", size: " +
    str(entry.stat().st_size) + " bytes.")

print("------------------6--------------------")
#A veces se desea almacenar informacion contenida en objetos Python,
#(diccionarios o listas por ejemplo). En este caso se puede utilizar el
#modulo pickle con su metodo dump, para serializar objetos.
#El siguiente codigo permite crear dos lista, un diccionario a partir de estas
#y por ultimo se serializan como objetos
import pickle
import pprint
name = ["mohit", "bhaskar", "manish"]
skill = ["Python", "Python", "Java"]
dict1 = dict([(k,v) for k,v in zip(name, skill)]) #Función .zip() para serializar estructuras de datos, luego las agrupa en una tupla y, finalmente, la convierte en diccionario
with open("C:\\Users\\dmcew\\proy_programacion\\Mision_TIC\\ciclo_1\\ejercicios_basicos\\Manejo_Archivos\\files\\programming_powers.pkl", "wb") as p_file:
    pickle.dump(name, p_file)
    pickle.dump(skill, p_file)
    pickle.dump(dict1, p_file)
    pprint.pprint(name) #Lista 
    pprint.pprint(skill) #Lista
    pprint.pprint(dict1) #Dicc

print("-------7------")

#Una imagen de tipo *.jpg es un archivo de tipo binario. Con cierto
#procesamiento es posible crear una copia de la imagen de la siguiente
#manera
with open("C:\\Users\\dmcew\\proy_programacion\\Mision_TIC\\ciclo_1\\ejercicios_basicos\\Manejo_Archivos\\files\\discurso.jpg", "rb") as imagen:
    data = imagen.read()
with open("C:\\Users\\dmcew\\proy_programacion\\Mision_TIC\\ciclo_1\\ejercicios_basicos\\Manejo_Archivos\\files\\copy.jpg", "wb") as f:
    f.write(data)

