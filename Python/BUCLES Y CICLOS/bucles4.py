inicio = int(input("Ingrese el numero de inicio: "))
fin = int(input("Ingrese el numero de fin: "))
for i in range(inicio, fin + 1):
    if i%2 == 0:
        print(i, end = ", ")