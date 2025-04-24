"""6-7. People: Start with the program you wrote for Exercise 6-1 (page 98). Make
two new dictionaries representing different people, and store all three dictionaries
in a list called people. Loop through your list of people. As you loop through
the list, print everything you know about each person."""

dani = {"first_name":"Daniel", "last_name":"Serrano", "age":10, "city":"Madrid"}
juan = {"first_name":"Juan", "last_name":"García", "age":56, "city":"Salamanca"}
mary = {"first_name":"María", "last_name":"Pérez", "age":32, "city":"Barcelona"}

people = [dani, juan, mary]

for person in people:
    for value, key in person.items():
        print(f"{value}: {key}")

"""6-8. Pets: Make several dictionaries, where each dictionary represents a different
pet. In each dictionary, include the kind of animal and the owner’s name.
Store these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet."""

pet1 = {"kind": "Dog", "owner": "Alice"}
pet2 = {"kind": "Cat", "owner": "Bob"}
pet3 = {"kind": "Parrot", "owner": "Charlie"}
pet4 = {"kind": "Rabbit", "owner": "David"}

pets = [pet1, pet2, pet3, pet4]

for pet in pets:
    print(f"Kind of animal: {pet['kind']}")
    print(f"Owner's name: {pet['owner']}")

"""6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places for
each person. To make this exercise a bit more interesting, ask some friends to
name a few of their favorite places. Loop through the dictionary, and print each
person’s name and their favorite places."""

favorite_places = {"manuel": "Madrid",
                   "Perico": "segovia",
                   "Jose": "Sevilla"
                   }

for key, value in favorite_places.items():
    print(f"{value.capitalize()} is the favourite place to {key.capitalize()}\n")


"""6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 98) so
each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers."""

favourite_numbers = {"Eduardo": 7, "Juan": [12, 6], "Manolo": [2,12,50], "Nuria": 45}

for key, value in favourite_numbers.items():
    if isinstance(value, list):  # Si el valor es una lista
        # Si es una lista, usamos ', '.join(map(str, value)) para convertirla en una cadena separada por comas.
        print(f"{', '.join(map(str, value))} are the favorite numbers to {key}")
    else:  # Si el valor es un solo número
        print(f"{value} is the favorite number to {key}\n")

"""6-11. Cities: Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the information
you have stored about it."""

cities = {"Madrid": {"Country": "Spain", "Population": 5000000, "Food": "Bocata de calamares"},
          "Paris": {"Country": "Spain", "Population": 7000000, "Food": "Crepes"},
          "London": {"Country": "Spain", "Population": 8000000, "Food": "Fish & Chips"},
          "Kyoto": {"Country": "Spain", "Population": 10000000, "Food": "Sushi"}}


for city, specs in cities.items():
    print(city.upper())
    for spec1, spec2 in specs.items():
        print(f"{spec1}: {spec2}")
    print("\n")

"""6-12. Extensions: We’re now working with examples that are complex enough
that they can be extended in any number of ways. Use one of the example programs
from this chapter, and extend it by adding new keys and values, changing
the context of the program, or improving the formatting of the output."""

