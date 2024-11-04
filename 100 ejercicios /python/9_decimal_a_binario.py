# /*
#  * Crea un programa se encargue de transformar un número
#  * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
#  */


# revertir el binario de los datos 


def convert_bin(number):
    
    binario = ""
    while number != 0 :
        
        resiudo = number % 2
        number = number // 2
        
        binario =  str(resiudo) + binario
        
    return binario
print(convert_bin(13))



