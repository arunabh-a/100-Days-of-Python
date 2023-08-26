# Turtle Dashed line: Day 18 Challenge 2
from turtle import Turtle, Screen

tutle = Turtle()
for i in range (20):
    tutle.forward(10)
    tutle.penup()
    tutle.forward(10)
    tutle.pendown()


diff = Screen()

diff.exitonclick()