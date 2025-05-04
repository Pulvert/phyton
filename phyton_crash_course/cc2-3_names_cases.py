# 2.3 - Personal Message:Use a variable to represent a person’s name, and print
# a message to that person. Your message should be simple, such as, “Hello Eric,
# would you like to learn some Python today?”


name = "Diego"

message = f"Hello {name}, would you like to learn some Python today?"

print (message)

# 2-4. Name Cases: Use a variable to represent a person’s name, and then print
# that person’s name in lowercase, uppercase, and title case.

name = "Diego"

print(name.lower())
print(name.upper())
print(name.title())

# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the
# quote and the name of its author. Your output should look something like the
# following, including the quotation marks:
# Albert Einstein once said, “A person who never made a mistake never
# tried anything new.”


print ('Albert Einstein once said, "A person who never made a mistake necer tried anything new"')

# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous
# person’s name using a variable called famous_person. Then compose your message
# and represent it with a new variable called message. Print your message.

famous_person = "Albert Einstein"

message = f'{famous_person} once said, "A person who never made a mistake necer tried anything new"'

print(message)

# 2-7. Stripping Names: Use a variable to represent a person’s name, and
# include some whitespace characters at the beginning and end of the name.
# Make sure you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(),
# rstrip(), and strip().

name = "  Diego \n\t Serrano"

print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

# 2-8. File Extensions: Python has a removesuffix() method that works exactly
# like removeprefix(). Assign the value 'python_notes.txt' to a variable called
# filename. Then use the removesuffix() method to display the filename without
# the file extension, like some file browsers do.

filename = "python.notes.txt"

print(filename.removesuffix(".txt"))