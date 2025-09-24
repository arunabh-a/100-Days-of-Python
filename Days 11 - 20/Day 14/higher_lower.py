from ui import logo
from ui import vs
from data import data
import random
from os import system

def data_format(user_data):
    username = user_data['name']
    userdesc = user_data['description']
    usercntry = user_data['country']
    return(f"{username}, a {userdesc}, from {usercntry}")

def compare(guess, afoll, bfoll):
    if afoll > bfoll:
        return guess == 'a'
    else:
        return guess == 'b'

choiceA = random.choice(data)
choiceB = random.choice(data)
while choiceA == choiceB:
    choiceB = random.choice(data)

retry = False
score = 0
while retry == False:
    fllwers_a = choiceA["follower_count"]
    fllwers_b = choiceB["follower_count"]

    print(f"Choice A : {data_format(choiceA)}")
    print(vs)
    print(f"Choice B : {data_format(choiceB)}")
    print("Who has more Followers ??")
    guess = input("Your Guess: ").lower()
    is_correct = compare(guess, fllwers_a, fllwers_b)
    system("CLR")
    system("clear")
    if is_correct:
        score += 1
        print(f"You were Right")
        choiceA = choiceB
        choiceB = random.choice(data)

    else:
        print(f"Wrong Answer, Your Final Score {score}")
        break






