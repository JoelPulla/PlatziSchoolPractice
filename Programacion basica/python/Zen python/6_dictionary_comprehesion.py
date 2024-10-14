""" Dict Comprehesion """

dic1 = {}

for i in range(1,5):
    dic1[i] = i
    
print(dic1)

dict2 = {i:i for i in range(1,11)}
print(dict2)

#agrega un valor ramndon a una diccionario que tiene las llaves 
# de una lita de ciudades
import random

peoples = random.randrange(0,1000000)
list_contries = ['col', 'mex', 'ecua', 'eu']
population_contries = {}

for i in list_contries:
    population_contries[i] = peoples
    
print(population_contries)


# # ejericico anteiror, utiliza dict comprehesion
population_contries = {i:peoples for i in list_contries}
print(population_contries)


# de una lista de nombres junta con una lista de edades
#con ello forma un programa que lo haga en un diccionrio 
# de la forma normal y con dictcompresion 

names = ['Joel', 'Fernanda', 'Valeria','Maria']
ages = [21, 23, 20,45]

dict3 = {}
for keys,value in zip(names, ages):
    dict3[keys]= value
print(dict3)

# con dict
dict4 = { keys:value for (keys,value) in zip(names,ages)}
print(dict4)

""" Dict comprehesion con condicionales"""

# En de una lista de paises pon numeros aleatorios 
# solo cuando sean mayores al numero 20 estos valores
# los obtenemos de otra lsita

import random

list_contries = ['col', 'ecu', 'arg', 'mex','bol']

dict5 = {keys:random.randint(1,30) for keys in list_contries  }
print(dict5)


dict6 = {keys:values for (keys, values) in dict5.items() if values> 20}
print(dict6)

# de un string cuales imprime en un diccionrio
# solo las bocales

text = 'Hola mi nombre es Joel Pulla'

dict7 ={abc.upper():abc.lower() for abc in text if abc in 'aeiou' }
print(dict7)

#agrega un contador