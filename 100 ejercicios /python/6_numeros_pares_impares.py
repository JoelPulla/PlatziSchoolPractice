"""Ejercicio 6:
Descripción: Crea un programa que muestre los numeros impares y los numeros pares.
Pista: Utiliza variables, ciclos o condicionales según corresponda ."""


for i in range(50):
    if i % 2 == 0:
        print (i," es numero par")
    else:
        print(i," es numero impar")
        
#### almacenalos en una lsita


par = [i for i in range(50) if i %2 ==0 ]
impar = [i for i in range(50) if i%2 != 0]

print("Numeros Pares => ",par)
print("Numeros Impares => ",impar)






