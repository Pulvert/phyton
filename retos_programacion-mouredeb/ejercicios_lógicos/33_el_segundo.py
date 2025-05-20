"""
 * Dado un listado de números, encuentra el SEGUNDO más grande
"""

def second (num:list)->list:
  num.sort() # Método 1 de ordenar: modifica la lista original
  print(num)
  print(sorted(num)) # Método 2 de ordenar: crea una nueva lista ordenada y deja la lista original sin cambios

  num_set = set(num) # Eliminamos repetidos convirtiendo en set
  num2 = list(num_set) # Volvemos a convertir en lista para pdoer acceder a índice
  print(num2[::-1][1]) # Le damos la vuelta e imprimimos el segundo más grande


# Chat GPT

def segundo_mas_grande(nums):
    # Eliminar duplicados
    nums_unicos = list(set(nums))
    # Ordenar en orden descendente
    nums_unicos.sort(reverse=True)
    # Verificar si hay al menos dos números
    if len(nums_unicos) < 2:
        return None  # O algún valor que indique que no hay suficiente números
    return nums_unicos[1]

# Ejemplo de uso
nums = [4, 9, 1, 3, 7, 9]
segundo = segundo_mas_grande(nums)
print(segundo)  # Output: 7





second([4,9,1,3,1,7])