"""3-8. Seeing the World: Think of at least five places in the world you’d like
to visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly;
just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the
actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse-alphabetical order without changing
the order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse() to change the order of your list. Print the list to show that its
order has changed.
• Use reverse() to change the order of your list again. Print the list to show
it’s back to its original order.
• Use sort() to change your list so it’s stored in alphabetical order. Print the
list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse-alphabetical order.
Print the list to show that its order has changed."""

places = ["Tailandia", "Japón", "Tanzania", "Sudáfrica", "Australia"]

print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

"""3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
through 3-7 (pages 41–42), use len() to print a message indicating the number
of people you’re inviting to dinner."""

guests = ["Napoleón", "Gandhi", "Jesús"]
print(f"There are {len(guests)} guests")

"""3-10. Every Function: Think of things you could store in a list. For example, you
could make a list of mountains, rivers, countries, cities, languages, or anything
else you’d like. Write a program that creates a list containing these items and
then uses each function introduced in this chapter at least once."""

cities = ["Madrid", "Zaragoza", "Valencia", "Barcelona"]

print(sorted(cities))

"""3-11. Intentional Error: If you haven’t received an index error in one of your programs
yet, try to make one happen. Change an index in one of your programs
to produce an index error. Make sure you correct the error before closing the
program."""

print (cities[5])