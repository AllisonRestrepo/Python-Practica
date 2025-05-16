import random
#CLASE DE JUGADOR
#--------------------------------------------
class Jugador:
    def __init__(self, nombre, calle=1):
        self.nombre = nombre
        self.calle = calle
    def desplazar(self, velocidad):
        self.calle += velocidad
    def __str__(self):
        return f""" Nombre -> {self.nombre} 
 Calle  -> {self.calle} """

print(" ---------------JUGADOR----------------")
j1 = Jugador("Luis",10)
print(j1)
j1.desplazar(2)
print(j1)

#CLASE DE ZOMBIES
#--------------------------------------------
class Zombie:
    def __init__(self):
        self.calle = random.randint(10,20)
        self.direccion = random.choice([ "Izquierda", "Derecha"])
    def __str__(self):
        return f"""direccion -> {self.direccion}
Calle -> {self.calle} """
    
    def desplazar (self):
        if self.direccion == "Izquierda":
            self.calle -= random.randint(1,3)
        elif self.direccion == "Derecha":
            self.calle += random.randint(1,3)
    def no_visible(self):
        return (self.calle < 1) or (self.calle >40)

print(" ---------------ZOMBIES----------------")
random.seed(10)
z1 = Zombie()
print(z1)
z1.desplazar()
print(z1)
z2 = Zombie()
print(z2)
z2.desplazar()
print(z2)
z3 = Zombie()
z3.desplazar()
print(z3)
print(z3.no_visible())
while not(z3.no_visible()):
    print("-")
    z3.desplazar()
print(z3.no_visible())
z4 = Zombie()
z4.desplazar()
print(z4)
#### PRINCIPAL
#from objetos import *
import os 
Alli = Jugador("Alli")
os.system("cls")
print("La ciudad esta llena de zombies......")
nombreJugador = input("Digite nombre del jugador: ")
jugador1 = Jugador(nombreJugador)
#print(jugador1.nombre)
horda = []
for z in range(4):
    z = Zombie()
    horda.append(z)
#print(horda)
while True:
    print(f"{jugador1.nombre} estas en la calle: {jugador1.calle}")
    print(f"Hay zombies en las calles: ")
    calles = []
    for z in horda:
        calles.append(z.calle)
    calles.sort()
    print(calles)

    if jugador1.calle>=40:
        print("GANASTE!!!")
        break
    perdio = False

    for z in horda:
        if z.calle ==jugador1.calle:
            perdio = True
            break

    if perdio:
        print("PERDISTE!!!")
        break
#desplazamiento del jugador 
    velocidad = 0
    while not (1<=velocidad and velocidad <=3):
        velocidad = int(input("Digite desplazamiento (1,2,3): "))

    jugador1.desplazar(velocidad)
    # desplazamiento de los zombies
    for z in horda:
        z.desplazar()
