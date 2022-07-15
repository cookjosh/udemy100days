# Day 55 exercise to practice creating decorators that accept arguments
# Create a decorator function that takes a functions inputs
# Prints the name of the function called
# Prints all given arguments

# Decorator
def logging_decorator(function):
    def wrapper_function(*args, **kwargs):
        print(f"The name of the function is {function.__name__}")
        for i in range(len(args)):
            print(f"Argument #{i + 1} is {args[i]}")
    return wrapper_function

# Test function
@logging_decorator
def test_function(a, b, c):
    return test_function

test_function("hi", "bye")
        