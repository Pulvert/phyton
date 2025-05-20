"""
 * Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
 * - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
 * - EXTRA: ¿Eres capaz de dibujar más figuras?
"""

def square(side: int):
  for x in range(side):
      print("*" * side)

def triangle (side: int):
  for x in range(1, side +1):
      print("*" * x)

def rectangle (widht: int):
  height = widht * 2
  for x in range(height):
      print("*" * widht)

square(6)
triangle(6)
rectangle(6)
