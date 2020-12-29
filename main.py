import pandas
from turtle import Turtle, Screen

data = pandas.read_csv("50_states.csv")

screen = Screen()
screen.title("U.S States Game")

marker = Turtle()

img = "blank_states_img.gif"

screen.addshape(img)
marker.shape("blank_states_img.gif")

def get_mouse_click_coor(x,y):
    print(x,y)

score = 0

def guess_state():
    if score == 0:
        return "Name a state"
    else:
        return "Name another state"

user_guess = "Alabama"
    # screen.textinput(title=f"{score}/50", prompt=f"{guess_state}")

state_check = data[data.state == f"{user_guess.capitalize()}"]

print(str(state_check.state))
print(int(state_check.x))
print(int(state_check.y))

marker.goto(state_check.x,state_check.y)
marker.write("Test")


screen.onscreenclick(get_mouse_click_coor)
screen.mainloop()

screen.exitonclick()