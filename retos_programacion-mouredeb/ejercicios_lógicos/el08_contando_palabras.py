"""
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
"""

def count_words (phrase):

    # divide palabras por espacios
    words = phrase.split()
    list = []
    count_dic = {} 

    for word in words:
        # elimino signos de puntuación
        clean_word = word.strip(".,")
        # todo en minúsculas para poder comparar
        clean_word = clean_word.lower()
        # lo meto en una nueva lista
        list.append(clean_word)

    # cuento las repeticiones
    for x in list:
        count = 0
        for y in list:
            if x == y:
                count += 1
        count_dic[x] = count

    # imprimo los resultados
    for z, y in count_dic.items():
        if y == 1:
            print(f"la palabra {z} se repite {y} vez")
        else:
            print(f"la palabra {z} se repite {y} veces")


count_words("un perros. dos PerroS tres ,perros")