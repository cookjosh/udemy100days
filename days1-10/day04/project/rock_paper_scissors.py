# Day 4 Project - Rock, Paper, Scissors Game
# Take user input for a choice, randomize computer choice, and compare the two for outcome.

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
print("----- Your Choice -----")
if user_choice == 0:
  print(rock)
elif user_choice == 1:
  print(paper)
elif user_choice == 2:
  print(scissors)

print("----- Computer's Choice -----")

computer_choice = random.randint(0, 2)
if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
elif computer_choice == 2:
  print(scissors)

choices = [user_choice, computer_choice]

print("----- Decision -----")

if choices[0] == 0:
  if choices[1] == 0:
    print("It's a tie!")
  elif choices[1] == 1:
    print("Computer wins!")
  elif choices[1] == 2:
    print("You win!")
elif choices[0] == 1:
  if choices[1] == 0:
    print("You win!")
  elif choices[1] == 1:
    print("It's a tie!")
  elif choices[1] == 2:
    print("Computer wins!")
elif choices[0] == 2:
  if choices[1] == 0:
    print("Computer wins!")
  elif choices[1] == 1:
    print("You win!")
  elif choices[1] == 2:
    print("It's a tie!")