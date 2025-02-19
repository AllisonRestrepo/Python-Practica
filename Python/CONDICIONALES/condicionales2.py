#condicional anidado es un condicional dentro de otro
edad = int(input("Ingrese su edad: "))
if 0<edad<100:
    print("Edad aceptada")
    if edad >=18:
        print("es mayor de edad")
    else:
        print("Es menor de edad")
else:
    print("La edad no es aceptada")