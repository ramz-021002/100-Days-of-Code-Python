from turtle import Turtle, Screen
import random
my_toto = Turtle()
screen = Screen()
my_toto.pensize(10)
my_toto.speed(0)
# colors = [
#     "red",
#     "blue",
#     "green",
#     "purple",
#     "yellow",
#     "cyan",
#     "magenta",
#     "gold",
#     "lime"
# ]

directions = [0,90,180,270]
def random_color():
  red = random.randint(0,255) / 255.0
  green = random.randint(0,255) / 255.0
  blue = random.randint(0,255) / 255.0
  color = (red, green, blue)
  return color

def random_walk():
  for _ in range(2000):
    my_toto.color(random_color())
    my_toto.forward(30)
    my_toto.setheading(random.choice(directions))
    #my_toto.color(random.choice(colors))


random_walk()




screen.exitonclick()

# side = 3

# while 360/side >= 45:
#   my_toto.color(random.choice(colors))
#   for _ in range(side):
#     my_toto.forward(length)
#     my_toto.left(360 / side)
#   side += 1