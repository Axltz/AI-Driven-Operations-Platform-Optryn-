consumo_kw = float(input("Introduce el consumo en kilowatts: "))
tarifa = float(input("Introduce costo por kilowatt: "))

pago = consumo_kw * tarifa
print("El pago por el consumo de energía eléctrica es: ", pago)
