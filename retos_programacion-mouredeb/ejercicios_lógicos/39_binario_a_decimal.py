"""
 * Crea un programa se encargue de transformar un número binario
 * a decimal sin utilizar funciones propias del lenguaje que
 * lo hagan directamente.
"""

def binary (num_bin):
  str_bin = str(num_bin) # Se convierte a str para dar la vuelta y poder iterar
  str_bin_reversed = str_bin[::-1] # Le damos la vuelta
  tot=0
  pot=0
  for x in str_bin_reversed:
    y = int(x)*2**pot
    pot += 1 # Potencias del 0 al 7
    tot += y # Vamos sumando los totales
  print(tot)


binary(10101100)