"""
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
"""

my_list = ["Banana", "Apple", "Orange"]
print(my_list[1])
my_list.append("Melon")
my_list.remove("Apple")
my_list[0] = "Pineapple"
my_list.sort()

print(my_list)

my_dictionary = {
  "Name": "Diego",
  "Surname": "García"
}

print (my_dictionary["Name"])
my_dictionary["Age"] = 40
my_dictionary.pop("Name")
my_dictionary["Surname"] = "Sánchez"

print (my_dictionary)

my_tuple = ()
my_set = {}


class Contacts:
  def __init__(self):
    self.my_contacts = {}

  def search_contact (self):
    search_number = input("Teléfono de: ")
    print(self.my_contacts[search_number])

  def add_contact (self):
    name = input("Añada contacto: ")
    if name in self.my_contacts:
      print("Contacto repetido")
    number = input("Añada teléfono: ")
    while not number.isdigit() or len(number) != 3:
      number = input("Añada teléfono con tres cifras: ")
    self.my_contacts[name] = number

  def contacts_list (self):
    print (self.my_contacts)

  def update_contact (self):
    name = input("Contacto a actualizar: ")
    new_number = input("Nuevo teléfono: ")
    self.my_contacts[name] = new_number

  def delete_contact (self):
    name = input("Contacto a eliminar: ")
    self.my_contacts.pop(name)

  def show_options (self):
    option = print(f"\n MENU PRINCIPAL\n ------------\n1-Mostrar contactos\n2-Búsqueda número\n3-Agregar contacto\n4-Actualizar contacto\n5-Eliminar contacto\n6-Salir")

p1 = Contacts()
p1.show_options()

while True:

  action = input("\n1 Elige opción ('help' para recordar opciones): ")

  if action == "1":
    p1.contacts_list()
  elif action == "2":
    p1.search_contact()
  elif action == "3":
    p1.add_contact()
  elif action == "4":
    p1.update_contact()
  elif action == "5":
    p1.delete_contact()
  elif action == "6":
    break
  elif action == "help":
    p1.show_options()

# Solución
"""
Estructuras
"""

# Listas
my_list: list = ["Brais", "Bl4ck", "Wolfy", "Visionos"]
print(my_list)
my_list.append("Castor")  # Inserción
my_list.append("Castor")
print(my_list)
my_list.remove("Brais")  # Eliminación
print(my_list)
print(my_list[1])  # Acceso
my_list[1] = "Cuervillo"  # Actualización
print(my_list)
my_list.sort()  # Ordenación
print(my_list)
print(type(my_list))

# Tuplas
my_tuple: tuple = ("Brais", "Moure", "@mouredev", "36")
print(my_tuple[1])  # Acceso
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple))  # Ordenación
print(my_tuple)
print(type(my_tuple))

# Sets
my_set: set = {"Brais", "Moure", "@mouredev", "36"}
print(my_set)
my_set.add("mouredev@gmail.com")  # Inserción
my_set.add("mouredev@gmail.com")
print(my_set)
my_set.remove("Moure")  # Eliminación
print(my_set)
my_set = set(sorted(my_set))  # No se puede ordenar
print(my_set)
print(type(my_set))

# Diccionario
my_dict: dict = {
    "name": "Brais",
    "surname": "Moure",
    "alias": "@mouredev",
    "age": "36"
}
my_dict["email"] = "mouredev@gmail.com"  # Inserción
print(my_dict)
del my_dict["surname"]  # Eliminación
print(my_dict)
print(my_dict["name"])  # Acceso
my_dict["age"] = "37"  # Actualización
print(my_dict)
my_dict = dict(sorted(my_dict.items()))  # Ordenación
print(my_dict)
print(type(my_dict))

"""
Extra
"""


def my_agenda():

    agenda = {}

    def insert_contact():
        phone = input("Introduce el teléfono del contacto: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] = phone
        else:
            print(
                "Debes introducir un número de teléfono un máximo de 11 dígitos.")

    while True:

        print("")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        option = input("\nSelecciona una opción: ")

        match option:
            case "1":
                name = input("Introduce el nombre del contacto a buscar: ")
                if name in agenda:
                    print(
                        f"El número de teléfono de {name} es {agenda[name]}.")
                else:
                    print(f"El contacto {name} no existe.")
            case "2":
                name = input("Introduce el nombre del contacto: ")
                insert_contact()
            case "3":
                name = input("Introduce el nombre del contacto a actualizar: ")
                if name in agenda:
                    insert_contact()
                else:
                    print(f"El contacto {name} no existe.")
            case "4":
                name = input("Introduce el nombre del contacto a a eliminar: ")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"El contacto {name} no existe.")
            case "5":
                print("Saliendo de la agenda.")
                break
            case _:
                print("Opción no válida. Elige una opción del 1 al 5.")


my_agenda()
