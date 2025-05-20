"""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
"""

def is_anagram (word, word2):
    
    if int(len(word.lower())) != int(len(word2.lower())):
        return False
    
    elif word.lower() == word2.lower():
        return False

    else:
        return sorted(word.lower()) == sorted(word2.lower())
                                         
print(is_anagram ("amor", "RomA"))      