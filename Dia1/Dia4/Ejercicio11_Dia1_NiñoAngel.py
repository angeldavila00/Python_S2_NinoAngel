## #######################################
## ########### EJERCICIO Dia 1 ###########
## #######################################


print("Ejercicio de generar una serie de Fibonacci")

cantMax= int(input("Dame el numero maximo de la sucesion: "))

a=0
b=1
x=1
while x <= cantMax:
    print("", a)
    c=a+b
    a=b
    b=c
    x=x+1

## Desarrollado por : Angel Niño Davila 
## Cedula : 1.005.335.914
