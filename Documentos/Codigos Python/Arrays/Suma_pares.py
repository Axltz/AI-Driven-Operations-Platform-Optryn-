#Suma de numeros pares
arr = []
suma = 0
while True:
    num = int(input("Ingresa los datos a guardar (0 para hacer la suma): "))
    if num == 0: 
        break
    if num % 2 == 0: 
        arr.append(num) #si es par el numero lo agrega al array 
        suma += num     #luego lo suma a la variable suma
print("La suma de los numeros pares ingresados es: ",suma)

      