#ejercicio 1) Realice un programa que lea 4 números y diga cuántos son pares y cuantos impares y devuelva la sumatoria de los pares.

#x = 0  #ciclos
#par = 0  
#impar = 0
#acumulador_par = 0
#acumulador_impar = 0
#while x < 4:
#    numero = int(input("ingrese un numero"))
#    if numero %2 == 0:
#        acumulador_par = acumulador_par + numero
#        par += 1
#    else:
#        acumulador_impar = acumulador_impar + numero
#        impar += 1
#   x += 1
#print("se han ingresado" ,par,"numeros pares y" ,impar, "numeros impares\n"
#      "la sumatoria de los numero pares es de ", acumulador_par, "y la sumatoria de numero impares es de", acumulador_impar )


#ejercicio 2)Leer 10 números y obtener la cantidad de mayores y la cantidad de menores a 100, cuál es el número máximo y cuál es el número mínimo.

#numeros = []
#mayores_a_100 = 0
#menores_a_100 = 0

#for i in range(10):
#    numero = int(input("Ingresa un número: "))
#    numeros.append(numero)
    
#    if numero > 100:
#        mayores_a_100 += 1
#    elif numero < 100:
#        menores_a_100 += 1

#numero_maximo = max(numeros)
#numero_minimo = min(numeros)


#print("Cantidad de números mayores a 100:", mayores_a_100)
#print("Cantidad de números menores a 100:", menores_a_100)
#print("Número máximo:", numero_maximo)
#print("Número mínimo:", numero_minimo)

#ejercicio 3)Ingresar las edades y el sexo de 15 personas y determinar cuántas son mujeres, cuántos varones, cuántos mayores de edad y cuántos
             #menores de edad.

#cantidad_personas = 15
#contador_mujeres = 0
#contador_varones = 0
#contador_mayores_edad = 0
#contador_menores_edad = 0

#for i in range(cantidad_personas):
#    print("Persona", i + 1)
#    edad = int(input("Ingrese la edad: "))
#    sexo = input("Ingrese el sexo (M para mujer, V para varón): ").upper()

#    if sexo == "M":
#        contador_mujeres += 1
#    elif sexo == "V":
#        contador_varones += 1

#    if edad >= 18:
#        contador_mayores_edad += 1
#    else:
#        contador_menores_edad += 1

#print("Cantidad de mujeres:", contador_mujeres)
#print("Cantidad de varones:", contador_varones)
#print("Cantidad de mayores de edad:", contador_mayores_edad)
#print("Cantidad de menores de edad:", contador_menores_edad)


#ejercicio 4) Leer 10 números y mostrar solamente los números positivos, y su sumatoria.

#numeros = []
#sumatoria = 0

#for i in range(10):
#    numero = int(input("Ingrese un número: "))
#    numeros.append(numero)
    
#    if numero > 0:
#        sumatoria += numero

#print("Números positivos:")
#for numero in numeros:
#    if numero > 0:
#        print(numero)

#print("Sumatoria de los números positivos:", sumatoria)


#ejercicio 5) Leer 15 números negativos y convertirlos a positivos e imprimir dichos números.

numeros_negativos = []

for i in range(15):
    numero = int(input("Ingrese un número negativo: "))
    numeros_negativos.append(numero)

numeros_positivos = [abs(numero) for numero in numeros_negativos]

print("Números positivos:")
for numero in numeros_positivos:
    print(numero)