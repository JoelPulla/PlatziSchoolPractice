"""LAMDA"""

# Nota: son funciones lamda o tambien llamadas anonimas 
# nos sirven para crear operaciones simples en la cual podemos
# o no podemos agrergar un nombre para usarlo se declara con la 
# palabra reservada lamda "en resumen no sirve para realizar operaciones 
# sencillas en un sola linea de codigo sin necesidad de crear una funcion "

# name  p reservada
suma = lambda a,b:    a+b
            # datos   operacion
print(suma(100,50))



## Lamda uso map 
#por cada posicion de un alista cumple un funcion 

numbers = range(11) #definimos un rango 
poten_num = list(map(lambda x: x**2, numbers)) # en una lista por cada dato usa lamda y elevale al x hasta numbers
print(f"Cuadrados: {poten_num} y su tamaño de carasteres es: {len(poten_num)}" )

#lamba filter pares 

pares = list(filter(lambda x : x%2 == 0, numbers ))
impares = list(filter(lambda x : x %2 ==1, numbers ))

print(f"Pares: {pares} Impares : {impares}")