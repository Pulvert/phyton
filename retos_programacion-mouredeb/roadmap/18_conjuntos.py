"""
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 * operaciones (debes utilizar una estructura que las soporte):
 * - Añade un elemento al final.
 * - Añade un elemento al principio.
 * - Añade varios elementos en bloque al final.
 * - Añade varios elementos en bloque en una posición concreta.
 * - Elimina un elemento en una posición concreta.
 * - Actualiza el valor de un elemento en una posición concreta.
 * - Comprueba si un elemento está en un conjunto.
 * - Elimina todo el contenido del conjunto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
"""

my_list = []

# Añade un elemento al final
my_list.append("Diego")
print(my_list)

# Añade un elemento al principio
my_list.insert(0,"Jose")
print(my_list)

# Añade varios elementos en bloque al final
elements = "Juan","Mario"
my_list.extend(elements)
print(my_list)

# Añade varios elementos en bloque en una posición concreta
elements2 = "Sandra" , "María"
my_list[1:1] = elements2
print(my_list)

# Elimina un elemento en una posición concreta.
my_list.pop(0)
print(my_list)

# Actualiza el valor de un elemento en una posición concreta
my_list[1] = "Eva"
print(my_list)

# Comprueba si un elemento está en un conjunto
"Eva" in my_list

# Elimina todo el contenido del conjunto
"""
del my_list
"""

# Extra
# Unión
my_list2 = ["John", "Mark"]
my_list3 = my_list + my_list2
print(my_list3)

# Intersección
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.intersection(b))

# Diferencia
print(a.difference(b))
print(b.difference(a))

# Diferencia simétrica
print(a.symmetric_difference(b))


# Solución
"""
Ejercicio
"""

data = [1, 2, 3, 4, 5]
print(f"Estructura inicial: {data}")

data.append(6)
print(f"Añadiendo elemento al final: {data}")

data.insert(0, 0)
print(f"Añadiendo elemento al principio: {data}")

data.extend([7, 8, 9])
print(f"Añadiendo elementos al final: {data}")

data[3:3] = [-1, -2, -3]
print(f"Añadiendo elementos en una posición: {data}")

del data[3]
print(f"Eliminando un elemento concreto: {data}")

data[4] = -1
print(f"Actualizando un elemento concreto: {data}")

print(f"Comprobar si un elemento existe: {-1 in data}")

print(f"Eliminar el contenido: {data.clear()}")

"""
Extra
"""

set_1 = {1, 2, 3, 4, 5}
set_2 = {1, 2, 3, 4, 6, 7}

print(f"Unión: {set_1.union(set_2)}")

print(f"Intersección: {set_1.intersection(set_2)}")

print(f"Diferencia: {set_1.difference(set_2)}")
print(f"Diferencia: {set_2.difference(set_1)}")

print(f"Diferencia simétrica: {set_1.symmetric_difference(set_2)}")