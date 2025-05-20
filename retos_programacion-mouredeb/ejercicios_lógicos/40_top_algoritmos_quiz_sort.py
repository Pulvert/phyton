"""
 * Implementa uno de los algoritmos de ordenación más famosos:
 * el "Quick Sort", creado por C.A.R. Hoare.
 * - Entender el funcionamiento de los algoritmos más utilizados de la historia
 *   Nos ayuda a mejorar nuestro conocimiento sobre ingeniería de software.
 *   Dedícale tiempo a entenderlo, no únicamente a copiar su implementación.
 * - Esta es una nueva serie de retos llamada "TOP ALGORITMOS",
 *   donde trabajaremos y entenderemos los más famosos de la historia.
"""
def quicksort(lista):
  # Caso base
  if len(lista) <= 1:
    return lista

  # Caso reursivo
  pivote = lista.pop()

  lista1 = []
  lista2 = []

  for e in lista:
    if e <= pivote:
      lista1.append(e)
    else:
      lista2.append(e)

  lista1 = quicksort(lista1)
  lista2 = quicksort(lista2)

  return lista1 + [pivote] + lista2

lista = [20, 19, 5, 6, 15, -4, 0, 18, 7, 3]

print(lista)
print(quicksort(lista))
