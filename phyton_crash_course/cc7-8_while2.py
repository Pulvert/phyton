"""7-8. Deli: Make a list called sandwich_orders and fill it with the names of various
sandwiches. Then make an empty list called finished_sandwiches. Loop through
the list of sandwich orders and print a message for each order, such as I made
your tuna sandwich. As each sandwich is made, move it to the list of finished
sandwiches. After all the sandwiches have been made, print a message listing
each sandwich that was made."""

sandwich_orders = ["Ahumados", "Atún" , "Vegetal", "Jamón"]

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)

    print(f"{sandwich} sandwich has made")

print("Your sandwichs are:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
    

"""7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches."""

 
sandwich_orders = ["Ahumados", "Pastrami" , "Atún" , "Pastrami", "Vegetal", "Jamón", "Pastrami"]

finished_sandwiches = []

while sandwich_orders:

    sandwich = sandwich_orders.pop()
    
    if sandwich == "Pastrami":
        continue
    else:

        finished_sandwiches.append(sandwich)
        print(f"{sandwich} sandwich has made")

print("Your sandwichs are:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)


"""7-10. Dream Vacation: Write a program that polls users about their dream vacation.
Write a prompt similar to If you could visit one place in the world, where
would you go? Include a block of code that prints the results of the poll."""

poll = {}

while True:

    name = input("What´s your name(q to quit): ")

    if name == "q":
        break

    place = input("If you could visit one place in the world, where would you go?(q to quit): ")

    if place == "q":
        break

    poll[name] = place

print("\nDream Vacation Poll Results:")
for key,value in poll.items():
    print(f"{key} would like to visit {value}")