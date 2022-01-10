# Exercise 7.1 - Check if user guess is in randomly selected word
# Build up to hangman game

import random
word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
random_word = word_list[random.randint(0,2 )]

# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a random letter! ").lower()

# Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in random_word:
    if guess == letter:
        print("Good guess!")
    else:
        print("Sorry!")