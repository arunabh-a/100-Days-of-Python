# Turtle Random Walk: Day 18 Challenge 4
from turtle import Turtle, Screen
import random

tutle = Turtle()
direc = [0, 90, 180, 270]
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", 
        "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


tutle.hideturtle()
tutle.width(10)
tutle.speed(10)
for i in range(100):
    roadlen = random.randint(1, 100)
    randirec = random.choice(direc)
    tutle.color(random.choice(colours))
    tutle.forward(10)
    tutle.setheading(randirec)

diff = Screen()
diff.exitonclick()