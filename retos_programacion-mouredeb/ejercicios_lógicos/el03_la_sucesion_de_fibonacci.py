"""
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci(numbers):

    # inicio los dos primeros números
    fib_list = [0,1]
    # establezco cantidad de veces para ejecutar (numbers fija cantidad)
    for x in range (numbers - 2):
        # calculo la suma de los dos últimos números de la lista
        new_fib = fib_list[-1] + fib_list[-2]
        # los añado a la lista existente
        fib_list.append(new_fib)

    print(fib_list)

fibonacci(50)