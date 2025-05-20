"""
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un pequeño sistema de gestión del estado de pedidos.
 * Implementa una clase que defina un pedido con las siguientes características:
 * - El pedido tiene un identificador y un estado.
 * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
 * - Implementa las funciones que sirvan para modificar el estado:
 *   - Pedido enviado
 *   - Pedido cancelado
 *   - Pedido entregado
 *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
 * - Implementa una función para mostrar un texto descriptivo según el estado actual.
 * - Crea diferentes pedidos y muestra cómo se interactúa con ellos.
"""
from enum import Enum

class Week(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

def day (num):
  day_enum = Week(num)
  print(day_enum.name)

day(7)

# Extra

class Order(Enum):
  PENDIENTE = 1
  ENVIADO = 2
  CANCELADO = 3
  ENTREGADO = 4

orders = {}

def new_stat():
  id = input("Nuevo pedido: Introduce id: ")
  status = int(input("Introduce estado(1-Pendiente, 2-Enviado, 3-Cancelado, 4-Entregado): "))

  orders[id] = Order(status).name

def change_stat():
  id = input("Actualizar pedido: Introduce id: ")
  status = int(input("Introduce estado(1-Pendiente, 2-Enviado, 3-Cancelado, 4-Entregado): "))

  if orders[id] == "CANCELADO":
    print("Este pedido está cancelado")

  elif orders[id] == "ENTREGADO":
    print("Este pedido ya está entregado")

  elif orders[id] == "PENDIENTE" and status == 4:
    print("No se puede entregar un paquete que no se ha enviado")

  else:
    orders[id] = Order(status).name

def consult_orders():
  print("  ID ---- STATUS")
  for key in orders.items():
    print(key)


print("1-Crear pedido")
print("2-Actualizar pedido")
print("3-Consultar pedidos")
print("4-Salir")

while True:

  option = input("Escriba opción: ")

  if option == "1":
    new_stat ()

  elif option == "2":
    change_stat()

  elif option == "3":
    consult_orders()

  elif option == "4":
    break

"""
Ejercicio
"""

class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

def get_day(number: int):
    print(Weekday(number).name)

get_day(1)
get_day(3)

"""
Extra
"""

class OrderStatus(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3
    CANCELLED = 4

class Order:

    status = OrderStatus.PENDING

    def __init__(self, id) -> None:
        self.id = id

    def ship(self):
        if self.status == OrderStatus.PENDING:
            self.status = OrderStatus.SHIPPED
            self.display_status()
        else:
            print("El pedido ya ha sido enviado o cancelado")

    def deliver(self):
        if self.status == OrderStatus.SHIPPED:
            self.status = OrderStatus.DELIVERED
            self.display_status()
        else:
            print("El pedido necesita ser enviado antes de entregarse.")

    def cancel(self):
        if self.status != OrderStatus.DELIVERED:
            self.status = OrderStatus.CANCELLED
            self.display_status()
        else:
            print("El pedido no se puede cancelar ya que ya se ha entregado.")

    def display_status(self):
        print(f"El estado del pedido {self.id} es {self.status.name}")


order_1 = Order(1)
order_1.display_status()
order_1.deliver()
order_1.ship()
order_1.deliver()
order_1.cancel()