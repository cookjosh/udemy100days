# Udemy 100 Days of Code - Python
# Day 9 Project - blind_auction.py

import os
from art import logo


def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

print(logo)
print("Welcome to The Secret Auction Program")

additional_bidder = "yes"
master_list = []

while additional_bidder == "yes":
  current_bid = {}
  bidder_name = input("Please enter your name: ")
  bid_amount = int(input("How much would you like to bid? $"))
  current_bid["Name"] = bidder_name
  current_bid["Bid"] = bid_amount
  master_list.append(current_bid)
  additional_bidder = (input("Are there any other bidders? Yes or no? ")).lower()
  screen_clear()

sorted_list = sorted(master_list, key=lambda d: d["Bid"], reverse=True)
highest_bidder = sorted_list[0]["Name"]
highest_bid = sorted_list[0]["Bid"]

print(f"{highest_bidder} has the highest bid at ${highest_bid}!")
