#Cadenas de texto y format

#Esto es una cadena de texto
d = "Hola Python";

#Se puede comprobar con type()
print("El tipo de dato de la variable d es: " + str(type(d)))

#Es posible utilizar comillas simples '' o tres comillas dobles

comillasSimples = 'Hola, Dwight!'
comillasTriples = """Are you Michael Scott?""" 

#Las cadenas pueden tener ninguno y uno o más caracteres

caracter = 'p'

cadenaVacia = '';

print("El caracter es {}".format(caracter) + " y la cadena vacía: {}".format(cadenaVacia))

#Se pueden realizar operaciones con las cadenas
print("Pamela " * 3)
print("Esta frase se concatena con " + "esta otra frase.")

#El acceso a datos de cadenas es posible, mediante sus índices

cadena = "String";
print(cadena[2])

print("Se acaba de imprimir la posición 2 de la cadena 'String' dando como resultado 'r'")

print("Para el uso de las cadenas se puede utilizar lo siguiente")

#Format sirve para colocar variables dentro de una cadena de texto durante la ejecución
nombre = "Julián"
print("Con Format utilizaremos el valor de la variable 'nombre' = {}".format(edad))

edad = 29

print("Con Format utilizaremos el valor de la variable (int) 'edad' = {}".format(nombre))

print("Con Format podemos insertar valores directamente: {} + {} = {}".format(6,9,15))
