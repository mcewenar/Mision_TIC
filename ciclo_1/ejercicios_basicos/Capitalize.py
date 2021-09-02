#Escribe un programa que le pida una frase al 
#usuario y capitalice cada palabra. Por ejemplo:

#Ingresa una frase: "esta es una prueba".
#Salida: "Esta Es Una Prueba"


#Fast way:
#quote = input("Enter a quote: ")
quote = "this is a test"
print(quote.title())

#Middle level way:
#quote = input("Enter a quote: ").split()
quote = "this is a test".split()
newText = []
for word in quote:
    newText.append(word.capitalize())
print(" ".join(newText))


#Hard way:
#quote = input("Enter a quote: ").split()
#1.
newText = []
for word in quote:
    newWord = word[0].upper() + word[1:]
    newText.append(newWord)
print(" ".join(newText))

#2.
newText = []
for word in quote: #[esta,es,una,prueba]
    firstLetter = word[0] #e e u p (a medida que recorre el for externo)
    newWord = firstLetter.upper()  #E E U P
    for index in range(1,len(word)): #Empieza en 1 para que no reescriba la primera letra de la palabra
        element = word[index] #sta s na rueba
        newWord += element #Esta Es Una Prueba
    newText.append(newWord)
print(' '.join(newText))
