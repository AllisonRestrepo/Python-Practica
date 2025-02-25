lista1 = [1,2,3,4,5,6,7,9,4,5,6,7]
lista2 = [2,1,4,5,3,6,7,0,3,4,5,6]

#elimine los elementos repetidos de ambas listas
a = set(lista1)
b = set(lista2)

union = list(a | b) #union de ambas listas
soloA = (a - b) #los que esta en a y no en b
soloB = (b - a) #los que esta en b y no en a
interseccion = list(a & b)
print(union)
print(soloA)
print(soloB)
print(interseccion)