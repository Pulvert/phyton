"""
 * Crea un función, que dado un año, indique el elemento
 * y animal correspondiente en el ciclo sexagenario del zodíaco chino.
 * - Info: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
 * - El ciclo sexagenario se corresponde con la combinación de los elementos
 *   madera, fuego, tierra, metal, agua y los animales rata, buey, tigre,
 *   conejo, dragón, serpiente, caballo, oveja, mono, gallo, perro, cerdo
 *   (en este orden).
 * - Cada elemento se repite dos años seguidos.
 * - El último ciclo sexagenario comenzó en 1984 (Madera Rata).
"""

def chinese_calendar (year:int)->str:

  element = ["madera", "fuego", "tierra", "metal", "agua"]
  # Repetir cada elemento dos veces
  element_x2 = []
  for el in element:
    element_x2.extend([el, el])
  repeated_element_x2 = (element_x2 * (60 // len(element_x2) + 1))[:60] #  multiplica por un número
  # suficiente de veces para asegurar que la lista resultante tenga al menos 60 elementos.
  # [:60] recorta la lista resultante para que tenga exactamente 60 elementos.
  animal = ["rata", "buey", "tigre", "conejo", "dragón", "serpiente", "caballo",
            "oveja", "mono", "gallo", "perro", "cerdo"]
  repeated_animal = (animal * (60 // len(animal) + 1))[:60]
  chinese_year = [x for x in range(1,61)]  # Creamos lista del 1 al 60
  oc_year = [x for x in range(1924, 1984)] # Creamos años del 1924 al 1983

  # Unimos
  master_list = []

  for i, x, c, d in zip(chinese_year, oc_year, repeated_animal,  repeated_element_x2):
    master_list.append([i, x, c, d])

  # Buscamos el año en la lista master
  for i in master_list:
	  if year in i:
  		print(i)


chinese_calendar(1983)


# Chat GPT

def zodiaco_chino(anio):
    elementos = ['Madera', 'Fuego', 'Tierra', 'Metal', 'Agua']
    animales = ['Rata', 'Buey', 'Tigre', 'Conejo', 'Dragón', 'Serpiente', 'Caballo', 'Oveja', 'Mono', 'Gallo', 'Perro', 'Cerdo']

    # Inicio del último ciclo sexagenario
    inicio_ciclo = 1984

    # Calcular el número de años desde el inicio del ciclo
    diferencia_anios = anio - inicio_ciclo

    # El ciclo de animales se repite cada 12 años
    indice_animal = diferencia_anios % 12

    # El ciclo de elementos se repite cada 10 años (cada elemento dura 2 años)
    indice_elemento = (diferencia_anios // 2) % 5

    return elementos[indice_elemento], animales[indice_animal]

# Ejemplo de uso:
anio = 2024
elemento, animal = zodiaco_chino(anio)
print(f"El año {anio} corresponde a {elemento} {animal}.")