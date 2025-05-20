"""
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
"""
def area (type):

  base = 5
  altura = 6

  if type == "triangle":
    return base * altura / 2
  elif type == "square":
    return base * base
  elif type == "rectangle":
    return base * altura


print (area("triangle"))