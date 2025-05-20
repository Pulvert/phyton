"""
 * Crea un programa que sea capaz de transformar texto natural a código
 * morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar
 *   la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
 *   o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en
 *   https://es.wikipedia.org/wiki/Código_morse.
"""

def morse (alph):
    # equivalencias código Morse. Espacio más separado para diferenciar mejor
    morse_code = {" ": "   ",
                "a": ".-",
                "b": "-...",
                "c": "-.-.",
                "d": "-.."}
    
    # lista con la conversión
    code_list = []

    # meto equivalencias en lista 
    for letter in alph:
        for key, value in morse_code.items():
            if letter == key:
                code_list.append(value)

    # conversión a string
    code_string = "".join(code_list)

    print (code_string)

morse ("abc d")