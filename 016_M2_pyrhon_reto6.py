'''
Reto seis. Reto: Diccionario telefónico

-Haz un programa que funcione como un directorio de números telefonicos

->Crea un diccionario que almacene números de telefono utilizando nombres
  como llaves, con al menos 5 números  
->Adquiere al menos uno de los números
->Agrega nuevas entradas al diccionario
'''

print("Programa: Diccionario telefónico")

diccionario_telefonico = {
  "María" : "33-1456-1454",
  "Iliana" : "33-1323-5456",
  "Nayeli" : "39-3932-9684",
  "Raúl" : "77-1334-6721",
  "Lana" : "33-0974-1257"
}

print("Este es el diccionario:",diccionario_telefonico)

nombre = input("Escribe el nombre del contacto: ")

print("El número telefónico de {} es: {}".format(nombre,diccionario_telefonico[nombre]))

print("\nPuedes agregar un nuevo dato")
nombre_nuevo = input("Escribe el nombre: ")
numero_nuevo = input("Número del contacto: ")

diccionario_telefonico[nombre_nuevo] = numero_nuevo

print("El directorio telefónico quedó así:",diccionario_telefonico)
