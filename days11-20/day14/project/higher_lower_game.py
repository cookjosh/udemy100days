import random
from art import logo, vs
from game_data import data


def first_selection():
    selection_a = random.randint(0, (len(data) - 1))
    first_comparison = data[selection_a]
    return first_comparison

def next_selection():
    selection_b = random.randint(0, (len(data) - 1))
    second_comparison = data[selection_b]
    return second_comparison

def set_comparison():
    print(logo)
    print(f"Compare A: {first_selection_info['name']}, a {first_selection_info['description']}, from {first_selection_info['country']}")
    print(vs)
    print(f"Against B: {second_selection_info['name']}, a {second_selection_info['description']}, from {second_selection_info['country']}")


first_selection_info = first_selection()
second_selection_info = next_selection()
comparison_string = f"{first_selection_info['name']} has {first_selection_info['follower_count']} followers and {second_selection_info['name']} has {second_selection_info['follower_count']} followers."


if first_selection_info == second_selection_info:
    while first_selection_info == second_selection_info:
        second_selection_info = next_selection()

set_comparison()
user_response = input("Who has more followers? Type 'A' or 'B': ").lower()
if first_selection_info["follower_count"] > second_selection_info["follower_count"]:
    if user_response == "a":
        print("You win!")
        print(f"{comparison_string}")
    else:
        print("You lose!")
        print(f"{comparison_string}")
elif first_selection_info["follower_count"] < second_selection_info["follower_count"]:
    if user_response == "b":
        print("You win!")
        print(f"{comparison_string}")
    else:
        print("You lose!")
        print(f"{comparison_string}")
