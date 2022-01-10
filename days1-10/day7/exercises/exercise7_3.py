# Exercise 7.3
# Build up to hangman game
# Note - in course, they use a boolean representation to whether the game is over or not
# The state of the game changes to True if "_" is NOT in display (list)

import random
word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
random_word = word_list[random.randint(0,2 )]

# Initialize list of 'blanks' to represent random_word
display = []
for letter in random_word:
    display.append("_")
print(display)

necessary_guesses = 0

while necessary_guesses != len(random_word):

    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a random letter! ").lower()

    # Loop through each position in random_word.
    # If letter exists in word, replace the matching '_' in display with guessed letter.

    for i in range(len(random_word)):
        if guess == random_word[i]:
            display[i] = guess
            necessary_guesses += 1
    print(display)

if necessary_guesses == len(random_word):
    print("You win!")
else:
    print("Something's wrong...")