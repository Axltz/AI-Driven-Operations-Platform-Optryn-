#Año Bisiesto

while True:
  año = int(input("Ingrese el año: "))
  if año % 4 == 0 and año % 100 != 0:
      print ("Es año bisiesto")
  else:
      print("No es año bisiesto")
      break