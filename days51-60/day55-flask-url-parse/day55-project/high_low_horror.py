# Day 55 project - High Low game on browser
# Create a server that accepts an index route and user-input integer route
# Parse the URl and use the user input as a guess against a random number from 0, 9
# Return specific text and gif based on whether guess is high, low, or on


import random
from flask import Flask

app = Flask(__name__)


# Decorators
def header_decorator(function):
    def header_wrapper(user_guess):
        random_color = random.choice(["black", "red", "green"])
        return f"<h1 style=color:{random_color};>{function(user_guess)}</h1>"
    header_wrapper.__name__ = function.__name__
    return header_wrapper


# Routes
@app.route("/")
def homepage():
    return "<h1>Guess a number between 0 and 9!</h1>" \
        "<br>" \
        "<img src='https://media.giphy.com/media/3o7TKSxdQJIoiRXHl6/giphy.gif' width=400>"

@app.route("/<int:user_guess>")
@header_decorator
def guess(user_guess):
    random_number = random.randrange(0, 9)
    if user_guess < random_number:
        return "Too low!" \
            "<br>" \
            "<img src='https://media.giphy.com/media/PuDvddCsN3B84/giphy.gif', width=400>"
    if user_guess > random_number:
        return "Too high!" \
            "<br>" \
            "<img src='https://media.giphy.com/media/OJF9voKrfdLDG/giphy.gif', width=400>"
    if user_guess == random_number:
        return "Lucky guess..." \
            "<br>" \
            "<img src='https://media.giphy.com/media/l0K4bRk3PeJhiyb6M/giphy.gif', width=400>"


if __name__ == "__main__":
    app.run(debug=True)