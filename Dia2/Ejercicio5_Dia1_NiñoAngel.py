## #######################################
## ########### EJERCICIO Dia 1 ###########
## #######################################


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

## Desarrollado por : Angel Niño Davila 
## Cedula : 1.005.335.914