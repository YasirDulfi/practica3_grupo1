#dependiento del nombre de la variable se seleciona
# la condicional apropiada  y se valida
def validateInput(inputName, inputValue):
    if((inputName == "modelName") and
        (inputValue.isdigit() == False)): return True

    if((inputName == "littersOfOil") and 
        (inputValue > 0)): return True

    if((inputName == "distance") and 
        (inputValue > 0)): return True

    if((inputName == "peso") and (1000>inputValue >2000)):
        return True 
    return False