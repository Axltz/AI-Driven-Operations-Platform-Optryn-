# Cálculo de Intereses Simples
capital = float(input("Introduce el capital: "))
tasa_interes = float(input("Introduce la tasa de interés (como decimal): "))
tiempo = float(input("Introduce el tiempo en años: "))

interes = capital * tasa_interes * tiempo

print(f"Interés: {interes}")
