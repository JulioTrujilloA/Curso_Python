'''
Módulo 2.

03. Ejemplo: Conjuntos

Los conjuntos o sets, son colecciones no mutables y no ordenadas,
tampoco se pueden repetir sus elementos. Utilizadas principalments
en operaciones de lógica y matemática.
'''

#Para declarar un conjunto (set)
set = set()
print("El tipo de dato set", type(set))


set = {1,2,4,5,6}
print("El conjunto se ha inicializado: ",set)

#Agregar un elemento al conjunto
set.add(3)
print("Se agregó 3 al conunto:",set)

#No es posible repetir los elementos del conjunto
set.add(3)
print("Se vuelve a agregar 3, pero no se repite: ",set)

#Para quitar elementos se usa remove()
set.remove(4)
print("Se quita el dato 4:",set)

#Se puede convertir el conjunto a una lista
print("Conversión de conjunto a lista:",list(set))

#También es posible realizar operaciones de conjuntos
conjunto = {4,5,6,7,8}
print("Se hace union de set y conjunto: ", set.union(conjunto))


print("Se realiza la intersección: ",set.intersection(conjunto))