# /*
#  * Escribe un programa que se encargue de comprobar si un número es o no primo.
#  * Hecho esto, imprime los números primos entre 1 y 100.
#  */

for i in range(1,100):
    if i % 2 != 0 and i % 3 != 0 and i%4 != 0 :
        print(i)