# The Pong Game: Day 22 Project
from turtle import Screen
import time
from pong_func import Pong
from ball import Ball

screen = Screen()
screen.setup(900, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


pad_r = Pong((410, 0))
pad_l = Pong((-410, 0))
ball = Ball()

screen.listen()
screen.onkey(pad_r.go_up, "Up")
screen.onkey(pad_r.go_down, "Down")
screen.onkey(pad_l.go_up, "w")
screen.onkey(pad_l.go_down, "s")
# screen.onkey(game_over, "Escape")

game_on = True
while game_on:
    screen.update()
    ball.move_it()
    time.sleep(0.1)

    if ball.ycor() > 280 or ball.ycor() < -280:
            ball.reflect("y")
    
    if ball.xcor() > 380 and ball.distance(pad_r) < 50 or ball.xcor() > -380 and ball.distance(pad_l) < 50 :
            ball.reflect("x")



screen.exitonclick()