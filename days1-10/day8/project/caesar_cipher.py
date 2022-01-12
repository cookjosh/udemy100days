# Udemy 100 Days of Code - Python
# Day 8 Project - Caesar Cipher

from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

user_response = "yes"
while user_response == "yes":

    print(f"{logo}\n")

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Leaving the below in code as reference to my original approach that did not incorporate a duplicate alphabet to deal with IndexErrors for range
    '''
    def encrypt(text, shift):
    decoded_list = [] # Original solution which did not incorporate a duplication of alphabet in list
    encoded_list = []
    for i in text:
        decoded_list.append(i)
    for i in decoded_list:
        if i == " ":
        encoded_list.append(" ")
        elif i == "z":
        new_index = shift - 1
        encoded_list.append(alphabet[new_index])
        else:
        index = alphabet.index(i)
        new_index = index + shift
        encoded_list.append(alphabet[new_index])
    encoded_word = ""
    for i in encoded_list:
        encoded_word += i
    print(encoded_word)
    '''

    def caesar(direction, text, shift):
        new_word = ""
        for i in text:
            if type(i) == "int" or i == " ":
                new_word += i
                continue
            else:
                old_index = alphabet.index(i)
                if direction == "encode":
                    new_index = old_index + shift
                elif direction == "decode":
                    new_index = old_index - shift
            new_word += alphabet[new_index]
        print(new_word)

    caesar(direction, text, shift)

    user_response = (input("Would you like to go again? Type 'yes' or 'no': \n")).lower()

