# ##########################
# #### Clase Dia 6 ######
# ##########################
# Diccionarios
#Un DICccionario  es una colección de elementos , donde cada elementos insertado tiene una llave úntica, 
# la cual va acompañada de un valor 

##Diccionario con listas
diccionarioRobusto={
    "id":1,
    "nombre":"Pedro",
    "apellido":"Gómez",
    "edad":25,
    "telefonos":[{"codigo":57,
                  "numero":3023019865,
                  "tipo":"trabajo"}
                 ,{"codigo":1,
                   "numero":3983054625,
                   "tipo":"personal"}]
}
diccionarioRobusto2={
    "id":2,
    "nombre":"Corpus",
    "apellido":"Bejarano",
    "edad":27,
    "telefonos":[{"codigo":58,
                  "numero":2323057565,
                  "tipo":"trabajo"}
                 ,{"codigo":22,
                   "numero":6857493658,
                   "tipo":"personal"}]
}
listaRobusta=[]
listaRobusta.append(diccionarioRobusto)
listaRobusta.append(diccionarioRobusto2)
print("")
print("")
print(listaRobusta)
print("")
print("")
#print(listaRobusta[0]["telefonos"][1]['numero'])

for i in range(len(listaRobusta[0]["telefonos"])):
    if(listaRobusta[0]["telefonos"][i]['tipo']=="trabajo"):
        print(listaRobusta[0]["telefonos"][i]['numero'])
print("")
print("")
numeroPrimeraPersona=listaRobusta[0]["telefonos"][1]['numero']
tipoNumeroPP=listaRobusta[0]["telefonos"][1]['tipo']
print(str(numeroPrimeraPersona)+ tipoNumeroPP)
userCant=2
booleanito = True
while(booleanito):
    print("#################")
    print("#### Librería de personas ####")
    print("#################")
    #CRUD (CREATE , READ , UPDATE & DELETE)
    print("1. Crear Persona")
    print("2. Mostrar todas las personas")
    print("3. Mostrar a una persona individual")
    print("4. Actualizar a una persona en específico")
    print("5. Eliminar a una persona en específico")
    print("6. Cerrar programa")
    opcionUsuario=int(input("Escoja una opción (Numérica):"))

    ###CREAR USUARIO    

    if(opcionUsuario==1):
        print("#################")
        print("#### Crear Persona ####")
        print("#################")
        
        ################################################33

        nombre=input("Ingresa el nombre: ")
        apellido=input("Ingresa el apellido: ")
        edad=int(input("Ingresa la edad: "))
        canTelefono=int(input("Ingresa la cantidad de telefonos: "))

        diccionarioUsuario={

            "id":(listaRobusta[len(listaRobusta)-1]),
            "Nmbre":nombre,
            "apellidio": apellido,
            "edad": edad,
            "telefono": []
        }

        for i in range(canTelefono):
            codigo= int(input("Dime el codigo: "))
            numero =int(input("Dime el numero: "))
            tipo = input("Ingresa el tipo de telefono: ")

            dataTelefono = {
                "codigo": codigo,
                "numero": numero,
                "tipo": tipo
        
        }
        
        diccionarioUsuario["telefono"].append(dataTelefono)


        listaRobusta.append(diccionarioUsuario)

       
        
        print(f"El usuario {nombre} fue creado con exito")
        
        

    elif(opcionUsuario==2):
        for i in range(len(listaRobusta)):
            print("#################")
            print("#### Persona #",i+1," ####")
            print("#################")
            print("ID:", listaRobusta[i]["id"])
            print("nombre:",listaRobusta[i]["nombre"])
            print("Apellido:",listaRobusta[i]["apellido"])
            print("Edad",listaRobusta[i]["edad"])
            
            for q in range(len(listaRobusta[i]["telefonos"])):
                print("---------------------------")
                print("Telefono#",q+1,":")
                print("#### - Código:",listaRobusta[i]["telefonos"][q]["codigo"])
                print("#### - Numero:",listaRobusta[i]["telefonos"][q]["numero"])
                if(listaRobusta[i]["telefonos"][q]["tipo"] == "personal"):
                    print("#### - Tipo: Es su número Personal")
                else:
                    print("#### - Tipo: Es su número de Trabajo")
                
                print("---------------------------")
    elif (opcionUsuario==3):
        print("##########################")
        print("### Persona individual#####")
        print("##########################")
        opcionIndividual = int(input("por favor ingresaa el ID de la persona"))
        print("##########################")
        print("Persona a", opcionIndividual)
        print("##########################")
        print("ID:", listaRobusta[opcionIndividual-1])


        
            
            
    elif(opcionUsuario==6):
        print("Chaousssss")
        booleanito=False
    else:
        print("No es una opción válida")

    
    
    
#Desarrollado por Pedro Felipe Gómez : C.C-1.555.444.333