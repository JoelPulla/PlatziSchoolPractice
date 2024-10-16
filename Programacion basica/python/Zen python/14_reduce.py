""" Funcion Reduce"""

import functools

numbers = ['Joel','tania', 'cristina', 'Erika']
# result =  functools.reduce(lambda counter, item: counter + item, numbers)
# print(result)

def count(counter , item):
    print("contador ===", counter)
    print("Item =====", item)
    
    return counter + item

result = functools.reduce(count, numbers)
print(result)

numbers = [1,2,3,4,5,6,7,8,9]
# result =  functools.reduce(lambda counter, item: counter + item, numbers)
# print(result)

def count(counter , item):
    print("contador ===", counter)
    print("Item =====", item)
    
    return counter + item

result = functools.reduce(count, numbers)
print(result)