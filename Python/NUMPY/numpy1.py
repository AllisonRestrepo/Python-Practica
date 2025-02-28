#numpy es POO
import numpy as np
vector =np.array([1,3,6])*3
print(vector)
ventas =np.array ([4, 5, 7, 8, 2, 4, 5, 6, 2, 4, 6, 3])
total = np.sum(ventas)
iva = ventas * 0.16
print(iva)
total_iva = np.sum(iva)
print(total_iva)
ventaFinal = total-total_iva
print(f"Valor sin iva: {total}")
print(f"Valor con iva: {ventaFinal}")