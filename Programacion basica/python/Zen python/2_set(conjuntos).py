""" SET => conjuntos """
# Los conjuntos no permiten duplicacion de datos 
# no tienen un orden 
# son mutables 

set1 = {'hola', 'este', 'es', 'un', 'set'}
print(set1)
print(type(set1))

# puedes ser de varios tipos 
set2 = {100, 'este', False, 'un', True, False, 10.30}
print(set2)

#define un set con la palabra reservada
set3 = set('Hola mundo JAJAJja')
print(set3)

#set de tuplas
set4 = set(('hola', True, 10,  5))
print(set4)
print(type(set4))


example_list = [1,2,3,4,5,5,6,7,8,9]
# set de una lista de numeros 
set5 = set(example_list)
print(set5)

#trasformamos un set a una lista
list_set = list(set5)
print(list_set)