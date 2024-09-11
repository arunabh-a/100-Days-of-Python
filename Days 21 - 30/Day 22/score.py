from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, "center", "center", ("Tahoma", 65, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, "center", "center", ("Tahoma", 65, "normal"))

    def score_update(self, lospad):
        if lospad == "right":
            self.l_score += 1
        elif lospad == "left":
            self.r_score += 1
        self.scoreboard()
