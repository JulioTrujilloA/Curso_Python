'''
Módulo 2.

05. Ejemplo: Ciclos

Los ciclos son estructuras que nos permiten hacer
que durante la ejecución de un programa, fracciones de
código se repitan bajo ciertas condiciones.
'''

#Los ciclos while, ejecutan un código repetidas veces mientras se cumpla su condición
i = 1

while i <= 5:
    print(i)
    i += 1
print("Programa terminado")

#Si un ciclo for siempre cumple su condicion, nunca se detendrá. Creandose un ciclo infinito.
"""
while True:
    print("Ciclo sin fin")
"""

#Para iterar a través de un cliclo for es posible utilizar 'range'
for i in range(3):
    print(i)
print("Programa terminado")

#Los ciclos for permiten recorrer estructuras iterables

#Listas
autos = ['Nissan', 'Chevrolet', 'Toyota', 'Ford']

for auto in autos:
    print("La marca de auto es: {}".format(auto))
print("Programa terminado")

#Diccionnarios

diccionario_autos = {"Nissan" : "March", "KIA" : "Rio", "Crysler" : "Stratus"}

#Se obtienen las llaves
llaves = diccionario_autos.keys()
print(llaves)

#Se obtienen los valores
valores = diccionario_autos.values()
print(valores)

#Se obtienen todos los datos del diccionario
cantidad_datos = diccionario_autos.items()
print(cantidad_datos)

#Obteniendo todos los datos se puede iterar en ellos
for campo, valor in cantidad_datos:
    print("La llave {} contine: {}".format(campo, valor))
print("Programa terminado")