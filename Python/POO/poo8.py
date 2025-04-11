class Punto:
    def __init__(self,coords):
        self.coords=coords
    
    def mostrarPosicion(self):
        c=f"("
        for i in self.coords:
            c+=str(i) + ","
        c+=")"
        return c
    
    def desplazar(self,d):
        for i in range(len(self.coords)):
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
