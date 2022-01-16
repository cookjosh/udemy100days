# Coinflip Game
# Udemy 100 Days of Code - Python; Day 4 exercise 1
# 1 = Heads, 0 = Tails

import random

coin_flip = random.randint(0, 1)

if coin_flip == 1:
    print("Heads")
else:
    print("Tails")