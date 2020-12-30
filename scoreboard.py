from turtle import Turtle
import pandas


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = len(pandas.read_csv("guessed_states.csv"))

    def update_scoreboard(self):
        self.clear()
        self.goto(200, 260)
        self.score += 1
        self.write(f"Score is {self.score}/50", align="center", font=("Courier", 20, "normal"))

    def reset_score(self):
        self.clear()
        self.score = 0