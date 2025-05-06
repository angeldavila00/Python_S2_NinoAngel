## #######################################
## ###########Clase Dia 1 ###########
## #######################################

#Iporimir el piton
print("Hola Mundo")

#Creacio de variables 
#1. DAto tipo string 
nombre = "Angel"
print(type(nombre))

#2.Dato tipo numero entero
numeroEntero=5
print(numeroEntero)
print(type(numeroEntero))

#3. Dato tipo numero decimal
numeroReal=5.3
print(type(numeroReal))

#4. Dato tipo double
numeroPi= 3.1416
print(numeroPi)
#5. Dato tipo booleano
booleanito = True
print(booleanito)

#6. Tipo de dato complejo 
numeroComplejo = 3 + 2j
print(numeroComplejo)
print(type(numeroComplejo))

#Convertir un numero entero (Int) a decimal (Float)
numeroNUevo = float(numeroEntero)
print(numeroNUevo)
# ######################################

# ciclo for (Hasta)
for i in range(5):
    print(i)
print ("")
# ciclo for (Desde - Hasta)
for i in range (0,5):
    print (i)
print ("")
# ciclo for (Desde - Hasta - paso)
for i in range (1,5,1):
    print(i)
print ("")  

# ######################################
# ciclo while 
booleanitoNuevo = True
while(booleanitoNuevo==True):
    print("sigo siendo verdadero")
    booleanitoNuevo =False

    
    # Opcion 2.
while(booleanitoNuevo):
    print("sigo siendo verdadero")
    booleanitoNuevo =False

print("")   
# ######################################

# Condicionales if .- else
texto =("corpus")
if(texto=="corpus"):
    print("El texto es igual a corpus")
else:
    if(texto=="Sharick"):
        print("El texto es igual a Sharick")
    else:
        print("El texto no es igual a corpus ni a Sharick")


# condiconal elif

if (texto=="corpus"):
    print("El texto es igual a corpus")
elif (texto=="Sharick"):
    print("El texto es igual a Sharick")
else:
    print("El texto no es igual a corpus ni a Sharick")

# Anidar condicionales  

booleanitocorpus1= True
booleanitocorpus2= False
if (booleanitocorpus1==True and booleanitocorpus2==True):
    print("Ambos son verdaderos")
else:
    print("ambos son iguales")
# ######################################

# Entrada de usuario
nombreusuario = input ("Cual es tu nombre: ")
print("Hola" ,nombreusuario)
# Cateo de string a numero 
edadUsuario = int(input("Cual es tu edad: "))
edadUsuario = edadUsuario + 5
print("La edad de " + nombreusuario + " es de " + str(edadUsuario))

# ######################################
# Funciones

def areaCirculo(radio):
    valorPi = 3.1416
    resultadoFinal = valorPi * (radio ** 2)
    return resultadoFinal

# Llamar la funcion
radioUsuario = float(input("Cual es el radio del circulo: "))
print("El area del circulo es: " + str(int(areaCirculo(radioUsuario))))

#2. Funcion con retorno y sin parametros
def valorDolar():
     return  4.299
valorFinalDolar=valorDolar()
print("El valor del dolar es: " + str(valorFinalDolar))

#3. Funcion sin retorno y con parametros
def concatenarNombres(nombre,apellido):
    print("El nombre completo es: " + nombre + " " + apellido)
concatenarNombres ("Angel", "Davila")
#4. Funcion sin retorno y sin parametros
def funcionX():
     print("Hola soy la funcion X")



## Desarrollado por : Angel Niño Davila - Cedula : 1.005.335.914
