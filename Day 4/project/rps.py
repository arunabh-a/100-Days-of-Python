# Rock Paper Scissors: Day 4 Project

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to Rock Paper Scissors")
print("For your turn, enter:- \n\n")
print("'0' for rock\n")
print("'1' for paper\n")
print("'2' for scissors\n")
comp_choice = random.randint(0,2)
user_choice = int(input("Your Choice: "))

if user_choice == comp_choice:
    print("IT'S A DRAW")
elif user_choice == 0 and comp_choice == 2:
    print(f"You chose: ROCK \n {rock}")
    print(f"I chose: Scissors \n {scissors}")
    print("You Won!")
elif user_choice == 1 and comp_choice == 0:
    print(f"You chose: PAPER \n {paper}")
    print(f"I chose: Rock \n {rock}")
    print("You Won!")
elif user_choice == 2 and comp_choice == 1:
    print(f"You chose: SCISSORS \n {scissors}")
    print(f"I chose: PAPER \n {paper}")
    print("You Won!")


elif comp_choice == 0 and user_choice == 2:
    print(f"You chose: Scissors \n {scissors}")
    print(f"I chose: ROCK \n {rock}")
    print("You Lost!")
elif comp_choice == 1 and user_choice == 0:
    print(f"You chose: ROCK \n {rock}")
    print(f"I chose: PAPER \n {paper}")
    print("You Lost!")
elif comp_choice == 2 and user_choice == 1:
    print(f"You chose: PAPER \n {paper}")
    print(f"I chose: Scissors \n {scissors}")
    print("You Lost!")
    