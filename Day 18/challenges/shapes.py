# Turtle Shapes: Day 18 Challenge 3
from turtle import Turtle, Screen
import random
tutle = Turtle()


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", 
        "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def shape(sidenum):
    angle = 360 / sidenum
    for _ in range(sidenum): # For Triangle
        tutle.forward(100)
        tutle.right(angle)

for _ in range(3, 10):
    tutle.color(random.choice(colours))
    shape(_)

diff = Screen()
diff.exitonclick()