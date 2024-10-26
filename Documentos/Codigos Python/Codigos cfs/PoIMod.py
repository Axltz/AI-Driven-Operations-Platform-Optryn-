def par(num):
    return num % 2 == 0

numero = int(input("Introduce un numero entero: "))
if par(numero):
    print("El numero", numero, "es par.")
else:
    print("El numero", numero, "es impar.")
