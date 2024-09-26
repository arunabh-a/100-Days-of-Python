# Etch-A-Sketch: Day 19 Project 1
import turtle as t

tim = t.Turtle()
screen = t.Screen()



def left():
    lefthead = tim.heading() + 10
    tim.setheading(lefthead)

def right():
    righthead = tim.heading() -  10
    tim.setheading(righthead)

def reverse():
    tim.backward(10)

def front():
    tim.forward(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key= "w", fun= front)
screen.onkey(key= "a", fun= left)
screen.onkey(key= "s", fun= reverse)
screen.onkey(key= "d", fun= right)
screen.onkey(key= "c", fun= clear)
screen.exitonclick()