import json

def abrirJSON():
    listaArtista=[]
    with open("./data.json",'r') as openFile:
        listaArtista=json.load(openFile)
    return listaArtista

def guardarJSON(dic):
    with open("./data/datos.json",'w') as outFile:
        json.dump(dic,outFile)
