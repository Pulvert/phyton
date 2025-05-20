"""
 * Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra
 * que calcule el mínimo común múltiplo (mcm) de dos números enteros.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
"""
#a
def mcm (num1, num2):

  dic = {}
  dic2 = {}
  desc2 = 2
  desc3 = 3
  desc5= 5
  count1= 0
  count2= 0
  count3= 0
  count4= 0
  count5= 0

  while num1 > 1:

    if num1 % desc2 == 0:
      count1 += 1
      dic[desc2] = count1
      num1 /= desc2

    elif num1 % desc3 == 0:
      count2 += 1
      dic[desc3] = count2
      num1 /= desc3

  while num2 > 1:

    if num2 % desc2 == 0:
      count3 += 1
      dic2[desc2] = count3
      num2 /= desc2

    elif num2 % desc3 == 0:
      count4 += 1
      dic2[desc3] = count4
      num2 /= desc3

    elif num2 % desc5 == 0:
      count5 += 1
      dic2[desc5] = count5
      num2 /= desc5

# Identificar las claves coincidentes
  common_keys = set(dic.keys()) & set(dic2.keys())

# Comparar y eliminar la clave con el menor valor
  for key in common_keys:
    if dic[key] <= dic[key]:
        del dic2[key]
    else:
        del dic[key]

  t=1
  for key, value in dic.items():
    t *= (key**value)
  for key, value in dic2.items():
    t *= (key**value)

  return(t)


def mcd(num1, num2):

  return num1*num2/ mcm(num1, num2)

print(mcm (72, 50))
print(mcd (72, 50))

#b ChatGPT
def calcular_MCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def calcular_mcm(a, b):
    mcd = calcular_MCD(a, b)
    # La relación entre MCD y mcm: mcm(a, b) = (a * b) / MCD(a, b)
    return (a * b) // mcd

# Ejemplo de uso:
num1 = int(input("Introduce el primer número entero: "))
num2 = int(input("Introduce el segundo número entero: "))

# Calcula y muestra el máximo común divisor (MCD)
print("El máximo común divisor (MCD) de", num1, "y", num2, "es:", calcular_MCD(num1, num2))

# Calcula y muestra el mínimo común múltiplo (mcm)
print("El mínimo común múltiplo (mcm) de", num1, "y", num2, "es:", calcular_mcm(num1, num2))