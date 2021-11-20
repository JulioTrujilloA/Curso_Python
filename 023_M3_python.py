'''
Módulo 3.

01. Args y kwargs

Existen dos tipos de argumentos en Python: los convencionales y
aquellos que están sujetos a un nombre específico, generalmente
identificados como args (argumentos) y kwargs (keyword arguments)
'''

#Se usa la palabra '*args' cuando queremos que una función acepte un numero no determinado de argumentos

def imprime(*argumentos):
        for argumento in argumentos:
            print(argumento)

imprime('Hola', 'a', 'Python!')

#Es posible mezclar argumentos comunes con *args

def imprime_varias(veces, *arg):
    for i in range(veces):
        for argumento in arg:
            print(argumento)

imprime_varias(3, 'Welcome', 'to', 'Alaska!')

#Si se pone al principio, se tiene que especificar sobre cuál parámetro

def imprime_cosas(*args, veces, tipo):
    for i in range(veces):
        for arg in args:
            print(arg)

    print(tipo)

imprime_cosas('Silla', 'Mesa','Banco',veces=2,tipo='String')

#Se usa kwargs para pasar parámetros por el nombre y no por posición

def saludo(**kwargs):
    print('\n\nHola {} de {}'.format(kwargs['nombre'], kwargs['empresa']))

saludo(empresa = 'Bimbo', nombre = 'Carlos')
saludo(nombre = 'Penelope', empresa = 'IBM')

#También es posible extraer llaves y valores de kwargs como de diccionarios

def diversion(**kwargs):
    for clave, valor in kwargs.items():
        print("\n%s == %s" %(clave, valor))

diversion(nombre = 'Guadalupe', empresa = 'HP', ciudad = 'Puebla')



