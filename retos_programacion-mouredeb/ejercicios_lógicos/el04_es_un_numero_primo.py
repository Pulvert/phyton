"""
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 (primos es un número mayor de 1 solo divisible entre 1 y él mismo)
"""

def is_prime(amount):

    # primo tiene que ser mayor de 1. El 2 es primo.
    print("1 is not prime")
    print("2 is prime")
    # establecemos rango del 3 a la cantidad solicitada
    for x in range (2, amount + 1):
        # establecemos los números que están entre él mismo y el 2
        for y in range (2, x):
            # si es divisiible entre algún número que esté entre él mismo y el 2 no es primo, cortamos.
            if x % y == 0:
                print(f"{x} is not prime")
        
                break
# el bloque else de un for se ejecuta solo si el bucle se completa sin que se haya usado un break
# es decir, si el número no enccuentra ningún divisible, es primo (solo divisible entre 1 y él mismo)
        else:
            print(f"{x} is prime")
        
is_prime (10)