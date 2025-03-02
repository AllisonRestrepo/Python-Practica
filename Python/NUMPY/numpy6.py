import numpy as np
# Ejercicio 1: Análisis de ventas con IVA
# 📌 Objetivo: Calcular ventas netas y con IVA en diferentes meses.
# Crea una matriz 5x12 con valores aleatorios entre 50 y 500 (representando ventas de 5 productos en 12 meses).
# Calcula el IVA del 19% para cada venta.
# Obtén la venta neta de cada mes (sin IVA).
# Muestra las ventas totales de junio y noviembre, junto con su IVA y venta neta.
np.random.seed(0)
ventas = np.random.randint(50,500,[5,12])
print(ventas)
ivaVentas = np.sum(ventas)*0.19
ventaTtotal = np.sum(ventas)
ventaJulio = (np.sum(ventas[:,5]))
ventaJulioIva = (np.sum(ventas[:,6]))*0.19
ventaNoviembre = (np.sum(ventas[:,10]))
ventaNoviembreiva = (np.sum(ventas[:,10]))*0.19
print(f"ventas totales: {ventaTtotal}")
print(f"ventas totales con iva: {ivaVentas}")
print(f"ventas totales julio: {ventaJulio}")
print(f"ventas totales julio con iva: {ventaJulioIva}")
print(f"ventas totales noviembre: {ventaNoviembre}")
print(f"ventas totales noviembre con iva: {ventaNoviembreiva}")