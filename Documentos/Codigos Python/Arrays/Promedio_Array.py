#Promedio Elementos

array = []
promedio = 0
suma = 0
while True:
    num = int(input("Ingresa los datos a guardar (0 para hacer el promedio): "))
    if num == 0: 
        break
    array.append(num) #si es par el numero lo agrega al array 
    suma += num     #luego lo suma a la variable suma
promedio = suma / len(array)
print("El promedio de los numeros ingresados es: ",promedio)

