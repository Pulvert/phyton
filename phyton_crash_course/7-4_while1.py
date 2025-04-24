"""7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping, print
a message saying you’ll add that topping to their pizza."""

message = "What topping do you want?" 
message += "\n(Press quit to exit): "

while True:
    topping = input(message)

    if topping == "quit":
        break
    else:
        print(f"Added {topping} to your pizza")
        
        
"""7-5. Movie Tickets: A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket."""

age = "How old are you?: "
age += "\n(Press quit to exit): "


while True:
    user_input = (input(age))

    if user_input.lower() == "quit":
        break

    if user_input.isdigit():
        user_input = int(user_input)
        if user_input < 3:
            print("The ticket is free")
    
        elif user_input >= 3 and user_input < 12:
            print("The ticket is $10")

        else:
            print("The ticket is $12")


"""7-6. Three Exits: Write different versions of either Exercise 7-4 or 7-5 that do
each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value."""

age = "How old are you?: "
age += "\n(Press quit to exit): "

active = True

while active:
    user_input = (input(age))

    if user_input.lower() == "quit":
        break

    if user_input.isdigit():
        user_input = int(user_input)
        if user_input < 3:
            print("The ticket is free")
    
        elif user_input >= 3 and user_input < 12:
            print("The ticket is $10")

        else:
            print("The ticket is $12")  


"""7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press
CTRL-C or close the window displaying the output.)"""

x = 5

while x > 1:
    print("loop never ends")
