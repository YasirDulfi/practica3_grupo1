import json

def writeJson(data):
    #Si data no es vacio se escribe su contenido en el json
    if(bool(data) == True):
        try:
            with open("data/coches.json", "w") as json_file:
               json.dump(data, json_file)

        except:
            print('No se ha podido escribir correctamente los datos')