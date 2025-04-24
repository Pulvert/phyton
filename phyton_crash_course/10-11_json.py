from pathlib import Path
import json

"""10-11. Favorite Number: Write a program that prompts for the user’s favorite 
number. Use json.dumps() to store this number in a file. Write a separate 
program that reads in this value and prints the message “I know your favorite
number! It’s _____.”"""
"""
favorite_number = input("What´s your favorite number?: ")
path = Path("favorite_number.json")
number = json.dumps(favorite_number)
path.write_text(number)

message = path.read_text()
print(f"I know your favorite number! It’s {message}")
"""

"""10-12. Favorite Number Remembered: Combine the two programs you wrote in 
Exercise 10-11 into one file. If the number is already stored, report the favorite 
number to the user. If not, prompt for the user’s favorite number and store it in a 
file. Run the program twice to see that it works."""


"""
# Ruta al archivo donde se guarda el número
path = Path("favorite_number.json")

if path.exists():
    # Si el archivo ya existe, leemos el número guardado
    favorite_number = json.loads(path.read_text())
    print(f"I know your favorite number! It’s {favorite_number}")
else:
    # Si no existe, pedimos el número y lo guardamos
    favorite_number = input("What’s your favorite number?: ")
    path.write_text(json.dumps(favorite_number))
    print("Got it! I’ll remember your favorite number.")
"""


"""10-13. User Dictionary: The remember_me.py example only stores one piece of 
information, the username. Expand this example by asking for two more pieces 
of information about the user, then store all the information you collect in a 
dictionary. Write this dictionary to a file using json.dumps(), and read it back 
in using json.loads(). Print a summary showing exactly what your program 
remembers about the user."""


"""
def greet_user():

    dic = {}

    path = Path('username_information.json')
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcome {username["name"]}")
        print(username)

    else:
        username = input("What is your name?: ")
        dic["name"] = username
        age = input("Age?: ")
        dic["age"] = age
        contents = json.dumps(dic)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {dic["name"]}!")
        print(username)
    

greet_user()
"""

"""10-14. Verify User: The final listing for remember_me.py assumes either that the 
user has already entered their username or that the  program is running for the 
first time. We should modify it in case the current user is not the person who last 
used the program.
Before printing a welcome back message in greet_user(), ask the user if this is the correct 
username. If it’s not, call get_new_username() to get the correct username."""


def greet_user():

    path = Path('username_information.json')
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        user_compr = input(f"Are you {username["name"]}?: ")
        if user_compr.lower() == "yes":
            print(f"Welcome {username["name"]}")
            print(username)
        else:
            get_new_user()
  
    else:
        get_new_user()

def get_new_user():
    dic = {}
    path = Path('username_information.json')
    username = input("What is your name?: ")
    dic["name"] = username
    age = input("Age?: ")
    dic["age"] = age
    contents = json.dumps(dic)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {dic["name"]}!")
    print(username)
    
greet_user()



