from turtle import Turtle, Screen
import turtle
import random

color = [0, 0, 0]
tutle = Turtle()
turtle.colormode(255)
def randcolor():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    rancol = (r,g,b)
    return rancol


tutle.hideturtle()
tutle.width(10)
tutle.speed(10)
for i in range(100):
    roadlen = random.randint(1, 100)
    col = randcolor()
    tutle.color(col)
    tutle.forward(10)
    tutle.setheading(90)


diff = Screen()

diff.exitonclick()