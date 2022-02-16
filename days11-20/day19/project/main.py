import random
from turtle import Turtle, Screen

screen = Screen()

player_bet = (screen.textinput("Place your bet!", "Which color do you want to bet on:")).lower()

# Create function for making turtles
turtles = []
leo = Turtle()
leo.color("blue")
turtles.append(leo)
leo.shapesize(3, 3, 3)
leo.penup()
leo.setx(-925)
leo.sety(600)
raph = Turtle()
raph.color("red")
turtles.append(raph)
raph.shapesize(3, 3, 3)
raph.penup()
raph.setx(-925)
raph.sety(200)
don = Turtle()
don.color("purple")
turtles.append(don)
don.shapesize(3, 3, 3)
don.penup()
don.setx(-925)
don.sety(-200)
mike = Turtle()
mike.color("orange")
turtles.append(mike)
mike.shapesize(3, 3, 3)
mike.penup()
mike.setx(-925)
mike.sety(-600)

# Create conditions to stop movement while still on screen
# Also end when first turtle hits edge
for name in turtles:
    while name.xcor() <= 950:
        for name in turtles:
            name.forward(random.randint(1, 30))
            name.xcor()







screen.listen()
screen.exitonclick()