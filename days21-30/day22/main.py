from operator import le
import paddle
import turtle
from ball import Ball
from paddle import Paddle
from turtle import Screen, Turtle

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
turtle.title("Pong")
screen.setup(width=800, height=600)

right_paddle = Paddle(350)
left_paddle = Paddle(-350)
ball = Ball()



screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")
screen.listen()

game_on = True
while game_on == True:
    ball.move(0, 0)
    screen.update()



turtle.exitonclick()