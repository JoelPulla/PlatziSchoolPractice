"""MOURDEV"""

#Crea ejemplos utilizando todo los tipos de opreadores

#Operadores aritmetricos 
print(F"Suma 10 + 3 = {10 + 3}")
print(f"Resta 10 - 5 = {10 - 5}")
print(f"Multiplicacion 2 * 2 = {2*2}")
print(f"Divicion 8//4 =  {8//4}")
print(f"divicion con decimal 8 / 4 = {8/4}")
print(f"Reciduo de la divicion 8 % 4 = {8 %4 }")
print(f"Potenciacion 4**2 = {4**2}")

# Comparacion 
print(f"Igualdad 3==3 = {3==3}")
print(f"Diferencia 3!=2 = {3!=2}")
print(f"Mayor que 10>3 =  {10>3}")
print(f"Memor que 10<20 = {10<23}")
print(f"Mayor que 10>=3 =  {10>=3}")
print(f"Memor que 10<=10 = {10<=10}")

# Operadores logicos
print(f"1==1 and && 2==3 => {1==1 and 2==3}")
print(f"1==1 or ||  2==3 => {1==1 or 2==3}")
print(f"NOT !: not 10 == 14 => {not 10 ==14 }")

# Operadores de asignacion 
a = 12 
print(f"A la variable a le asigne el valor de = {a}") 

a +=1 #asignacion mas suma 
print(a)

#operadores de bit 

# Transformas a bti 

"""Estructuras de control """

#conficionales 
name = "Joel pulla"

if name == "Joel pulla":
    print(f" name si es igual a {name}")
elif name == "Pulla":
    print ("Es igual a Pulla ")
else:
    print("No es igual")
    
# Bucles

# for i in range(80):
#     print(i)
   
a = 0 
while True:
    a+=1
    print(a)
    if a == 50:
        break
    
#Manjeo de execpciones 

try:
    print(10/0) 
except:
    print("no puedes divir entre 0")
finally:
    print("Fin del codigo ")
    
""" Crea un programa que imprima por consola todos los numeros
    entre 10 y 55 (includo), pares, y que no son ni el 16b ni mjultiplos del 3
     
"""


for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i %3 == 0:
        print(i)
    