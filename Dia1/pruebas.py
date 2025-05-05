print ("")  
print ("Hola ejercicio para convertir grados Celsius a Fahrenheit ")

numeroEntero =  int(input("Dime los grados Celsius: "))
fahrenheit = (numeroEntero * 9/5) + 32
numeroEntero = float(numeroEntero)
print(" la temparatura en Fahrenheit es: " + str (fahrenheit))
print ("")
##################################################################
print(int(input("selecciona el tipo de pan: ")))

print(int(input("Selecciona el tipo de carne: 1. 250Gr 2. 300Gr")))

def valor_tipoPan(sele, acumulado):
    if sele ==1:
        acumulado = acumulado + 1000
        sele = float(input("Cual es el valor del pan: "))
        print("El valor del pan es: " + str(acumulado))
    elif sele ==2:
        acumulado = acumulado + 1500
        print ("El valor del pan es: " +str (acumulado))