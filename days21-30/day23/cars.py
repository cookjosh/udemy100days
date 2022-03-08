from random import randint
from turtle import Turtle

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
color_index = randint(0, 5)

class Cars(Turtle):
    def __init__(self, xcoord):
        super().__init__()
        self.penup()
        self.setx(xcoord)
        self.sety(randint(-580, 580))
        self.shape("square")
        self.turtlesize(stretch_wid=2, stretch_len=8)
        self.setheading(180)
        self.color(colors[color_index])
        self.x_move = -50
        self.speed("slowest")


    def move(self):
        new_x = self.xcor() + self.x_move
        self.goto(new_x, self.ycor())
