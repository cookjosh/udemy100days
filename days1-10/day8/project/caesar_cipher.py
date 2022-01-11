# Udemy 100 Days of Code - Python
# Day 8 Project - Caesar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
  decoded_list = [] # Improve by just iterating through string and not use lists
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
      if new_index > 25:
        new_index = new_index - 25
      encoded_list.append(alphabet[new_index])
  encoded_word = ""
  for i in encoded_list:
    encoded_word += i
  print(encoded_word)

def decrypt(text, shift): # Not complete, review if math is correct for handling IndexErrors
  decoded_list = [] # Improve by just iterating through string and not use lists
  encoded_list = []
  for i in text:
    encoded_list.append(i)
  for i in encoded_list:
    if i == " ":
      decoded_list.append(" ")
    elif i == "z":
      new_index = shift - 1
      decoded_list.append(alphabet[new_index])
    else:
      index = alphabet.index(i)
      new_index = index - shift
      if new_index < 0:
        new_index = new_index + 26
      decoded_list.append(alphabet[new_index])
  decoded_word = ""
  for i in decoded_list:
    decoded_word += i
  print(decoded_word)

if direction == "encode":
  encrypt(text, shift)