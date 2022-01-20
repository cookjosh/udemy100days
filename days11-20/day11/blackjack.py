# Udemy 100 Days of Code - Day 11
# blackjack.py
import random
from os import system, name
from time import sleep

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

start_game = input("Would you like to play Blackjack? Y or N: ").lower()

while start_game == "y":
    print("Shuffling...")
    sleep(2)
    cards = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6,
    7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
    10, 10, 10, 10, 11, 11, 11, 11]

    game_over = False

    while game_over == False:
        dealer_hand = []
        user_hand = []

        dealer_first_card = cards[random.randint(0, (len(cards) - 1))]
        cards.remove(dealer_first_card)
        dealer_hand.append(dealer_first_card)
        user_first_card = cards[random.randint(0, (len(cards) - 1))]
        cards.remove(user_first_card)
        user_hand.append(user_first_card)
        dealer_second_card = cards[random.randint(0, (len(cards) - 1))]
        cards.remove(dealer_second_card)
        dealer_hand.append(dealer_second_card)
        user_second_card = cards[random.randint(0, (len(cards) - 1))]
        cards.remove(user_second_card)
        user_hand.append(user_second_card)
        print(user_hand)
        user_score = user_hand[0] + user_hand[1]
        dealer_score = dealer_hand[0] + dealer_hand[1]

        for i in range(len(user_hand)):
            if user_hand[i] == 11:
                if user_score > 21:
                    user_hand[i] = 1
            else:
                continue

        for i in range(len(dealer_hand)):
            if dealer_hand[i] == 11:
                if dealer_score > 21:
                    dealer_hand[i] = 1
            else:
                continue
                    
        user_score = user_hand[0] + user_hand[1]
        dealer_score = dealer_hand[0] + dealer_hand[1]

        if user_score > 21:
            print("Bust, you lose!")
            break # Should these be replaced with 'break' statements? These don't seem to work to break loop
        elif dealer_score > 21:
            print("Dealer busts, you win!")
            break

        print(f"Your cards: {user_hand}, current score: " + str(user_score))
        print(f"Dealers up card: {dealer_hand[1]}")

        if user_score == 21:
            if dealer_score == 21:
                print("Dealer has Blackjack! You lose.")
                break
            else:
                print("Blackjack! You win.")
                break

        while user_score <= 21:
            user_play = input("Would you like to hit or stay?: ").lower()
            if user_play == "hit":
                user_next_card = cards[random.randint(0, (len(cards) - 1))]
                cards.remove(user_next_card)
                user_hand.append(user_next_card)
                user_score += user_next_card
                print(f"Your updated hand: {user_hand}, and updated score: {user_score}")
                if user_score > 21:
                    break
            elif user_play == "stay":
                break

        if user_score > 21:
            print("Bust, you lose!")
            break

        while dealer_score <= 16:
            dealer_next_card = cards[random.randint(0, (len(cards) - 1))]
            cards.remove(dealer_next_card)
            dealer_hand.append(dealer_next_card)
            dealer_score += dealer_next_card
        
        if dealer_score > 21:
            print("Dealer busts! You win.")
            break

        print(f"Your updated hand: {user_hand}, and updated score: {user_score}")
        print(f"Dealers updated hand: {dealer_hand}, and updated score: {dealer_score}")

        # Compare scores - needs fix to end game early if dealer or user has already broken 21
        
        if user_score > dealer_score and user_score != 21:
            print("You win!")
            break
        elif user_score < dealer_score:
            print("Dealer wins!")
            break
        elif user_score == dealer_score:
            print("Tie, dealer wins!")
            break

    start_game = input("Would you like to play again? Y or N: ").lower()
    clear()