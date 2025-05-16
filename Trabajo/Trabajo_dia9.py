from funciones.funcionesGGDD import *

listaArt = abrirJSON()

booleanito = True

while(booleanito):
    listaArt=abrirJSON()
    print("_________________________________")
    print("Bienvenido a nuestra base de datos de artistas musicales")
    print("_________________________________")
    print("1. Registrar datos de un nuevo Artista")
    print("2. Registrar de paises")
    print("3. Registro de los generos musicales")
    print("4. Mostrar todos los artistas de un pais y tiempo especifico")
    print("5. Generacion de modulo de resportes")
    opcionUsuario=int(input("Escoja una opción (Numérica): "))
    if(opcionUsuario==1):
        print("_________________________________")
        print("Registro de un nuevo artista: ")
        print("_________________________________")
        nombreArt= input("Dime el nombre del artista: ")
        pais= input("Dime el pais del artista: ")
        añosActividad= int(input("Dime cuantos años lleva: "))
        añoLanzamiento= int(input("Dime el año del primer lanzamiento: "))
        genero=input("Dime cual es el genero de musica: ")
        unidades= (input("Dime: "))
        ventas= int(input("Dime el numero de  ventas reclamadas: "))
        estado=int(input("Dime el estado del artista 1.Activo 2.Inactivo: "))
        
        if estado==1:
            print("Estado Activo")
            estadoTexto= "Estado Activo!"
        elif estado==2:
            print("Estado Inactivo")
            estadoTexto = "Estado Inactivo"

    DiccionarioArtista={
        "Artist name": nombreArt,
        "Country": pais,
        "Active years": añosActividad,
        "Release year of first charted record": añoLanzamiento,
        "Genre": genero,
        "Total certified units":unidades,
        "Claimed sales": ventas,
        "state":estado
    }
    listaArt.append(DiccionarioArtista)
    print(f"persona {nombreArt} fue creada con exito y se encuentra en {estadoTexto}")


    if(opcionUsuario==2):
        print("_________________________________")
        print("Actualizacion y registro de paises: ")
        print("_________________________________")
        print("1. Registrar un pais ")
        print("2.Leer el pais de algun artista: ")
        print("3. modificar un pais:  ")
        print("4. Eliminar un pais: ")
        opcionUsuario=int(input("Escoja una opción (Numérica): "))
        if opcionUsuario==1: #Estoy guardando el usuario a modificar
            paisTemporal= input("¿Cuál es el pais que quieres registrar?:")
            nombreTemporal=input("¿Cuál es el nombre del artista que quieres poner en ese pais?: ")
            cantPaises= int(input("¿Cuántos paises quieres registrar? "))
            listaPaisTemporal=[]
            for i in range(cantPaises):
                areaPais=int(input(f'¿Cuál es el pais # ${i+1}?:'))
                nombrePersonal=int(input(f"¿Cuál es el nombre del artista {i+1}? " ))
                tipoPais=(input("seguro desear agregar ese pais? 1. si 2. No "))
                if(tipoPais==1):
                    diccionarioTemporal={
                        "Country":paisTemporal,
            "Artist name":nombreTemporal,
            "tipo":"personal"
                }
                listaPaisTemporal.append(diccionarioTemporal)
        elif(tipoPais==2):
            print ("No se realizo el registro")
                
        listaPaisTemporal.append(diccionarioTemporal)
        

    
        if(opcionUsuario==3):
            pass
        if(opcionUsuario==4):
            pass
        if(opcionUsuario==5):
            pass


    
    

