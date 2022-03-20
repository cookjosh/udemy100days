#import csv

"""
with open("weather_data.csv", "r") as file:
    each_line = file.readline()
    while each_line:
        print(each_line)
        each_line = file.readline()


with open("weather_data.csv") as file:
    data = csv.reader(file)
    next(data)
    temperatures = []
    for row in data:
        temperatures.append(int(row[1]))
    print(temperatures)
"""

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])