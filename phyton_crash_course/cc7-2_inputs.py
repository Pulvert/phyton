"""7-1. Rental Car: Write a program that asks the user what kind of rental car they
would like. Print a message about that car, such as “Let me see if I can find you
a Subaru.”"""

brand = input("What brand of car do you prefeer?: ")

print(f"Let me see if I can find you a {brand}\n")

"""7-2. Restaurant Seating: Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message saying
they’ll have to wait for a table. Otherwise, report that their table is ready."""

people = input("how many persosons are you?: ")
people = int(people)

if people > 8:
    print("you will have to wait for a table\n")

else:
    print("your table are ready\n")

"""7-3. Multiples of Ten: Ask the user for a number, and then report whether the
number is a multiple of 10 or not."""

number = input("Write a number: ")
number = int(number)

if number % 10 == 0:
    print("is a multiple of 10")

else:
    print("is not a multiple of 10")