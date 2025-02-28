tupla = (10,3,"AB",4,"CD",10,-2)
print("--------TUPLA---------")
print(tupla)
print("----------------------")
print(f"1) {tupla[1:4]}")
print(f"2) {tupla[3:]}")
print(f"3) {tupla[:2]}")
print(f"4) {tupla[-1]}")
print(f"5) {tupla[-2]}")

lista = [1,2,3,4]
print("--------LISTA---------")
print(lista)
print("----------------------")
lista.append([4,5,6])
print(f"1) {lista}")
lista.remove(2)
lista.pop()
print(f"2) {lista}")

diccionario = {"c1":"valor1", "c2":"valor2", "c3":"valor3", "c4":"valor4"}
print("--------DICCIONARIO---------")
print(diccionario)
print("----------------------")
print(diccionario.get("green"))
print(diccionario.get("c1"))
print(diccionario.get("c3"))
print(diccionario.get("valor3"))
print("----------------------")
resp = input("Ingrese un color : ")
if resp not in diccionario:
    print("No existe en el dicionario.")
    llave = input("Ingrese la nueva llave: ")
    valor = input("Ingrese el nuevo valor: ")
    diccionario[llave] = valor
    print(diccionario)
else:
    print(f"Clave {resp} -> valor: {diccionario[resp]}")