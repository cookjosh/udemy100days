import time
import turtle
from cars import Cars
from player import Player
from random import randint
from scoreboard import Scoreboard
from turtle import Screen, Turtle


screen = Screen()
screen.tracer(0)
turtle.title("Turtle Crossing")
screen.setup(width=1600, height=1200)

main_player = Player(-580)
car_class = Cars()
scoreboard = Scoreboard()

screen.onkeypress(main_player.move_up, "Up")
screen.onkeypress(main_player.move_down, "Down")
screen.onkeypress(main_player.move_right, "Right")
screen.onkeypress(main_player.move_left, "Left")
screen.listen()

game_on = True
while game_on == True:
    time.sleep(0.1)
    screen.update()
    car_class.create_car(800)
    # Need to figure out the collision detection...
    car_class.move()
    if main_player.ycor() >= 590:
            print("You win!")
            main_player.reset_player()
            time.sleep(2)
            scoreboard.level_up()
    for car in car_class.car_list:
        if car.xcor() - main_player.xcor() <= 30 and car.xcor() - main_player.xcor() >= -30:
            print("xcor " + str(car.xcor() - main_player.xcor()))
            if car.ycor() - main_player.ycor() > -45 and car.ycor() - main_player.ycor() < 45:
                scoreboard.game_over()
                time.sleep(5)
    










turtle.exitonclick()