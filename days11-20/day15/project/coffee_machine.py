# Udemy 100 Days of Code - Python: Day 15
# coffee_machine.py

from itertools import count
import sys



MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

money = {
    "quarter": .25,
    "dime": .10,
    "nickel": .05,
    "penny": .01,
}


resources = {
    "water": 500,
    "milk": 200,
    "coffee": 100,
    "money": 0.00,
}


def process_order():
    individual_ingredients = 0
    ingredient_number = 0
    for key in resources:
        if key in MENU[user_choice]["ingredients"]:
            ingredient_number += 1
            if resources[key] >= MENU[user_choice]["ingredients"][key]:
                individual_ingredients += 1
                resources[key] -= MENU[user_choice]["ingredients"][key]
                adding_coins = True
                while adding_coins == True:
                    if resources["money"] < MENU[user_choice]["cost"]:
                        print(f"A {user_choice} costs ${MENU[user_choice]['cost']}")
                        while resources["money"] < MENU[user_choice]["cost"]:
                            user_coin = input("Please insert money! Type 'quarter', 'dime', 'nickel', or 'penny'.\n").lower()
                            coin_amount = int(input("How many of that coin would you like to insert?\n"))
                            resources["money"] += (money[user_coin] * coin_amount)
                            print(resources["money"])
                    else:
                        adding_coins = False
            else:
                print(f"Sorry! Not enough {key}")
    if individual_ingredients == ingredient_number:
        print(f"Making your {user_choice}")
        print("Enjoy!")
        resources["money"] -= MENU[user_choice]["cost"]
        if resources["money"] > 0:
            change = "{:.2f}".format(resources["money"])
            resources["money"] = 0.00
            print(f"Here is ${change} in change!")
            print(resources)
        return resources
    else:
        return resources

machine_on = True
while machine_on == True:
    user_choice = input("What would you like? Espresso/Latte/Cappuccino: ").lower()
    if user_choice == "off":
        sys.exit()
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\n")
    elif user_choice == "espresso" or "latte" or "cappuccino":
        resources = process_order()
