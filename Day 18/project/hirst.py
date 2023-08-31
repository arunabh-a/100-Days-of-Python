# The Hirst Painting: Day 18 Project
import turtle as t
import random


t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

# Extracted the Colors using colorgram: https://replit.com/@arunabh22/Colorgram-Color-Extractor
colorlist = [(138, 78, 52), (49, 26, 23), (41, 78, 183), (226, 237, 248), (196, 158, 118), (80, 234, 202), (66, 200, 226), (237, 169, 164), (240, 16, 16), (174, 178, 231), (224, 19, 119), (27, 40, 156), (81, 80, 213), (238, 227, 5), (248, 236, 31), (63, 233, 242), (222, 248, 240), (225, 138, 205), (238, 156, 218), (19, 150, 23), (222, 78, 50), (11, 226, 238), (6, 245, 223), (10, 79, 111), (239, 41, 154), (249, 223, 239), (18, 20, 44), (39, 213, 68), (195, 15, 11), (196, 12, 32), (10, 96, 61), (16, 54, 243), (84, 206, 148), (73, 9, 31), (3, 66, 40), (247, 9, 42), (156, 131, 93)]


tim.setheading(225)
tim.forward(300)
tim.setheading(0)
dotnum = 101

for dotcount in range(1, dotnum):
    tim.dot(20, random.choice(colorlist))
    tim.forward(50)

    if dotcount % 10 == 0:  
        tim.setheading(90)  
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()

screen.exitonclick()