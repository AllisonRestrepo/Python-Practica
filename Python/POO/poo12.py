#HERENCIA 
class Ave:
    pass
class Ganso(Ave):
    pass
class Pato(Ave):
    pass
p1 = Pato()
print(isinstance(p1,Pato))
print(isinstance(p1,Ave))
print(isinstance(p1,Ganso))
print(issubclass(Pato,Ave))
print(issubclass(Ave,Pato))
print(issubclass(Pato,Ganso))
#--------------------------------#
class Rectangulo:
    def __init__(self,b,h):
        self.b = b
        self.h = h
    def area(self):
        return self.b * self.h 
    
class Triangulo:
    def __init__(self,b,h):
        self.b = b
        self.h = h
    def areaT(self):
        return self.b * self.h / 2
        
r1 = Rectangulo(20,30)
print(f"El area del cuadrado es: {r1.area()}")

t1 = Triangulo(20,30)
print(f"El area del trinagulo es: {t1.areaT()}")

