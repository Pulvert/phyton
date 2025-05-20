"""
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la
 *   sucesión de Fibonacci (la función recibe la posición).
"""
# Recursividad cuenta atrás
def rec(n):
  if n < 0:
    return
  print(n)
  rec (n - 1)
  print(n)

rec(10)

# Recursividad factorial
def fact (n):
  if n == 1:
    return 1
  return n * fact(n-1)

print(fact(5))


# Fibonacci sin recursividad
f = [0, 1]
def fibonacci (n):
  for x in range(n-1):
    c = f[-2] + f[-1]
    f.append(c)
    print(f)
  print(f[-1])

fibonacci (5)

# Recursividad Fibonacci
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Ejemplo de llamada a la función para la posición 10
posicion = 5
resultado = fibonacci(posicion)
print(f"El valor en la posición {posicion} de la sucesión de Fibonacci es {resultado}")

# Solución
"""
Ejercicio
"""


def countdown(number: int):
    if number >= 0:
        print(number)
        countdown(number - 1)


countdown(100)

"""
Extra
"""


def factorial(number: int) -> int:
    if number < 0:
        print("Los números negativos no son válidos")
        return 0
    elif number == 0:
        return 1
    else:
        return number * factorial(number - 1)


print(factorial(5))


def fibonacci(number: int) -> int:
    if number <= 0:
        print("La posición tiene que ser mayor que cero")
        return 0
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(5))

