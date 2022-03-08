import time
import turtle
from cars import Cars
from player import Player
from random import randint
from turtle import Screen, Turtle


screen = Screen()
screen.tracer(0)
turtle.title("Turtle Crossing")
screen.setup(width=1600, height=1200)

main_player = Player(-580)

demo_car = Cars(780)

screen.onkeypress(main_player.move_up, "Up")
screen.onkeypress(main_player.move_down, "Down")
screen.onkeypress(main_player.move_right, "Right")
screen.onkeypress(main_player.move_left, "Left")
screen.listen()

game_on = True
while game_on == True:
    time.sleep(0.1)
    screen.update()
    demo_car.move()
    # Need to figure out the collision detection...
    if demo_car.xcor() - main_player.xcor() <= 10 and demo_car.xcor() - main_player.xcor() >= -10:
        print("On same x plane")
        if demo_car.ycor() - main_player.ycor() > -5 and demo_car.ycor() - main_player.ycor() < 5:
            print("Game Over")
            time.sleep(5)










turtle.exitonclick()