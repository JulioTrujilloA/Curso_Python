'''
Cierre de Unidad.
Reto: Calculadora

Se creará una calculadora con lo siguiente:

-Solicitar al usuario dos números
-El usuario puede seleccionar diferentes operaciones (suma, resta, multiplicación, división, etcétera)
-Imprimir los resultados
-Considerar validaciones de divisón entre cero y caracteres no definios como operaciones
'''

print("Calculadora para números enteros\n")
numero1 = int(input("Escribe el primer número entero: "))
numero2 = int(input("Escribe el segundo número entero: "))

print('''
\nSelecciona alguna operación:
1. Suma
2. Resta
3. Multiplicación
4. División
5. Residuo de división\n
''')

seleccion = int(input("Número de operación: "))



if seleccion == 1:
    resultado = numero1 + numero2
elif seleccion == 2:
    resultado = numero1 - numero2
elif seleccion == 3:
    resultado = numero1 * numero2
elif seleccion == 4:
    if(numero2 == 0):
        resultado = "No es posible divisón entre cero"
    else:
        resultado = numero1 / numero2
elif seleccion == 5:
    if(numero2 == 0):
        resultado = "No es posible divisón entre cero"
    else:
        resultado = numero1 % numero2
else:
    print("Error")


print("El resultado es: {}".format(resultado))