import random
from turtle import Turtle, Screen

timmy = Turtle()
"""
# Challenge 1 - draw a square
for x in range(0, 4):
    timmy.forward(100)
    timmy.right(90)

# Challenge 2 - dashed lines
for x in range(0, 20):
    timmy.pd()
    timmy.forward(10)
    timmy.pu()
    timmy.forward(10)


# Challenge 3
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def draw_shapes(sides):
    turtle_color = random.choice(colors)
    timmy.color(turtle_color)
    for x in range(sides):
        angle = 360 / sides
        timmy.forward(100)
        timmy.right(angle)

for x in range(3, 11):
    draw_shapes(x)
"""

# Challenge 4
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
angles = [0, 90, 180, 270]
def random_walk():
    turtle_color = random.choice(colors)
    timmy.color(turtle_color)
    heading = random.choice(angles)
    timmy.speed("fastest")
    timmy.seth(heading)
    timmy.forward(100)

for x in range(0, 101):
    random_walk()


screen = Screen()
screen.exitonclick()