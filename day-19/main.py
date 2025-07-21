from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
# def move_forward():
#     tim.forward(10)
#
# def move_backward():
#     tim.backward(10)
#
# def turn_left():
#     tim.left(10)
#
# def turn_right():
#     tim.right(10)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which tutle do you think will win the race, enter a color:")
color = ["red", "orange", "blue", "green", "yellow", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
turtles = []
for turtle_index in range(0, len(color)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y_position[turtle_index])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winner = turtle.pencolor()
            if user_bet == winner:
                print("You win!")
            else:
                print(f"You lose! {winner} is the winner!")
            # break
        else:
            random_distance = random.randint(0,20)
            turtle.forward(random_distance)



screen.exitonclick()



#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(key="space", fun=move_forward)
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d",fun=turn_right)
# screen.onkey(key="c", fun=clear)
