# Day 27 - args exercise(s)

# *args
# Practice with unlimited arguments for a func
# Create a function using *args to sum inputs
# Note - the arguments get passed into the func as a tuple
from numpy import multiply


def add_all(*args):
    total = 0
    for n in args:
        total += n
    print(total)

add_all(1, 2, 3, 4)

# **kwargs
# practice with keyword arguments for a func
# Note - the keyword and value get passed to func as a dict
def calculate(n, **kwargs):
    n += kwargs["add"]
    print(n)
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=5, multiply=10)

# **kwargs can be used when creating classes
class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        # self.make = kwargs.get("make") - using this method would not return an error if a "make" was not passed into the func call
        # The above would just return a None type for self.make
        self.model = kwargs["model"]

my_car = Car(make="Honda", model="Civic")
print(my_car.make)
print(my_car.model)

