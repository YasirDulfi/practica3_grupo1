import json
import os
from models.showInformation import showInformation
from models.restKm import resetKm
from models.deleteCar import deleteCar
from models.addCar import addCar
from models.addOil import addOil
from models.travel import travel

from utils.doesJsonExist import doesJsonExists
from utils.validateInput import validateInput


def main():
    """
        1ºSe verifica si existe el json y si no se crea
        2ºSe muestra un menu en donde el cliente debe de escoger 
          una opción que cuadre dentro de las presentadas si no se 
          entrara en un bucle hasta que se cumpla de 
    """
    doesJsonExists()
    isMenuOpen = True

    while isMenuOpen ==  True:
        print('-----------------------------------------------------------')
        print('1º Mostramos la informacíon de los diferentes vehiculos \n')
        print('2º Añada un nuevo vehiculo a la lista \n')
        print('3º Añade combustible \n')
        print('4º Recorremos distancia \n')
        print('5º Resear el kilometraje de un vehiculo \n')
        print('6º Eliminar un vehiculo \n')
        print('0º Salir')
        print('-----------------------------------------------------------')

        isInputValid = False
        while isInputValid == False: 
            try:
                enteredOption = int(input('Introduzca el numero de la opción que desee: '))
                
            except:
                print('Introduzca un numero valido')
                print('-----------------------------------------------------------')
                continue

            print('-----------------------------------------------------------')
            if(isinstance(enteredOption, int) == True) : 
                isInputValid = True 
            elif( (enteredOption < 0) or (enteredOption >5)): 
                isInputValid = False 
    

        #Menu
        if(enteredOption < 0) : print('\n Introduzca un valor preestablecio \n') 
        if(enteredOption > 0) : optionManagement(enteredOption)
        if(enteredOption == 0) : 
            print('\n Esperamos que le haya gustado el programa \n')
            isMenuOpen = False



def optionManagement(option) :
    goBackMsg = '\n Si desea volver al menu pulse 0 en caso contrario introduzca cualquier otro valor: '

    if option == 1:
        funtionIsDone = False

        while not funtionIsDone:
            try:
                modelName = input('1º Introduce el nombre del modelo: ').strip().lower()

                if(validateInput('modelName', modelName) == True):
                    if showInformation(modelName) == True : funtionIsDone = True
                else:
                    raise Exception('\n Valor incorrecto, recuerde que el nombre del modelo no debe de llevar solo numeros')

            except Exception as errorMsg:
                print(errorMsg)

                returnMenu = input(goBackMsg)
                if(returnMenu == '0') : funtionIsDone = True
               
    if option == 2:
        funtionIsDone = False

        while not funtionIsDone:
            try:
                if addCar() == True : funtionIsDone = True
            except Exception as errorMsg:
                print(errorMsg)

                returnMenu = input(goBackMsg)
                if(returnMenu == '0') : funtionIsDone = True

    if option == 3:
        funtionIsDone = False

        while not funtionIsDone:
            try:
                modelName = input('-Introduce el nombre del modelo: ').strip().lower()

                try:   
                    littersOfOil = int(input('-Introduce cuantos litros se desea añadir:'))
                except:
                    print('Introuzca un valor valido')
                    print('-----------------------------------------------------------')
                    continue

                if((validateInput('modelName', modelName) == True) 
                and (validateInput("littersOfOil", littersOfOil )) ):
                    if addOil(modelName, littersOfOil) == True : funtionIsDone = True
                else:
                    raise Exception('\n Valor incorrecto, recuerde que el nombre del modelo no debe de llevar solo numeros')

            except Exception as errorMsg:
                print(errorMsg)

                returnMenu = input(goBackMsg)
                if(returnMenu == '0') : funtionIsDone = True
    
    if option == 4:
        funtionIsDone = False

        while not funtionIsDone:
            try:
                modelName = input('1º Introduce el nombre del modelo: ').strip().lower()
                
                try:
                    distance = float(input('Distancia a recorrer: '))
                except:
                    print('Introuzca un valor valido')
                    print('-----------------------------------------------------------')
                    continue

                if((validateInput('modelName', modelName) == True) 
                and (validateInput('distance', distance) == True)):
                    if travel(modelName, distance) == True : funtionIsDone = True
                else:
                    raise Exception('\n Valor incorrecto, recuerde que el nombre del modelo no debe de llevar solo numeros')

            except Exception as errorMsg:
                print(errorMsg)

                returnMenu = input(goBackMsg)
                if(returnMenu == '0') : funtionIsDone = True


    if option == 5:
        funtionIsDone = False

        while not funtionIsDone:
            try:
                modelName = input('1º Introduce el nombre del modelo: ').strip().lower()

                if(validateInput('modelName', modelName) == True):
                    if resetKm(modelName) == True : funtionIsDone = True
                else:
                    raise Exception('\n Valor incorrecto, recuerde que el nombre del modelo no debe de llevar solo numeros')

            except Exception as errorMsg:
                print(errorMsg)

                returnMenu = input(goBackMsg)
                if(returnMenu == '0') : funtionIsDone = True
    
    if option == 6:
        funtionIsDone = False

        while not funtionIsDone:
            try:
                modelName = input('1º Introduce el nombre del modelo: ').strip().lower()
                
                if(validateInput('modelName', modelName) == True):
                    if deleteCar(modelName) == True : funtionIsDone = True
                else:
                    raise Exception('\n Valor incorrecto, recuerde que el nombre del modelo no debe de llevar solo numeros')

            except Exception as errorMsg:
                print(errorMsg)

                returnMenu = input(goBackMsg)
                if(returnMenu == '0') : funtionIsDone = True



main()