'''
Módulo 2.

02. Ejemplo: Tuplas

Las tuplas son estructuras de datos similares 
a las listas, pero que se caracterizan por ser inmutables.
'''

print("Se creará una tupla vacía")
tupla_vacia = ()
empty_tuple = tuple()

print(type(tupla_vacia))
print(type(empty_tuple))

print("Se puede crear una tupla de un solo elemento")
tupla_dato = (1, ) #Se tiene que escribir la coma
print(tupla_dato)

print("Se puede crear dos tupla de un solo paso")
tupla1, tupla2 = (20, 40)

print("Tupla1: ", tupla1)
print("Tupla2: ", tupla2)

#Las tuplas no se pueden modificar
#t1.insert(0, 1)
#t1.append(10)

#Se puede acceder a los valores almacenados
tupla_ejemplo = (3.1415, 2.13333)
dato_tupla = tupla_ejemplo[0]
print("Se accesde al dato en la posición 0:",dato_tupla)

print("Se puede convertir a una lista la tupla")
lista_tupla = list(tupla_ejemplo)
print("Se conviirtió la tupla en lista:",lista_tupla)