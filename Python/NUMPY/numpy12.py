import numpy as np

#Solucion de sistemas lineales
A = np.array([[2,3],[4,-1]])
B = np.array([[8],[2]])
X = np.dot(np.linalg.inv(A),B)
print(X)
#Todo eso se puede calcular en una sola funcion 
print("-----------------------")
Z = np.linalg.solve(A,B)
print(Z)
#Calcular Determinante
det = np.linalg.det(A)
print(det)