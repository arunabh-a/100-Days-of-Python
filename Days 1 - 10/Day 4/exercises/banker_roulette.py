# Banker Roulette: Day 4 Exercise 2
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

randname = random.choice(names)
# randname = r.randint (0, (len(names) - 1))

print(randname + " is going to buy the meal today!")
