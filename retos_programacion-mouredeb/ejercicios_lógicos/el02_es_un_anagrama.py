"""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
"""

def is_anagram (word1, word2):
    # minúsculas para comparar
    word1 = word1.lower()
    word2 = word2.lower()
    # dos palabras iguales no son anagrama
    if word1 == word2:
        return False
    
    # ordenamos por orden alfabético y si son iguales True
    elif sorted(word1) == sorted(word2): 
        return True
    
    # si no False
    else:
        return False
    

print(is_anagram ("Roma", "amOr"))
