import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

lucky_winner = names[random.randint(0, (len(names)) - 1)]
print(f"{lucky_winner} is going to buy the meal today!")