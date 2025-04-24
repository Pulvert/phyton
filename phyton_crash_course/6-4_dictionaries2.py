"""6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 99) by replacing your series of print()
calls with a loop that runs through the dictionary’s keys and values. When
you’re sure that your loop works, add five more Python terms to your glossary.
When you run your program again, these new words and meanings should
automatically be included in the output."""

glossary = {
    "dic":"key_value", 
    "if":"condition", 
    "elif": "condition2",
    "else":"last_condition",
    "for":"iteration"
    }

for k, v in glossary.items():
    print(f"{k} : {v}\n")

"""6-5. Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
• Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
• Use a loop to print the name of each river included in the dictionary.
• Use a loop to print the name of each country included in the dictionary."""

rivers = {"Amazonas":"Brasil", "Nilo":"Egipto", "Yangtsee":"China"}

for river,country in rivers.items():
    print (f"The {river} runs through {country}")

for river in rivers.keys():
    print (river)

for country in rivers.values():
    print (country)

"""6-6. Polling: Use the code in favorite_languages.py (page 96).
• Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
• Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll."""

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

new_persons = ["Juan", "Pedro", "edward", "jen"]

for new_person in new_persons:
    if new_person in favorite_languages.keys():
        print(f"thanks for responding {new_person}")
    else:
        print(f"can you take the poll {new_person}?")