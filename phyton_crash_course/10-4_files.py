from pathlib import Path

"""10-4. Guest: Write a program that prompts the user for their name. When they 
respond, write their name to a file called guest.txt."""

name = input("What´s your name?: ")

path = Path("guest.txt")
path.write_text(name)


"""10-5. Guest Book: Write a while loop that prompts users for their name. Collect 
all the names that are entered, and then write these names to a file called 
guest_book.txt. Make sure each entry appears on a new line in the file."""


path = Path("guest_book.txt")
while True:


    name = input("What´s your name?(press 'e' to exit): ")

    if name == "e":
        break

    else:
        # Usamos open(path, "a") para abrir el archivo en modo de adición.
        with open(path, "a") as file:
            file.write(name + "\n")