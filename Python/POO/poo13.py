class Poligono:
    def __init__(self,b,h):
        self.b = b
        self.h = h
    def P_info(self):
        return "en Poligono" 
class Rectangulo(Poligono):
    def areaR(self):
        return self.b * self.h
class Triangulo(Poligono):
    def areaT(self):
        return self.b * self.h / 2
class TrianguloPolar(Poligono):
    def __init__(self,b,h,angulo):
        super().__init__(b,h)
        self.angulo = angulo
    def areaP(self):
        return self.b * self.h * self.angulo / 2
    
r1 = Rectangulo(20,30)
print(f"El area del cuadrado es: {r1.areaR()}")
t1 = Triangulo(20,30)
print(f"El area del trinagulo es: {t1.areaT()}")
Tpolar = TrianguloPolar(20,30,30)
print('Area del triangulo polar: ', Tpolar.areaP())