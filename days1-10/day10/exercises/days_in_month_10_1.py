# Exercise 10.1 - Days in Month
# Outputs days in a given month
# Checks whether or not given year is a leap year first

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

# My code below
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  leap_year = is_leap(year)
  if month == 2:
    if leap_year == True:
      return 29
    else:
      return 28
  else:
    return month_days[month - 1]

  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)