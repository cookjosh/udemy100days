# More Day 26 exercises - dictionary comprehension
# formula:
# new_dict = {new_key:new_value for item in list if test}
import random

# Generate random score for each name in list names
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
random_scores = {name:random.randint(0, 100) for name in names}
print(random_scores)

# Take newly created dict and perform another dict comp
# Select students  with a passing score (> 60)
passing_students = {name:score for (name, score) in random_scores.items() if score >= 60}
print(passing_students)

# Split a string then create dict with word and length with dict comp
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
single_words = sentence.split()
result = {word:len(word) for word in single_words}
print(result)

# Convert a dict of celsius temps to a new dict of farenheit temps
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day:((temp * 9/5) + 32) for (day, temp) in weather_c.items()}

print(weather_f)