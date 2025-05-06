## #######################################
## ########### EJERCICIO Dia 1 ###########
## #######################################
## Desarrollado por : Angel Niño Davila 
## Cedula : 1.005.335.914
## #######################################

print ("Hola soy el ejercicio Sumar")

numero1 = int (input("Dime un numero: "))
numero2 = int (input("segundo numero: "))
print("")
print ("La suma de estos numeros es: " +str(numero1 + numero2))


print ("")  

print ("Hola soy el ejercicio de restar")

numero1 = int (input("primer nummero:"))
numero2 = int (input("Segundo numero: "))
print("")
print ("La resta es : " + str (numero1-numero2))

print ("")  

print ("Hola soy el ejercicio de el mayor de tres numeros ")

numero1 = int (input("primer numero: "))   
numero2 = int (input("Segundo numero: "))
print("Dime el tercer numero")
numero3 = int (input("Tercer numero: "))
print("")
if numero1>numero2:
    print("el mayor es: " +str( numero1))
else:
    if numero2 > numero1 and numero3 :
        print("el numero mayor es: " +str (numero2 ) )
    else:
        print("El mayor es: " +str (numero3))


print ("")  

print ("Algoritmo para calcular el factorial de un número")

factorial = int (input("Numero a factorizar: "))
for i in range (1,factorial):
    factorial = factorial * i
print("")   
print ("El factorial es: " +str(factorial))


print ("")  

print("Hola soy el ejercicio para saber si es un numero primo o no")
print("")
num = int (input("numero : "))

if num <= 1: 
    print("El número no es primo.")
else:
    contador = 0 
for i in range(2,num -1):
    if num % i == 0:
        contador += 1
if contador == 0:
    print("El número es primo.")
else: 
    print("El número no es primo.")


print ("")  

print ("Hola ejercicio para convertir grados Celsius a Fahrenheit ")

numeroEntero =  int(input("Dime los grados Celsius: "))
fahrenheit = (numeroEntero * 9/5) + 32
print("")
print(" la temparatura en Fahrenheit es: " + str (fahrenheit))


print ("")

print ("Algoritmo para determinar si un número es par o impar ")

def es_par(n):
    return n % 2 == 0
n = int(input("Ingrese un número entero: "))
if es_par(n):
    print("Es par" )
else:
    print("Es impar")

print ("")  

print ("Hola ejercicio para calcular el área de un triángulo")
print("")
base = float(input("Base del triángulo: "))
altura = float(input("Altura del triángulo: "))
area = (base * altura) / 2
print("Área del triángulo:", area)

print ("")  

print("Ejercicio para crear una tabla de multiplicar")
print("")   

n = int(input("Ingrese un número entero: "))
for i in range(1, 10+1):
    print(f"{n} x {i} = {n * i}")

print ("")  

print("Ejercicio para calcular el área de un círculo")
print("")  
circulo = float(input("Ingrese el radio del círculo: "))
area = 3.14 * (circulo ** 2)
print("Área del círculo:", area)