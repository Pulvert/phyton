"""
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
"""

# For
for x in range (1, 11):
  print (x)

# While
x = 0
while x != 10:
  x += 1
  print(x)

# Recursividad
def count (a):
  if a == 0:
    return 1
  else:
    count(a-1)
  print(a)

count(10)


# Solución

"""
Ejercicio
"""
# For
for i in range(1, 11):
    print(i)

# While
i = 1
while i <= 10:
    print(i)
    i += 1

# Recursividad
def count_ten(i=1):
    if i <= 10:
        print(i)
        count_ten(i + 1)

count_ten()

"""
Extra
"""

for e in [1, 2, 3, 4]:
    print(e)

for e in {1, 2, 3, 4}:
    print(e)

for e in (1, 2, 3, 4):
    print(e)

for e in {1: "a", 2: "b", 3: "c", 4: "d"}:
    print(e)

for e in {1: "a", 2: "b", 3: "c", 4: "d"}.values():
    print(e)

print(*[i for i in range(1, 11)], sep="\n")

for c in "Python":
    print(c)

for e in reversed([1, 2, 3, 4]):
    print(e)

for e in sorted(["m", "o", "u", "r", "e"]):
    print(e)

for i, e in enumerate(sorted(["m", "o", "u", "r", "e"])):
    print(f"Índice: {i}, valor: {e}")