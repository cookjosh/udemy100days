# Day 25 Project - 50 States Game
# Given a blank map of the US, user enters in guesses of states
# A correct guess should write the state name roughly in the vicinity of the state on the map
# Correct guesses are removed from original list and stored in a guessed list
# Current issue is scale of map to window doesn't allow for accurate state placements

import pandas
import turtle


screen = turtle.Screen()
screen.setup(width=1000, height=800)
screen.screensize(1000, 800)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state = turtle.Turtle()
state.hideturtle()
state.penup()

data = pandas.read_csv("50_states.csv")
state_list = (data["state"]).tolist()
guessed_states = []

correct_guesses = 0
game_on = True
while game_on == True:
    user_answer = screen.textinput(title=f"{correct_guesses}/50 Guess a State", prompt="Guess another state: ")
    if user_answer in state_list:
        correct_guesses += 1
        print("Great guess!")
        guess_data = data[data.state == user_answer]
        state.goto(int(guess_data.x), int(guess_data.y))
        state.write(user_answer)
        state_list.remove(user_answer)
        guessed_states.append(user_answer)
        state.home()
        if correct_guesses == 50: # This could be eliminated by replacing while loop to len(guessed_states) < 50
            game_on = False
    else:
        print("Hmm...")
        print(f"{user_answer} is either spelled wrong or has already been guessed. Guess again!")


