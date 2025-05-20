"""
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
"""

my_string = "El perro de San Roque no tiene rabo"

# Acceso a letra
for x in my_string:
  if x == "R":
    print(x)

# Acceso según posición
print(my_string[1])

# Devuelve boolean
print("perro" in my_string)

# Longitud de caracteres
print(len(my_string))

# Condicional
if "perro" in my_string:
  print("perro is in my_string")

# Rango de caracteres
print(my_string[0:8])

# Convertir en mayúsculas
print(my_string.upper())

# Convertir en minúsculas
print(my_string.lower())

# Reemplazar
print(my_string.replace("rabo", "pies"))

# Crea en lista substrings separados por algún caracter
print(my_string.split (" "))

# Concatenación
my_other_string = "porque Ramón Ramírez se lo ha cortado"
string_complete = my_string + " " + my_other_string
print(string_complete)

# Palíndromos
palindrome = "dábale arroz a la zorra el abad"

pal2 = palindrome.replace(" ", "") # Quitamos espacios
pal3 = pal2.replace('á' , 'a') # Quitamos acentos
pal4 = pal3.lower() # Pasamos a minúsculas
pal5 = pal4[::-1] # Invertimos cadena

if pal5 == pal5: # Comparamos
  print("Es palíndromo")
else:
    print("No es palíndromo")

# Anagramas

def anagram (str1, str2):
  s1 = str1.lower() # Pasamos a minúsculas
  s2 = s1.replace(" ", "") # Quitamos espacios
  s3 = sorted(s2) # Ordenamos alfabéticamente

  st1 = str2.lower() # Pasamos a minúsculas
  st2 = st1.replace(" ", "") # Quitamos espacios
  st3 = sorted(st2) # Ordenamos alfabéticamente

  if s3 == st3: # Comparamos
    print("Anagrama")
  else:
    print("No anagrama")

anagram("Toledo","el todo")

# Isograma

def isogram (str1):
  dic = {}
  s = str1.lower() # Pasamos a minúsculas
  for x in s: # Contamos repeticiones en un diccionario
    if x in dic:
      dic[x] += 1
    else:
      dic[x] = 1

  for x in dic: # En el caso de que se repita una palabra, no es iso
    if dic[x] > 1:
      print("No es un isograma")
      return
  print("Es un isograma")

isogram ("Toledo")

# Solución

"""
Operaciones
"""

s1 = "Hola"
s2 = "Python"

# Concatenación
print(s1 + ", " + s2 + "!")

# Repetición
print(s1 * 3)

# Indexación
print(s1[0] + s1[1] + s1[2] + s1[3])

# Longitud
print(len(s2))

# Slicing (porción)
print(s2[2:6])
print(s2[2:])
print(s2[0:2])
print(s2[:2])

# Busqueda
print("a" in s1)
print("i" in s1)

# Reemplazo
print(s1.replace("o", "a"))

# División
print(s2.split("t"))

# Mayúsculas, minúsculas y letras en mayúsculas
print(s1.upper())
print(s1.lower())
print("brais moure".title())
print("brais moure".capitalize())

# Eliminación de espacios al principio y al final
print(" brais moure ".strip())

# Búsqueda al principio y al final
print(s1.startswith("Ho"))
print(s1.startswith("Py"))
print(s1.endswith("la"))
print(s1.endswith("thon"))

s3 = "Brais Moure @mouredev"

# Búsqueda de posición
print(s3.find("moure"))
print(s3.find("Moure"))
print(s3.find("M"))
print(s3.lower().find("m"))

# Búsqueda de ocurrencias
print(s3.lower().count("m"))

# Formateo
print("Saludo: {}, lenguje: {}!".format(s1, s2))

# Interpolación
print(f"Saludo: {s1}, lenguje: {s2}!")

# Tranformación en lista de caracteres
print(list(s3))

# Transformación de lista en cadena
l1 = [s1, ", ", s2, "!"]
print("".join(l1))

# Transformaciones numéricas
s4 = "123456"
s4 = int(s4)
print(s4)

s5 = "123456.123"
s5 = float(s5)
print(s5)

# Comprobaciones varias
s4 = "123456"
print(s1.isalnum())
print(s1.isalpha())
print(s4.isalpha())
print(s4.isnumeric())

"""
Extra
"""


def check(word1: str, word2: str):

    # Palíndromos
    print(f"¿{word1} es un palíndromo?: {word1 == word1[::-1]}")
    print(f"¿{word2} es un palíndromo?: {word2 == word2[::-1]}")

    # Anagramas
    print(f"¿{word1} es anagrama de {word2}?: {sorted(word1) == sorted(word2)}")

    # Isogramas

    def isogram(word: str) -> bool:

        word_dict = dict()
        for character in word:
            word_dict[character] = word_dict.get(character, 0) + 1

        isogram = True
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isogram = False
                break

        return isogram

    print(f"¿{word1} es un isograma?: {isogram(word1)}")
    print(f"¿{word2} es un isograma?: {isogram(word2)}")


check("radar", "pythonpythonpythonpython")
# check("amor", "roma")