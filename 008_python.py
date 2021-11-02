#Sentencia condicional "if, elif, else"
#Sirve para establecer una condición que de ser cierta ejecutará el código propuesto

print('''Primer ejemplo:
        edad = 29
        if edad > 29:
            print("Es una persona adulta")\n''')

edad = 29

if edad > 18:
    print("La persona es adulta y tiene INE")

#Cualquier código que esté dentro del "else" se ejecutará cuando no se cumpla la condición del "if"

print('''Segundo ejemplo
            velocidad = 70
            límite = 90
            
            if velocidad > limite:
                print("Límite de velocidad sobrepasado")
            else:
                print("Vas bien, mantén la velocidad")\n''')

velocidad = 70
limite = 90

if velocidad > limite:
    print("Límite de velocidad sobrepasado")
else:
    print("Vas bien, mantén la velocidad")


# Si se tienen varias opciones a elegir es posible utilizar elif

numero = -3

if numero == 0:
    print("El número es 0")
elif numero > 0:
    print("El número es positivo")
else:
    print("El número es negativo")
