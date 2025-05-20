"""
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
"""

# Clases

class My_class:

  def __init__(self, a, b):
    self.a = a
    self.b = b

  def show (self):
    print(self.a)
    print(self.b)

p1 = My_class(10,20)
p2 = My_class(50,70)

p1.show()
p2.show()


class Fifo:

  def __init__(self):
    self.my_list = [1,2,3,4]
    self.my_second_list =[]

  def remove(self):
    self.my_second_list.append(self.my_list[-1])
    self. my_list.pop(-1)

  def show(self):
    print(self.my_list)
    print(self.my_second_list)

  def add(self):
    self.my_list.append(self.my_second_list[-1])
    self.my_second_list.pop(-1)


fifo1 = Fifo()

fifo1.remove()
fifo1.remove()
fifo1.show()
fifo1.add()
fifo1.show()


class Lifo:

  def __init__(self):
    self.my_list = [1,2,3,4]
    self.my_second_list =[]

  def show(self):
    print(self.my_list)
    print(self.my_second_list)

  def l_remove(self):
    self.my_second_list.append(self.my_list[0])
    self.my_list.pop(0)

  def l_add(self):
    self.my_list.append(self.my_second_list[0])
    self.my_second_list.pop(0)


lifo1 = Lifo()
lifo1.l_remove()
lifo1.l_remove()
lifo1.show()
lifo1.l_add()
lifo1.show()

# Solución

"""
Ejercicio
"""


class Programmer:

    surname: str = None

    def __init__(self, name: str, age: int, languages: list):
        self.name = name
        self.age = age
        self.languages = languages

    def print(self):
        print(
            f"Nombre: {self.name} | Apellidos: {self.surname} | Edad: {self.age} | Lenguajes: {self.languages}")


my_programmer = Programmer("Brais", 36, ["Python", "Kotlin", "Swift"])
my_programmer.print()
my_programmer.surname = "Moure"
my_programmer.print()
my_programmer.age = 37
my_programmer.print()

"""
Extra
"""

# LIFO


class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.count() == 0:
            return None
        return self.stack.pop()

    def count(self):
        return len(self.stack)

    def print(self):
        for item in reversed(self.stack):
            print(item)


my_stack = Stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
print(my_stack.count())
my_stack.print()
my_stack.pop()
print(my_stack.count())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.count())

# FIFO


class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.count() == 0:
            return None
        return self.queue.pop(0)

    def count(self):
        return len(self.queue)

    def print(self):
        for item in self.queue:
            print(item)


my_queue = Queue()
my_queue.enqueue("A")
my_queue.enqueue("B")
my_queue.enqueue("C")
print(my_queue.count())
my_queue.print()
my_queue.dequeue()
print(my_queue.count())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.count())
