"""
 * Crea un programa que determine si dos vectores son ortogonales.
 * - Los dos array deben tener la misma longitud.
 * - Cada vector se podría representar como un array. Ejemplo: [1, -2]
"""

def is_ortogonal(v1: list, v2:list) -> bool:
  if len(v1) != 2 or len(v2) != 2: # Solo pueden tener dos números
    raise ValueError("Las dos listas deben de tener dos componentes")
  elif v1[0] * v2[0] + v1[1] * v2[1] == 0: # Fórmula
    return True
  else:
    return False

print(is_ortogonal([1, -2],[2, 1]))