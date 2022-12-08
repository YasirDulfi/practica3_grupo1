from utils.loadJson import loadJson

def doesCarExist(modelName):
    data = loadJson()

    for car in data['cars']:
        if(car['modelo'] == modelName):
            return True

    return False