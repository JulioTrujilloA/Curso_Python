'''
Módulo 2.

01. Ejemplo: Listas
'''

#Formas de declarar una lista vacía
lista_vacia = []
empty_list = list()

print("Se imprimen las dos listas vacías, verificando que sea lo mismo")
print(lista_vacia, type(lista_vacia))
print(empty_list, type(empty_list))

#Las listas pueden inicializarse con datos
print("Las lístas pueden inicializarse con datos")

lista_int = [2,5,6,8,3,1]
lista_fl = [3.1415,2.4, 0.23, 15.90]
lista_str = {'Michael', 'Scott','!' }

print(lista_int)
print(lista_fl)
print(lista_str)

#Las listas pueden contener datos de distinto tipo y otras listas también
lista_mezcla = [1, 1.56, 'Cadena de texto', lista_int]
print(lista_mezcla)

#Ahora veremos algunas características de las listas

print("Operaciones con listas")

numeros = [1,2,3,4,5]
print("Datos de la lista:", numeros)

print("Acceso por índice")
dato = numeros[3]
print("El número en la posición 3 es: ",dato)

print("Obtener porciones o rangos de la lista")
sublista = numeros[1:4]
print("La sublista del rango 1:4 es: ", sublista)

print("Agregar elementos a la lista")
numeros.append(7)
print("Se agrego al final de la lista el número 7: ",numeros)

print("Insertar numeros en la lista")
numeros.insert(4, 'monty')
print("Se insertó en la posición 4 la palabra monty: ",numeros)

print("Sacar y tomar elementos de la lista")
dato = numeros.pop(3)
print("Se saco el elemento de la posición 3: ",numeros)
print("El dato es: ",dato)

print("Se pueden convertir las cadenas a listas")
lista_de_cadena = list('Fue lo que ella dijo')
print(lista_de_cadena)