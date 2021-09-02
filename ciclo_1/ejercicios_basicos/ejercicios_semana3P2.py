#1. Desarrollar un algoritmo que reciba dos cadenas de caracteres y
#determine si la primera esta incluida en la segunda. Se dice que una
#cadena esta incluida en otra, si todos los caracteres (con repeticiones)
#de la cadena esta en la segunda cadena sin tener en cuenta el orden
#de los caracteres

#def cadenaCont(cad1,cad2):
#    contador=0
#    for i in range(len(cad2)):
#        if cad2[i] in cad1:
#            contador+=1
#            continue
#    if len(cad1) == contador:
#        return "Sí"  
#    return "No"
#print(cadenaCont(input("Escriba cadena 1: "),input("Escriba cadena 2: ")))

#La cadena \prosa" esta incluida en la cadena \la profesora de idiomas".
#La cadena \pepito" no esta incluida en la cadena \un pedazo de tierra", ya que le falta una \p".
#La cadena \pepito" si esta incluida en la cadena \tijeras o papel".


#def finder(palabra,frase):
#    existe: bool = True
#    for letra in palabra:
#        NN=len(frase) #Importante este dentro del ciclo for. Se va recortando l longitud
#        if letra in frase:
#            pos = frase.find(letra)
#            print("Posición",pos, ", letra",letra,":", end=" ") #Consiste en rebanar la cadena y omitit los letras que están contenidas
#            izq = frase[0:pos]
#            der = frase[pos+1:NN]
#            print(izq,der)
#            frase = izq + der
#        else:
#            existe = False
#            print(existe,": No hallo la letra",letra)
#            break
#    return existe
#print(finder(input("Escriba cadena 1: "),input("Escriba cadena 2: ")))
#
#

#Desarrollar un algoritmo que determine si una cadena de caracteres es
#palndrome. Una cadena se dice palndrome si al invertirla es igual a
#ella misma.
#Ejemplos:

#\ala" es palndrome.
#\amor a roma" es palndrome.
#\anita atina" es palndrome.
#\al sur de Colombia" NO es palndrome.
#\anula las alas a la luna" NO es palndrome. (Al invertirla: \anul
#al a sala sal aluna") no es igual a la original.
#\la tele letal" NO es palndrome.
#from math import ceil
#def palindromo(cadena):
#    NN = len(cadena)
#    long2 = NN//2 #Para separar si son pares o impares
#    izq = cadena[0:long2] #slice o rebanada, exclueye la pos [long2]
#    der1 = cadena[long2:NN] if NN % 2 == 0 else cadena[long2+1:NN]
#    der = der1[::-1] # reversa el lado derecho
#    res: bool = der == izq 
#    return res
#
##print(math.ceil(3.2))
#lista=["amor a roma","anita atina","al sur de Colombia","anula las alas a la luna", \
#"anulal a sala sal aluna","la tele letal"]
#for frase in lista: #frase es una cadena
#  res=palindromo(frase)
#  print(frase,'\t',res)



#Desarrollar un algoritmo que determina si una cadena de caracteres es
#frase palndrome, esto es, si es palndrome al eliminarle espacios,
#tldes, signos de puntuacion y al considerar mayusculas=minusculas.
#\Anula las alas a la luna" es frase palndrome.
#\Dabale arroz a la zorra el abad" es frase palndrome.
#\la tele letal" es frase palndrome.
#\arriba la birra" es frase palndrome.
#\Isaac no ronca as" es frase palndrome.
#\sometamos o matemos" es frase palndrome.
#\Anita, la latina" es frase palndrome.

#parte2: palindrome de frase, donde mayusculas se consideran igual a minusculas
# se ignoran signos de puntuacion (. : ; , ? ! ), y espacios, aun falta quitar tildes
def esPalindrome(palabra):
  NN = len(palabra)   
  long2=NN//2   
  izq = palabra[0:long2] #slice o rebanada, excluye la pos [long2]
  der1 = palabra[long2:NN] if (NN % 2 == 0) else palabra[long2+1:NN]  #ani l ina
  der = der1[::-1] # reversa el lado derecho
  res= der == izq  #compara ambas en orden lexicografico
  return res
lista=['Anula las alas a la luna  ',".... Dabale arroz a la zorra el abad .?!;:,", \
       'La tela letal?', '!Arriba la birra', 'Isaac no ronca asi...','Anita la latina'] #Forma de salto de línea
for frase in lista:
   frase=frase.strip() #quito espacios a izq y derecha
   frase=frase.strip('.,?;!:') #quita estos simbolos a la izq y a la derecha, pero no internas
   frase=frase.upper() #convierto a mayusculas
   NN=len(frase) #Vamos a quitarle los espacios intermedios, uno a la vez
   conta=frase.count(' ')
   for i in range(conta): #genero una coleccion 0, 1,2, sirve para controlar cuantos espacios voy a quitar
     pos= frase.find(' ') #detecto la posicion del primer espacio
     izq=frase[0:pos] #Como las cadenas son inmutables, no puedo cambiar sus caracteres
     der=frase[pos+1:NN] #genero dos subcadenas, izq y der, elimino el espacio intermedio
     print(izq, der) #subcadenas con funcion slice, notacion de range, [ini:fin:incr]
     frase = izq + der #Junto las 2 subcadenas, omito el espacio
   print(esPalindrome(frase)) #solucion

    






#Forma ineficiente
#def palindromo(cadena):
#    cadenaLow=cadena.lower()
#    cadenaEspa=cadenaLow.replace(" ","")
#    cadeInv = cadenaEspa[::-1]
#    if cadena == "":
#        print("No es palíndromo")
#    elif cadeInv == cadenaEspa:
#        print("Es palíndromo")
#    else:
#        print("No es palíndromo")
#while True:
#    letra=input("Ingresa una palabra: ")
#    palindromo(letra)