from turtle import Screen, Turtle
import time
from snakefunc import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_over = False

while game_over == False:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    # if turtles[0].xcor() > 270:
    #     game_over = True




screen.exitonclick()