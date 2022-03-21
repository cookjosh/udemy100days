# Day 25 Squirrel Exercise
# Take a large csv file and condense one series to a new DataFrame
# Specifically count total occurrences of each fur color

from turtle import color
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color_list = data["Primary Fur Color"] # Series in question
color_dict = (color_list.value_counts().to_dict()) # Counts occurrence of each value in Series and creates dict
colors = []
color_counts = []

for key in color_dict:
    colors.append(key)
    color_counts.append(color_dict[key])

data_dict = {
    "Fur Colors": colors,
    "Totals": color_counts
}

final_data = pandas.DataFrame(data_dict)
