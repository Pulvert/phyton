"""
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
 * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
 * - Nombre
 * - Edad
 * - Fecha de nacimiento
 * - Listado de lenguajes de programación
 * Muestra el contenido de los archivos.
 * Borra los archivos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
"""
import json
import os

data = {"Nombre": "Diego",
        "Edad": 40,
        "Fecha de Nacimiento": "11/03/1984",
        "Lenguajes": ["Python", "JavaScript", "C++"],
        }

# json
# indent=4 es para hacer el JSON más legible
json_file = "pulvert.json"

# Escribir el diccionario en el archivo JSON
with open(json_file, 'w') as file:
    json.dump(data, file, indent=4)  # indent=4 es para hacer el JSON más legible

# Reabrir el archivo en modo lectura para cargar los datos
with open(json_file, 'r') as file:
    data2 = json.load(file)

# Mostrar el contenido del JSON
print(data2)

os.remove(json_file)

# xml

import xml.etree.ElementTree as ET

# Crear el elemento raíz
persona = ET.Element("persona")

# Crear subelementos
nombre = ET.SubElement(persona, "nombre")
nombre.text = "Diego"

edad = ET.SubElement(persona, "edad")
edad.text = "40"

fecha_nacimiento = ET.SubElement(persona, "fecha_de_nacimiento")
fecha_nacimiento.text = "11/03/1984"

lenguajes = ET.SubElement(persona, "lenguajes")
lenguaje1 = ET.SubElement(lenguajes, "lenguaje")
lenguaje1.text = "Python"
lenguaje2 = ET.SubElement(lenguajes, "lenguaje")
lenguaje2.text = "JavaScript"
lenguaje3 = ET.SubElement(lenguajes, "lenguaje")
lenguaje3.text = "C++"

# Convertir el elemento raíz en un árbol ElementTree
arbol = ET.ElementTree(persona)

# Escribir el árbol en un archivo XML
archivo_xml = "pulvert.xml"
with open(archivo_xml, "wb") as file:
    arbol.write(file, encoding="utf-8", xml_declaration=True)

    arbol = ET.parse(archivo_xml)
    raiz = arbol.getroot()

    # Mostrar el contenido del XML
    print(f"Nombre: {raiz.find('nombre').text}")
    print(f"Edad: {raiz.find('edad').text}")
    print(f"Fecha de Nacimiento: {raiz.find('fecha_de_nacimiento').text}")

    print("Lenguajes:")
    for lenguaje in raiz.find('lenguajes').findall('lenguaje'):
        print(f" - {lenguaje.text}")


os.remove(archivo_xml)
