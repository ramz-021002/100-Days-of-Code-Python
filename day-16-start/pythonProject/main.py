# import turtle
# import another_module
# print(another_module.another_variable)
#
# timmy = turtle.Turtle()
# screen = turtle.Screen()
# timmy.shape("circle")
# timmy.color("DarkBlue")
#
# timmy.forward(1)
# timmy.circle(100)
#
# screen.exitonclick()

import prettytable
from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Sqirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])
table.align = 'l'

print(table)