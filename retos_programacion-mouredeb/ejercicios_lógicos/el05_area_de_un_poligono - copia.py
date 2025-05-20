"""
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
"""

# h = none para hacer el h opcional para el caso del cuadrado, que no se neesita altura
def area (pol, b, h=None):
    if pol == "triangle":
        return b*h/2
    elif pol == "square":
        return b*b
    elif pol == "rectangle":
        return b*h
    

tr = area("triangle", 5, 10)
sq = area("square", 5)
rec = area("rectangle", 5, 10)

print(tr)
print(sq)
print(rec)
