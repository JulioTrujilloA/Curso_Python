# Revisaremos los operadores aritméticos y lógicos

#Variables a utilizar
operando1 = 8
operando2 = 20
incremento = 0

#Lógica
print("*Operadores aritméticos*")
print("Operando 1 = 8, Operando 2 = 20")
print("Suma")
suma = operando1 + operando2
print(suma)
print("Resta")
resta = operando1 - operando2
print(resta)
print("Multiplicación")
producto = operando1 * operando2
print(producto)
print("División")
cociente = operando1 / operando2
print(cociente)
print("Operando 1 = 20, Operando 2 = 8")
print("División entera")
cocienteEntero = operando2 // operando1
print(cocienteEntero)
print("Módulo")
residuo = operando2 % operando1
print(residuo)

print("*Operadores booleanos*")

operando3 = True
operando4 = False

#Compuerta AND
print("Operador AND")

operador_and = operando3 and operando4
print("El resultado de True AND False es:")
print(operador_and)

#Compuerta OR
print("Operador OR")

operador_or = operando3 or operando4
print("El resultado de True OR False es:")
print(operador_or)

#Operador NOT
print("Operador NOT")

negacionTrue = not operando3
print("El resultado de negar (NOT) True es:")
print(negacionTrue)

negacionFalse = not operando4
print("El resultado de negar (NOT) False es:")
print(negacionFalse)