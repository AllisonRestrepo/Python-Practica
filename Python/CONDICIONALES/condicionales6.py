saldo = 1000
opcion = int(input("""Ingrese una opcion: 
1) Ingresar dinero en la cuenta
2) Retirar dinero de la cuenta
3) Mostrar dinero disponible
4) Salir
-------------------------------
"""))
if opcion == 1:
    print(f"saldo disponible: {saldo}")
    extra = float(input("Digite la cantidad de dinero que desea ingresar: "))
    total = saldo + extra
    print(f"Dinero total: {total}")
elif opcion == 2:
    print(f"saldo disponible: {saldo}")
    resta = float(input("Digite la cantidad de dinero que desea retirar: "))
    total = saldo - resta
    print(f"Dinero total: {total}")
elif opcion == 3:
    print(f"Dinero total: {saldo}")
elif opcion == 4:
    print("saliendo...")