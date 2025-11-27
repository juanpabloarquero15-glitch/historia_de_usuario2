
# 1. Lista de productos

inventario = [] #variable que crea una lista


# 2. Función para agregar productos

def agregar_producto():
    while True:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if nombre == "":
            print("El nombre no puede estar vacío.")
            continue
        elif nombre.isdigit():
            print("El nombre no puede ser un número.")
            continue
        break

    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio < 0:
                print("El precio no puede ser negativo.")
                continue
            break
        except:
            print("Entrada inválida. Ingrese un número.")

    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
                continue
            break
        except:
            print("Entrada inválida. Ingrese un entero.")

    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)
    print("Producto agregado con éxito.\n")


# 3. Función para mostrar inventario

def mostrar_inventario():
    if not inventario:
        print("El inventario está vacío.")
        return

    print("\n--- Inventario ---")
    for i, producto in enumerate(inventario, start=1):
        print(f"{i}. Nombre: {producto['nombre']}, Precio: {producto['precio']:.2f}, Cantidad: {producto['cantidad']}")


# 4. Función para calcular estadísticas

def calcular_estadisticas():
    total_productos = len(inventario)
    valor_total = sum(p['precio'] * p['cantidad'] for p in inventario)
    precio_promedio = valor_total / total_productos if total_productos > 0 else 0

    print("\n--- Estadísticas ---")
    print(f"Total de productos: {total_productos}")
    print(f"Valor total del inventario: {valor_total:.2f}")
    print(f"Precio promedio por producto: {precio_promedio:.2f}")


# 5. MENÚ PRINCIPAL

while True:
    print("\n--- Menú de Inventario ---")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        if inventario:
            calcular_estadisticas()
        else:
            print("El inventario está vacío. No se pueden calcular estadísticas.")
    elif opcion == "4":
        print("Saliendo del sistema.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")