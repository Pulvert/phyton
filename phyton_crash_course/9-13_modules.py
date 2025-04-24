from random import randint, choice


"""9-13. Dice: Make a class Die with one attribute called sides, which has a 
default value of 6. Write a method called roll_die() that prints a random 
number between 1 and the number of sides the die has. Make a 6-sided die
and roll it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times."""

class Die:
    def __init__(self):
        self.die = 6

    def roll_die (self):
        result = randint(1,self.die)
        print(result)
    
b = Die()
b.roll_die()
b.roll_die()
b.roll_die()
b.roll_die()
b.roll_die()

print("\n")

"""9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters.
Randomly select 4 numbers or letters from the list and print a message saying that
any ticket matching these 4 numbers or letters wins a prize."""

numbers_lottery = [2, 5, 9, 3, 1, 6, 7, 3, 4, 1, "b", "j" ,"t", "u", "o"]
lottery_win = []

for x in range(4):

    number = choice(numbers_lottery)
    lottery_win.append(number)
    numbers_lottery.remove(number)

print(lottery_win)
print("\n")

"""9-15. Lottery Analysis: You can use a loop to see how hard it might be to win 
the kind of lottery you just modeled. Make a list or tuple called my_ticket. Write 
a loop that keeps pulling numbers until your ticket wins. Print a message 
reporting how many times the loop had to run to give you a winning ticket."""

my_ticket = [5,2,"b","j"]
numbers_lottery = [2, 5, 9, 3, 1, 6, 7, 3, 4, 1, "b", "j" ,"t", "u", "o"]
lottery_win = []

count = 0
while True:

    # Reiniciar listas al comienzo de cada intento
    lottery_win2 = []
    numbers_lottery2 = numbers_lottery.copy()

    # Se crea la lista premiada
    for x in range(4):
        number = choice(numbers_lottery2)
        lottery_win2.append(number)
        numbers_lottery2.remove(number)
    
    # Se cuentan los intentos
    count += 1
        
    # Sigue el bucle hasta que coincide con tu boleto e imprime los intentos
    if lottery_win2 == my_ticket:
        print(count)
        break

