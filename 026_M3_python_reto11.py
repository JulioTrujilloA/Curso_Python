'''
Reto. Importar módulos

Desarrollo
    ->  Importa la librería estándar math
    ->  Usa las funciones factorial() y sqrt()
    ->  Importa gcd() (máximo común divisor) desde math usando un alias
    ->  Usa gcd()    
'''

from math import factorial, gcd,sqrt
from math import gcd as maximo_comun_divisor #Con alias

#Utilizaremos factorial para conocer el factorial de algún número
numero = int(input("Escribe un número: "))
print("El factorial de {} es {}".format(numero,factorial(numero)))

#Ahora calcularemos la raíz cuadrada con sqrt python
numero = int(input("Escribe un número: "))
print("La raíz cuadrada de {} es {}".format(numero,sqrt(numero)))

#Pediremos dos números al usuario para obtener su máximo común divisor
num1 = int(input("Escribe el número 1: "))
num2 = int(input("Escribe el número 2: "))
print("El máximo común divisor entre {} y {} es {}".format(num1, num2, maximo_comun_divisor(num1,num2)))
