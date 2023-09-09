from turtle import Turtle
import random as r
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self) :
        self.carlist = []

    def cargen(self):
        chance = r.randint(1, 6)
        if chance == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(1,2)
            car.color(r.choice(COLORS))
            car.penup()
            car.goto(310, r.randint(-250, 250))
            self.carlist.append(car)
    
    def move_it(self):
        for car in self.carlist:
            car.setheading(180)
            car.forward(STARTING_MOVE_DISTANCE)

    def spedup(self):
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
        self.forward(STARTING_MOVE_DISTANCE)

