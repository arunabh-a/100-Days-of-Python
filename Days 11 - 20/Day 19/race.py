# Turtle Races: Day 19 Project 2
from turtle import Turtle, Screen
import random as r

turtles = ['leo', 'donte', 'raphael', 'micheal', 'skell']
colors = ['blue', 'purple', 'red', 'orange', 'yellow']

begin = False
screen = Screen()
screen.setup(600, 400)

user_bet = screen.textinput(title= "Color Bet", prompt= 'Which Color will win this race')
col = 0
yaxis = 120
for tutle in turtles:
    tutle = Turtle('turtle')
    tutle.penup()
    tutle.color(colors[col])
    col += 1
    tutle.goto(-270, yaxis)
    yaxis -= 60

if user_bet:
    begin = True


while begin:
    for runner in turtles:
        if runner.xcor() > 270:
            begin = False
            won = runner.pencolor() 
            if won == user_bet:
                print(f"You've Won ! {runner} is the winner.")
            else:
                print(f"You've Lost ! {runner} is the winner ")
        distance = r.randint(0, 10)
        runner.forward(distance)

screen.exitonclick()