usuario_correcto = "Axel"
contrasena_correcta = "programador123"
maximo_intentos = 5
intentos = 0

while intentos < maximo_intentos:
    usuario = input("Ingrese el usuario: ")
    contrasena = input("Ingrese la contrasena: ")

    if usuario == usuario_correcto and contrasena == contrasena_correcta:
        print("Bienvenido(a), has ingresado (a) al sistema")
        break
    else:
        print("Usuario o contrasena incorrectos")
        intentos += 1
