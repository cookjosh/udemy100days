# Udemy 100 Days of Code - Day 12
# number_guess.py

import random
from art import logo

def easy_mode():
    lives = 10
    while lives != 0:
        user_guess = int(input("What's your guess?: "))
        if user_guess == winning_number:
            print(f"You win! The hidden number was {winning_number}")
            break
        elif user_guess != winning_number:
            if user_guess > winning_number:
                print("Too high! Sorry, guess again!")
                lives -= 1
                print(f"You have {lives} lives remaining!")
            elif user_guess < winning_number:
                print("Too low! Sorry, guess again!")
                lives -= 1
                print(f"You have {lives} lives remaining!")
    if lives == 0:
        print("You lost! Would you like to play again?")
    play_again = input("Type 'yes' or 'no': ").lower()
    return play_again

def hard_mode():
    lives = 5
    while lives != 0:
        user_guess = int(input("What's your guess?: "))
        if user_guess == winning_number:
            print(f"You win! The hidden number was {winning_number}")
            break
        elif user_guess != winning_number:
            if user_guess > winning_number:
                print("Too high! Sorry, guess again!")
                lives -= 1
                print(f"You have {lives} lives remaining!")
            elif user_guess < winning_number:
                print("Too low! Sorry, guess again!")
                lives -= 1
                print(f"You have {lives} lives remaining!")
    if lives == 0:
        print("You lost! Would you like to play again?")
    play_again = input("Type 'yes' or 'no': ").lower()
    return play_again



print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 0 and 100.")
game_mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

game_on = "yes"
while game_on == "yes":
    winning_number = random.randint(0, 100)
    print(winning_number)
    if game_mode == "easy":
        game_on = easy_mode()
    elif game_mode == "hard":
        game_on = hard_mode()

