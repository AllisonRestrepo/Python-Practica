#atributos
class Alumno:
    __cod__ = 0 #atributo privado
    nombre = "" #atributo publico
    edad = 0
    estatura = 0
    materias = []

print(Alumno)
copia = Alumno
print(copia)
#----------------------------------------------------------------
alumno1 = Alumno() #cree un objeto de la clase alumno
alumno2 = Alumno()
#----------------------------------------------------------------
#una instancia de la clase alunmo
#no se puede poner alunmo.cod porque esta privado
# print(alumno1.edad) #acceder al atributo de edad del objeto1
alumno1.edad = 19
alumno1.nombre = "Allison"
alumno1.estatura = 1.61
alumno1.materias.append("POO") 
alumno1.materias.append ("Bases de datos")
alumno1.materias.append ("Calculo integral")
#----------------------------------------------------------------
print(alumno1.edad)
print(alumno1.nombre)
print(alumno1.estatura)
print(alumno1.materias)