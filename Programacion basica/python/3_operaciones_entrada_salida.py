"""Operaciones de entrada y salida IMPUT"""

name = input("Hola, ingresa tu nombre: ") #un imput siempre lo interpretara como un string 
age = int(input("tu edad: ")) #podemos cambiar a un imput a que solo acepte un entero o cualquier tipo de dato 

print(f"un gusto conocerte {name}, wow ya tinees {age}")

print(type(name))
print(type(age))