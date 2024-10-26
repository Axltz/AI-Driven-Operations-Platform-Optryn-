Directorio = []

def Agregar_Contacto():
  
  print("Has seleccionado agregar contacto")
  print("Ingresa el nombre del contacto: ")   
  nombre = input()
  print("Numero de telefono: ")
  telefono = input() 
  print("Correo electronico: ")
  correo = input()
  contacto = (nombre, telefono, correo)
  Directorio.append(contacto) v

print("Agenda telefonica")

while True: 
  print("¿Qué desea hacer? (Seleccione una opción)")
  print("1.Agregar contacto\n2.Editar contacto\n3.Eliminar Contacto\n4.Mostrar lista de contactos\n5.Consultar\n0.Salir")
  opcion = int(input( ))
  if (opcion == 0):
     break
  elif (opcion == 1):
     Agregar_Contacto()
     print("Contacto agregado exitosamente.")
  elif (opcion == 2):
     print("Has seleccionado añadir contacto")
     print("Qué contacto deseas editar")
     for lista, contacto in enumerate(Directorio):
         print(f"{lista}: {contacto[0]}: Telefono: {contacto[1]} - Correo: {contacto[2]}")
     i = int(input())
     nombre = input("Nombre: ")
     telefono = input("Telefono: ")
     correo = input("Correo electronico: ")
     Directorio[i] = (nombre, telefono, correo)
  elif (opcion == 3):
     print("¿Qué contacto desea eliminar?")
     for lista, contacto in enumerate(Directorio):
         print(f"{lista}: {contacto[0]}: Telefono: {contacto[1]} - Correo: {contacto[2]}")
     i = int(input())
     print(f"¿Estás seguro de eliminar a {Directorio[i]} de tu lista de contactos? (si/no)")
     eliminar = input()
     if eliminar.lower() == "si":
         del Directorio[i]
         print("Eliminando contacto...")
         print("Contacto eliminado exitosamente!!!")
     else:
            print("Contacto NO eliminado...")

  elif (opcion == 4):
      print("Esta es la lista de contactos.")
      for lista, contacto in enumerate(Directorio):
         print(f"{lista}: {contacto[0]}: Telefono: {contacto[1]} - Correo: {contacto[2]}")
  
print("Has seleccionado salir, ¡hasta luego!...")