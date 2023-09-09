# Turtle Crossing Game: Day 23 Project
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

play = Player()
cars = CarManager()
screen.listen()
screen.onkey(play.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for _ in range(2):
        cars.move_it()
    cars.cargen()