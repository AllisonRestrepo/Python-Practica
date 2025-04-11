class Producto:
    def __init__(self, codigo, nombre, descripcion, precio):
        self.__codigo = codigo  # atributo privado
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

    def get_codigo(self):
        return self.__codigo

    def __str__(self):
        return f"Código: {self.__codigo} | Nombre: {self.nombre} | Descripción: {self.descripcion} | Precio: ${self.precio}"

# Lista de inventario (producto + cantidad)
inventario = [
    {"producto": Producto("001", "Pan", "Pan integral", 1500), "cantidad": 10},
    {"producto": Producto("002", "Leche", "Leche deslactosada", 3000), "cantidad": 5},
    {"producto": Producto("003", "Huevos", "Docena de huevos", 7000), "cantidad": 3}
]

# Función para mostrar inventario
def mostrar_inventario():
    print("\n Inventario actual:")
    for item in inventario:
        print(item["producto"], f"| Cantidad: {item['cantidad']}")
    print()

# Función para agregar un nuevo producto
def agregar_producto():
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad en inventario: "))

    nuevo = Producto(codigo, nombre, descripcion, precio)
    inventario.append({"producto": nuevo, "cantidad": cantidad})
    print("Producto agregado con éxito.\n")

# Función para calcular el total del inventario
def calcular_total():
    total = 0
    for item in inventario:
        total += item["producto"].precio * item["cantidad"]
    print(f"Total del inventario: ${total}\n")

# Menú
while True:
    print("==== MENÚ ====")
    print("1. Ver inventario")
    print("2. Agregar producto")
    print("3. Calcular total")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        mostrar_inventario()
    elif opcion == "2":
        agregar_producto()
    elif opcion == "3":
        calcular_total()
    elif opcion == "4":
        print(" Hasta luego")
        break
    else:
        print(" Opción no válida\n")
