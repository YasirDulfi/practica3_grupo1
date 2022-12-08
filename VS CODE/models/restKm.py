import json
from utils.writeJson import writeJson
from utils.loadJson import loadJson

def resetKm(modelName):
    print('execution resetKm')
    data = loadJson()


    for car in data['cars']:
        if(car['modelo'] == modelName):
            car['km'] = 0
            writeJson(data)

    