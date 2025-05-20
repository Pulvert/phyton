"""
 * Crea una función que imprima los 30 próximos años bisiestos
 * siguientes a uno dado.
 * - Utiliza el menor número de líneas para resolver el ejercicio.
"""

def leap_year(year:int)->list:

  count = 0
  for i in range (year+1, year + 1000):
    if count == 30:
      break
    elif i % 100 == 0 and i % 400 == 0:
      count += 1
      print(i)
    elif i % 100 == 0:
      pass
    elif i % 4 == 0:
      count += 1
      print(i)

leap_year(2024)

def proximos_bisiestos(año):
    print([a for a in range(año + 1, año + 121) if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0)][:30])

# Ejemplo de uso:
proximos_bisiestos(2024)

