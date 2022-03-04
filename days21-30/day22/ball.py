import turtle
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.turtlesize(stretch_wid=0.5, stretch_len=0.5)
        self.fillcolor("white")
        self.speed("slowest")

    def move(self, xcoord, ycoord):
        new_x = self.xcor() + 0.03
        new_y = self.ycor() + 0.03
        self.goto(new_x, new_y)