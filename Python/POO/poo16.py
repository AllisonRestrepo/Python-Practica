class Electrodomestico:
    colores = ["blanco", "negro", "rojo", "azul", "gris"]
    precios = {"A": 100, "B": 80, "C": 60, "D": 50, "E": 30, "F": 10}

    def __init__(self, precio_base=100, color="blanco", consumo="F", peso=5):
        self.precio_base = precio_base
        self.color = self.comprobarColor(color)
        self.__consumo = self.ConsumoEnergetico(consumo)
        self.__peso = peso
    
    def __str__ (self):
        return f"Contructor-> precio base: {self.precio_base}, color: {self.color}, consumo: {self.consumo}, peso: {self.peso}"
    @classmethod
    def precioYpeso(cls, precio, peso):
        return cls(precio_base=precio, peso=peso)
    @classmethod
    def todosLosAtributos(cls, precio, color, consumo, peso):
        return cls(precio_base=precio, color=color, consumo=consumo, peso=peso)
    def getConsumo(self):
        return self.__consumo
    def setConsumo(self, consumo):
        self.__consumo = self.ConsumoEnergetico(consumo)
    def getPeso(self):
        return self.__peso
    def setPeso(self, peso):
        self.__peso = peso
    @staticmethod
    def ConsumoEnergetico(valor):
        valor = valor.upper()
        if valor in ["A","B","C","D","E","F"]:
            return valor
        return "F"
    @classmethod
    def comprobarColor(cls, color):
        if color.lower() in cls.colores:
            return color.lower
        return "Blanco"

    def PrecioFinal(self):
        precio = self.precio_base
        precio += self.precios.get(self.__consumo, 10)
        if self.__peso <= 19:
            precio += 12
        elif self.__peso <= 49:
            precio += 48
        elif self.__peso <= 79:
            precio += 70
        else:
            precio += 110
        return precio
    
class Nevera(Electrodomestico):
    def __init__(self, precio_base=100, color="blanco", consumo="F", peso=5, carga = 5, Tecnologia = "No Frost"):
        super().__init__(precio_base=100, color="blanco", consumo="F", peso=5)
        self.carga = carga 
        self.Tecnologia = Tecnologia
    def __str__ (self):
        return f"Contructor-> precio base: {self.precio_base}, color: {self.color}, consumo: {self.consumo}, peso: {self.peso}, carga: {self.carga}, tecnologia: {self.tecnologia}"
    @classmethod
    def precio_peso(cls, precio, peso):
        return cls(precio_base=precio, peso=peso)
    
class tv(Electrodomestico):
    def __init__(self, precio_base=100, color="blanco", consumo="F", peso=5, resolucion = 20, sintonizador = False ):
        super().__init__(precio_base=100, color="blanco", consumo="F", peso=5)
        self.resolucion = resolucion
        self.sintonizador = sintonizador 
    def __str__ (self):
        return f"Contructor-> precio base: {self.precio_base}, color: {self.color}, consumo: {self.consumo}, peso: {self.peso}, resolucion: {self.resolucion}, sintonizador: {self.sintonizador}"

p1 = Nevera()
p2 = tv()
print(isinstance(p1,Nevera))
print(isinstance(p1,tv))

electrodomestico1 = Electrodomestico(120, "rojo","A",30)
print(f"Electrodomestico 1: {electrodomestico1.atributos}, {electrodomestico1.getatributos}")

electrodomestico2 = Electrodomestico(200, "No Frost", True, 30)
electrodomestico2.setatributos("A",45)
print(f"Electrodomestico 2: {electrodomestico2.getatributos}")


