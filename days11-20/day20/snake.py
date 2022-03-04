import turtle
from turtle import Turtle

class Snake:

    def __init__(self):
        self.create()

    def left_turn(self):
        self.left(90)
    
    def right_turn(self):
        self.right(90)

    def move(self):
        new_snake.forward(3)
        new_snake.heading()
        if new_snake.heading() == 0:
            turtle.onkeypress(left_turn, "Up")
            turtle.onkeypress(right_turn, "Down")
        elif new_snake.heading() == 90:
            turtle.onkeypress(left_turn, "Left")
            turtle.onkeypress(right_turn, "Right")
        elif new_snake.heading() == 180:
            turtle.onkeypress(right_turn, "Up")
            turtle.onkeypress(left_turn, "Down")
        else:
            turtle.onkeypress(left_turn, "Right")
            turtle.onkeypress(right_turn, "Left")

    def create(self):
        new_snake = Turtle()
        new_snake.penup()
        new_snake.shape("square")
        new_snake.shapesize(stretch_wid=1, stretch_len=6)
        new_snake.color("white")
        new_snake.speed("fastest")

    def move_up(self):
        if self.heading() == 0:
            left_turn()
        elif self.heading() == 180:
            right_turn()

    def move_down(self):
        if self.heading() == 0:
            right_turn()
        elif self.heading() == 180:
            left_turn()