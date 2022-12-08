import json
from utils.writeJson import writeJson
from utils.loadJson import loadJson
from utils.doesCarExist import  doesCarExist
def addCar():
    print("Se ejecuta addCard")
    data = loadJson()

    isCarInfoValid = False
    while isCarInfoValid == False:
        carModel = input('Introduzca el nombre del modelo:  ').strip().lower()
        try:
            carWeight = float(input('Intruce el peso del coche: '))
        except:
            print('Introduce un numero que sea valido')

        if(doesCarExist(carModel)== False):
            carInfo = {
                "modelo": carModel,
                "peso": carWeight,
                "cargaCombustible": 0,
                "km": 0,
                "autonomia": 0
            }
            data['cars'].append(carInfo)
            writeJson(data)

            print (" su coche modelo {} dispone de 0 autonomia".format(carModel))
            print ("su coche modelo {} ha recorrido 0 km".format(carModel))

            return True
        else:
            print("este modelo ya existe, introduca uno nuevo \n")
            return False
    

                        