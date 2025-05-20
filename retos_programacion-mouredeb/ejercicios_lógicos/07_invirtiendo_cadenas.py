"""
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""
list_string = []
string = "Hola mundo"

for i in string[::-1]:
    list_string.append(i)

new_string = "".join(list_string)
print(new_string)
