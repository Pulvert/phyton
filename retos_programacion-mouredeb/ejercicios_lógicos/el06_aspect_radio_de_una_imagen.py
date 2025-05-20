"""
 * Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo:
 *   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
"""

# librería popular para trabajar con imágenes
from PIL import Image
# librería para trabajar con fracciones
from fractions import Fraction

# guardamos la ruta (estoy haciendo el ejercicio con imagen en local)
file_location = r"C:\Users\Usuario\Documents\Formación\phyton\retos_programacion-mouredeb\ejercicios_lógicos\psicologa.jpg"

# trabajamos con Image de PIL para sacar el ancho y el alto
with Image.open(file_location) as img:
    ancho, alto = img.size
    # lo dividimos
    aspect_ratio = ancho / alto

    # convertir aspect ratio decimal a fracción simplificada
    frac = Fraction(aspect_ratio).limit_denominator(100)  # limita denominador para no tener fracciones raras

print(f"Dimensiones: {ancho}x{alto}")
print(f"Aspect Ratio decimal: {aspect_ratio:.4f}")
print(f"Aspect Ratio como proporción: {frac.numerator}:{frac.denominator}")