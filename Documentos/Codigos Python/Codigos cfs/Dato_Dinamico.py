# Dato Dinamico
entrada = input("Introduce un valor: ")


if entrada.isdigit():  
    tipo_dato = "entero"
    valor = int(entrada)
elif entrada.replace('.', '', 1).isdigit() and entrada.count('.') < 2:  
    tipo_dato = "flotante"
    valor = float(entrada)
else:
    tipo_dato = "cadena"
    valor = entrada


print(f"El tipo de dato es: {tipo_dato}")
print(f"El valor es: {valor}")