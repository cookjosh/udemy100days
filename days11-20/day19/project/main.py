import random
from turtle import Turtle, Screen

screen = Screen()

player_bet = (screen.textinput("Place your bet!", "Which color do you want to bet on:")).lower()
turtles = []
color_list = ["blue", "red", "purple", "orange"]

def make_turtle(name):
    name = Turtle()
    turtles.append(name)
    name.shapesize(3, 3, 3)
    name.penup()
    name.speed("fast")
    return name

for x in range(0, 4):
    turtle_name = input("What's your turtle's name? (max 4!): ")
    turtle = make_turtle(turtle_name)
    turtle.color(color_list[x])
    if x == 0:
        turtle.setx(-925)
        turtle.sety(600)
    elif x == 1:
        turtle.setx(-925)
        turtle.sety(200)
    elif x == 2:
        turtle.setx(-925)
        turtle.sety(-200)
    elif x == 3:
        turtle.setx(-925)
        turtle.sety(-600)


ending_order = []
for name in turtles:
    while name.xcor() <= 950:
        if name.xcor() == 950:
            ending_order.append(name)
            break
        else:   
            for name in turtles:
                forward_spaces = random.randint(1, 30)
                if name.xcor() + forward_spaces > 950:
                    forward_spaces = 950 - name.xcor()
                    ending_order.append(name)
                    break
                name.forward(forward_spaces)
                name.xcor()

winning_turtle = ending_order[0]
winning_color = winning_turtle.color()

if player_bet == winning_color[1]:
    print(f"Congrats! {player_bet} won. You won your bet!")
else:
    print(f"Sorry...{winning_color[1]} won. You lost your bet!")
        

screen.listen()
screen.exitonclick()