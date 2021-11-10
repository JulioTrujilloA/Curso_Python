'''
Reto cuatro. Reto: Precio de la nieve

-Escribe un programa que devuelva el precio de una nieve
 solicitada por el cliente de acuerdo al topping:

 1. Nieve con zarzamora: $19
 2. Nieve con coco todtado: $23
 3. Nieve con chocolate: $24
 4. Nieve con mermelada: $28
 5. Nieve con lunetas: $28

'''

print('''
Buen día.

Selecciona tu helado
 1. Nieve con zarzamora $19
 2. Nieve con coco todtado $23
 3. Nieve con chocolate $24
 4. Nieve con mermelad $28
 5. Nieve con lunetas $28
''')

seleccion = int(input("Número de tu elección: "))

if seleccion == 1:
    print("El precio de tu nieve es de $19")
elif seleccion == 2:
    print("El precio de tu nieve es de $23")
elif seleccion == 3:
    print("El precio de tu nieve es de $24")
elif seleccion == 4:
    print("El precio de tu nieve es de $28")
elif seleccion == 5:
    print("El precio de tu nieve es de $28")
else:
    print("El precio del helado sin topping es de $18")