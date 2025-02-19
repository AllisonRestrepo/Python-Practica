#conjuntos, no puede tener colecciones dentro de los conjuntos, ni valores duplicados, es desordenado
conjunto = set() #le avisamos que esto sera un conjunto y uno un diccionario
conjunto = {1,2,3,4}
conjunto.add(8) #lo agrega en cualquier parte del conjunto
conjunto.discard(3) #eliminar un elemento especifico
conjunto.clear() #para limpiar todo el conjunto
print(5 in conjunto)
print(4 not in conjunto)