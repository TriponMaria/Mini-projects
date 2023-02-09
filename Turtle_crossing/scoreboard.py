from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.score()

    def score(self):
        self.clear()
        self.penup()
        self.goto(-280, 260)
        self.hideturtle()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.hideturtle()
        self.write(f"GAME OVER", align="center", font=FONT)

