""" 
Udemy 100 Days of Code (Python) - Day 3 Tip Calculator
1. Greet the user
2. Ask for total bill
3. Give 3 percentage tip options and take user input
4. Ask how many ways to split the bill
5. Calculate the payment for each member of the party.
"""

print('Welcome to the tip calculator!')
total = float(input("What was the total bill? "))
tip_percent = float(input("What percent tip would you like to leave? 15, 20, or 25: "))
total_tip = (tip_percent / 100) * total
new_total = (total + total_tip)
diner_number = float(input("How many people are splitting the bill? "))
individual_total = round((new_total / diner_number), 2)

print(f"Each person should pay: ${individual_total}")
