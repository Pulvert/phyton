# 3-1. Names: Store the names of a few of your friends in a list called names. Print
# each person’s name by accessing each element in the list, one at a time.

friends = ["Pueyo", "Chente", "Javi", "Miguelín"]

print(friends[0])
print(friends[1])
print(friends[2])
print(friends[-1])

""" 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
printing each person’s name, print a message to them. The text of each message
should be the same, but each message should be personalized with the
person’s name """

print(f"{friends[0]} es mi amigo")
print(f"{friends[1]} es mi amigo")
print(f"{friends[2]} es mi amigo")
print(f"{friends[3]} es mi amigo")

"""3-3. Your Own List: Think of your favorite mode of transportation, such as a
motorcycle or a car, and make a list that stores several examples. Use your list
to print a series of statements about these items, such as “I would like to own a
Honda motorcycle.”"""

brand_motorcycle = ["honda", "ducati", "bmw", "yamaha"]

print (f"I would like to own a {brand_motorcycle[0]} motorcycle")