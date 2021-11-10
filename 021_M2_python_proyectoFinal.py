'''
Proyecto Final del Módulo 2.

Conversiones con SET y LIST
'''

def ordenar_sin_repetidos(lista):
    conjunto = set(lista)
    return conjunto

print("\n*Ordenaremos y devolveremos tu lista de números sin repetidos*")

bandera = True
lista = []

while bandera:
    numero = int(input("\nEscribe un número: "))
    lista.append(numero)

    bandera2 = True

    while bandera2:
        respuesta = input("¿Deseas escribir otro número? (Sí o No): ")
        if respuesta == "Sí" or respuesta == "Si" or respuesta == "si" or respuesta == "sí":
            bandera2 = False
        elif respuesta == "No" or respuesta == "no":
            bandera = False
            bandera2 = False
        else:
            print("Escribe bien tu respuesta.\n")

print("\nTu lista original ")

for numero in lista:
    print("Número: {}".format(numero))

print("\nTu lista ordenada y sin repetidos ")

lista = list(ordenar_sin_repetidos(lista))
for numero in lista:
    print("Número: {}".format(numero))

print("\nFin.")