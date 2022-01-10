# Exercise 7.1 - Check if user guess is in randomly selected word
# Build up to hangman game

import random
word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
random_word = word_list[random.randint(0,2 )]

# Initialize list of 'blanks' to represent random_word
display = []
for letter in random_word:
    display.append("_")
print(display)

# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a random letter! ").lower()

# Loop through each position in random_word.
# If letter exists in word, replace the matching '_' in display with guessed letter.

for i in range(len(random_word)):
    if guess == random_word[i]:
        display[i] = guess
        print("Correct guess")
    else:
        print("Wrong guess")

print(display)