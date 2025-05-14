#####
#PRUEBAS DE CODIGO##
# ##########################
# #### Clase ######
# ##########################

lista = [{
        "color":"rosado",
        "cosa":"pinza",
        "textura":"corrugado",
        "forma":"triangular"
}, {
        "color":"rojo",
        "cosa":"carta",
        "textura":"lisa",
        "forma":"circular"
}, {
        "color":"azul",
        "cosa":"mariposa",
        "textura":"suave",
        "forma":"cuadrado"
}]


#imprimir la textura de cada diccionario
for i in range(len(lista)):
    print(lista[i]["textura"])

#crear una nueva lista despues de la nueva lista
texturas=[]

lista.append(texturas)

abc={
    "aa":1,
    "bb":2
}
texturas.append(abc)
print(texturas)



#agregar una nueva key : nueva informacion
lista[0]["tamaño"]="mediano"
print (lista[0])
    
print(lista[1]["cosa"])



## Desarrollado por : Angel Niño Davila 
## Cedula : 1.005.335.914