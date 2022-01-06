# Leap Year Calculator

year = int(input("What year would you like to check? "))

def leapyear(x):
  if x % 4 == 0:
    if x % 100 == 0 and x % 400 == 0:
      print("Leap Year!")
    else:
      print("Not a Leap Year!")
  else:
    print("Not a Leap Year!")

leapyear(year)  