from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.loopend = False
        self.x_pace = 10
        self.y_pace = 10
        self.move_speed = 0.1
    

    def move_it(self, turn):
        if turn == "r":
            x_cor = self.xcor() + self.x_pace
            y_cor = self.ycor() + self.y_pace

        elif turn == "l":
            x_cor = self.xcor() + self.x_pace
            y_cor = self.ycor() + self.y_pace
        self.goto(x_cor, y_cor)
        

    def reflect(self, axis):
        if axis == "y":
            self.y_pace *= -1
        elif axis == "x":
            self.x_pace *= -1
            self.move_speed *= 0.9
    
    def missed(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.reflect("x")
    
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER", align='center', font=('Tahoma', 42, 'bold'))
        self.loopend = True