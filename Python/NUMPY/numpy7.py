# Ejercicio 2: Producto más vendido por mes
# 📌 Objetivo: Encontrar qué producto se vendió más cada mes.

# Genera una matriz 4x12 con valores aleatorios entre 10 y 100.
# Identifica qué producto (fila) tuvo la mayor venta en cada mes (columna).
# Muestra un array con los índices de los productos más vendidos en cada mes.
# Pista: Usa np.argmax().
import numpy as np
np.random.seed(0)
matriz = np.random.randint(10,100,[4,12])
print(matriz)
sumaMatriz = np.sum(matriz)
matrizIva = sumaMatriz *0.16
totalconIva = sumaMatriz - matrizIva
print("----------------------------------------")
print(f"La suma total de la matriz; {sumaMatriz}")
print(f"La suma final del iva: {matrizIva}")
print(f"La suma total de la matrizcon iva: {totalconIva}")
respuestaFilas = np.argmax(matriz, axis = 1)
print(f"El mayor indice por filas: {respuestaFilas}")
respuestaColumnas = np.argmax(matriz,axis = 0)
print(f"El mayor indice por columnas: {respuestaColumnas}")
print("----------------------------------------")