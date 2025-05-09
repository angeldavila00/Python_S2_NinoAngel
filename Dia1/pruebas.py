#####
#PRUEBAS DE CODIGO##
# Leer la cantidad de estudiantes
if __name__ == '__main__':
    estudiantes = []
    for _ in range(int(input())):
        nombre = input()
        calificacion = float(input())
        estudiantes.append([nombre, calificacion])
    
    # Encontrar la segunda calificación más baja
    # Primero obtenemos todas las calificaciones únicas y las ordenamos
    calificaciones_unicas = sorted({est[1] for est in estudiantes})
    segunda_calificacion = calificaciones_unicas[1]
    
    # Filtrar estudiantes con esa calificación y ordenar sus nombres
    estudiantes_segunda = [est[0] for est in estudiantes if est[1] == segunda_calificacion]
    estudiantes_segunda_ordenados = sorted(estudiantes_segunda)
    
    # Imprimir cada nombre en una línea nueva
    for nombre in estudiantes_segunda_ordenados:
        print(nombre)



## Desarrollado por : Angel Niño Davila 
## Cedula : 1.005.335.914