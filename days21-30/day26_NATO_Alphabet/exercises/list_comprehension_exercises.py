# Day 26 Exercises - List comprehension

"""
# old method - creating new list with for loop
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)

# new method - using list comprehension to create new list from old
new_list_2 = [(n + 1) for n in numbers]
print(new_list_2)

# exercise with string
word = "exercise"
exercise_list = [letter for letter in word]
print(exercise_list)


# exercise with range
double_list = [n * 2 for n in range(1, 5)]
print(double_list)


# list comp with test
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) <= 4]
print(short_names)

cap_names = [name.upper() for name in names if len(name) >= 5]
print(cap_names)


# squared_numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)

# even numbers
even_numbers = [number for number in numbers if (number % 2) == 0]
print(even_numbers)
"""

# Overlap exercise
# create lists from numbers in both txt files
# create list with numbers that appear in both
with open("file1.txt") as file:
    first_list = file.read().splitlines()


with open("file2.txt") as file2:
    second_list = file2.read().splitlines()

compared_list = [int(number) for number in first_list if number in second_list]