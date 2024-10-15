"""Map"""

#aplica procesos a todo los elementos de una lista

numbres = [1,2,3,4,5,6,7,8,9]
numbres_res1 = []

# de una lista de numeros, reliza la multiplicacion *2

for i in numbres:
    i = i*2
    numbres_res1.append(i)
    
print(numbres_res1)

# =========> Map <===========
                        #recive i y el resultado es i*2
                                #recore en numbers
numbres_res2 = map(lambda i:i *2, numbres)
# trasforma en una lsita
print(list(numbres_res2))

#### Ejemplo 2 

numbers_1= [1,2,3,4,5,]
numbers_2= [6,7,8,9] 

result = list(map(lambda x,y: x+y, numbers_1, numbers_2))

print(result)