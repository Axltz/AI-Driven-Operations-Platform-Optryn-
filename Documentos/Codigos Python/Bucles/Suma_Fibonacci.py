#Suma Fibonacci

numero = int(input("¿Hasta donde de la sucesion quieres mostrar?"))
a = 0
b = 1
sucesion = 0
while numero > 1:
    print(b)
    sucesion = a + b
    a = b
    b = sucesion
    numero -= 1
