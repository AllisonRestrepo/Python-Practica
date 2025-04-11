#que tan restringidos estan los atributos normal es publico, con una linea abajo es protegido y con dos abajo es privado
class Empleado:
    def __init__(self,nombre, salario):
        self.nombre = nombre
        self.__salario = salario
    def getSalary(self):
        return self.__salario
    def setSalary(self , s):
        self.__salario=s

e1 = Empleado("Allison",1000)
print(e1.nombre)
print(e1.getSalary())
e1.setSalary(1200)
print(e1.getSalary())
#---------------------------------------#
class Punto:
    def __init__(self,coords):
        self.__coords=coords
    
    def mostrarPosicion(self):
        c=f"("
        for i in self.coords:
            c+=str(i) + ","
        c+=")"
        return c
    
    def desplazar(self,d):
        for i in range(len(self.__coords)):
            self.__coords[i]+= d[i]
        
    @staticmethod
    def distancia(punto1,punto2):
        distancia=0
        for i in range (len(p1.coords)):
            distancia+=(punto2.coords[i]-punto1.coords[i])**2
        distancia=distancia**(1/2)
        return distancia


p1=Punto([2,7,0])
print(p1.mostrarPosicion())
p2=Punto([6,10,0])
print(p2.mostrarPosicion())
print(Punto.distancia(p1,p2))
