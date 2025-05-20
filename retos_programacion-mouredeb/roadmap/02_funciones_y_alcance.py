"""
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""
# Funciones básicas
def function1 ():
  a = 25

def function2 ():
  print ("hello world")

def function3 (num1):
  return num1 + 3

def function4 (str1, str2):
  print (str1 + str2)

print(function1())
function2()
print(function3(10))
function4("hello ", "world")

# Función dentro de función
def function5 (a):
  if a == 0:
    return 1
  else:
    function5 (a-1)
  print(a)

function5(20)

# Función del lenguaje
b = float (10)

print (b)

# Ejemplo variable local y global
c = 15

if c > 10:
  c = 5
  if c < 10:
    print ("now c is lower than 10")


def function6 (str_1, str_2):

  count = 0

  for x in range (101):
    if x % 3 == 0 and x % 5 == 0:
      print(str_1 + " " + str_2)
    elif x % 3 == 0:
      print(str_1)
    elif x % 5 == 0:
      print(str_2)
    else:
      count += 1
      print(x)
  print (f"Se han impreso {count} números")

function6 ("hola", "mundo")


# Solución

"""
Funciones definidas por el usuario
"""

# Simple


def greet():
    print("Hola, Python!")


greet()

# Con retorno


def return_greet():
    return "Hola, Python!"


print(return_greet())

# Con un argumento


def arg_greet(name):
    print(f"Hola, {name}!")


arg_greet("Brais")

# Con argumentos


def args_greet(greet, name):
    print(f"{greet}, {name}!")


args_greet("Hi", "Brais")
args_greet(name="Brais", greet="Hi")

# Con un argumento predeterminado


def default_arg_greet(name="Python"):
    print(f"Hola, {name}!")


default_arg_greet("Brais")
default_arg_greet()

# Con argumentos y return


def return_args_greet(greet, name):
    return f"{greet}, {name}!"


print(return_args_greet("Hi", "Brais"))

# Con retorno de varios valores


def multiple_return_greet():
    return "Hola", "Python"


greet, name = multiple_return_greet()
print(greet)
print(name)

# Con un número variable de argumentos


def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {name}!")


variable_arg_greet("Python", "Brais", "MoureDev", "comunidad")

# Con un número variable de argumentos con palabra clave


def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"{value} ({key})!")


variable_key_arg_greet(
    language="Python",
    name="Brais",
    alias="MoureDev",
    age=36
)

"""
Funciones dentro de funciones
"""


def outer_function():
    def inner_function():
        print("Función interna: Hola, Python !")
    inner_function()


outer_function()

"""
Funciones del lenguaje (built-in)
"""

print(len("MoureDev"))
print(type(36))
print("MoureDev".upper())

"""
Variables locales y globales
"""

global_var = "Python"


def hello_python():
    local_var = "Hola"
    print(f"{local_var}, {global_var}!")


print(global_var)
# print(local_var) No se puede acceder desde fuera de la función

hello_python()

"""
Extra
"""


def print_numbers(text_1, text_2) -> int:
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(text_1 + text_2)
        elif number % 3 == 0:
            print(text_1)
        elif number % 5 == 0:
            print(text_2)
        else:
            print(number)
            count += 1
    return count


print(print_numbers("Fizz", "Buzz"))
