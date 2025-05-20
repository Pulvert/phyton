"""
 * Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
 * ¿De cuántas maneras eres capaz de hacerlo?
 * Crea el código para cada una de ellas.
"""
for i in range (1,101):
  print (i)

b=0
while b < 100:
  b += 1
  print(b)
"""
"""
def count100 (num):

  if num == 0:
    return 1
  else:
    count100 (num-1)

  print(num)

count100 (100)
"""
"""
string = "ejscmvrpymsdqqwertfmcswyoplrtpoirtv..e921rtfv8574aqwpobfresgtpwcx45zor84.,ò6yqazfghk23dcpirscmt`+rfi"

b=0
for i in string:
  b += 1
  print (b)
"""
"""
# ChatGPT
# Método 4: Usando la función map y range
list(map(lambda x: print(x), range(1, 101)))

# Método 5: Usando la función list comprehension (aunque no es la forma más común)
[print(i) for i in range(1, 101)]

# Método 6: Usando la función reduce de functools
from functools import reduce

def imprimir(x, y):
    print(y)
    return y

reduce(imprimir, range(1, 101))

# Método 7: Usando itertools y un bucle for
import itertools

for i in itertools.count(1):
    if i > 100:
        break
    print(i)

# Método 8: Usando una función generadora
def generador_contar():
    for i in range(1, 101):
        yield i

for i in generador_contar():
    print(i)