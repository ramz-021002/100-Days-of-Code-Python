from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.title("U.S States Game")
turtle = Turtle()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coordinates(x,y):
#     print(x,y)
#
# turtle.onclick(get_mouse_click_coordinates)
data = pd.read_csv("50_states.csv")
states = data["state"].tolist()
guessed_states = []

def write_state_names(name):
    t = Turtle()
    t.hideturtle()
    t.penup()
    x_pos = data[data["state"] == name].x.item()
    y_pos = data[data["state"] == name].y.item()
    t.goto(x_pos, y_pos)
    t.pendown()
    t.write(name, align="center", font=("Arial", 10, "normal"))

def update_score():
    score = Turtle()
    score.penup()
    score.hideturtle()

def generate_report():

    states_missed = [state for state in states if state not in guessed_states]

    # for state in states:
    #     if state not in guessed_states:
    #         states_missed.append(state)
    df = pd.DataFrame(states_missed)
    df.to_csv("missed_states.csv")

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="Enter your guess for a state name: ").title()
    if answer_state == "Exit":
        generate_report()
        break

    if answer_state in states:
        write_state_names(answer_state)
        guessed_states.append(answer_state)

