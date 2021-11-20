'''
Módulo 3.

03. Módulos

Los módulos nos permiten estructurar nuestro código en más de un archivo,
cualquier archivo .py puede considerarse un módulo.
'''

#Si tenemos un paquete podemos importarlo enteramente, con alias
import modulos.aritmetica as aritmetics

print(aritmetics.promedio(1,3,5,8))
print(aritmetics.suma(1,3,5,8))
print(aritmetics.producto(1,3,5,8))

#Importamos una función en específico
from modulos.aritmetica import suma
print(suma(5,5,5,10,20))

#Usaremos un alias para elementos importados
from modulos.aritmetica import promedio as prom
print(prom(1,2,3,4,5,6,7,8))