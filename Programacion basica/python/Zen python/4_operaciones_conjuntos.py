
set1 = {'col', 'mex', 'bol'}
set2 = {'pe', 'col', 'ecu'}


###union 
set1_set2 = set1.union(set2)
print(set1_set2)
print(set1|set2) # "|" operador de union 

## Interseccion 

set1_set2 = set1.intersection(set2) # muestra cual es el comun entre dos conjuntos 
print(set1_set2) 
print(set1&set2) # & operarador de interseccion 

## Diferrencia o restas de set 
set1_set2 = set1.difference(set2)
print(set1_set2)
print(set1- set2)

# Symetric diference => muestra los conjuntos que no son similares 
set1_set2 = set1.symmetric_difference(set2)
print(set1_set2)
print(set1^set2) #signo de intercalacion


############### Ejercicio ##############

"""
Para resolver este desafío, debes escribir un algoritmo que elimine los elementos repetidos para obtener un conjunto único llamado new_set.

Este algoritmo recibirá como entrada cuatro conjuntos de países, estos países serán de todo el continente americano divididos de la siguiente manera:

countries - Países del continente en general.
northAmerica - Países del norte de América.
centralAmerica - Países del centro de América.
southAmerica - Países del sur de América.
En resumen, el algoritmo deberá eliminar los elementos repetidos de los cuatro conjuntos de países y obtener un conjunto único llamado new_set.

"""

countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = countries|northAm|centralAm|southAm

new_set = set(new_set)
# Escribe tu solución 👇


print(new_set)
