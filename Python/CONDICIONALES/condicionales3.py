num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))

if num1%2 == 0 and num2 %2 == 0:
    print("ambos son numeros pares")
elif num1 %2 ==0 and num2%2 !=0:
    print(f"Solo {num1} es par")
elif num1 %2 !=0 and num2%2 ==0:
    print(f"Solo {num2} es par")
else:
    print("ambos son impares")