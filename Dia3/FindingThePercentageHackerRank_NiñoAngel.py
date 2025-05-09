if __name__ == '__main__':
    n = int(input())
    estudiantes = {}
    
    for _ in range(n):
        datos = input().split()
        nombre = datos[0]
        calificaciones = list(map(float, datos[1:]))
        estudiantes[nombre] = calificaciones
    
    query_name = input()
    
    if query_name in estudiantes:
        promedio = sum(estudiantes[query_name]) / len(estudiantes[query_name])
        print("{0:.2f}".format(promedio))
    else:
        print("Estudiante no encontrado")