'''
Proyecto Final del Mósulo 1

Calculadora de intereses

'''

print("Calculadora de intereses\n")

nombreTarjeta = input("Nombre de tarjeta: ")
tasaInteres = float(input("Escribe la tasa de interés anual (%): "))
cantidadDeuda = float(input("Escribe la deuda actual: "))
pagoActual = float(input("Ingresa el total del pago actual: "))
cargosNuevos = float(input("Ingresa la cantidad de cargos nuevos realizados: "))

if pagoActual > cantidadDeuda:
    print("\n Debido a políticas internas no es posible pagar más de lo de la deuda del mes anterior\n")
    pagoActual = float(input("Ingresa de nuevo el total del pago actual: "))
    
print('''
Aquí están tus datos:
Nombre de la tarjeta: {}
Tasa de interés: {}%
Deuda actual: ${}
Cantidad a pagar actual: ${}
Total de cargos nuevos: ${}
'''.format(nombreTarjeta,tasaInteres,cantidadDeuda,pagoActual,cargosNuevos))

#Obtenemos el interés mensual
interesMensual = (tasaInteres / 12) / 100

#Obtenemos la deuda recalculada
recalculoDeuda = (cantidadDeuda - pagoActual) * (1 + interesMensual)

#Obtenemos el próximo cargo

proximoCargo = recalculoDeuda + cargosNuevos


print("\n Tu pago próximo es de: ${:.2f}".format(proximoCargo))

