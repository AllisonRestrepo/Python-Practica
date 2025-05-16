class A:
    def __init__(self):
        print("contruyendo A")
    def a (self):
        return "Metodo de A"
class B:
    def __init__(self):
        print("Contruyendo B")
    def b(self):
        return "Metodo B"
class C (A,B):
    def __init__(self):
        print("contruyendo c")
    def c(self):
        return "Metodo C"

class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
class carrera:
    def __init__(self,nombre_carrera, duracion):
        self.nombre_carrera = nombre_carrera
        self.duracion = duracion
    def __Str__(self):
        return self.nombre, self.edad, self.nombre_carrera, self. duracion
class estudiante(persona, carrera):
    def __init__(self, nombre, edad, nombre_Carrera, duracion):
        persona.__init__(self, nombre, edad)
        carrera.__init__(self, nombre_Carrera, duracion)
    def presentacion(self):
        return f"mi nombre es {self.nombre}, tengo {self.edad} anos, estudio {self.nombre_carrera} que tiene una duracion de {self.duracion} anos"
    #estudiante.mro()