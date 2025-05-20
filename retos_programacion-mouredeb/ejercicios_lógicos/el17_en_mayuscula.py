"""
 * Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
"""

def capitalize(string):

    # creo lista con palabras del string    
    list_string = [x for x in string]
    new_list_string = []
    len_list_string = len(list_string)

    # creo diccionario con abecedario y su correspondiente mayúscula
    abcd = {"a": "A",
            "b": "B",
            "c": "C",
            "d": "D",
            "e": "E"}

    
    # comparo la primera letra con las keys del diccionario
    for key, value in abcd.items():
        # si la primera letra coincide con alguna en keys (minúsculas) o en values (mayúscula), 
        # añade a nueva lista el value (su correspondiente mayúscula) 
        if key == list_string[0] or value == list_string[0]:
            new_list_string.append(value)
            break
    
    # otra forma de revisar si es la primera maýuscula
    """ 
    # si no (la primera letra es mayúscula), la mete
    else:
        new_list_string.append(list_string[0])
    """                
            
    # añado resto de letras (de la posición 1: a la última)
    for x in list_string[1:len_list_string]:
            new_list_string.append(x)

    # convierto en string la nueva lista con la primera letra en mayúscula
    new_string = "".join(new_list_string)
    print(new_string)


capitalize ("Diego")