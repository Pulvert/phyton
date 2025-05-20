"""
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
"""
phrase = "La gente de la playa, estaba con otra gente"
# Convertir a minúsculas y eliminar la coma
phrase_lower = phrase.lower().replace(",", "")
# Dividir la frase en palabras
words = phrase_lower.split(" ")

# Crear un diccionario para contar las palabras
word_count = {}

# Iterar sobre las palabras y contar las frecuencias
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


# Imprimir las palabras repetidas y sus frecuencias
repeated_words = {word: count for word, count in word_count.items() if count > 1}

print("Palabras repetidas y sus frecuencias:")
for word, count in repeated_words.items():
    print(f"{word}: {count}")