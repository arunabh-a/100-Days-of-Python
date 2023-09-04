from turtle import Turtle
import random as r
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        rand_x = r.randint(-280, 280)
        rand_y = r.randint(-280, 280)
        self.goto(rand_x, rand_y)