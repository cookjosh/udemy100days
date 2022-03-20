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
"""
#print(data)
#print(data["temp"])

data_dict = data.to_dict()

temp_list = data["temp"].to_list()

# Get average temperature
average_temp = sum(temp_list) / len(temp_list)
print(average_temp)
# OR using Pandas
print(data["temp"].mean())

# Print largest number in temp series
print(data["temp"].nlargest(1))
# OR
print(data["temp"].max()) # Cleaner

# Selecting columns - two methods
print(data["temp"])
print(data.temp)


# Getting data from rows
print(data[data.temp == data.temp.max()])

# Convert a particular day's temperature to Farenheit
monday_data = data[data.day == "Monday"]
monday_farenheit = (int(monday_data.temp) * 1.8) + 32
print(monday_farenheit)
"""

# Create DataFrame from scratch - example data
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)