import math
diccionario = {"c1":"valor1", "c2":"valor2", "c3":"valor3", "c4":"valor4"}
resp = input("Ingrese una llave : ")
resp2 = input("Ingrese un valor: ")
if resp in diccionario:
    print("-----------------------------")
    print("Si existe en el diccinoario")
    print(f"{resp} : {diccionario[resp]}")
    print(diccionario)
else:
    print("-----------------------------")
    print("Agregado al diccionario correctamente.")
    diccionario[resp] = resp2
    print(diccionario)