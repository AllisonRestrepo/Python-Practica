import numpy as np
arreglo = np.array([[1,2,3,4,5,6],
                   [2,4,5,3,6,7,],
                   [5,3,7,8,9,0,]])

totalArreglo = np.sum(arreglo)
print(totalArreglo)
total = (np.sum(arreglo[:,3]))