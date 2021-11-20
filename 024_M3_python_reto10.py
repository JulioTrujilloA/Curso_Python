'''
Reto. Args y kwargs

Desarrollo
    ->  Crea una función que permita obtener una cantidad indeterminada
        de valores y sumarlos o multiplicarlos usando args.

    ->  Crea una función que adquiera un número indeterminado de personas
        y su número de teléfono e imprima el directorio ordenado alfabéticamente.     
'''

def multiplicador(*args):
    acumulador = 1
    for arg in args:
        acumulador *= arg
        print("{} *".format(arg))
    print("--------")
    print("= {}\n".format(acumulador))

def sumador(*args):
    acumulador = 0
    for arg in args:
        acumulador += arg
        print("{} +".format(arg))
    print("--------")
    print("= {}\n".format(acumulador))

def directorio(**kwards):
    for clave, valor in sorted(kwards.items()):
        print("{} :: {}".format(clave,valor))

multiplicador(5,2,2,3,2)
sumador(5,2,2,3,2)
directorio(Guadalupe = "33 1938 5413", Alejandra = '33 5492 7491', Raúl = '33 4341 7793', Bernardo = '33 4439 7192')
