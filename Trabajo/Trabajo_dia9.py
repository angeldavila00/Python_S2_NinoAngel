from funciones.funcionesGGDD import *

listaArt = abrirJSON()

booleanito = True

while(booleanito):
    listaArt=abrirJSON()
    print("_________________________________")
    print("Bienvenido a nuestra base de datos de artistas musicales")
    print("_________________________________")
    print("1. Registrar datos de un nuevo Artista")
    print("2. Registro y gestion de los paises")
    print("3. Registro de los generos musicales")
    print("4. Mostrar todos los artistas de un pais y tiempo especifico")
    print("5. Generacion de modulo de resportes")
    opcionUsuario=int(input("Escoja una opción (Numérica):"))
    if(opcionUsuario==1):
        print("")
        


