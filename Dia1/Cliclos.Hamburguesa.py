## #######################################
## ########### EJERCICIO Hamburguesa ###########
## #######################################
## Desarrollado por : Angel Niño Davila 
## Cedula : 1.005.335.914
## #######################################


print("Bienvenido a la hamburguesa")

# Inicializar la variable acumulado
acumulado = 0

cantidadHamburguesas = int(input("Cuantas hamburguesas desea: "))
print(cantidadHamburguesas)

for i in range(cantidadHamburguesas):
    tipoPan = int(input("Seleccione el tipo de pan 1. para centeno, 2. para avena: "))
    if tipoPan == 1:
        print("El tipo de pan es centeno")
        acumulado = acumulado + 1000
    elif tipoPan == 2:
        print("El tipo de pan es avena")
        acumulado = acumulado + 1500
    else:
        print("Opción no válida, intente nuevamente.")

    tipoCarne= int(input("que tipo de carne deseas: 1.250gr o 2. 300gr: "))
    if tipoCarne ==1:
        print ("seleccionaste carne de 250gr")
        acumulado = acumulado + 5000
    elif tipoCarne ==2:
        print ("Escogiste la carne de 300gr")
        acumulado = acumulado + 7000  
    else:
        print("Opción no válida, intente nuevamente.")

    tipoPollo = int(input(" Que cantidad de pollo deseas. 1. 250gr, 2. 350gr: "))
    if tipoPollo ==1: 
        print("Seleccionaste pollo de 250gr")
        acumulado = acumulado + 4500
    elif tipoPollo ==2:
        print("Seleccionaste pollo de 350gr")
        acumulado=acumulado+5500

    tipoPolloD = int(input("Selecciona la cantidad de pollo Desmechado, 1.250gr o 2.350gr: "))
    if tipoPolloD==1:
        print("Seleccionaste pollo desmechado de 250gr")
        acumulado = acumulado + 6500
    elif tipoPolloD==2:
        print("Seleccionaste pollo desmechado de 350gr")
        acumulado = acumulado + 7500

    tipoTocineta = int (input("Selecciona la cantidad de tocineta, 1. Una lonja o 2. Dos lonjas: "))
    if tipoTocineta==1:
        print("Seleccionaste una lonja de tocineta")
        acumulado = acumulado + 1500
    elif tipoTocineta==2:
        print("Seleccionaste dos lonjas de tocineta")
        acumulado = acumulado + 2500

    tipoPapa = int(input("Selecciona el tipo de papa: 1. francesa o 2. cascos: "))
    if tipoPapa==1:
        print("Seleccionaste papa francesa")
        acumulado = acumulado + 5000
    elif tipoPapa==2:
        print("Seleccionaste papa en cascos")
        acumulado = acumulado + 6000

    tipoBebida = int (input("Selecciona la bebida 1. Gaseosa 2. Cerveza club 3. naranjada: "))
    if tipoBebida==1:
        print("Seleccionaste gaseosa")
        acumulado = acumulado + 5000
    elif tipoBebida==2:
        print("Seleccionaste cerveza club")
        acumulado = acumulado + 8000
    elif tipoBebida==3:
        print("Seleccionaste naranjada")
        acumulado = acumulado + 9000 
    
    total = acumulado + (acumulado*0.1)
    print("El Servivio del 10 Porciento es: ", int (acumulado*0.1))
    print("El total con Servicio Incluido es: " , int(total))