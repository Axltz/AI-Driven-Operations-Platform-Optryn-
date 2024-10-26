#Gestor de inventario simple

Lista_Productos = []

def mostrar_inventario():
    print("Inventario: ")
    for i, producto in enumerate(Lista_Productos, start=1):
      nombre, cantidad, precio = producto
      print(f"{i}. Nombre: {nombre}, Cantidad: {cantidad}, Precio por unidad: ${precio:.2f}")
def Editar_inventario():
    print("¿Qué deseas realizar? ")
    while True:
      print("\n\t1. Agregar Producto.\n\t2. Eliminar Producto.\n\t3. Editar Producto.\n\t4. Mostrar el inventario\n\t0. Salir")
      seleccion = int(input("Opción elegida: "))
      if seleccion == 1:
          print("Agregar producto.\n")
          print("Ingresa el nombre del producto a agregar: ")
          producto_agg = input()
          print("Ingresa la cantidad a agregar de ese producto:")   
          stock = int(input())
          precio = float(input("Ingresa el precio del producto por unidad: "))
    
          Lista_Productos.append([producto_agg, stock, precio])

          print("Actualizando inventario...")
          print("Inventario actualizado correctamente!\n")
          mostrar_inventario()      
      elif seleccion == 2:
          print("Eliminación de producto.\n")
          print("¿Qué elemento deseas eliminar?\n") 
          mostrar_inventario()
          eleccion = int(input("Número del producto a eliminar: "))
          del Lista_Productos[eleccion - 1]
          print("Procesando solicitud...")
          print("Eliminando...")
          print("Producto eliminado exitosamente!")
      elif seleccion == 3:
          print("Editor de inventario.\n")
          print("¿Qué elemento deseas editar?\n")
          mostrar_inventario()
          eleccion = int(input("Número del producto a editar: "))
          print("Ingresa el nombre del producto: ")
          producto_agg = input()
          print("Ingresa la cantidad a agregar de ese producto:")   
          stock = int(input())
          precio = float(input("Ingresa el precio del producto por unidad: "))
          Lista_Productos[eleccion - 1] = ([producto_agg, stock, precio])
          print("Actualizando inventario...")
          print("Inventario actualizado correctamente!\n")
          mostrar_inventario()    
      elif seleccion == 4:
              mostrar_inventario()  
      elif seleccion == 0:
          print("Saliendo del programa...")
          break
        
      else:
          print("Opción no válida. Por favor, elige una opción del menú.")  
def mostrar_proveedores(proveedores):
    if not proveedores:
        print("No hay proveedores registrados.")
    else:
        print("\nLista de Proveedores:")
        for nombre, datos in proveedores.items():
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {datos['telefono']}")
            print(f"Dirección: {datos['direccion']}")
            print(f"Email: {datos['email']}")
            print("-" * 40)
def agregar_proveedor(proveedores):
    while True:
        nombre = input("Ingrese el nombre del proveedor: ")
        telefono = input("Ingrese el teléfono del proveedor: ")
        direccion = input("Ingrese la dirección del proveedor: ")
        email = input("Ingrese el email del proveedor: ")

        if nombre in proveedores:
            print("El proveedor ya existe.")
        else:
            proveedores[nombre] = {
                "telefono": telefono,
                "direccion": direccion,
                "email": email
            }
            print(f"Proveedor '{nombre}' agregado correctamente.")

        agregar_otros = input("¿Desea agregar otro proveedor? (s/n): ").lower()
        if agregar_otros != 's':
            break
def editar_proveedor(proveedores):
    nombre = input("Ingrese el nombre del proveedor a actualizar: ")

    if nombre in proveedores:
        print("Ingrese los nuevos datos del proveedor (deje en blanco para mantener el actual):")
        telefono = input(f"Teléfono actual ({proveedores[nombre]['telefono']}): ") or proveedores[nombre]["telefono"]
        direccion = input(f"Dirección actual ({proveedores[nombre]['direccion']}): ") or proveedores[nombre]["direccion"]
        email = input(f"Email actual ({proveedores[nombre]['email']}): ") or proveedores[nombre]["email"]

        proveedores[nombre] = {
            "telefono": telefono,
            "direccion": direccion,
            "email": email
        }
        print(f"Proveedor '{nombre}' actualizado correctamente.")
    else:
        print("El proveedor no existe.")
def eliminar_proveedor(proveedores):
    nombre = input("Ingrese el nombre del proveedor a eliminar: ")

    if nombre in proveedores:
        del proveedores[nombre]
        print(f"Proveedor '{nombre}' eliminado correctamente.")
    else:
        print("El proveedor no existe.")
def info_proveedores(proveedores):
    proveedores
def monitoreo_stock():
    print()
def descuentos():
    print()
def Historial_Transacciones():
    print()
def Calculo_valorInvent():
    print()
def Generacion_reportes():
    print()  
print("*******************************************************************")
print("*Gestor de inventario de la empresa (ingrese nombre de la empresa)*")
print("*******************************************************************")

print("¿Qué es lo que deseas realizar?")
print("\n\t1. Mostrar el inventario.\n\t2. Editar el inventario.\n\t3. Proveedores")
eleccion = int(input())
