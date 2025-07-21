from turtle import Turtle, Screen
import random
my_toto = Turtle()
screen = Screen()
angle = 5
my_toto.speed(0)
my_toto.pensize(1)

def random_color():
  red = random.randint(0,255) / 255.0
  green = random.randint(0,255) / 255.0
  blue = random.randint(0,255) / 255.0
  color = (red, green, blue)
  return color

for _ in range(int(360/angle)):
    my_toto.color(random_color())
    my_toto.circle(150)
    my_toto.setheading(my_toto.heading() + angle)


screen.exitonclick()