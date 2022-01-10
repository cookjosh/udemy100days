# Exercise 7.4
# Build up to hangman game
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6
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
    if guess not in random_word:
        lives -= 1
    print(display)
    print(lives)
    print(stages[lives])
    if lives == 0:
        print("Game over, you lose...")
        print(stages[0])
        break

if necessary_guesses == len(random_word):
    print("You win!")
