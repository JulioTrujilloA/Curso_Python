'''
Reto 8. Mínimo común múltiplo

-Escribe un programa que calcule el mínimo común múltiplo entre dos números
'''

print("Programa. Mínimo común múltiple entre dos números\n")

numero1 = int(input("Escribe el primer número: "))
numeroX = int(input("Escribe el segundo número: "))


#Con esta condición siempre tendremos a numero1 mayor a numero2
if numero1 != 0 or numeroX != 0:

    if numero1 > numeroX:
        numero2 = numeroX
    else:
        numero2 = numero1
        numero1 = numeroX

    bandera = True
    i = 1

    while bandera:
        n1 = numero1 * i
        i += 1

        n2 = 0
        comun = 1
        
        while n2 < n1:        
            n2 = numero2 * comun
            comun += 1

            if n1 == n2:
                print("\nEl mínimo común múltiplo de {} y {} es: {}".format(numero1,numero2,n1))
                bandera = False
else:
    print("\nNúmeros mayores a cero, por favor.")

print("\nFin.")   
