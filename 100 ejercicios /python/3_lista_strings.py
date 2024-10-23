"""Ejercicio 3:
Descripción: Crea un programa que ingrese una lista de nombres y los muestre.
Pista: Utiliza variables, ciclos o condicionales según corresponda."""

#agregare unas cosas mas


list_name = []

while True:
    name = str(input("Ingresa un nombre: "))
    list_name.append(name)
    a = int(input("1 para seguir y 0 pra parar: "))
    if a != 1:
        break

print("Los nombres son", list_name)