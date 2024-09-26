# The Pong Game: Day 22 Project
from turtle import Screen
import time
from paddle import Pong
from ball import Ball
from score import Score



screen = Screen()
screen.setup(900, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

game_on = True
def game_over():
    game_on = False

pad_r = Pong((400, 0), "red")
pad_l = Pong((-400, 0), "blue")
ball = Ball()
score = Score()

screen.listen()
screen.onkey(pad_r.go_up, "Up")
screen.onkey(pad_r.go_down, "Down")
screen.onkey(pad_l.go_up, "w")
screen.onkey(pad_l.go_down, "s")
screen.onkey(ball.game_over, "Escape")


while game_on:
    screen.update()
    ball.move_it("r")
    time.sleep(ball.move_speed)


    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.reflect("y")
    
    if ball.distance(pad_l) < 50 and ball.xcor() < -370 or ball.distance(pad_r) < 50 and ball.xcor() > 370 :
        print("Made Contact")
        ball.reflect("x")

    if ball.xcor() > 380:
        ball.missed()
        score.score_update("right")
    elif ball.xcor() < -380:
        ball.missed()
        score.score_update("left")
    
    if ball.loopend:
        game_on = False



screen.exitonclick()