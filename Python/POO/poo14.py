#METODO SUPER
class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return f'vehiculo: color: {self.color}, ruedas: {self.ruedas}'
v1 = Vehiculo('rojo',4)
print(v1)
print("-------------------------------------------------------------")
class Sedan(Vehiculo):
    def __init__(self, color, ruedas,velocidad,cilindraje):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindraje = cilindraje
    def __str__(self):
        return f'Sedan: {super().__str__()}, velocidad: {self.velocidad}, cilindraje: {self.cilindraje}'
s1 = Sedan('blanco',4,200,1600)
print(s1)
print("-------------------------------------------------------------")
class Camioneta(Sedan):
    def __init__(self,color,ruedas,velocidad,cilindraje,carga):
        super().__init__(color,ruedas,velocidad,cilindraje)
        self.carga = carga 
    def __str__(self):
        return f"Camion: {super().__str__()}, carga: {self.carga}"
c1 = Camioneta("rojo",6,300,2000,45)
print(c1)
print("-------------------------------------------------------------")
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas,tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return f'Bicicleta: {super().__str__()}, velocidad: {self.tipo}'
b1 = Bicicleta('blanco',2,"urbano")
print(b1)
print("-------------------------------------------------------------")
class Motocicleta(Bicicleta):
    def __init__(self,color,ruedas,tipo,velocidad,cilindraje):
        super().__init__(color,ruedas,tipo)
        self.velocidad = velocidad
        self.cilindraje = cilindraje
    def __str__(self):
        return f"Motocicleta: {super().__str__()}, cilindraje: {self.cilindraje}"
m1 = Motocicleta("rojo",2,120,500,100)
print(m1)
print("-------------------------------------------------------------")
#lista con los objetos de cada subclase
vehiculos = [v1,s1,c1,b1,m1]
class Catalogo:
    def __init__(self,vehiculos):
        self.vehiculos = vehiculos
    def listar(self):
     for vehiculos in self.vehiculos:
        print(f"-> {vehiculos}")
    def cantRuedas(self,cant_ruedas):
        contador = 0
        for vehiculos in self.vehiculos:
            if vehiculos.ruedas == cant_ruedas:
                contador += 1
                print(f"-> {vehiculos}")
        print(f"Se han encontrado {contador} vehiculos con {cant_ruedas} ruedas")
catalogo = Catalogo(vehiculos)
catalogo.listar()
print("-------------------------------------------------------------")
catalogo.cantRuedas(2)

