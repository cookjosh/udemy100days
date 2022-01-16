# Udemy 100 Days of Code - Day 10 Project
# Calculator
import operator


def calculation(number_one):
  print("+\n-\n*\n/")
  choosen_operation = input("Pick an operator: ")
  number_two = int(input("What's the next number?: "))

  operatorlookup = {
      '+': operator.add,
      '-': operator.sub,
      '*': operator.mul,
      '/': operator.truediv
  }

  used_operation = operatorlookup.get(choosen_operation)
  result = used_operation(number_one, number_two)
  print(f"{number_one} {choosen_operation} {number_two} = {result}")
  continue_calculating = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
  if continue_calculating == "y":
    number_one = result
    return number_one
  else:
    return continue_calculating

number_one = int(input("What's the first number?: "))

continue_calculating = "y"

while continue_calculating == "y":
  calculation(number_one)