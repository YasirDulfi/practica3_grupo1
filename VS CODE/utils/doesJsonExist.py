import json
import os
#Se comprueba si el JSON existe y dependiendo 
def doesJsonExists():
    print('execute doesJsonExists')

    doesFileExists = os.path.exists("data/coches.json")

    if(doesFileExists == True):
        return True
    else:
        with open('data/coches.json', 'w') as f:
            f.write("ladsf")