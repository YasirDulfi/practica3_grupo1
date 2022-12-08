
from utils.loadJson import loadJson
from utils.writeJson import writeJson

def travel(modelName, distance):
    print('se ejecuta travel')
    CONSUMO = 6
    data = loadJson()

    for car in data["cars"]: 
        if car["modelo"] == modelName:
            autonomia = (car["cargaCombustible"] *100 / CONSUMO) 
            autonomia_restante = (autonomia - distance)

            if distance < autonomia:
                car['autonomia'] = autonomia_restante
                car['km'] = car['km'] + distance
                print("Has recorrido {} y te quedan {} de autonomia".format (distance,distancia_recorrida))
                writeJson(data)
            else:
                print("no tienes suficiente combustible para recorrer {} km".format(distance))
                print('-----------------------------------------------------------')

                return False
            return True
    return False



        


