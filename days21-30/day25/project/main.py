# Day 25 Project - 50 States Game

import pandas
import turtle


screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()

data = pandas.read_csv("50_states.csv")
state_list = (data["state"]).tolist()
# state_coord = data[]
guessed_states = []

game_on = True
while game_on == True:
    user_answer = screen.textinput(title="Guess a State", prompt="Guess another state: ")
    if user_answer in state_list:
        print("Great guess!")
        guess_data = data[data.state == user_answer]
        x_coor = (int(guess_data.x))
        y_coor = (int(guess_data.y))
        turtle.goto(x_coor, y_coor)
        turtle.pendown()
        turtle.write(user_answer)
        turtle.penup()
        state_list.remove(user_answer)
        guessed_states.append(user_answer)

    else:
        print("Hmm...")
        print(f"{user_answer} is either spelled wrong or has already been guessed. Guess again!")


