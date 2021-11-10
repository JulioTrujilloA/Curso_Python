#Recibe dos números desde la consola
#Convierte los números a variables enteras
#Realiza la operación a= b+c con las variables enteras
#Realiza la misma operación con las variables string
#Imprime los resultados para ambas operaciones
#¿Hay alguna diferencia?

print("Escribe el Número 1")
numero1 = input();
print("Escribe un Número 2")
numero2 = input();

print("Las variables no se han convertido a int")

sumaStr = numero1 + numero2
print(sumaStr)

numInt1 = int(numero1)
numInt2 = int(numero2)

print("Las variables ya se convirtieron a int")

suma = numInt1 + numInt2
print(suma)

print("La diferencia es que si no se convierte a int se concatenan los números.")