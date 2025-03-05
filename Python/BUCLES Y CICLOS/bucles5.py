frase = input("Ingrese una palabra: ").lower()
vocales = "aeiou"
contador = 0

for i in frase:
    if i in vocales:
        contador += 1
print(contador)