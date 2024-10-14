"""Fucniones Return"""

#reutilizacion de codigo que podemos llamar desde cualquier parte
# usar el return 

def sum_range(min, max):
    
    sum = 0
    for i in range(min,max):
        sum += i  
    return sum

sum_range(1,10)

"""User Return """      #asiganmos valores en caso de obtener un nulo
def fin_volume(lenght, width=1, depth =1):
    return lenght * width * depth, width, True

lalo, man, tile = fin_volume(10, 2, 5)

print(lalo)
print(man)
print(tile)