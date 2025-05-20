"""
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def invert (string):
    invert_stream = []
    # [:: -1] para empezar desde el final hacia el principio
    for x in string[:: -1]:
        invert_stream.append(x)
    
    print(invert_stream)

    # Para convertir la lista en un string
    invert_stream = "".join(invert_stream)
    print(invert_stream)
    

invert("Hola mundo")