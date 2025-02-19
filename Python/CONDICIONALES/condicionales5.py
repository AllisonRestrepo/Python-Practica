#7:34
operacion = input("""Elija una opcion entre : 
* Suma
* Resta
* Multiplicacion
* Division 
-----------------------------------
""")
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

if operacion == "Suma":
    suma = num1 + num2
    print(suma)
elif operacion == "Resta":
    resta = num1 - num2
    print(resta)
elif operacion == "Multiplicacion":
    multiplicacion = num1 * num2
    print(multiplicacion)
elif operacion == "Division":
    division = num1 * num2
    print(division)