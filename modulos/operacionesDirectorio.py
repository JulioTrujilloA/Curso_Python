'''
Módulo que realiza multiplicación y suma de n números

También lanza una imagen
'''
from PIL import Image

def multiplicador(*args):
    acumulador = 1
    for arg in args:
        acumulador *= arg
        
    return acumulador

def sumador(*args):
    acumulador = 0
    for arg in args:
        acumulador += arg
    return acumulador

def directorio(**kwards):
    for clave, valor in sorted(kwards.items()):
        print("{} :: {}".format(clave,valor))

def mostrar_imagen():
    im = Image.open('./modulos/ejemplo.jpg')
    im.show()