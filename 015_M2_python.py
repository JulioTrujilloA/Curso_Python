'''
Módulo 2.

04. Ejemplo: Diccionarios

Los diccionarios son estructuras de datos que
nos permiten almacenar datos, asignandolas a llaves.

El acceso a los diccionarios debe realizarse mediante
las llaves, no permiten realizarlo por índice.
'''

#Formas de declarar un diccionario
declara1 = {}
declara2 = dict()

print("Se imprime el tipo de ambas declaraciones:", type(declara1), type(declara2))

#Declarar e inicializar un dicionario
diccionario = {"Usuario": "user123", "Correo":"us12@correo.com", "Empresa":"GOB"}
print("Se imprime el diccionario: ",diccionario)

#Es posible obtener las llaves de la lista
print("Se imprimen las llaves del diccionario: ",diccionario.keys())

#Es posible obtener los valores de la lista
print("Se imprimen los valores del diccionario: ",diccionario.values())

#También es posible agregar entradas en un diccionario
diccionario['País'] = "México"
print("Se agregó [País: Ciudad]", diccionario)

#También se puede acceder al valor mediante la llave
print("El valor de la llave 'País' es:",diccionario['País'])

#Se puede extraer entradas con el método "pop"
extracción = diccionario.pop('Correo')
print("La llave Correo con su valor: {}, se eliminó".format(extracción))
print("El diccionario quedó así: ",diccionario)
