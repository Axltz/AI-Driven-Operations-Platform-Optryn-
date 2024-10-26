#Producto de un Array

array = []
producto = 1
while True:
  numeros = int(input("ingresa elementos (0 para salir): "))
  if numeros == 0:
    break
  array.append(numeros)
  producto *= numeros


print("el producto de los datos ingresados es: ", producto)
