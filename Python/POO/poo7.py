#static method
class Clase:
    @staticmethod
    def metodoEstatico():
        return "Metodo estatico"
obj = Clase()
print(obj.metodoEstatico())
#uantificador all if all([0<=i<=5 for i in notas]):
#all equivale para todo  cuantificador de universalidad
#any equivale a que debe existir cuantificaor de existencialidad
class Promedio:
    def __init__(self,notas):
        self.notas = notas
    def mostrarNotas(self):
        return self.notas
    @staticmethod
    def validar_notas(notas):
        for i in notas:
            if not(0<=i<=5):
                return False
        return True
    def __str__(self):
        return f"{self.notas}"
n1 = Promedio.validar_notas([5.0,4.8,3.6])
print(n1)
notas = [3.8,4.0,4.5]
print(Promedio.validar_notas(notas))
Promedio.validar_notas(notas)
#---------------------------------------#
class Punto:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def mostrarPosicion(self):
        return f"({self.x} , {self.y} , {self.z})"
    def desplazar(self,dx,dy,dz):
        self.x += dx
        self.y += dy
        self.z += dz
    @staticmethod
    def distancia(p1,p2):
       distancia = ((p2.x - p1.x)**2 + (p2.y - p1.y)**2)**(1/2)
       return distancia

p1 = Punto(2,7,5)
print(p1.mostrarPosicion())
# p1.desplazar(2,4,5)
print(p1.mostrarPosicion())
p2 = Punto(6,10,1)
print(Punto.distancia(p1,p2))
