import random
from turtle import Turtle

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

class Cars(Turtle):
    def __init__(self):
        self.car_list = []

    def create_car(self, xcoord):
        random_chance = random.randint(1, 6) # random chance method borrowed from course
        if random_chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.setx(xcoord)
            new_car.sety(random.randint(-450, 500))
            new_car.shape("square")
            new_car.turtlesize(stretch_wid=2, stretch_len=8)
            new_car.setheading(180)
            new_car.color(random.choice(colors))
            new_car.x_move = -50
            new_car.speed("slowest")
            self.car_list.append(new_car)

    def move(self):
        for car in self.car_list:
            car.forward(50)
