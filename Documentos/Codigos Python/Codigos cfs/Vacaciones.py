dias = int(input("Introduce el número de días del viaje: "))
costo_hotel = float(input("Introduce el costo diario del hotel: "))
costo_comida = float(input("Introduce el costo diario de la comida: "))
otros_gastos = 100.00

total_hotel = dias * costo_hotel
total_comida = dias * costo_comida
total_otros = dias * otros_gastos

total = total_hotel + total_comida + total_otros
print("El monto total del cheque es: ", total)
