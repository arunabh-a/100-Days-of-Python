# Guess the Number (Game): Day 12 Project
import random

num_list = []
for i in range(100):
    num_list.append(i)

RANDNUM = int(random.choice(num_list))

print("Welcome to 'Guess the Number'")
diff = input("Type your difficulty: ").lower()
print("I'm thinking of a number between 1 and 100.")

if diff == 'easy':
    tries = 10
elif diff == 'hard':
    tries = 5
else:
    print("Please mention a valid difficulty.")

def compare():
    if GUESS > RANDNUM:
        print("Try Lower")
    elif GUESS < RANDNUM:
        print("Try Higher")
    else:
        print("How ??")

while tries != 0:
    print(f"You got {tries} tries")
    GUESS = int(input("Your Guess: "))
    if GUESS == RANDNUM:
        print("You Win")
        break
    else: 
        compare()
        tries -= 1

