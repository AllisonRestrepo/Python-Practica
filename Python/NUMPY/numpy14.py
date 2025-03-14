import numpy as np
#Allison Mariana Restrepo Palacio 
np.random.seed(0)
print("------------------------------------")
import numpy as np

x = np.random.randint(0, 10)
y = np.sin(x / 2) ** 2  
expresion = 2 * y 
expresion2 = 1 - np.cos(x)

print(f"{expresion} = {expresion2}")

# Punto 5
print("------------------------------------")
print(f"1 - cos({x}) = {expresion2}")
# Punto 6
print("------------------------------------")
vector = np.random.randint(-10,10, 100) 
#le puse de -10 a 10 porque si ponia de -6 a 6, solo iba a moar valores desde -5 y 5
condicion = (vector >= -6) & (vector <= 6)
print(vector[condicion])

