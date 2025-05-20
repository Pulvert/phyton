"""
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un
 * archivo .txt.
 * - Cada producto se guarda en una línea del archivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
 """
import os

f = open('Pulvert.txt', 'w')
f.write ("- Diego\n- 40\n- Phyton")
f.close()

f = open("Pulvert.txt" , "r")
f.read()
f.close()
os.remove("Pulvert.txt")


# Ejercicio

product_name = []
product_sold = []
product_price = []

print ("1 - Añadir")
print ("2 - Consultar")
print ("3 - Actualizar")
print ("4 - Eliminar")
print ("5 - Venta total producto")
print ("6 - Venta total")
print ("7 - Salir")

while True:

  option = input("Elija opción: ")

  if option == "1": # Guardamos producto, ventas y precio en 3 listas
    pro_nam = input("Introduzca el nombre del producto: ")
    product_name.append(pro_nam)

    pro_sold = int(input("Cantidad vendida: "))
    product_sold.append(pro_sold)

    pro_price = int(input("Precio unitario: "))
    product_price.append(pro_price)

  elif option == "2": # Mostramos enumerando para poder trabajar con sus índices
    print ("Producto")
    for x in enumerate(product_name, start = 1):
      print(x)
    print ("Ventas")
    for x in enumerate(product_sold, start = 1):
      print(x)
    print ("Precio")
    for x in enumerate(product_price, start = 1):
      print(x)

  elif option == "3": # Actualizamos los tres valores según índice
    update = int(input("Qué número de producto quieres actualizar?"))

    new_pro_nam = input("Introduzca el nuevo nombre del producto: ")
    product_name[update-1] = new_pro_nam

    new_pro_sold = int(input("Nueva Cantidad vendida: "))
    product_sold[update-1] = new_pro_sold

    new_pro_price = int(input("Nuevo Precio unitario: "))
    product_price[update-1] = new_pro_price

  elif option == "4": # Eliminamos los tres valores según índice
    dele = int(input("Qué número de producto quieres eliminar?"))
    product_name.pop(dele-1)
    product_sold.pop(dele-1)
    product_price.pop(dele-1)

  elif option == "5": # Calculamos multiplicando unidades por precio
    sale_num_pro = int(input("Venta total de producto número: "))
    sale_pro = int(product_sold[sale_num_pro-1]) * int(product_price[sale_num_pro-1])
    print(sale_pro)

  elif option == "6": # Calculamos multiplicando unidades por precio de todos los valores
    len_product = len(product_name)
    tot = 0
    for x in range (0, len_product):
      tot_p = product_sold[x] * product_price[x]
      tot += tot_p
    print(f"La venta total es de: {tot}")

  elif option == "7": # Salimos
    break

t = open("management.txt", "w")

# Escribimos en el .txt los datos con espacios y , (menos el del final)
for x in product_name:
  t.write(x)
  if x != product_name[-1]:
    t.write(",")

for x in product_sold:
  if x == product_sold[0]:
    t.write("\n")
    t.write(str(x))
    t.write(",")
  elif x != product_sold[-1]:
    t.write(str(x))
    t.write(",")
  else:
    t.write(str(x))

t.close()

t = open("management.txt" , "r")
t.read()
t.close()

# Solución

import os

"""
Ejercicio
"""

file_name = "mouredev.txt"

with open(file_name, "w") as file:
    file.write("Brais Moure\n")
    file.write("36\n")
    file.write("Python")

with open(file_name, "r") as file:
    print(file.read())

os.remove(file_name)

"""
Extra
"""

file_name = "mouredev_shop.txt"

open(file_name, "a")

while True:
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar producto")
    print("4. Borrar producto")
    print("5. Mostrar productos")
    print("6. Calcular venta total")
    print("7. Calcular venta por producto")
    print("8. Salir")

    option = input("Selecciona una opción: ")

    if option == "1":
        name = input("Nombre: ")
        quantity = input("Cantidad: ")
        price = input("Precio: ")
        with open(file_name, "a") as file:
            file.write(f"{name}, {quantity}, {price}\n")
    elif option == "2":
        name = input("Nombre: ")
        with open(file_name, "r") as file:
            for line in file.readlines():
                if line.split(", ")[0] == name:
                    print(line)
                    break
    elif option == "3":
        name = input("Nombre: ")
        quantity = input("Cantidad: ")
        price = input("Precio: ")
        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file:
            for line in lines:
                if line.split(", ")[0] == name:
                    file.write(f"{name}, {quantity}, {price}\n")
                else:
                    file.write(line)
    elif option == "4":
        name = input("Nombre: ")
        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file:
            for line in lines:
                if line.split(", ")[0] != name:
                    file.write(line)
    elif option == "5":
        with open(file_name, "r") as file:
            print(file.read())
    elif option == "6":
        total = 0
        with open(file_name, "r") as file:
            for line in file.readlines():
                components = line.split(", ")
                quantity = int(components[1])
                price = float(components[2])
                total += quantity * price
        print(total)
    elif option == "7":
        name = input("Nombre: ")
        total = 0
        with open(file_name, "r") as file:
            for line in file.readlines():
                components = line.split(", ")
                if components[0] == name:
                    quantity = int(components[1])
                    price = float(components[2])
                    total += quantity * price
                    break
        print(total)
    elif option == "8":
        os.remove(file_name)
        break
    else:
        print("Selecciona una de las opciones disponibles.")