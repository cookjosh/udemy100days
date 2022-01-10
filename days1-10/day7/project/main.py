# Udemy 100 Days of Code - Python
# Day 7 - Hangman

import hangman_art
import random
from words_list import words_list

lives = 6
random_word = random.choice(words_list)

# Initialize list of 'blanks' to represent random_word
display = []
for letter in random_word:
    display.append("_")

print(hangman_art.logo)
print("")
print("Let's play... Word selected!\n")
print(display)
print("")

necessary_guesses = 0
already_guessed = []

while necessary_guesses != len(random_word):

    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a random letter: ").lower()
    if len(guess) > 1:
        print("Please only type 1 letter\n")
        continue
    
    if guess in already_guessed:
        print(f"You already guessed the letter {guess}!\n")
        continue
    already_guessed.append(guess)
    # Loop through each position in random_word.
    # If letter exists in word, replace the matching '_' in display with guessed letter.

    for i in range(len(random_word)):
        if guess == random_word[i]:
            display[i] = guess
            necessary_guesses += 1
    if guess not in random_word:
        print(f"The letter {guess} is not in the word. Guess again.\n")
        lives -= 1

    print(display)
    print(hangman_art.stages[lives])

    if lives == 0:
        print(f"The word was {random_word}!\n")
        print("Game over, you lose...")
        print(hangman_art.stages[0])
        break

if necessary_guesses == len(random_word):
    print("You win!")
