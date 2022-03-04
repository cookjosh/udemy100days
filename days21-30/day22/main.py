import turtle
from turtle import Screen, Turtle

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.listen()
turtle.title("Pong")
screen.setup(width=800, height=600)

right_paddle = Turtle()
right_paddle.penup()
right_paddle.shape("square")
right_paddle.turtlesize(stretch_wid=1, stretch_len=4)
right_paddle.fillcolor("white")
right_paddle.setx(350)
right_paddle.setheading(90)


left_paddle = Turtle()
left_paddle.penup()
left_paddle.shape("square")
left_paddle.turtlesize(stretch_wid=4, stretch_len=1)
left_paddle.fillcolor("white")
left_paddle.setx(-350)

def move_up():
    right_paddle.forward(50)

def move_down():
    right_paddle.backward(50)

screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")

game_on = True
while game_on == True:
    screen.update()


turtle.exitonclick()