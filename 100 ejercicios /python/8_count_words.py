# *
#  * Crea un programa que cuente cuantas veces se repite cada palabra
#  * y que muestre el recuento final de todas ellas.
#  * - Los signos de puntuación no forman parte de la palabra.
#  * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
#  * - No se pueden utilizar funciones propias del lenguaje que
#  *   lo resuelvan automáticamente.
#  */


def counter_word(message):
    
    
    dict_word = {}
    
    #format word
    message = message.lower().split()
    
    for i in message:
        if i in dict_word:
            dict_word[i] += 1
        else:
            dict_word[i] = 1
    print(dict_word)
    
counter_word("Hola Mundo mundo mundo ")