"""
 * Crea una función que reciba dos cadenas como parámetro (str1, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO
 *   estén presentes en str1.
"""

def strings (str1, str2):

    # lo convierto todo en minúscula para poder comparar
    str1 = str1.lower()
    str2 = str2.lower()

    out1 = []
    out2 = []

    # si el caracter de str1 no está en str2 se mete en out1
    for char in str1:
        if char not in str2:
            out1.append(char)

    # si el caracter de str2 no está en str1 se mete en out1
    for char in str2:
        if char not in str1:
            out2.append(char)
    
    print(out1)
    print(out2)


strings ("santiago", "Diego")