import numpy as np
np.random.seed(1)
matriz = np.random.randint(100,1000,[6,12])
print(matriz)

#sacarle el promedio a cada fila
promedioFila = np.round(np.mean(matriz, axis = 0))
print(promedioFila)

#Sacar el mas alto de los promedios
MayorPromedio = np.max(promedioFila)
print(MayorPromedio)
