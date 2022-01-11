# Exercise 8.2 - Prime number checker
# Take user input and check if prime number
# Works but solution in course is cleaner/only checks range(2, number) for modulus == 0
# This makes sense we already expect 1 and number would be True for the above

def prime_checker(number):
    count = 0
    for n in range(1, number + 1):
        if number % n == 0:
            count += 1
    if count == 2:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)