from turtle import Screen
import time
from snakefunc import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(score.game_over, "Escape")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()

    if snake.head.distance(food) < 13 :
        food.refresh()
        score.add_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.returning()





screen.exitonclick()