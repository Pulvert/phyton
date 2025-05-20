"""
 * Crea un programa que comprueba si los paréntesis, llaves y corchetes
 * de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran
 *   en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios.
 *   No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
"""
def estan_equilibrados(expresion):
    # Crear un diccionario de pares de delimitadores
    pares = {')': '(', ']': '[', '}': '{'}
    # Crear una pila para rastrear los delimitadores abiertos
    pila = []

    # Recorrer cada carácter en la expresión
    for char in expresion:
        # Si el carácter es un delimitador de apertura, agregarlo a la pila
        if char in pares.values():
            pila.append(char)
        # Si el carácter es un delimitador de cierre
        elif char in pares.keys():
            # Comprobar si la pila está vacía o si el delimitador superior de la pila no coincide
            if not pila or pila[-1] != pares[char]:
                return False
            # Si coincide, eliminar el delimitador superior de la pila
            pila.pop()

    # Si la pila está vacía al final, los delimitadores están equilibrados
    return not pila

# Ejemplos de uso
expresion1 = "{ [ a * ( c + d ) ] - 5 }"
expresion2 = "{ a * ( c + d ) ] - 5 }"

print(estan_equilibrados(expresion1))  # Debería devolver True
print(estan_equilibrados(expresion2))  # Debería devolver False