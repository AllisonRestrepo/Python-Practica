class Fecha:
    def __init__(self,dia,mes,año):
        self.__dia = dia
        self.__mes = mes
        self.año = año
    def getDia(self):
        return self.__dia
    def getMes(self):
        return self.__mes
    def setDia(self,dia):
        self.__dia = dia
    def setMes(self,mes):
        self.__mes = mes
    def __str__(self):
        return f"--------------"

hoy = Fecha(11,4,2025)
print(hoy)