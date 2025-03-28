class Alumno:
    def __init__(self, *args): #método (constructor) es de objeto, se convirte en un metodo de objeto cuando se le añade la palabra self
        # self.__cod=cod #atributo de objeto (se intancia cuando se crea el objeto) (privado)
        # self.nombre= nombre
        # self.edad=edad
        # self.estatura=estatura
        # self.materias=materias 
        if len (args)==2:
            self.cod=""+args[0]
            self.nombre=""+args[1]
            self.edad=0
            self.estatura=0
            self.materias=[]
        elif len (args)==4:
            self.cod=""+args[0]
            self.nombre=""+args[1]
            self.edad=args[2]
            self.estatura=args[3]
            self.materias=[]
        elif len(args)==5:
            self.cod=""+args[0]
            self.nombre=""+args[1]
            self.edad=args[2]
            self.estatura=args[3]
            self.materias=args[4]


    def matricular(self, materia):
        self.materias.append(materia)

    def cancelarMateria(self,materia):
        if materia in self.materias:
            self.materias.remove(materia)
        else:
            return('La materia no existe')
        


alumno1=Alumno("1223","Sofia")
print(f"imprimiendo el objeto: {alumno1.nombre}, {alumno1.materias}")

alumno2=Alumno("1223","Sofia",12,1.7)
print(f"imprimiendo el objeto: {alumno2.nombre}, {alumno2.materias}")

alumno3=Alumno("1223","Sofia",12,1.7,["POO","Bases de datos"])
print(f"imprimiendo el objeto: {alumno3.nombre}, {alumno3.materias}")


    

# juan=Alumno(123,'juan', 20, 1.6, []) #llamando al constructor (__init__)


# print(f"imprimiendo el objeto juan: {juan.nombre}, {juan.materias}")
# #print(Alumno.nombre) Error, la clase alumno no tiene un atributo de clase llamado nombre

# juan.matricular("POO") #Agregar materia al objeto juan
# juan.matricular("Bases de datos")
# print(f"imprimiendo el objeto juan: {juan.nombre}, {juan.materias}")

# print(juan.cancelarMateria("calculo")) #Cancelar materia del objeto juan
# print(f"imprimiendo el objeto juan: {juan.nombre}, {juan.materias}")
    #metodos (de clase) No funciona en los objetos
    # def matricular(self,materia:str):
    #     self.materias.append(materia)

    # #metodo de instancia
    # def matricular(self,materia:str):
    #     #atributo de instancia
    #     self.materias.append(materia)

# alumno2=Alumno()
# alumno2.nombre="Maria"
# alumno2.matricular("POO")
# alumno2.matricular("Cálculo")
# alumno2.matricular("IA")

# print(alumno2.materias)


# print(Alumno)
# copia =Alumno
# print(copia)
# alumno1=Alumno()
# print(alumno1)

# alumno2=Alumno()
# print(alumno2)


# print(alumno1.edad) #Acceder al atributo edad del objeto alumno1
# alumno1.edad=19
# print(alumno1.edad)
# alumno1.estatura=1.7
# alumno1.nombre="Luis"
# # alumno1.__cod no puedo acceder directamente a un atributo privado
# alumno1.materias.append ("POO")
# alumno1.materias.append ("Bases de datos")
# alumno1.materias.append("Cálculo integral")

# print(alumno1.materias)

#---------------------------------------------------------------------------------------------------
#21 marzo 
#Ejemplo sobrecarga de constructores
#1. Multiples argumentos (tipo de atributos)

class Clase:
    def __init__(self, *args):
        if isinstance(args[0], int):
            self.argumento=args[0]
        if isinstance(args[0],str):
            self.argumento=""+args[0]

c1=Clase(1)
print(c1.argumento)

c2=Clase("Uno")
print(c2.argumento)

c3=Clase("2")
print(c3.argumento)

#2. Cantidad de atributos 

class Clase:
    def __init__(self,*args):
        if len(args)>2:
            self.argumento="mas de dos argumentos"
        elif len(args)==2:
            self.argumento="dos argumentos"
        else:
            self.argumento="menos de dos argumentos"

c1=Clase(1)
print(c1.argumento)

c2=Clase(1, "hola")
print(c2.argumento)

c3=Clase(1,"hola",[1,2,3])
print(c3.argumento)


#Ejercicio
#En la clase alumno crear los siguientes constructores:
#1. Crer el objeto con cod y nombre
#2. cod, nombre, edad y estatura
#3. cod,nombre,edad,estatura, materias


#Atributos de clase y de objeto
class Perro:
    #Atributo de clase (atributo comun)
    especie="mamifero"
    #constructor
    def __init__(self, nombre, raza):
        self.nombre=nombre
        self.raza=raza
        print(f"creando objeto...{self.nombre}, {self.raza}")

mascota=Perro("Newton", "Snaucer")
print(mascota.especie)

        
mascota2=Perro("Tony", "San bernardo")
print(mascota2.especie)

#Otro ejemplo
class Coche:
    ruedas=4 #Atributo de clase

    def __init__(self, color, aceleracion): #constructor con atributos del objeto o instancia
        self.color=color
        self.aceleracion=aceleracion
        self.velocidad=0

    def acelerar(self):
        self.velocidad=self.velocidad + self.aceleracion
    
    def frenar(self):
        v=self.velocidad - self.aceleracion
        if v<0:
            v=0
        self.velocidad= v

    
vehi=Coche("Azul", 10)
vehi.acelerar()
vehi.acelerar()
vehi.frenar()
vehi.velocidad
c1=Coche("Rojo", 20)
c2=Coche("Azul", 20)

# Coche.ruedas=6 = si cambio el valor de ruedas de la clase se cambia para todos los objetos

print(f"vehi= {vehi.color}, {vehi.aceleracion}, {vehi.velocidad}, {vehi.ruedas}")
print(f"c1= {c1.color}, {c1.aceleracion}, {c1.velocidad}, {vehi.ruedas}")
print(f"c2= {c2.color}, {c2.aceleracion}, {c2.velocidad}, {vehi.ruedas}")

#Ejercicio 1
class Ecuacion:
    def __init__(self, a, b, c):
        self.a=a
        self.b=b
        self.c=c

    def calcularDiscriminante(self):
        discriminante=(self.b)**2 - 4*(self.a)*(self.c)
        return discriminante

    def CalucularEcuacion(self):
        determinante=self.calcularDiscriminante()
        if determinante < 0:
            return ("Determinante menor a 0")
        if determinante == 0:
            x=(-(self.b)+(determinante)**(1/2))/(2*self.a)
            return x
        if determinante>0:
            X1=(-(self.b)-(determinante)**(1/2))/(2*self.a)
            X2=(-(self.b)+(determinante)**(1/2))/(2*self.a)
            return (X1,X2)
    

ec1=Ecuacion(1,2,1)
print(ec1.CalucularEcuacion()) #-1.0


ec2=Ecuacion(1,3,1)
print(ec2.CalucularEcuacion()) #-0.382  -2.618


ec3=Ecuacion(3,1,1)
print(ec3.CalucularEcuacion()) #raices complejas


#Ejercicio  2
class Estudiante:
    def __init__(self, nombre, carrera, notas):
        self.nombre=nombre
        self.carrera=carrera
        self.notas=notas
        self.promedio=0
    def calcularPromedio(self):
        porcentajes=[]
        if len(self.notas) <= 3:
            return ("Error")
        elif len(self.notas)==4:
            for i in range (len(self.notas)):
                Porcentaje=float(input("Ingrese el porcentaje de la nota: "))
                porcentajes.append(Porcentaje)
            promedio=self.notas[0]*porcentajes[0] + self.notas[1]*porcentajes[1] + self.notas[2]*porcentajes[2] + self.notas[3]*porcentajes[3]
            self.promedio=promedio
            return promedio
        
        elif len(self.notas)==5:
            for i in range (len(self.notas)):
                Porcentaje=float(input("Ingrese el porcentaje de la nota: "))
                porcentajes.append(Porcentaje)
            promedio=self.notas[0]*porcentajes[0] + self.notas[1]*porcentajes[1] + self.notas[2]*porcentajes[2] + self.notas[3]*porcentajes[3] + self.notas[4]*porcentajes[4]
            self.promedio=promedio
            return promedio

        elif len(self.notas)==6:
            for i in range (len(self.notas)):
                Porcentaje=float(input("Ingrese el porcentaje de la nota: "))
                porcentajes.append(Porcentaje)
            promedio=self.notas[0]*porcentajes[0] + self.notas[1]*porcentajes[1] + self.notas[2]*porcentajes[2] + self.notas[3]*porcentajes[3] + self.notas[4]*porcentajes[4] + self.notas[5]*porcentajes[5]
            self.promedio=promedio
            return promedio
        
        elif len(self.notas)>=6:
            promedio=(sum(self.notas))/len(self.notas)
            self.promedio=promedio
            return promedio

    def presentacion(self):
        return f"mi nombre es {self.nombre}, estudio {self.carrera} y mi promedio de notas es de: {self.calcularPromedio()}"
        
            
estudiante0=Estudiante("Carlos","sistemas",[5.0,2.5,3.0])
print(estudiante0.presentacion())

        

estudiante1=Estudiante("Sofia","sistemas",[5.0,2.5,3.0,4.0]) #25 25 25 25
print(estudiante1.presentacion())


estudiante2=Estudiante("Juan","sistemas",[5.0,2.5,3.0,4.0,3.0]) #20 20 20 20 20
print(estudiante2.presentacion())

estudiante3=Estudiante("Paulina","sistemas",[5.0,2.5,3.0,4.0,3.0,2.5])#10 20 10 15 20 25
print(estudiante3.presentacion())


estudiante4=Estudiante("Pedro","sistemas",[5.0,2.5,3.0,4.0,3.0,5.0,2.0])
print(estudiante4.presentacion())














            

        
            







    


            

        
    


        
    





    





