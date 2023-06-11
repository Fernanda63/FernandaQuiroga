#Ejercicios estructura condicional simple:
# ejercicio 1) Realice un programa que solicite dos letras ingresadas por el usuario y verifique si son iguales o no, mostrando un mensaje.

#letras1=str(input("Ingrese una letra:"))
#letras2=str(input("Ingrese una letra:"))
#if letras1==letras2:
#    print ("usted ingreso dos letras iguales")
#else: 
#    print ("usted no ingreso dos letras iguales")


#ejercicio 2) Hacer un programa que permita decidir si dos palabras son iguales o diferentes. Mostrar mensaje por pantalla.

#palabra1=str(input("Ingrese una palabra:"))
#palabra2=str(input("Ingrese otra palabra:"))
#if palabra1==palabra2:
#    print ("usted ingreso la misma palabra")
#else: 
#    print ("usted ingraso diferentes palabras")


#ejercicio 3) Realizar un programa que permita ingresar “f” o “m” y determinar si vota en mesa femenina o masculina.

#opcion1=str(input("Ingrese f o m: "))
#if opcion1 == "f":
#    print ("usted vota en mesa femenina")
#elif opcion1 == "m": 
#    print ("usted vota en mesa masculina")
#else:
#    print("Opcion no valida, vuelva al menu principal")


#ejercicio 4) Realice un programa que lea dos números y diga cuál es el mayor.

#numero1 = str(input("ingrese un numero "))
#numero2 = str(input("ingrese otro numero "))
#if numero1 > numero2:
#    print("el primer valor ingresado es mayor")
#elif numero1 < numero2:
#    print("el segundo valor ingresado es mayor")


#ejercicio 5) Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo el cambio de dólares a pesos y que sea el usuario quién decida qué tipo de cambio quiere, si de dólares a pesos o viceversa.

#operacion = input("ingrese la opcion deseada: \n"
#                  "1. cambio de dolares a pesos\n"
#                  "2. cambio de pesos a dolares\n")
#monto = float(input("ingrese el monto a cambiar:"))
#cotizacion_compra = 500
#cotizacion_venta = 510
#if operacion == "1":
#    print("usted recibira", monto * cotizacion_compra, "pesos")
#elif operacion == "2":
#    print("usted recibira", monto / cotizacion_venta, "dolares")
#else:
#    print("opcion no valida, por favor ingrese una opcion valida")


#ejercicio 6) Realice un programa donde el usuario ingrese su edad. Si es mayor de 16 años, muestre un mensaje diciendo “puede votar”, sino “no vota”.

#edad = int(input("ingrese su edad: "))
#if edad > 16:
#    print("puede votar")
#else:
#    print("no vota")


#Ejercicios estructura condicional compuesto (IF anidados)

#ejercicio 1) Introducir los lados de un triángulo y visualizar por pantalla si dicho triángulo es equilátero, isósceles o escaleno.

#lado1 = input("ingrese el valor del lado1: ")
#lado2 = input("ingrese el valor del lado2: ")
#lado3 = input("ingrese el valor del lado3: ")   

#if lado1 == lado2 ==lado3:
#    print("el triangulo es equilatero")
#elif lado1 == lado2 != lado3:
#    print("el triangulo es isosceles")
#elif lado2 == lado3 != lado1:
#    print("el triangulo es isosceles")
#elif lado3 == lado1 != lado2:
#    print("el triangulo es isosceles")
#else:
#     print("el triangulo es escaleno")


#ejercicio 2)Realice un programa que le permita al usuario simular el pago ingresando el importe y la forma de pago:
#• Contado (1): se aplica un descuento del 10% al importe
#• Tarjeta (2): se aplica un interés de 10%
#• Débito (3): se aplica un descuento del 5%
#Mostrar el importe, el descuento o interés y el importe total.


#importe = float(input("Ingrese el importe: "))
#forma_pago = int(input("Ingrese la forma de pago (1: Contado, 2: Tarjeta, 3: Débito): "))

#descuento = 0
#interes = 0

#if forma_pago == 1:
#    descuento = importe * 0.10
#    importe_total = importe - descuento
#elif forma_pago == 2:
#    interes = importe * 0.10
#    importe_total = importe + interes
#elif forma_pago == 3:
#    descuento = importe * 0.05
#    importe_total = importe - descuento
#else:
#    print("Forma de pago inválida. Por favor, elija una opción válida.")

#print("Importe: $", importe)
#print("Descuento: $", descuento)
#print("Interés: $", interes)
#print("Importe total: $", importe_total)


#ejercicio 3)Realice un programa que lea tres números, muestre cuál es el mayor y determine si es par o impar.

#num1 = int(input("Ingrese el primer número: "))
#num2 = int(input("Ingrese el segundo número: "))
#num3 = int(input("Ingrese el tercer número: "))

#mayor = max(num1, num2, num3)

#print("El número mayor es:", mayor)

#if mayor % 2 == 0:
#    print("El número mayor es par.")
#else:
#    print("El número mayor es impar.")


#ejercicio 4) Confeccione un programa que pida un número del 1 al 7 y diga el día de la semana correspondiente.

#numero = int(input("ingresa un numero del 1 al 7:"))
#if numero == 1:
#    print("lunes")
#elif numero == 2:
#    print("martes")
#elif numero == 3:
#    print("miercoles")
#elif numero == 4:
#    print("jueves")
#elif numero == 5:
#    print("viernes")
#elif numero == 6:
#    print("sabado")
#elif numero == 7:
#    print("domingo")
#else:
#    print("el numero ingresado no es valido") 


#ejercicio 5)Realice un programa que pida un número del 1 al 12 y diga el nombre del mes correspondiente.

#numero = int(input("ingresa un numero del 1 al 12:"))
#if numero == 1:
#    print("enero")
#elif numero == 2:
#    print("febrero")
#elif numero == 3:
#    print("marzo")
#elif numero == 4:
#    print("abril")
#elif numero == 5:
#    print("mayo")
#elif numero == 6:
#    print("junio")
#elif numero == 7:
#    print("julio")
#elif numero == 8:
#    print("agosto")
#elif numero == 9:
#    print("septiembre")
#elif numero == 10:
#    print("octubre")
#elif numero == 11:
#    print("noviembre")
#elif numero == 12:
#    print("diciembre")
#else:
#    print("el numero ingresado no es valido") 
