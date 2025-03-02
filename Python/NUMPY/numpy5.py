import numpy as np
#analisis exploratorio de datos
np.random.seed(0)
datos = np.random.randint(15,30,30)
print(datos)
promedio = np.mean(datos)
print(promedio) #promedio de la matriz
print(np.max(datos))
print(np.min(datos))
print(np.median(datos)) #para ver que valor se repite
print("------------------------------")
condicion = (datos>=18) & (datos<=22)
print(condicion)
print(np.sum(condicion))
print("------------------------------")
