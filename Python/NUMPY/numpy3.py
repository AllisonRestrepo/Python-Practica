import numpy as np
#crear una matriz 4*12 con valores arbitrarios 
ventas =np.array ([[1,2,3,4,5,6,7,8,9,10,11,12],
                [3,2,5,7,3,5,8,9,6,7,2,4],
                [2,4,3,5,21,7,34,9,10,3,7,11],
                [34,26,11,3,5,8,3,6,14,16,8,3]])

iva = ventas * 0.16
total_iva = np.sum(iva)
ventaTotal = (np.sum(ventas))-total_iva

ventaMarzo = np.sum(ventas[:,2])
ivaMarzo = ventaMarzo * 0.16
ivaTotalMarzo = np.sum(ivaMarzo)
totalMarzo = ventaMarzo -ivaTotalMarzo

ventaDiciembre = np.sum(ventas[:,11])
ivaDiciembre = ventaDiciembre * 0.16
ivaTotalDiciembre = np.sum(ivaDiciembre)
totalDiciembre = ventaDiciembre -ivaTotalDiciembre
print("-----------------------------------")
print(f"Las ventas totales es de: {ventaTotal}")
print(f"Las ventas totales de marzo es de: {totalMarzo}")
print(f"Las ventas totales de diciembre es de: {totalDiciembre}")
print("-----------------------------------")
#Se podia haer todas las operaciones anteriores con solo una linea por cada uno
ventaNeta = (np.sum(ventas[:])-(np.sum(ventas[:]*0.16)))
print(f"La venta neta de todos los meses: {ventaNeta}")
ventaNetaMarzo = (np.sum(ventas[:,2])-(sum(ventas[:,2]*0.16)))
print(f"La venta neta de marzo es: {ventaNetaMarzo}")
ventaNetaDiciembre = ((np.sum(ventas[:,11])-(np.sum(ventas[:,11]*0.16))))
print(f"La venta neta de diciembre es: {ventaNetaDiciembre}")
print("-----------------------------------")

ivaVentas = ventas*0.16
VentasNetas1 = ventas-ivaVentas
ventastotalesnetas = np.sum(VentasNetas1)
print(ventastotalesnetas)
print(np.sum(VentasNetas1[:,2]))
print(np.sum(VentasNetas1[:,11]))
