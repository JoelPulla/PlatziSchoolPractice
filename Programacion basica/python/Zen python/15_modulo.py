"""Modulos"""

#son como las librerias que utilizamos 
# Modulos son ficheros que contienen un conjunto de funciones, variables o clases y que pueden ser usados por otros módulos


### sys ###
# para saber rutas 
import sys 

sys.path

### Re ###
# Comprensiones reguales 
import re 
text = "Mi numero de telefono es 409999 mi codiogo de pais 57436464 y suerte es 34i583"

result = re.findall('[0-9]+', text)
print(result)


### Time ###
# pra fechas

import time 

timestamp = time.time()
local = time.localtime()
local = time.asctime(local)
print(local)

### Colections ###
# Frecuencia de un caracter 
import collections

numbers = [ 1,23,43,5,3,43,46,6,4,4,5,67,7,7 ]
counter = collections.Counter(numbers)

print(counter)
