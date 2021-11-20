'''
Reto. Crear módulo

Desarrollo
    ->  Convierte el archivo del reto 01 args en un módulo
    ->  Llama la función de suma y producto desde otro archivo
'''
import modulos.operacionesDirectorio as moduloEjemplo

print("La suma de 9 + 3 + 5 = {}".format(moduloEjemplo.sumador(9,3,5)))

print("La multiplicación de 9 * 3 * 5 = {}".format(moduloEjemplo.multiplicador(9,3,5)))

#Con esta línea mandamos llamar una imagen para abrirla con el visor del sistema
moduloEjemplo.mostrar_imagen()