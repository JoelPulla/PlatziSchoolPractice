"""
list_v1 = []

for numbers in range(1,11):
    list_v1.append(numbers)
    
print(list_v1)

list_v2 = [numbers  for numbers in range(1,11)]
print(list_v2)"""

# Ejercicios con list compresion

#escribre un sistema para calcualr numeros pares de forma calsica 

numpar = []

for i in range(1, 21):
    
    if i%2 ==0:
        numpar.append(i)

print(numpar)


# Escribe un sistema para calular numeros pares con listCompresion
numpar= [i for i in range(1,21) if i %2  == 0]
print(numpar)