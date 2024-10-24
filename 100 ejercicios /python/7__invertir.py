# /*
#  * Crea un programa que invierta el orden de una cadena de texto
#  * sin usar funciones propias del lenguaje que lo hagan de forma automática.
#  * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
#  */

def invertir(mesage):
    mesage = mesage[::-1]
    return mesage

print(invertir("Hola Mundo"))


### Con for ##

def invertir_v2(mesage):
    
    other = ''
    for i in mesage[::-1]:
       other = other + i
    return str(other)

print(invertir_v2("Hola mundo"))