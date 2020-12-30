from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(200, 260)
        self.score += 1
        self.write(f"Score is {self.score}/50", align="center", font=("Courier", 20, "normal"))

    def reset_score(self):
        self.clear()
        self.score = 0