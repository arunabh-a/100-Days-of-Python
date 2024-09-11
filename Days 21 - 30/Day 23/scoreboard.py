from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.loopend = False
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-220, 250)
        self.level_update()


    def level_update(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}",align="center", font=FONT)


    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER", align='center', font=('Tahoma', 42, 'bold'))
        self.loopend = True
