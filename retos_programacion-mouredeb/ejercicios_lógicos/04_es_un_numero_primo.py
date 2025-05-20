"""
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
"""
#a
def primos():

    for n in range (2, 102):
        es_primo = True
        for h in range (n-1,1,-1):
            if n % h == 0: # Si no hay resto es divisible, con lo cual no es primo
                es_primo = False
                print (f"{n} no es primo")
                break
                

        if es_primo:
            print (f"{n} es primo") # Primero se comprueba todas las itinerancias del for, si
                     # no se cumplen, ya tiene que ser primo


primos()

#b

def is_prime():

    for number in range(1,101):
        if number >= 2:

            is_divisible = False

            for i in range (2, number):
                if number % i == 0:
                    is_divisible = True
                    break
            
            if not is_divisible:
                print(number)


print(is_prime())
