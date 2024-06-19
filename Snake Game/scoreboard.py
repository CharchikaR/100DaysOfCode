from turtle import Turtle

SCORE_ALIGNMENT = "center"
SCORE_FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-20, 270)
        self.update_score()

    def update_score(self):
        self.write(arg=f"Score: {self.score}", align=SCORE_ALIGNMENT, font=SCORE_FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"Game Over", align=SCORE_ALIGNMENT, font=SCORE_FONT)
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()


