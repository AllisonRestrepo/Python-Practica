import numpy as np
import matplotlib.pyplot as plt

print("Temperatura de Pereira")
pe = np.random.seed(0)
pereira = np.random.randint(19,31,[100])
print(pereira)
print("------------------------------------")
print("Temperatura de Manizales")
manizales = np.random.randint(13,23,[100])
print(manizales)
print("------------------------------------")
print("GRAFICO EN VENTANA")
plt.scatter(range(len(pereira)),pereira, color="g",marker="o",label="Valores pereira")
plt.scatter(range(len(manizales)),manizales, color="b",marker="o",label="Valores manizales")
plt.xlabel("Muestras (Índice)")
plt.ylabel("Temperatura (°C)")
plt.title("Variación de Temperatura en Pereira")
plt.legend()
plt.grid()
plt.show()
print("------------------------------------")
print("Las temperaturas que esten dentro de 20 y 25 grados en pereira")
gradosPe = pereira[(pereira>=20) & (pereira<=25)]
print(gradosPe)
print("------------------------------------")
print("Las temperaturas que esten dentro de 20 y 25 grados en manizales")
gradosma = manizales[(manizales>=20) & (manizales<=25)]
print(gradosma)
print("------------------------------------")

pei = np.argmax(pereira)
p = pereira[pei]
man = np.argmax(manizales)
m = manizales[man]
perei =np.argmin(pereira)
pr = pereira[perei]
mani = np.argmin(manizales)
mz = manizales[mani]

print(f"""
Calcular el dia mas caluroso:
Temp mas calurosa pereira: {p}
Temp mas calurosa manizales: {m}
------------------------------------
Calcular el dia mas frio:
Temp mas fria en pereira: {pr}
Temp mas fria en manizales: {mz} """)
print("------------------------------------")

# Gráfica de las temperaturas más altas
print("GRAFICO DE TEMPERATURA MAS ALTA EN P Y M")
plt.scatter(p, p, color="r", marker="o", label="Día más caluroso Pereira")
plt.scatter(m, m, color="m", marker="o", label="Día más caluroso Manizales")
plt.xlabel("Día")
plt.ylabel("Temperatura (°C)")
plt.title("Temperaturas más altas registradas")
plt.legend()
plt.grid()
plt.show()
print("------------------------------------")
print("GRAFICO DE TEMPERATURA MAS BAJA EN P Y M")
# Gráfica de las temperaturas más bajas
plt.scatter(pr, pr, color="c", marker="o", label="Día más frío Pereira")
plt.scatter(mz, mz, color="b", marker="o", label="Día más frío Manizales")
plt.xlabel("Día")
plt.ylabel("Temperatura (°C)")
plt.title("Temperaturas más bajas registradas")
plt.legend()
plt.grid()
plt.show()
print("------------------------------------")

indices_pereira=np.where((pereira>=20) & (pereira<=25))
valores_filtrados_per=pereira[indices_pereira]
indices_manizales=np.where((manizales>=20) & (manizales<=25))
valores_filtrados_man=manizales[indices_manizales]

max_per=np.max(pereira)
max_man=np.max(manizales)
min_per=np.min(pereira)
min_man=np.min(manizales)

max_pereira=np.where(pereira==max_per)
valores_max_per=pereira[max_pereira]
max_manizales=np.where(manizales==max_man)
valores_max_man=manizales[max_manizales]

min_pereira=np.where(pereira==min_per)
valores_min_per=pereira[min_pereira]
min_manizales=np.where(manizales==min_man)
valores_min_man=manizales[min_manizales]

plt.scatter((indices_pereira),valores_filtrados_per, color="m",marker="o",label="Temperaturas entre 20 y 25 en pereira")
plt.scatter((indices_manizales),valores_filtrados_man, color="b",marker="o",label="Temperaturas entre 20 y 25 en manizales")
plt.xlabel("Muestras (Índice)")
plt.ylabel("Temperatura (°C)")
plt.title("Variación de Temperatura en Pereira y Manizales")
plt.legend()
plt.grid()
plt.show()
print("------------------------------------")
promedioP = np.mean(pereira)
promedioM = np.mean(manizales)
print(f"""PROMEDIO EN P Y M:
promedio pereira: {promedioP}
promedio manizales: {promedioM}""")
print("------------------------------------")
print(f"""MAXIMO DE P Y M:
Maximo pereira: {p}
Maximo Manizales: {m}
MINIMO DE P Y M:
Minimo pereira: {pr}
Minimo Manizales: {mz}""")
print("------------------------------------")
desvP = np.std(pereira)
desvM = np.std(manizales)
print(f"""DESVIACION ESTANDAR:
desviacion estandar Pereira: {desvP}
desviacion estandar Manizales: {desvM}""")
print("------------------------------------")
mediaP = np.median(pereira)
mediaM = np.median(manizales)
print(f"""MEDIA P Y M:
Media de pereira: {mediaP}
Media de Manizales: {mediaM} """)
print("------------------------------------")
x = np.linspace(-5,5,100)
funcion = (1) /( 1 + np.exp(-x))
print(funcion)
print("------------------------------------")
A = np.array([[1,2,3,4],[2,3,4,1],[3,4,1,2],[4,1,2,3]])
B = np.array([[10],[12],[13],[14]])

#Calcular Determinante
det = np.linalg.det(A)
print(det)
#Todo eso se puede calcular en una sola funcion 
print("-----------------------")
Z = np.linalg.solve(A,B)
print(Z)
