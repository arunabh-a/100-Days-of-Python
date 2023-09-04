from turtle import Turtle, Screen
MOVE_PACE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
POS_BORDER = 280
NEG_BORDER = -280
screen = Screen()
class Snake():
    
    def __init__(self):
        self.turtles = []
        self.orgn_xaxis = 0
        self.createSnake()
        self.head = self.turtles[0]

    def createSnake(self):
        for i in range (4):
            new_turt = Turtle(shape="square")
            new_turt.penup()
            new_turt.color("white")
            new_turt.goto(x = self.orgn_xaxis, y = 0)
            self.orgn_xaxis -= MOVE_PACE
            self.turtles.append(new_turt)

    def move(self):
        for turtle in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[turtle - 1].xcor()
            new_y = self.turtles[turtle - 1].ycor()
            self.turtles[turtle].goto(new_x, new_y)
        self.head.forward(MOVE_PACE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
            if self.head.heading() != LEFT:
                self.head.setheading(RIGHT)

    def returning(self):
        if self.head.xcor() > POS_BORDER:
            self.head.goto(x = NEG_BORDER, y = self.head.ycor())

        if self.head.xcor() < NEG_BORDER:
            self.head.goto(x = POS_BORDER, y = self.head.ycor())
        
        if self.head.ycor() > POS_BORDER:
            self.head.goto(x = self.head.xcor(), y = NEG_BORDER)
        
        if self.head.ycor() < NEG_BORDER:
            self.head.goto(x = self.head.xcor(), y = POS_BORDER)
