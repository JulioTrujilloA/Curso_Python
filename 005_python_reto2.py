'''
Reto: Operadores

Desarrollo
-Crea un programa que solicite dos números e imprima los siguientes resultados:
  -Resta usando el operador -
  -Módulo usando el operador %
-Además realizar el or entre un valor true y un false
'''

#Se obtienen los valores de las variables a utilizar

print("Escribe dos números enteros\n")
#print("Número 1:")
strNumero1 = input("Número 1: ")
#print("Número 2:")
strNumero2 = input("Número 2: ")

#Se crea la lógica a utilizar
intNumero1 = int(strNumero1)
intNumero2 = int(strNumero2)

resta = intNumero1 - intNumero2
residuo = intNumero1 % intNumero2

#Se imprime el resultado
print("\nLa resta de {} - {} = {}".format(strNumero1,strNumero2,str(resta)))
print("El residuo de la operación con módulo (%) de {} % {} = {}\n".format(strNumero1,strNumero2,str(residuo)))