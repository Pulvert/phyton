"""
 * Crea una función que reciba dos array, un booleano y retorne un array.
 * - Si el booleano es verdadero buscará y retornará los elementos comunes
 *   de los dos array.
 * - Si el booleano es falso buscará y retornará los elementos no comunes
 *   de los dos array.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
"""
def array (arr1, arr2, bool):

  dic = {}
  list_ = []

  if len(arr1) >= len(arr2):

    for i in arr1:
      for b in arr2:
          if i == b:
            dic[i] = 1
            break
          else:
            dic[i] = 0

  elif len(arr2) > len(arr1):

    for i in arr2:
      for b in arr1:
          if i == b:
            dic[i] = 1
            break
          else:
            dic[i] = 0

  if bool == True:
    for key, value in dic.items():
      if value == 1: list_.append(key)

  elif bool == False:
    for key, value in dic.items():
      if value == 0: list_.append(key)

  return list_

print(array([1, "Diego", "Phyton"], [5, "Diego", "Javascript", 1], True))

#Resultado Chatgpt


def filtrar_elementos(array1, array2, comunes):
    resultado = []

    if comunes:
        # Buscar elementos comunes
        for elemento in array1:
            if elemento in array2 and elemento not in resultado:
                resultado.append(elemento)
        # También buscar en array2 para los elementos no duplicados de array1
        for elemento in array2:
            if elemento in array1 and elemento not in resultado:
                resultado.append(elemento)
    else:
        # Buscar elementos no comunes
        for elemento in array1:
            if elemento not in array2 and elemento not in resultado:
                resultado.append(elemento)
        for elemento in array2:
            if elemento not in array1 and elemento not in resultado:
                resultado.append(elemento)

    return resultado

# Ejemplo de uso:
array1 = [1, 2, 3, 4]
array2 = [3, 4, 5, 6, 8]
comunes = True

print(filtrar_elementos(array1, array2, comunes))  # Salida: [3, 4]

comunes = False
print(filtrar_elementos(array1, array2, comunes))  # Salida: [1, 2, 5, 6]