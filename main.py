import pandas
from turtle import Turtle, Screen
import time

data = pandas.read_csv("50_states.csv")

screen = Screen()
screen.title("U.S States Game")
img = "blank_states_img.gif"

screen.addshape(img)
map = Turtle(img)

marker = Turtle()
marker.penup()
marker.color("black")

states = data.state.to_list()

def get_mouse_click_coor(x,y):
    print(x,y)

score = 0

def guess_state():
    if score == 0:
        return "Name a state"
    else:
        return "Name another state"

while score < 50:
    user_guess = screen.textinput(title=f"{score}/50", prompt=f"{guess_state()}")
    print(states)
    if user_guess.title() in states:
        print("True")
        print(user_guess.capitalize())
        state_check = data[data.state == f"{user_guess.title()}"]
        marker.goto(int(state_check.x), int(state_check.y))
        marker.write("Hello", align="center", font=("Courier", 12, "normal"))
        score += 1
        marker.goto(200, 200)
        marker.write(f"{score}/50", align="center", font=("Courier", 12, "normal"))
    print("False")
screen.mainloop()
screen.exitonclick()