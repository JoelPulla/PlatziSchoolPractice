# /*
#  * Escribe una función que reciba dos palabras (String) y retorne
#  * verdadero o falso (Bool) según sean o no anagramas.
#  * - Un Anagrama consiste en formar una palabra reordenando TODAS
#  *   las letras de otra palabra inicial.
#  * - NO hace falta comprobar que ambas palabras existan.
#  * - Dos palabras exactamente iguales no son anagrama.
#  */
 
def anagrama(word_1, word_2):
    if word_1.lower() == word_2.lower():
        return False 
    
    if sorted(word_1.lower()) == sorted(word_2.lower()):
        return True


print(f"Es un anagrama = {anagrama("Amor", "Roma")}")