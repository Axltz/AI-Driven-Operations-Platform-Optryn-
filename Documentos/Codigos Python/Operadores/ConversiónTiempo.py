# Conversión de Horas, Minutos y Segundos
segundos_totales = int(input("Introduce el tiempo en segundos: "))
horas = segundos_totales // 3600
minutos = (segundos_totales % 3600) // 60
segundos = segundos_totales % 60

print(f"{horas} horas, {minutos} minutos, {segundos} segundos")
