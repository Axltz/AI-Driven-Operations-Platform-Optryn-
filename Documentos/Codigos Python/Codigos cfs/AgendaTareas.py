tareas = []  

def Agregar_Tarea():
    tarea = input("Ingresa la tarea a realizar: ")
    fecha = input("Fecha límite para entrega: ")
    materia = input("Materia a la que corresponde: ")
    tareas.append((tarea, fecha, materia))

def Editar_Tarea():
    print("¿Qué tarea deseas editar?")
    for i, tarea in enumerate(tareas):
        print(f"{i}: {tarea[0]}")
    seleccion = int(input())
    tarea = input("Ingresa la tarea a realizar: ")
    fecha = input("Fecha límite para entrega: ")
    materia = input("Materia a la que corresponde: ")
    tareas[seleccion] = (tarea, fecha, materia)

def Eliminar_Tarea():
    print("¿Qué tarea deseas eliminar?")
    for i, tarea in enumerate(tareas):
        print(f"{i}: {tarea[0]}")
    seleccion = int(input())
    confirmacion = input("¿Estás seguro de eliminar esta tarea? (si/no): ")
    if confirmacion.lower() == "si":
        del tareas[seleccion]
        print("Tarea eliminada.")
    else:
        print("Cancelando la eliminación.")

def Limpiar_lista():
    tareas.clear() 

while True:
    print("AGENDA DE ACTIVIDADES")
    print("¿Qué deseas hacer?")
    print("1. Agregar tarea\n2. Editar tarea\n3. Eliminar tarea\n4. Mostrar lista de tareas\n5. Limpiar lista.")
    seleccion = int(input())
    if seleccion == 1:
        Agregar_Tarea()
    elif seleccion == 2:
        Editar_Tarea()
    elif seleccion == 3:
        Eliminar_Tarea()
    elif seleccion == 4:
        print(tareas)
    elif seleccion == 5:
        Limpiar_lista()
