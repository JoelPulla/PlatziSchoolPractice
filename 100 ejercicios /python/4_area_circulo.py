"""Ejercicio 4:
Descripción: Crea un programa que calcule el área de un círculo.
Pista: Utiliza variables, ciclos o condicionales según corresponda."""

radio = int(input("Ingresa el valor del radio => "))

VARIABLE_PI = 3.1415

radio_v1 = VARIABLE_PI * (radio **2)
print("el area del circulo es => ",radio_v1)


########## Mejorada #####

import math

radi_v2 = math.pi * (radio**2)
print("el area del circulo es => ",radi_v2)