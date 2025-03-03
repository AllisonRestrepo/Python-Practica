import numpy as np

# Generar la matriz de ventas 5x12 con valores entre 50 y 800
np.random.seed(0)
ventas = np.random.randint(50, 800, (5, 12))

print("Matriz de ventas:\n", ventas)

# Calcular la diferencia de ventas mes a mes
diferencias = np.diff(ventas, axis=1)  # Resta cada mes con el anterior

print("\nDiferencia de ventas mes a mes:\n", diferencias)

# Encontrar los meses con mayor y menor crecimiento en ventas
mayor_crecimiento = np.argmax(np.sum(diferencias, axis=0)) + 1  # +1 porque diff reduce una columna
menor_crecimiento = np.argmin(np.sum(diferencias, axis=0)) + 1

print(f"\nEl mes con mayor crecimiento es el mes {mayor_crecimiento}")
print(f"El mes con menor crecimiento es el mes {menor_crecimiento}")
