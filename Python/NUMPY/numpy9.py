import numpy as np
np.random.seed(1)
matriz = np.random.randint(100,1000,[6,12])
print(matriz)

#sacarle el promedio a cada fila
promedioFila = np.mean(matriz, axis = 0)
print(promedioFila)

#sacarle el promedio a cada columna
promedioCol = np.mean(matriz, axis = 1)
print(promedioCol)

#Sacar el mas alto de los promedios
MayorPromedio = np.sum(matriz, axis = 1)

print(MayorPromedio)
135