'''
Proyecto Final. Módulo 2.

Continuación del proyecto de la Calculadora de intereses.
'''
import math

def crea_tarjeta():
    nombreTarjeta = "AMEX" #input("Nombre de tarjeta: ")
    tasaInteres = 60 #float(input("Escribe la tasa de interés anual (%): "))
    cantidadDeuda = 1000 #float(input("Escribe la deuda actual: "))
    pagoActual = 500 #float(input("Ingresa el total del pago actual: "))
    cargosNuevos = 500 #float(input("Ingresa la cantidad de cargos nuevos realizados: "))

    if pagoActual > cantidadDeuda:
            print("\nNo es posible realizar un pago mayor a la deuda actual.\n")
            pagoActual = float(input("Ingresa de nuevo el total del pago actual: "))

    tarjeta = {
        "Nombre de tarjeta" : nombreTarjeta,
        "Tasa de interés" : tasaInteres,
        "Cantidad de deuda actual" : cantidadDeuda,
        "Cargos nuevos en tarjeta": cargosNuevos,
        "Pago actual": pagoActual
    }

    return tarjeta

def captura_nueva_deuda(tarjetas):
    #Obtenemos el interés mensual
    interesMensual = (tarjetas['Tasa de interés'] / 12) / 100

    #Obtenemos la deuda recalculada
    recalculoDeuda = (tarjetas['Cantidad de deuda actual'] - tarjetas['Pago actual']) * (1 + interesMensual)

    #Obtenemos el próximo cargo

    proximoCargo = recalculoDeuda + tarjetas['Cargos nuevos en tarjeta']

    tarjetas['Deuda nueva'] = proximoCargo

    return tarjetas

def generar_reporte(diccionario):
    #Se imprimen los datos de la tarjeta
    print("Los datos de tu tarjeta son los siguientes:\n")

    for campo, clave in diccionario.items():
        print("{} = {}".format(campo,clave))
       
        
def lista_tarjetas(tarjetero):
    for tarjeta in tarjetero:
        generar_reporte(captura_nueva_deuda(tarjeta))
        pago_recurrente(captura_nueva_deuda(tarjeta))

def pago_recurrente(tarjeta):
    #Se imprimirán los pagos fijos cada mes de acuerdo a un monto dado por el usuario
    monto_Pago = int(input("Escribe el monto a pagar cada mes: $"))

    division_monto = math.ceil(tarjeta['Deuda nueva'] / monto_Pago)
    residuo_monto = tarjeta['Deuda nueva'] % monto_Pago

    i = 1
    pago = tarjeta['Deuda nueva']

    while i <= division_monto:
        print("Deuda total del mes {} = {} ".format(i,pago))
        
        if pago == residuo_monto:
            pago -= residuo_monto
            print("Deuda del mes {} = {} ".format(i+1,pago))

        pago -= monto_Pago
        i += 1
        
        
print("\nPrograma. Tarjetas e intereses y pagos.\n")
bandera_menu = True
tarjeta_nueva = []

while bandera_menu:
    print('''   Menú\n
            1. Crear tarjeta
            2. Generar reporte de tarjetas
            3. Salir''')


    opcion = int(input("\nEscribe la opción deseada: "))

    if opcion == 1:        
        bandera = True

        while bandera:
            bandera2 = True
            
            #Se agregan tarjetas cuantas veces el usuario requiere
            print("\nEscribe los datos de la tarjeta\n")
            tarjeta_nueva.append(crea_tarjeta())

            while bandera2:
                respuesta = input("¿Deseas ingresar otra tarjeta? (Sí o No): ")
                if respuesta == "Sí" or respuesta == "Si" or respuesta == "si" or respuesta == "sí":
                    bandera2 = False
                elif respuesta == "No" or respuesta == "no":
                    bandera = False
                    bandera2 = False
                else:
                    print("Escribe bien tu respuesta.\n")
    elif opcion == 2:
        print(tarjeta_nueva)
        lista_tarjetas(tarjeta_nueva)
    elif opcion == 3:
        print("\nFin.")
        bandera_menu = False
