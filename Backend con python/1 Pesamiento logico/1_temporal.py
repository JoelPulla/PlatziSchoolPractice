import sys

sys.setrecursionlimit(50000)



"""Complejidad Temporar"""

# Para saber el tiempo depende de muchos factores 
#por que mi computadoira ademas de usar para programar se 
# para hacer varias cosas mas es decir
# que tengo los recuersos compartidos por ello 
# se demorar mas o menos dependiendo de los recurso de la Compuitadora 


"""Nota: Medir el tiempo no spermite saber como se comportara nuestro 
   algoritmo con el tiempo cuando creceran los datos

"""

import time


#dscubre el factorial
def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta

#descubre fatorial con funciones recursivas
def factorial_r(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)


if __name__ == '__main__':
    n = 200000

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final - comienzo)