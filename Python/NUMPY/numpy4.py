#Algunas funciones para crear matrices
import numpy as np
unos = np.ones([4,12])
print(unos)
print("--------------------------------------")
ceros = np.zeros([2,10])
print(ceros)
print("--------------------------------------")
#primero va el rango es decir de que numero a qeu numero y luego las medidas de la matriz
random = np.random.randint(0,20,[4,14]) 
print(random)
print("--------------------------------------")
np.random.seed(4) #para fijar las matrices que he hecho random 
print("--------------------------------------")
