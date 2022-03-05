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
        self.x_move = 0.05
        self.y_move = 0.05

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1
