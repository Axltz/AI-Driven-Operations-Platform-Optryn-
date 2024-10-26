#invertir valores

array = []

while True:
    elemento = input("Ingresa algo al array (E para salir): ")
    if elemento == "E":
        break
    array.append(elemento)
i = 0
j = len(array) - 1

while i < j :
    array[i], array[j] = array[j], array[i]
    i += 1
    j -= 1

print(array)