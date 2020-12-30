import pandas
from turtle import Turtle, Screen
from scoreboard import Scoreboard

data = pandas.read_csv("50_states.csv")

screen = Screen()

screen.title("U.S States Game")
img = "blank_states_img.gif"

screen.addshape(img)
map = Turtle(img)
screen.tracer(0)

marker = Turtle()
marker.penup()
marker.color("black")
marker.hideturtle()

score_marker = Turtle()
score_marker.penup()
score_marker.color("black")
score_marker.hideturtle()

states = data.state.to_list()

def get_mouse_click_coor(x,y):
    print(x,y)

scoreboard = Scoreboard()
score = scoreboard.score

def guess_state():
    if scoreboard.score == 0:
        return "Name a state"
    else:
        return "Name another state"

guessed_states = []

#TODO Clear marker scoreboard
while scoreboard.score < 50:
    user_guess = screen.textinput(title=f"{scoreboard.score}/50", prompt=f"{guess_state()}")
    if user_guess == "exit":
        break
    if user_guess.title() in states and user_guess.title() not in guessed_states:
        print(user_guess.capitalize())
        guessed_states.append(user_guess.title())
        state_check = data[data.state == f"{user_guess.title()}"]
        set_difference = set(guessed_states) - set(states)
        list_difference = list(set_difference)
        print(f"states = {states}")
        print(f"Guessed States ={guessed_states}")
        print(f"List differences = {list_difference}")
        marker.goto(int(state_check.x), int(state_check.y))
        marker.write(f"{user_guess.title()}", align="center", font=("Courier", 12, "normal"))
        scoreboard.update_scoreboard()

