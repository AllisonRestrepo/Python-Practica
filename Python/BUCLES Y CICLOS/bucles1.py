import math
numero = int(input("Ingrese un numero: "))

while numero <0 or numero>100:
    print("Error -> Deberia de ser un numero positivo")
    numero = int(input("Ingrese un numero: "))

print(f"su raiz cuadrada es: {(math.sqrt(numero)): .2f}")
