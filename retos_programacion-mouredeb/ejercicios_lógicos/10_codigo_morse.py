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

import string

def morse ():

  morse = ".- -... -.-. -.. .-.-."
  palabras = morse.split()
  list_morse = []
  abecedario = string.ascii_lowercase

  dic_morse = {" ":" ","a":".-","b":"-...","c":"-.-.","d":"-.."}

  if morse[0] in abecedario:

    for i in morse:
      if i in dic_morse:
        for key, value in dic_morse.items():
          if i == key:
            print (value)
  else:

    for i in palabras:
        for key, value in dic_morse.items():
          if i == value:
            list_morse.append(key)
    string_morse = "".join(list_morse)
    print (string_morse)

morse ()