"""Los slides para las listas"""

#Nota: Sirven para cuando yo copio la informacion de una lista no se duplique si 
#      aplico algun metodo la lista que copie los datos por ejemplo 

list_a = [1,2,3,4,5,6]
list_b = list_a

print(list_a)
print(list_b)

del list_a[0:2] #realizamos una operacion cualqueira

print(list_a) 
print(list_b) #vemos que ambas varibles fueron afectadas apesar de que solo aplique en una 

print(id(list_a)) #con el metodo id podemos identificar el espacio en memoria donde se ubico la informacion
print(id(list_b)) #ambas bariables a y b apuntan al mismo id por lo que si se afecta en una se afectan en ambas 

        ##Aplicamode metodo slice 
m_slice = list_a[:] #realizamos una copia exacta
print(id(list_a)) 
print(id(list_b))
print(id(m_slice)) # nos aroja un diferente espacio en memoria

list_a.append(100)
print(list_a)
print(list_b)
print(m_slice) # vemos que esta varible no recibio al gun campo 