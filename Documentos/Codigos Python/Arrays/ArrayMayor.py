#Arr mas grande
array = []


while True: 
    num = int(input("Ingrese un numero entero (0 para terminar): "))
   
    if num == 0:
        break
    array.append(num)


if not array:
    print("No se ingresaron números.")
else:
    max_valor = array[0]
    for i in range(1, len(array)):
        if array[i] > max_valor:
            max_valor = array[i]
    
    print("El valor máximo del array es:", max_valor)
