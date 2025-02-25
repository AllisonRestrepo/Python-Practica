#for
for i in [1,2,3,4,5]:
    print(f"elemento: {i}")
print("------------------")
coleccion = {"Alli":22,"maria":13,"jose":40}
for i in coleccion:
    print(f"elemento: {i}")
print("------------------")
for i in coleccion:
    print(f"clave: {coleccion[i]}")
print("------------------")
for i in coleccion:
    print(f"Clave: {i} -> valor: {coleccion[i]}")
print("------------------")
for clave,valor in coleccion.items():
    print(f"{clave} -> {valor}")
print("------------------")
col = "allison"
for i in col:
    print(f"{i}", end= " ")