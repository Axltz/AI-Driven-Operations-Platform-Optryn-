def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

while True:
    numero = int(input("Introduce un numero: "))
    print("El factorial de", numero, "es", factorial(numero))
    input("Presiona cualquier tecla para continuar...")
