from shutil import move
from turtle import Screen, Turtle, Screen

tim = Turtle()

# Test module listener and action 'onkey'
"""
def move_forwards():
    tim.forward(10)


screen = Screen()
screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()
"""

# Challenge - Etch-a-Sketch Game

def move_forwards():
    tim.forward(10)

def right_turn():
    tim.right(5)
    
def left_turn():
    tim.left(5)

screen = Screen()
screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.onkey(key="Right", fun=right_turn)
screen.onkey(key="Left", fun=left_turn)
screen.exitonclick()