# Day 5 Project - Password Generator
# password_generator.py
# Code below until separator is started code from the course
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#-----Code below this is mine-----#

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
'''
final_password = ""
for n in range(1, (nr_letters + 1)):
  randomizer = random.randint(0, (len(letters) - 1))
  final_password += letters[randomizer]

for n in range(1, (nr_numbers + 1)):
  randomizer = random.randint(0, (len(numbers) - 1))
  final_password += numbers[randomizer]

for n in range(1, (nr_symbols + 1)):
  randomizer = random.randint(0, (len(symbols) - 1))
  final_password += symbols[randomizer]

print(final_password)
'''
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = []
for n in range(1, (nr_letters + 1)):
  randomizer = random.randint(0, (len(letters) - 1))
  password.append(letters[randomizer])

for n in range(1, (nr_numbers + 1)):
  randomizer = random.randint(0, (len(numbers) - 1))
  password.append(numbers[randomizer])

for n in range(1, (nr_symbols + 1)):
  randomizer = random.randint(0, (len(symbols) - 1))
  password.append(symbols[randomizer])

random.shuffle(password)
final_password = ""

for i in password:
  final_password += str(i)
print(f"Your autogenerated password is: {final_password}")