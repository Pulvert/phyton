"""5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least ten tests. Have at least five tests evaluate to True and
another five tests evaluate to False."""

"""5-2. More Conditional Tests: You don’t have to limit the number of tests you
create to ten. If you want to try more comparisons, write more tests and add
them to conditional_tests.py. Have at least one True and one False result for
each of the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and
less than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list"""

name = "Diego"
print("Is name == Diego? I predict True")
print(name == "Diego")

number_1 = 50
number_2 = 45
print("Is number_1 < number_2? I predict False")
print(number_1 < number_2)

number_3 = 20
number_4 = 22
print("Is number_3 and number_4 > 18 I predict True")
print(number_3 and number_4 > 18)

games = ["Zelda", "Mario", "Tetris", "Gran Turismo"]
print("Is Mario in the list?I predict True")
print("Mario" in games)

game_name = "gran Turismo"
# creo una lista con todo en minúsculas
games_lower = [game.lower() for game in games]
print("Is gran Turismo in the list?I predict True")
print(game_name.lower() in games_lower)

number_5 = 18
print("Is 19 not iqual to 18?I predict True")
print(number_5 != 19)

number_6 = 87
number_7 = 72
print("Is number_6 or number_7 upper to 75?I predict True")
print(number_6 > 75 or number_7 > 75)

game_active = True
print("Is game active?I predict True")
print(game_active)
