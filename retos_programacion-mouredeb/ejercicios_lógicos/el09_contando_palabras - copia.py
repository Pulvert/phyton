"""
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
"""

def binary (number):
    list = []

    # bucle hasta que el número sea mayor de 0
    while number > 0:
        # si es par 0, si no 1 (concepto de binario)
        if number % 2 == 0:
            list.append(0)
        else:
            list.append(1)

        # dividimos (mecánica para calcular binarios)
        number = number / 2

        # quitamos restos (mecánica)
        if number % 2 != 0:
            number = int(number)

    # damos la vuelta (mecánica)
    print(list[::-1])
        

binary (46)
