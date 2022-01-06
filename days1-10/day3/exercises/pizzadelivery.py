# Python Pizza Deliveries

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")

total = 0.00
if size == "S":
  if extra_cheese == "Y":
    total += 16
  else:
    total += 15
elif size == "M":
  if add_pepperoni == "Y" and extra_cheese == "Y":
    total += 24
  elif add_pepperoni == "N" and extra_cheese == "Y":
    total += 21
  elif add_pepperoni == "Y" and extra_cheese == "N":
    total += 23
  else:
    total += 20
elif size == "L":
  if add_pepperoni == "Y" and extra_cheese == "Y":
    total += 29
  elif add_pepperoni == "N" and extra_cheese == "Y":
    total += 26
  elif add_pepperoni == "Y" and extra_cheese == "N":
    total += 28
  else:
    total += 25

formatted_total = (round(float(total), 2))
print(f'${formatted_total}')