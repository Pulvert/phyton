"""
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
"""

def binary (num):

  bin_list = []
  num = int(num)

  while num > 0:

    if num % 2 == 0:
      bin_list.append("0")
    else:
      bin_list.append("1")
    num = int(num/2)

  bin_list.reverse()

  bin_nums = "".join(bin_list)

  print(bin_nums)

binary(458)