# funciones.py

def agregar_tarea(tareas):
    tarea = input("Introduce la nueva tarea: ")
    tareas.append(tarea)
    print("Tarea añadida correctamente.")

def ver_tareas(tareas):
    print("Lista de tareas:")
    for i, tarea in enumerate(tareas, start=1):
        print(f"{i}. {tarea}")

def marcar_completada(tareas):
    ver_tareas(tareas)
    try:
        indice = int(input("Selecciona el número de la tarea completada: ")) - 1
        tareas.pop(indice)
        print("Tarea marcada como completada.")
    except (ValueError, IndexError):
        print("Opción inválida. Introduce un número válido.")

def eliminar_tarea(tareas):
    ver_tareas(tareas)
    try:
        indice = int(input("Selecciona el número de la tarea a eliminar: ")) - 1
        tarea_eliminada = tareas.pop(indice)
        print(f"Tarea '{tarea_eliminada}' eliminada correctamente.")
    except (ValueError, IndexError):
        print("Opción inválida. Introduce un número válido.")
