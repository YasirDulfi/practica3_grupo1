import json
#Se carga el archivo y se devulve 
def loadJson():
    try:
            with open("data/coches.json", "r") as json_file:
                data = json.load(json_file)
                return data
    except:
            print('No se ha podido cargar correctamente la base de datos')
            return False

