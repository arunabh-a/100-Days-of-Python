from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_pace = 10
        self.y_pace = 10
    
    def move_it(self):
        x_cor = self.xcor() + self.x_pace
        y_cor = self.ycor() + self.y_pace
        self.goto(x_cor, y_cor)
        

    def reflect(self, axis):
        if axis == "y":
            self.y_pace *= -1
        elif axis == "x":
            self.x_pace *= -1