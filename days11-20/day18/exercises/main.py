import random
import turtle
from turtle import Turtle, Screen

timmy = Turtle()
"""
# Exercise 1 - draw a square
for x in range(0, 4):
    timmy.forward(100)
    timmy.right(90)

# Exercise 2 - dashed lines
for x in range(0, 20):
    timmy.pd()
    timmy.forward(10)
    timmy.pu()
    timmy.forward(10)


# Exercise 3
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


# Exercise 4 - random walk
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


# Exercise 5 - random walk with rand color tuple
turtle.colormode(255)
angles = [0, 90, 180, 270]
def random_walk():
    turtle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    timmy.color(turtle_color)
    heading = random.choice(angles)
    timmy.speed("fastest")
    timmy.seth(heading)
    timmy.forward(100)

for x in range(0, 101):
    random_walk()
"""

# Exercise 6 - Spirograph
timmy.speed("fastest")
turtle.colormode(255)

def spirograph_shift():
    timmy.circle(100)
    
heading = 0
for x in range(0, 101):
    turtle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    timmy.color(turtle_color)
    spirograph_shift()
    timmy.setheading(heading)
    heading += 3.6




screen = Screen()
screen.exitonclick()