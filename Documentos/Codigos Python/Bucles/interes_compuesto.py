#Calculo de interes compuesto

Capital_Ini = float(input("Ingresa capital inicial: "))
Tasa_InteresA = float(input("Ingresa tasa de interes inicial: "))
n = int(input("Ingresa número de veces que se capitaliza por año: "))
años = int(input("¿Por cuantos años es el interes? "))
año_actual = 1

while año_actual <= años:
    interes_compuesto = Capital_Ini * (1 + Tasa_InteresA / n) ** (n * año_actual)
    print(f"Al final del año {año_actual}, el capital acumulado es: {interes_compuesto:.2f}")
    año_actual += 1
