import pandas
from turtle import Turtle, Screen

data = pandas.read_csv("50_states.csv")

screen = Screen()
screen.title("U.S States Game")
img = "blank_states_img.gif"

screen.addshape(img)
map = Turtle(img)

marker = Turtle()
marker.penup()
marker.hideturtle()


def get_mouse_click_coor(x,y):
    print(x,y)

score = 0

def guess_state():
    if score == 0:
        return "Name a state"
    else:
        return "Name another state"

user_guess = screen.textinput(title=f"{score}/50", prompt=f"{guess_state}")

state_check = data[data.state == f"{user_guess.capitalize()}"]

print(int(state_check.x))
print(int(state_check.y))

marker.goto(int(state_check.x),int(state_check.y))
marker.write("Hello", align="center", font=("Courier", 12, "normal"))

screen.onscreenclick(get_mouse_click_coor)
screen.mainloop()

screen.exitonclick()