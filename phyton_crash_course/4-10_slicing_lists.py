"""4-10. Slices: Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to
print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. Then use a
slice to print three items from the middle of the list.
• Print the message The last three items in the list are:. Then use a slice to
print the last three items in the list."""

foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']

a,b,c = (foods[0:3])

print (f"The first three items from the list are {a}, {b} and {c}")

a,b,c = (foods[1:4])
print (f"The three items from the middle of the list are {a}, {b} and {c}")

a,b,c = (foods[2:])
print (f"The last three items from the list are {a}, {b} and {c}")

"""4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56).
Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the
following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite pizzas
are:, and then use a for loop to print the first list. Print the message My
friend’s favorite pizzas are:, and then use a for loop to print the second list.
Make sure each new pizza is stored in the appropriate list."""

pizzas = ["Barbacoa", "Hawaiana", "Diabola"]

friend_pizzas = pizzas[0:]

pizzas.append("Carbonara")
friend_pizzas.append("Margarita")

print(f"My favorites pizzas are:")
for pizza in pizzas:
    print(pizza)

print(f"My friends favorites pizzas are:")
for pizza in friend_pizzas:
    print(pizza)


"""4-12. More Loops: All versions of foods.py in this section have avoided using
for loops when printing, to save space. Choose a version of foods.py, and
write two for loops to print each list of foods."""

my_foods = ['pizza', 'falafel', 'carrot cake']
for food in my_foods:
    print(food)