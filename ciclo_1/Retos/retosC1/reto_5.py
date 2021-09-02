#Una biblioteca tiene libros que se identifican mediante números enteros, empezando desde 0. Obviamente, cada libro tiene un autor. 
#La biblioteca tiene una lista de los libros que le hacen falta para completar la colección de libros de cada autor y otra lista 
#de los libros repetidos que tienen para intercambiar con otras bibliotecas. Los libros de un autor se intercambian por otros libros 
#del mismo autor. El trabajo consiste en: a) (vale 1 punto) crear una librería llamada “libros”, que conste como mínimo de las siguientes 
#funciones:
#
#b). (Vale 1 punto) La función "autores” , sirve para que, a partir de una lista de autores de toda la colección que se ambiciona tener, 
#generar una lista de autores, sin repetición.
#Por ejemplo, si la colección completa tuviera diez libros, cada uno tiene su autor, como en la siguiente lista:
#
#['Shakespeare', 'Cervantes', ‘Shakespeare’, 'Gabo', 'Shakespeare', 'Gabo', 'Cervantes', 'Gabo', 'Gabo', 'Cervantes']
#
#La función debe retornar: [‘Shakespeare ', 'Cervantes', 'Gabo'] 
#
#c) (Vale 1 punto). La función "mefaltandeunautor": Sirve para que a partir de la lista de números de los libros que hacen falta para 
#completar la colección, la lista de los autores de las obras de la colección cuando esté completa y el nombre de un autor dado (en ese orden), 
#retorne una lista de los libros de ese autor dado que hacen falta para completar la colección. Note que el número que identifica a un libro, 
#apunta a su respectivo autor en la lista de autores.
#
#Ejemplo, al invocar la función con las listas: [2, 4, 5, 8],  
#
#['Shakespeare', 'Cervantes', ‘Shakespeare’, 'Gabo', 'Shakespeare', 'Gabo', 'Cervantes', 'Gabo', 'Gabo', 'Cervantes'],
#
#y la cadena con el nombre del autor ‘Gabo',   debe retornar la lista [5,8]
#
#d) (Vale 1 punto). La función "losnecesito": dada una lista de los libros disponibles para intercambio que tiene otra biblioteca y una
# lista de los libros repetidos que tiene mi biblioteca para intercambio, (en ese orden), retorna la lista con los libros que me interesan 
# de la otra biblioteca.
#
#Por ejemplo, al invocar la función con las listas otrabiblioteca = [9, 3, 7, 10, 15, 16],   y mibibloteca= [2, 10, 3, 8]
#
#debe retornar la lista: [9, 7, 15, 16]
#
#e) (Vale 1 punto) Para simplificar la primera versión de la librería de funciones decidieron levantar la restricción que solo cambian 
#libros que son de un mismo autor, y por lo tanto, ahora la lista que maneja cada biblioteca simplemente indica los números de los libros 
#repetidos que tienen para intercambiar y aquellos números que no están en dicha lista son los que necesitan. De esta manera deben crear una 
#función "puedocambiar”, que reciba la lista de los libros repetidos que tiene la otra biblioteca y la lista de los libros repetidos que 
#tiene mi biblioteca y que retorne la cantidad de libros que pueden cambiar.
#
#Por ejemplo, al invocar la función con las listas [13, 6, 17, 11, 15, 16] y  [4, 11, 6, 8]
#debe retornar 2
#
#Es decir, a la otra biblioteca solo le interesan dos libros que tiene mi biblioteca: [4,8], mientras que a mi biblioteca me interesan cuatro 
#libros que tiene la otra biblioteca: [13,17,15,16], o sea que en total se pueden intercambiar solo 2 libros.
def autores(listaAut):
    result = []
    for autor in listaAut:
        if autor not in result:
            result.append(autor)
    return result

def mefaltandeunautor(ListaFaltan,ListaAutor,autor):
    listaFinal = []
    for i in ListaFaltan:
        if i in range(len(ListaAutor)) and autor == ListaAutor[i]:
            listaFinal.append(i)
    return listaFinal

def losnecesito(librosDisponibles,librosRepetidos):
    librosInteresan = []
    for libro in librosDisponibles:
        if libro not in librosRepetidos:
            librosInteresan.append(libro)
    return librosInteresan

def puedocambiar(RepetidosOtra,RepetidosMiBi):
    cont1=0
    cont2=0
    for i in RepetidosMiBi:
        if i not in RepetidosOtra:
            cont1+=1
            
    for j in RepetidosOtra:
        if j not in RepetidosMiBi:
            cont2+=1

    return cont1 if cont1 < cont2 else cont2

print(autores(['Shakespeare', 'Cervantes', 'Shakespeare', 'Gabo', 'Shakespeare', 'Gabo', 'Cervantes', 'Gabo', 'Gabo', 'Cervantes']))
print(mefaltandeunautor([2, 4, 5, 8],['Shakespeare', 'Cervantes', 'Shakespeare', 'Gabo', 'Shakespeare', 'Gabo', 'Cervantes', 'Gabo', 'Gabo', 'Cervantes'],"Gabo"))
print(losnecesito([9, 3, 7, 10, 15, 16],[2, 10, 3, 8]))
print(puedocambiar([13, 6, 17, 11, 15, 16],[4, 11, 6, 8] ))
