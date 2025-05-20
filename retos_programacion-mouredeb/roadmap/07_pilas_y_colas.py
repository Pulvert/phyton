"""
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
"""

my_list = [1,2,3,4]
my_second_list =[]

# FIFO

def f_remove():
  my_second_list.append(my_list[-1])
  my_list.pop(-1)
  print(my_list)
  print(my_second_list)

def f_add():
  my_list.append(my_second_list[-1])
  my_second_list.pop(-1)
  print(my_list)
  print(my_second_list)

# LIFO

def l_remove():
  my_second_list.append(my_list[0])
  my_list.pop(0)
  print(my_list)
  print(my_second_list)

def l_add():
  my_list.append(my_second_list[0])
  my_second_list.pop(0)
  print(my_list)
  print(my_second_list)

# Páginas Web

back_web_list = ["www.elpais.com", "www.marca.com"]
actual_web_list = ["www.larazon.com"]
forward_web_list = ["www.abc.es"]

def back():
  actual_web_list.append(back_web_list[-1])
  back_web_list.pop(-1)
  forward_web_list.append(actual_web_list[0])
  actual_web_list.pop(0)
  print(f"Las webs de atrás son{back_web_list}")
  print(f"La web actual es{actual_web_list}")
  print(f"Las webs de adelante son{forward_web_list}")

def forward():
  actual_web_list.append(forward_web_list[-1])
  forward_web_list.pop(-1)
  back_web_list.append(actual_web_list[0])
  actual_web_list.pop(0)
  print(f"Las webs de atrás son{back_web_list}")
  print(f"La web actual es{actual_web_list}")
  print(f"Las webs de adelante son{forward_web_list}")

back()
back()
forward()
forward()
forward()
back()


# Printer

print_list = ["file1.txt", "file2.txt", "file3.txt"]

def impr_printer ():
  print_list.pop(0)
  print(print_list)

def add_file_printer ():
  print_list.append("fileX.txt")
  print(print_list)

def remove_file_printer ():
  print_list.pop(-1)
  print(print_list)

impr_printer ()
add_file_printer ()
remove_file_printer ()

# Solución

"""
Ejercicio
"""

# Pila/Stack (LIFO)

stack = []

# push
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

# pop
stack_item = stack[len(stack) - 1]
del stack[len(stack) - 1]
print(stack_item)

print(stack.pop())

print(stack)

# Cola/Queue (FIFO)

queue = []

# enqueue
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

# dequeue
queue_item = queue[0]
del queue[0]
print(queue_item)

print(queue.pop(0))

print(queue)

"""
Extra
"""

# Web


def web_navigation():

    stack = []

    while True:

        action = input(
            "Añade una url o interactúa con palabras adelante/atrás/salir: "
        )

        if action == "salir":
            print("Saliendo del navegador web.")
            break
        elif action == "adelante":
            pass
        elif action == "atrás":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(action)

        if len(stack) > 0:
            print(f"Has navegado a la web: {stack[len(stack) - 1]}.")
        else:
            print("Estás en la página de inicio.")


web_navigation()


def shared_printed():

    queue = []

    while True:

        action = input("Añade un documento o selecciona imprimir/salir: ")

        if action == "salir":
            break
        elif action == "imprimir":
            if len(queue) > 0:
                print(f"Imprimiendo: {queue.pop(0)}")
        else:
            queue.append(action)

        print(f"Cola de impresión: {queue}")


shared_printed()


