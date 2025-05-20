"""
 * Crea una función que ordene y retorne una matriz de números.
 * - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
 *   adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
 *   o de mayor a menor.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan
 *   automáticamente.
"""

def numbers (numbers_list: list, metod: str)->list:

  n = len(numbers_list)

  if metod == "desc":

    for i in range(n):
        for j in range(0, n-i-1):
            if numbers_list[j] < numbers_list[j+1]: # Si es menor..
                # ...intercambia los elementos
                numbers_list[j], numbers_list[j+1] = numbers_list[j+1], numbers_list[j]
    print(numbers_list)


  elif metod == "asc":

      for i in range(n):
        for j in range(0, n-i-1):
            if numbers_list[j] > numbers_list[j+1]: # Si es mayor..
                # ...intercambia los elementos
                numbers_list[j], numbers_list[j+1] = numbers_list[j+1], numbers_list[j]
  print(numbers_list)



numbers([2, 4, 9, 8, 6], "asc")