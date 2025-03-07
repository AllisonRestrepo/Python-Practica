import numpy as np
# arreglo = np.array([[2,4,-1],[2,4,0],[2,4,2]])
# print(arreglo)
# print(arreglo-4)
# print(arreglo*4)
# M = arreglo=np.eye(3)*2
# print(M)

#Multiplicacion escalar
#Multiplicacion Elemento a elemento
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print("---------------------")
print(f"A:{A}")
print(f"B:{B}")
print("---------------------")
C = A*B #Elemento a Elemento
print(C)

#Multiplicacion Matricial - Producto punto
print("---------------------")
D = np.dot(A,B) #Para multiplicar de manera algebraica, fila con columna
F = np.dot(B,A)
print(D)
print(F)
