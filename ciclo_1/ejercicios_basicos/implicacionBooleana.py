#se puede denir una funcion que permite calcular la operacion condicional
#de un par de variables booleanas y que retorna el resultado de operar los
#valores mediante un condicional, de la siguiente manera
#condicional : B x B --> B
#aqu se tienen dos casos, primero, si el antecedente es verdadero y el
#consecuente es falso, entonces el resultado de aplicar el condicional el
#falso, para cualquier otro caso el condicional es verdadero. En notacion
#matematica esto puede ser escrito de la siguiente manera


#(p,q)---> F, si (e(p)==V) y (e(q)=F)
#          V, en cualquier otro caso

#Forma Python:
def condicional(p,q):
    if p == True and q == False:
        return False
    else:
        return True

#en esta funcion se tiene en cuenta que si la premisa p tiene valor True,
#entonces el resultado esta dado por el valor de la conclusion q, y si el valor
#de p es False, entonces el condicional tendra como valor True.
#Forma más óptima: MÁS INTELIGENTE
def condicional2(p,q):
    if p:
        return q
    return True


print(condicional2(True,False))
print(condicional(True,False))


