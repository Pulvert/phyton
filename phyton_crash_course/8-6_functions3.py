"""8-6. City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the values
that are returned."""


def city_country(city, country):
    return (f"{city}, {country}")
    

c = city_country("Madrid", "España")
print (c)

print (city_country("London", "England"))
print (city_country("Paris", "France"))


"""8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the 
album information correctly.
Use None to add an optional parameter to make_album() that allows you to
store the number of songs on an album. If the calling line includes a value for
the number of songs, add that value to the album’s dictionary. Make at least
one new function call that includes the number of songs on an album."""

def make_album(name, title, songs = None):
    albums = {}
    albums["Name"] = name
    albums["Title"] = title
    if songs:
        albums["Songs"] = songs

    
    print(albums)

make_album("El Fary", "Caribirubi")
make_album("El Fary", "Caribirubi", 12)


"""8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop."""

def make_album(albums):
    print(albums)

albums = {}
while True:
    
    name = input("Write the album (q to quit): ")
    if name == "q":
        break
    else:
        albums["Name"] = name

    title = input("Write the artist(q to quit): ")
    if title == "q":
        break
    else:
        albums["Title"] = title

make_album(albums)