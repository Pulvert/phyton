"""
 * Crea una función que reciba un texto y muestre cada palabra en una línea,
 * formando un marco rectangular de asteriscos.
 * - ¿Qué te parece el reto? Se vería así:
 *   **********
 *   * ¿Qué   *
 *   * te     *
 *   * parece *
 *   * el     *
 *   * reto?  *
 *   **********
"""

def frame (text):

  max_len_word = 0
  for x in text.split():
    len_word = (len(x))
    if len_word > max_len_word:
      max_len_word = len_word

  print("*" * max_len_word + "****")

  for x in text.split():
    len_word = (len(x))
    print("* "+ x + " " * (max_len_word-len_word) + " *")

  print("*" * max_len_word + "****")


frame("¿Qué te parece el retoooooooooo?")