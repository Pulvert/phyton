"""
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
"""
def fibonacci(num_fib):
    list = [0,1]

    

    for i in range (1, num_fib):
        last_num = list[-1] + list[-2]
        list.append(last_num)

    print(list)

fibonacci(50)