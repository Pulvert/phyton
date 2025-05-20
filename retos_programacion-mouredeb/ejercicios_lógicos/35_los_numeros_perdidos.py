"""
 * Dado un array de enteros ordenado y sin repetidos,
 * crea una función que calcule y retorne todos los que faltan entre
 * el mayor y el menor.
 * - Lanza un error si el array de entrada no es correcto.
"""

def order_numbers (numbers_list):

  for i in range(0,len(numbers_list)-1):
    if (numbers_list[i] > numbers_list[i+1]):
        print("error, la lista debe estar ordenada")
        return
    else:
        continue

  com_list = [x for x in range(numbers_list[0],numbers_list[-1])][::-1]

  miss_numbers = []
  for i in com_list:
    if i in numbers_list:
      pass
    else:
      miss_numbers.append(i)

  print(miss_numbers)

order_numbers([-1, 0, 14, 16])