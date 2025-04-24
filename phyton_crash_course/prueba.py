import json
from pathlib import Path

# Ruta al archivo .json
path = Path("slista_numero.json")

# Leer el contenido del archivo y convertirlo desde JSON
with open(path) as f:
    numeros = json.load(f)

# Imprimir cada número por separado
for numero in numeros:
    print(numero)