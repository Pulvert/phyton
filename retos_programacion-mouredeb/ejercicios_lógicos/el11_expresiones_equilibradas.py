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

def expression(string):

    # convierto string en lista para poder iterar
    list_string = [x for x in string]
    dic_caracters = {"{":"}",
                     "[":"]",
                     "(":")"}

    # fijo el primer elemento de la lista (0)
    order_value = 0
    order_key = 0
    order_list = 0
    # fijo el último elemento de la lista:
    size = int(len(list_string))-1

    # comprobación de que los que abren, cierran.
    # keys = delimitadores que abren
    """while first != last:"""
    
    for key, value in dic_caracters.items():
        for caract in list_string:
            if key[order_key] == caract[order_list]:
                while order_list != size:
                    order_list += 1
                    if value[order_value] == list_string[order_list]:
                        print(f"{key[order_key]} tiene su {value[order_value]} después")
                        break
                

    """
    print(dic_caracters.keys())
    for x in string:        
        if x in dic_caracters.keys():
            if
            
            print(f"{x} coincide")
"""
"""
    for caracter in string:
        if caracter == dic_caracters.keys():
            for caract in string:
                for y in string:
                    if y == dic_caracters.values():
                        print("balanced expression")
                    else:
                        print("not balanced expression")
"""

expression("{ [ a * ( c + d ) ] - 5 }")
"""
expression("{ a * ( c + d ) ] - 5 }")
"""