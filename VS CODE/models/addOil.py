import json
from utils.writeJson import writeJson
from utils.loadJson import loadJson

def addOil(modelName, littersOfOil):
    print('execution addOil')
    CONSUMO = 6
    data = loadJson()

    for car in data ['cars']:
        if ((car['modelo'] == modelName) and (int(car['cargaCombustible']) + littersOfOil <= 60)):                                          
           car['cargaCombustible'] = float(littersOfOil) + car['cargaCombustible']
           car['autonomia'] = (car['cargaCombustible'])*100/CONSUMO
           autonomia = 6 * float(car['cargaCombustible'])
           print('Tiene {aut} de autonomia'.format(aut = str(autonomia)))                
           writeJson(data)
           return True        
        if ((car['modelo'] == modelName) and (int(car['cargaCombustible']) + littersOfOil > 60)):
            max = 60 - int(car['cargaCombustible'])
            print('Ha excedido el limite de 60 litros')
            print('Puede añadir un maximo de {maxLiters}'.format(maxLiters = str(max)))
            print('-----------------------------------------------------------')

            return False 
    return False
        
        