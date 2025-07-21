import colorgram
import random

def random_color():
    red = random.randint(0,255) / 255.0
    green = random.randint(0,255) / 255.0
    blue = random.randint(0,255) / 255.0
    color = colorgram.Color(red, green, blue,10)
    print(color)

random_color()