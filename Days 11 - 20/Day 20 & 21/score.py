from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Tahoma', 12, 'bold')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.loopend = False
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.loopend = True

    def update_score(self):
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()
    