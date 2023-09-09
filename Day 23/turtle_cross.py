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
score = Scoreboard()
screen.listen()
screen.onkey(play.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for _ in range(2):
        cars.move_it()
    cars.cargen()
    
    if play.ycor() > 280:
        cars.spedup()
        play.homepos()
        score.level_update()

    for car in cars.carlist:
        if car.distance(play) < 30:
            score.game_over()
    
    if score.loopend:
        game_is_on = False


screen.exitonclick()
