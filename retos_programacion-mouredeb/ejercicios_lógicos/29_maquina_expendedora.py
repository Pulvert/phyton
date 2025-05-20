"""
 * Simula el funcionamiento de una máquina expendedora creando una operación
 * que reciba dinero (array de monedas) y un número que indique la selección
 * del producto.
 * - El programa retornará el nombre del producto y un array con el dinero
 *   de vuelta (con el menor número de monedas).
 * - Si el dinero es insuficiente o el número de producto no existe,
 *   deberá indicarse con un mensaje y retornar todas las monedas.
 * - Si no hay dinero de vuelta, el array se retornará vacío.
 * - Para que resulte más simple, trabajaremos en céntimos con monedas
 *   de 5, 10, 50, 100 y 200.
 * - Debemos controlar que las monedas enviadas estén dentro de las soportadas.
"""

def machine(my_product: str, my_coins: list):

  products = {
     "pipas": 140,
     "fanta": 110,
     "patatas": 200,
     "pistachos": 320
  }

  coins = [200, 100, 50, 10, 5] # monedas aceptadas

  # Revisa si el producto solicitado está entre las válidos
  if my_product not in products.keys():
    print(f"{my_product} no disponible")
    return

  # Revisa si la moneda introducida está entre las válidas
  for x in my_coins:
    if x not in coins:
      print (f"moneda no válida, devolvemos monedas:{my_coins}")
      return

  # Revisa si el dinero introducido no es suficiente
  tot = sum(my_coins)  # Total moendas insertadas
  if tot < products[my_product]:
    print("importe insuficiente")

  # Revisa si hay que devolver vueltas con el menor número de monedas
  else:
    tot_exchange = tot-products[my_product]  # Cambio total
    exchange_list = [] # Lista de monedas del cambio

    while tot_exchange > 0: # Mientras exista cambio pendiente
      for x in coins:
        if x > tot_exchange: # Si la moneda es mayor al cambio pendiente pasa
          pass
        else:
          tot_exchange -= x # Restamos total a la moneda
          exchange_list.append(x) # Guardamos la moneda

    print(f"{my_product}: {exchange_list}")

machine("pipas", [100,100])
machine("pistachos", [100, 200])
machine("patatas", [200])
machine("risketos", [200,100])
machine("pipas", [75,100])