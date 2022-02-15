import colorgram
import random
import turtle
from turtle import Turtle, Screen

# extract colors with colorgram
colors = colorgram.extract("dots.jpg", 10)

color_list = []
index = 0
for color in colors:
    current_color = colors[index]
    rgb = current_color.rgb
    color_list.append((rgb.r, rgb.g, rgb.b))
    index += 1

# Turtle things
turtle.colormode(255)
timmy = Turtle()


def draw_dots():
    for x in range(0, 11):
        rgb = random.randint(0, 9)
        timmy.pendown()
        timmy.dot(50, color_list[rgb])
        timmy.penup()
        timmy.forward(100)
    timmy.dot(50, color_list[rgb])

def right_turn():
    timmy.right(90)
    timmy.forward(100)
    timmy.right(90)

def left_turn():
    timmy.left(90)
    timmy.forward(100)
    timmy.left(90)

def odd_rows():
    draw_dots()
    right_turn()

def even_rows():
    draw_dots()
    left_turn()

timmy.speed("fastest")
timmy.penup()
timmy.setheading(45)
timmy.forward(800)
timmy.setheading(180)

for x in range(0, 6):
    even_rows()
    odd_rows()
    



screen = Screen()
screen.exitonclick()
