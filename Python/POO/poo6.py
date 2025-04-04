class Convercion:
    def __init__(self,temperatura):
        self.temperatura = temperatura
    @classmethod
    def celafa(cls,temperatura):
        return cls(temperatura *1.8 +32)
    def __str__(self):
        return f"------{self.temperatura}--------"
    
c1 = Convercion(30)
print(c1)
c2 = Convercion.celafa(10)
print(c2)

#-----------------------------------------------------#
class Persona:
    num_instancias = 0
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def instancias(cls,nombre,edad):
        Persona.num_instancias += 1
        return cls(nombre,edad)
    
    def __str__(self):
        return f"------{Persona.num_instancias}--------"
c3 = Persona.instancias("allison",20)
c4 = Persona.instancias("sofia",20)
print(c3)
print(c4)
print(Persona.num_instancias)
#------------------------------------------------------#

class Validador:
    contrasena ="locolocoloco"
    def __init__(self,contrasena):
        self.contrasena = contrasena
    @classmethod
    def comprobar(cls,contrasena):
        if len (contrasena) >= 8:
            return f"{cls(contrasena)}"
        else:
            return("contrasena invalida")
    def __str__(self):
        return f"------{self.contrasena}--------"
n1 = Validador.comprobar("Hello")
print(n1)
n2 = Validador.comprobar("holacomoestasamiga")
print(n2)
#------------------------------------------------------#