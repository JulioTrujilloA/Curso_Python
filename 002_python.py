#Tipos de datos numéricos
entero = 4
print("El dato introducido contiene:")
print(entero)
print("Es de tipo:")
print(type(entero))

print("--------------------")

pi = 3.14159
print("El dato introducido contiene:")
print(pi)
print("Es de tipo:")
print(type(pi))

print("--------------------")
print("--------------------")

#Cadenas de texto
mensaje = "Hola Python"
print("El dato introducido contiene:")
print(mensaje)
print("Es de tipo:")
print(type(mensaje))

print("--------------------")
print("--------------------")

#Cadenas de texto
verdadero = True
print("El dato introducido contiene:")
print(verdadero)
print("Es de tipo:")
print(type(verdadero))

print("--------------------")
print("--------------------")

print("Conversión de tipos")

#Se puede definir números como cadenas si se encierran en comillas
numero1 = "100"
numero2 = "3.14159"
print(type(numero1))
print(type(numero2))

print("--------------------")
#Sentencia para convertir a entero
entero = int(numero1)
print(type(entero))

print("--------------------")
#Sentencia para convertir a flotante
flotante = float(numero2)
print(type(flotante))

print("--------------------")
#También se puede convertir un número a dacena de texto
num = 300
cadena = str(num)
print(type(cadena))
