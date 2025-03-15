#metodos en poo
class Alumno:
    __cod__ = 0 #atributo privado
    nombre = "" #atributo publico
    edad = 0
    estatura = 0
    materias = []

#para matricular materias
#metodo de instancia son los que funcionan, es decir, pornerle self
    def matricular (self, materias):
        #atributo de instancia
        self.materias.append(materias)

#matriculando una materia 
alumno1 = Alumno()
alumno1.matricular("POO")
print(alumno1.materias)