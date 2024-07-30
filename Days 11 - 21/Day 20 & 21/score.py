from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Tahoma', 12, 'bold')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.loopend = False
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def saveHighScore(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))
    
    def fetchHighScore(self):
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        return self.high_score

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.saveHighScore()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.fetchHighScore()}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_score()
    
    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.saveHighScore()
        self.goto(0,0)
        self.saveHighScore()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.loopend = True