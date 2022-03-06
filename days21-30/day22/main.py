from operator import le
import paddle
import time
import turtle
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
from turtle import Screen, Turtle, right

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
turtle.title("Pong")
screen.setup(width=800, height=600)

right_paddle = Paddle(360)
left_paddle = Paddle(-360)
ball = Ball()
scoreboard = Scoreboard()



screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")
screen.listen()

game_on = True
while game_on == True:
    ball.move()
    screen.update()
    # detects upper and lower boundary hits
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.vertical_bounce()
    # detecs paddle contact
    if ball.distance(right_paddle) < 30 and ball.xcor() > 340 or ball.distance(left_paddle) < 30 and ball.xcor() > -340:
        ball.horizontal_bounce()
    # detect paddle miss right
    if ball.xcor() > 390:
        ball.reset_ball()
        time.sleep(1)
        scoreboard.clear()
        scoreboard.left_point()
    # detect paddle miss left
    if ball.xcor() < -390:
        ball.reset_ball()
        time.sleep(1)
        ball.setheading(-180)
        scoreboard.clear()
        scoreboard.right_point()


turtle.exitonclick()