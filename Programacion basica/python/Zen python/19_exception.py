"""Execption"""

# un Exception corta el sistema y te devuelve el error que tu podias aver identificado 



print('Hola')

suma = lambda x,y: x + y
assert suma(2,2) == 4

print('Hola 2')

age = 10
if age < 18:
  raise Exception('No se permiten menores de edad')

print('Hola 2')

# ==========> Manera Eficientoe <=============
# No rompe el sistena