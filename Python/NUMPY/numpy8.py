import numpy as np

# Generar la matriz de ventas (6 productos x 12 meses)
np.random.seed(0)
matriz = np.random.randint(100, 1000, [6, 12])
print("Matriz de ventas:")
print(matriz)

# 1. Promedio de ventas por producto en el año
promedio_por_producto = np.mean(matriz, axis=1)
print("\nPromedio de ventas por producto en el año:")
print(promedio_por_producto)

# 2. Mes con mayor venta total
ventas_por_mes = np.sum(matriz, axis=0)
mes_mayor_venta = np.argmax(ventas_por_mes)
print(f"\nMes con mayor venta total: {mes_mayor_venta + 1}")  # +1 para representar enero como 1

# 3. Total vendido por cada producto en el año
total_por_producto = np.sum(matriz, axis=1)
print("\nTotal vendido por cada producto en el año:")
print(total_por_producto)

# 4. Producto con mayor venta total
producto_mayor_venta = np.argmax(total_por_producto)
print(f"\nProducto con mayor venta total: {producto_mayor_venta + 1}")  # +1 para que sea más legible
