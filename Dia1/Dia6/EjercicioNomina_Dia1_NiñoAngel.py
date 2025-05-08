## #######################################
## ########### EJERCICIO Nomina ###########
## #######################################


print("Bienvenido a la Nómina ACME")

# Inicializar variables
valorHora = 20000
totalBruto = 0
totalNeto = 0
totalEPS = 0
totalPension = 0  

mayorNeto = float('-inf')  
menorNeto = float('inf')  
nombreMayor = ""
nombreMenor = ""

# Ingreso de la cantidad de empleados
N = int(input("Ingrese la cantidad de empleados: "))

for i in range(1, N + 1):
    print(f"\nIngrese el nombre del empleado {i}:")
    nombre = input()

    print(f"Ingrese las horas trabajadas del empleado {i}:")
    horasTrabajas = int(input())

    sueldoBruto = horasTrabajas * valorHora
    descuentoEPS = sueldoBruto * 0.04
    descuentoPension = sueldoBruto * 0.04
    sueldoNeto = sueldoBruto - descuentoEPS - descuentoPension

    totalBruto += sueldoBruto
    totalEPS += descuentoEPS
    totalPension += descuentoPension
    totalNeto += sueldoNeto

    if sueldoNeto > mayorNeto:
        mayorNeto = sueldoNeto
        nombreMayor = nombre
    
    if sueldoNeto < menorNeto:
        menorNeto = sueldoNeto
        nombreMenor = nombre

    # Información del empleado
    print("-----------------------------")
    print("Empleado:", nombre)
    print("Sueldo Bruto:", sueldoBruto)
    print("Descuento EPS:", descuentoEPS)
    print("Descuento Pensión:", descuentoPension)
    print("Sueldo Neto:", sueldoNeto)
    print("-----------------------------")

if N > 0:
    promedioBruto = totalBruto / N
    promedioNeto = totalNeto / N
else:
    promedioBruto = 0
    promedioNeto = 0

# Información general
print("\n-----------------------------")
print("Total Sueldos Brutos:", totalBruto)
print("Total Descuento EPS:", totalEPS)
print("Total Descuento Pensión:", totalPension)
print("Total Sueldos Netos:", totalNeto)
print("-----------------------------")
print("El empleado que más gana es:", nombreMayor, "con un sueldo neto de:", mayorNeto)
print("El empleado que menos gana es:", nombreMenor, "con un sueldo neto de:", menorNeto)
print("-----------------------------")
print("Promedio de Sueldos Brutos:", promedioBruto)
print("Promedio de los Sueldos Netos:", promedioNeto)

## Desarrollado por : Angel Niño Davila 
## Cedula : 1.005.335.914