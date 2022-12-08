from utils.writeJson import writeJson
from utils.loadJson import loadJson

def deleteCar(modelName):
    print('execution deleteCar')
    data = loadJson()

    """
    Se itera en cada coche en busqueda del modelo
    que se ha de eliminar.
    Como el JSON tiene guardado a cars en un array
    he decidio crear una variable i
    la cual en cada iteración añade un +1 el
    cual nos sirve para hallar el index del objeto a 
    eliminar
    """
    i = 0
    for car in data['cars']:
        
        if(car['modelo'] == modelName):
            del data['cars'][i]
            writeJson(data)
            return True
        i = i+1