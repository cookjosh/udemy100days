# Udemy 100 Days of Code - Day 11
# blackjack.py
import random

cards = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6,
7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
10, 10, 10, 10, 11, 11, 11, 11]

dealer_pair = []
user_pair = []

dealer_first_card = cards[random.randint(0, (len(cards) - 1))]
cards.remove(dealer_first_card)
dealer_pair.append(dealer_first_card)
user_first_card = cards[random.randint(0, (len(cards) - 1))]
cards.remove(user_first_card)
user_pair.append(user_first_card)
dealer_second_card = cards[random.randint(0, (len(cards) - 1))]
cards.remove(dealer_second_card)
dealer_pair.append(dealer_second_card)
user_second_card = cards[random.randint(0, (len(cards) - 1))]
cards.remove(user_second_card)
user_pair.append(user_second_card)
print(user_pair)
user_score = user_pair[0] + user_pair[1]

for i in range(len(user_pair)):
    if user_pair[i] == 11:
        if user_score > 21:
            user_pair[i] = 1
    else:
        continue
            
user_score = user_pair[0] + user_pair[1]

print(f"Your cards: {user_pair}, current score: " + str(user_score))