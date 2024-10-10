"""Crud de python """

# Crud corresponde a C => Create, R=> Read, U=> Update, D => Delete, nos permite
# intercatuar con los datos esta ideologia se puede utilizar el valor en cualquier lenguaje

set_contries = {'mex', 'ecu','col', 'usa'}
print(len(set_contries)) #saber el tamano

# condicinal en un conjunto # Read
print( 'lop' in set_contries)

##Create
set_contries.add('jap')
print(set_contries)

## update 
set_contries.update({'esp', 'bol', 'jap'})
print(set_contries)

## Delete
set_contries.remove('jap')
print(set_contries) #con este metodo si no ecuentra el valor del set nuestro programa estallara

## Delete no explotable 
set_contries.discard('jap')
print(set_contries)

## Vaciar la lista 
print(set_contries.clear())


""" Funciones de set:

add(): Añade un elemento.

update(): Añade cualquier tipo de objeto iterable como: listas, tuplas.

discard(): Elimina un elemento y si ya existe no lanza ningún error.

remove(): Elimina un elemento y si este no existe lanza el error “keyError”.

pop(): Nos devuelve un elemento aleatorio y lo elimina y si el conjunto está vacío lanza el error “key error”.

clear(): Elimina todo el contenido del conjunto
"""