import json
from utils.loadJson import loadJson

def showInformation(modelName):
    print('execution showInformation')
    data = loadJson()

    for car in data['cars']:
        if(car['modelo'] == modelName):
            print ('\nPeso:', car['peso'])
            print ('\nCombustible:', car ['cargaCombustible'])
            print ('\nKm recorridos:', car['km'])
            print ('\nAutonomia:', car['autonomia'])
            print ('')
            return True
    return False
            
           
            
    
