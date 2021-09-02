import numpy as np
a = np.array(list(range(1,5))) # Crea un arreglo lineal
print(type(a)) # Imprime "<class 'numpy.ndarray'>"
print(a)
print(a.shape) # Imprime "(4,)" es de tama~no 4, de 1 dimension
print(a[0], a[1], a[2])
a[0] = -4
print(a)
b = np.array([[1,2,3,5,6],[4,5,6,7,8]]) # Crea un arreglo 2-dimensional
print(b.shape)
print(b)
b[0,0] = 1590
print(b)
print(b[0,0], b[0,1], b[1,0])



#VSCode tiene problemas con las librerías, toca arreglarlo