# Day 26 Project - NATO Phonetic Alphabet converter
# Take CSV and create a dict of letter and NATO phonetic alphabet key:value pairs
# Take a user input word and return the corresponding NATO code for each letter in word

import pandas

alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter:row.code for (index, row) in alphabet_data.iterrows()} # create dict from CSV

user_word = [letter for letter in (input("Enter a word: ")).upper()]
code_list = [alphabet_dict.get(letter) for letter in user_word] # Create list of NATO codes per letter in input word
print(code_list)