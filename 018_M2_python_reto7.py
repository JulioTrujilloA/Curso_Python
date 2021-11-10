'''
Reto seis. Reto: Diccionario telefónico

-Haz un programa que funcione como un directorio de números telefonicos

->Realiza un ciclo que imprima todos los números de la serie Fibonacci menores a 1000.
->Realiza un ciclo for que itere sobre los valores de una tupla.
'''

#Fibonacci
print("Se imprimen los primeros números de la serie Fibonacci hasta el 100.")

i = 0
acum = 0
retroceso = 1


while i <= 100:
    if acum == 0:
        print(acum)
    acum += retroceso
    retroceso = acum - retroceso
    print(acum)
    i += 1

print("\nSe imprimen los valores de una tupla")

tupla = ("Hola", "Adiós")

for dato in tupla:
    print(dato)
