"""6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each piece
of information stored in your dictionary."""

dani = {"first_name":"Daniel", "last_name":"Serrano", "age":10, "city":"Madrid"}

print(dani["age"])

"""6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
Dictionaries 99
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program."""

favourite_numbers = {"Eduardo": 7, "Juan": 12, "Manolo": 2, "Nuria": 45}

for favourite_number in favourite_numbers:
    print(f"The favourite number of {favourite_number} is {favourite_numbers[favourite_number]}")


"""6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
• Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output."""

glossary = {
    "dic":"key_value", 
    "if":"condition", 
    "elif": "condition2",
    "else":"last_condition",
    "for":"iteration"
    }

for gloss in glossary:
    print(f"{gloss} : {glossary[gloss]}\n")