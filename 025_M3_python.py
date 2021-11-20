'''
Módulo 3.

02. Importar módulos de la librería estándar y de librerías externas

La librería estándar se incluye preinstalada en Python y contine una serie
de módulos para distintos propósitos, para utilizarlas usamos la palabra reservada 'import'
'''

#Para importar datos desde la librería estándar
import os

#Para obtener ayuda sobre un módulo
#help(os)

#Uso de una función que se encuentra dentro del módulo. Una lista de directorios.
files = os.listdir()
print(files)

#Para obtener el tamaño de un archivo en kilobytes
size = os.path.getsize('Readme.md')
print(size)

#Se muestran algunos otros ejemplos de importar módulos
import os.path #Sólo un submódulo específico.
from os import path #Similar al anterior, sólo se llama a 'path' directamente
from os import path as pt #Se importa con un alias de identificación

#Para instalar un paquete es necesario instalar pip
#Los paquetes se instalan desde la línea de comandos
#Una vez realizado lo anterior se puede instalar el paquete e importar de manera usual
from flask import Flask

app = Flask(__name__)