"""
 * Explora el concepto de funciones de orden superior en tu lenguaje
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
 *
 * DIFICULTAD EXTRA (opcional):
 * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y
 * lista de calificaciones), utiliza funciones de orden superior para
 * realizar las siguientes operaciones de procesamiento y análisis:
 * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
 *   y promedio de sus calificaciones.
 * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
 *   que tienen calificaciones con un 9 o más de promedio.
 * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
 * - Mayor calificación: Obtiene la calificación más alta de entre todas las
 *   de los alumnos.
 * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
"""

# Aplica una función a todos los elementos de una lista (u otro iterable) y devuelve un nuevo iterable con los resultados

def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]

# Filtra los elementos de una lista (u otro iterable) aplicando una función que devuelve True o False.

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5]
even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # Output: [2, 4]


# Aplica una función de manera acumulativa a los elementos de una lista (u otro iterable), reduciéndolos a un único valor
from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
total = reduce(add, numbers)
print(total)  # Output: 15

# Función que devuelve otra función

def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier(3)
times5 = make_multiplier(5)

print(times3(10))  # Output: 30
print(times5(10))  # Output: 50

# Extra

students_list = [["Pedro", "25-02-91", [9.2, 9.8, 8.8]],
["Juan", "01-08-87", [7.1, 5.8, 3.2]],
["Mario", "28-05-96", [2.2, 4.5, 6.5]],
["Isabel", "14-09-76", [5.8, 7.3, 4.7]],
["Marta", "21-01-88", [4.5, 8, 9.2]]]


# Promedio calificaciones

# Se calcula la media (suma de total / nº de notas)
calculate_average = lambda student: sum(student[2]) / len(student[2])

# Utiliza map para aplicar calculate_average a cada elemento de students_list, generando una lista de medias de notas
average_scores = list(map(calculate_average, students_list))

# zip toma dos o más iterables (como listas, tuplas, etc.) y las agrupa en tuplas.
# Cada tupla contiene elementos que están en las mismas posiciones en los iterables originales
for student, average in zip(students_list, average_scores):
    print(f"{student[0]}: {average:.2f}")

# Mejores estudiantes

def is_best(x):
    return x > 9

# Devuelve el filtro (mayor de 9)
the_best = list(filter(is_best, average_scores))

for student, average in zip(students_list, the_best):
    print(f"{student[0]}: {average:.2f}")


# Nacimiento

from datetime import datetime

# Función auxiliar para convertir la fecha a un objeto datetime
def convertir_fecha(fecha_str):
    return datetime.strptime(fecha_str, "%d-%m-%y")

# Ordenar la lista de estudiantes por fecha de nacimiento
students_list_ordenada = sorted(students_list, key=lambda x: convertir_fecha(x[1]))

# Imprimir la lista ordenada
for student, date in zip(students_list_ordenada, students_list_ordenada):
    print(f"{student[0]}: {date[1]}")


# Mayor calificación


# Solución

from functools import reduce
from datetime import datetime

"""
Ejercicio
"""

# Función como argumento


def apply_func(func, x):
    return func(x)


print(apply_func(len, "MoureDev"))

# Retorno de función


def apply_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier


multiplier = apply_multiplier(2)
print(multiplier(5))
print(apply_multiplier(3)(2))

#  Sistema

numbers = [1, 3, 4, 2, 5]

# map()


def apply_double(n):
    return n * 2


print(list(map(apply_double, numbers)))

# filter()


def is_even(n):
    return n % 2 == 0


print(list(filter(is_even, numbers)))

# sorted()

print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(sorted(numbers, key=lambda x: -x))

# reduce()


def sum_values(x, y):
    return x + y


print(reduce(sum_values, numbers))

"""
Extra
"""

students = [
    {"name": "Brais", "birthdate": "29-04-1987", "grades": [5, 8.5, 3, 10]},
    {"name": "moure", "birthdate": "04-08-1995", "grades": [1, 9.5, 2, 4]},
    {"name": "mouredev", "birthdate": "15-12-2000", "grades": [4, 6.5, 5, 2]},
    {"name": "supermouredev", "birthdate": "25-01-1980",
        "grades": [10, 9, 9.7, 9.9]}
]


def average(grades):
    return sum(grades) / len(grades)

# Promedio


print(
    list(map(lambda student: {
        "name": student["name"],
        "average": average(student["grades"])}, students)
    )
)

# Mejores

print(
    list(
        map(lambda student:
            student["name"],
            filter(lambda student: average(student["grades"]) >= 9, students)
            )
    )
)

# Fecha de nacimiento ordenada

print(sorted(students, key=lambda student: datetime.strptime(
    student["birthdate"], "%d-%m-%Y"), reverse=True))

# Califiación más alta

print(max(map(lambda student: max(student["grades"]), students)))
