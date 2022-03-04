import turtle
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, xcoord):
        super().__init__()
        self.penup()
        self.setx(xcoord)
        self.shape("square")
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.fillcolor("white")
        self.setheading(90)

    def move_up(self):
        self.forward(50)

    def move_down(self):
        self.backward(50)