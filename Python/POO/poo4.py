import numpy as np
class Estudiante:
    def __init__(self,cod,nombre,notas,carrera,promedio):
        self.cod = cod
        self.nombre = nombre
        self.notas = notas
        self.carrera = carrera
        self.promedio = promedio
#-------------------------------------------------------#
    def presentacion(self):
        return f"Hola, mi nombre es {self.nombre}"
#-------------------------------------------------------#
    #sobre carga del metodo str
    def __str__(self):
        return f"Hola, mi nombre es {self.nombre}"
#-------------------------------------------------------#
Luis = Estudiante(887,"luis",[4,4,5],"sistemas",4)
print(Luis.presentacion())
print(Luis)
#-------------------------------------------------------#  
class Clase:
    def __init__(self,atr1,atr2):
        self.atr1 = atr1
        self.atr2 = atr2
    @classmethod
    def metododeclase(cls):
        return "metodo de la clase", cls
    
print(Clase.metododeclase())    
clase = Clase("a","b")
print(clase.metododeclase())
#-------------------------------------------------------#  
#ejemplo
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def calculate(self):
        return self.width * self.height
#metodo de clase
    @classmethod
    def cuadrado(cls, side_lenght):
        return cls(side_lenght,side_lenght)
    
r1 = Rectangle(4,5)
print(r1.calculate())

r2 = Rectangle(4,5)
print(r2.calculate())

c1 = Rectangle.cuadrado(5)
print(c1.calculate())

c2 = c1.cuadrado(10)
print(c2.calculate())
#-------------------------------------------------------#  
class Student:
    nombre_colegio = "ABC school"
    def __init__(self, nombre,age):
        self.nombre = nombre
        self.age = age

    def __str__(self):
        return f"--------------"
    @classmethod
    def cambiar_colegio(cls,name):
        print(Student.nombre_colegio)
        Student.nombre_colegio = name
        print(Student.nombre_colegio)
jessa = Student("Jessa", 14)
Student.cambiar_colegio("XYZ school")

camila = Student("camila", 13)
print(camila)
Student.cambiar_colegio("HJK school")
print(camila)
#-------------------------------------------------------#  
