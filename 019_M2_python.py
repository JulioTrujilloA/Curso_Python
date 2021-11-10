'''
Módulo 2.

06. Funcionaes

Las funciones son porciones de código que se puedan
llamar para hacer uso de su código.
'''

#Algunas ya las conocemos. Se mandan llamar usando su nombre y, a veces, parámetros.
print("Hello Python!")
input()

#Las funciones se definen con la palabra reservada 'def'
def mensaje():
    print("Lee este mensaje")

#Las funciones se mandan llamar por su nombre.
mensaje()

#Se pueden configurar parámetros
def saludo(persona):
    print("Hola {}".format(persona))

#Se puede mandar llamar repetidas veces con diferentes argumentos
saludo("Ismael")
saludo("Ricardo")
saludo("Kevin")
saludo("María")

#Las funciones pueden devolver datos
def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

#Luego se manda llamar

print("\nÁrea de triángulo\n")
base = int(input("Escribe la base: "))
altura = int(input("Escribe la altura: "))

print("El área del triángulo de <base = {} por altura = {}> es: {}".format(base,altura,area_triangulo(base,altura)))