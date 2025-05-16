# class Component:
#     def __init__(self, at):
#         self.at = at # component attribute
#         print("Component object created")
#     def m1 (self):
#         print("Component method")

# c1 = Component("Componente 1")
# print(c1.at)
# c1.m1() 

# class Composite:
#     def __init__ (self):
#         self.obj1 = Component("componente 1")
#         print("Composite was created")
#     def m2 (Self):
#         print("Composite method")

# compuesta = Composite()
# print(compuesta.obj1.at)
# compuesta.obj1.m1
# compuesta.m2()

# #ALTERNATIVA DE LA CLASE COMPUESTA

# class Composite:
#     def __init__ (self,obj1):
#         self.obj1 = obj1
#         print("Composite was created")
#     def m2 (Self):
#         print("Composite method")

# obj3 = Component("Atributo")
# compuesta2 = Composite(obj3)
# print(compuesta2.obj1.at)

# class Empleado:
#     def __init__(self,id,name,address):
#         self.id = id
#         self.name = name
#         self.address = address

# class Direccion:
#     def __init__(self,street,street2,city,state,zipcode):
#         self.street = street
#         self.street2 = street2
#         self.city = city
#         self.state = state
#         self.zipcode = zipcode

# direccion1 = Direccion("Calle 141", "#15-32", "Pereira", "Risaralda", 346)
# empleado1 = Empleado(123, "Allison", direccion1)
# print(empleado1.address.city)
# print(direccion1.street)
# #-------------------------------------------------
# class Engine:
#     def start(self):
#         print("Engine started")
#     def stop(self):
#         print("Engine stopped")

# class Car:
#     def __init__(self):
#         self.engine = Engine()
#     def start_car(self):
#         self.engine.start()
#     def stop_car(self):
#         self.engine.stop()

# #create car objet 
# my_car = Car()
# my_car.start_car()
# my_car.stop_car()
# #------------------------------------------------
# class Habitacion:
#     def __init__(self, area, color):
#         self.area = area
#         self.color = color

# class CentroDV:
#     def __init__(self, recepcion, bano):
#         self.recepcion = recepcion
#         self.bano = bano

# class Recepcion(Habitacion):
#     def registrar_llamadas(self):
#         print("LLamada en curso")
# class Bano(Habitacion):
#     def disponibilidad(self):
#         print("Revisando la disponibilidad")

# recepcion = Recepcion(32, "Blanco")
# bano = Bano(54, "Verde")
# centro = CentroDV(recepcion, bano)

# print(centro.bano.area)

#------------------------------------------------
class Punto:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def desplazar(self,dx,dy):
        self.x+=dx
        self.y+=dy
    
    def __str__(self):
        return f"({self.x}, {self.y})"

class Linea:
    def __init__(self,punto1,punto2):
        self.punto1=punto1
        self.punto2=punto2

    def desplazar(self,dx,dy):
        self.punto1.desplazar(dx,dy)
        self.punto2.desplazar(dx,dy)

    def __str__(self):
        return f"punto 1: {self.punto1}, punto 2: {self.punto2}"

class Poligono:
    def __init__(self,lineas):
        self.lineas=lineas
    def desplazar(self,dx,dy):
        for linea in self.lineas:
            linea.desplazar(dx,dy)

    def mostrar(self):
        for index,linea in enumerate((self.lineas), start=1):
            print(f"linea {index} : {linea}")

class Figura:
    def __init__(self,poligonos):
        self.poligonos=poligonos

    def desplazar(self,dx,dy):
        for poligono in self.poligonos:
            poligono.desplazar(dx,dy)
    
    def mostrar(self):
        for poligono in self.poligonos:
            poligono.mostrar()
            


punto1= Punto(0,0)
print(punto1)
# punto1.desplazar(-4,5)
# print(punto1)
punto2=Punto(4,4)
punto3=Punto(2,3)
punto4=Punto(1,2)

linea1=Linea(punto1,punto2)
print(linea1)
linea1.desplazar(2,0)
print(linea1)
linea2=Linea(punto3,punto4)

poligono=Poligono([linea1,linea2])
print("Poligono 1")
poligono.mostrar()
poligono.desplazar(2,2)
print("Poligono desplazado")
poligono.mostrar()

print("Figura 1")
figura=Figura([poligono])
figura.mostrar()
print("figura desplazada")
figura.desplazar(2,2)
figura.mostrar()

p1=Punto(2,4)
p2=Punto(4,4)
p3=Punto(6,3)
p4=Punto(4,2)
p5=Punto(2,2)

# l1=Linea(p1,p2)
# l2=Linea(p2,p3)
# l3=Linea(p3,p4)
# l4=Linea(p4,p5)
# l5=Linea(p5,p1)

l1=Linea(Punto(2,4),Punto(4,4))
l2=Linea(Punto(4,4),Punto(6,3))
l3=Linea(Punto(6,3),Punto(4,2))
l4=Linea(Punto(4,2),Punto(2,2))
l5=Linea(Punto(2,2),Punto(2,4))

poligono2=Poligono([l1,l2,l3,l4,l5])
poligono2.mostrar()
poligono2.desplazar(10,0)
print("--------------------------------------------")
figuras=Figura([poligono2])
figuras.mostrar()

