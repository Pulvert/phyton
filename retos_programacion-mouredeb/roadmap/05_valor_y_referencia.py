"""
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 """
# Asignación por valor con int
a = 10
b = a  # a se asigna por valor a b
b = 20  # Modificamos b
print(a)  # Imprime 10 (a no ha cambiado)

# Asignación por valor con str
s1 = "Hola"
s2 = s1  # s1 se asigna por valor a s2
s2 = "Hola Mundo"  # Modificamos s2
print(s1)  # Imprime "Hola" (s1 no ha cambiado)

 # Asignación por referencia con listas
lista1 = [1, 2, 3]
lista2 = lista1  # lista1 se asigna por referencia a lista2
lista2.append(4)  # Modificamos lista2
print(lista1)  # Imprime [1, 2, 3, 4] (lista1 también ha cambiado)

# Asignación por referencia con diccionarios
dict1 = {'a': 1, 'b': 2}
dict2 = dict1  # dict1 se asigna por referencia a dict2
dict2['c'] = 3  # Modificamos dict2
print(dict1)  # Imprime {'a': 1, 'b': 2, 'c': 3} (dict1 también ha cambiado)

def value (int1):
  int2 = int1
  int2 = 20
  return int2

print(value(10))

def reference (my_list):
  my_list2 = my_list
  my_list.append(5)
  return my_list2

reference ([1,2,3,4])


def pro1 (x, y):
  x = y
  y = x
  x1 = x
  y1 = y
  return x1

def pro2 (z, p):
  print(z)

v1 = "Hola"
v2 = "Phyton"

r1 = ["Phyton", "Java", "C"]
r2 = {"Name": "Diego", "Surname": "García"}

v3 = 10
v4 = 20
r3 = [1, 2, 3, 4]
r4 = {'a': 1, 'b': 2}

print (pro1 (v1,v2))
print (pro1 (r1,r2))

"""
pro2 (v3, v4)
pro2 (r3,r4)
"""

# Solución
"""
Valor y referencia
"""

# Tipos de dato por valor

my_int_a = 10
my_int_b = my_int_a
my_int_b = 20
# my_int_a = 30
print(my_int_a)
print(my_int_b)

# Tipos de dato por referencia

my_list_a = [10, 20]
my_list_b = my_list_a
my_list_b.append(30)
print(my_list_a)
print(my_list_b)

# Funciones con datos por valor


def my_int_func(my_int: int):
    my_int = 20
    print(my_int)


my_int_c = 10
my_int_func(my_int_c)
print(my_int_c)

# Funciones con datos por referencia


def my_list_func(my_list: list):
    my_list.append(30)

    my_list_d = my_list
    my_list_d.append(40)

    print(my_list)
    print(my_list_d)


my_list_c = [10, 20]
my_list_func(my_list_c)
print(my_list_c)

"""
Extra
"""

# Por valor


def value(value_a: int, value_b: int) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b


my_int_d = 10
my_int_e = 20
my_int_f, my_int_g = value(my_int_d, my_int_e)

print(f"{my_int_d}, {my_int_e}")
print(f"{my_int_f}, {my_int_g}")

# Por referencia


def ref(value_a: list, value_b: list) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b


my_list_e = [10, 20]
my_list_f = [30, 40]
my_list_g, my_list_h = ref(my_list_e, my_list_f)
print(f"{my_list_e}, {my_list_f}")
print(f"{my_list_g}, {my_list_h}")