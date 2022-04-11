# Udemy 100 Days of Code - Day 29 Project
# GUI Password Manager - WARNING, not for actual use
# !! Saves data to a plaintext txt file !!
# Takes user input for service, username, and password (or generates random password)
# Writes all inputs to txt file, prompts success dialogue box, and clears entry fields
# Also includes simple func to validate user has not left service or password entries blank

from email.mime.message import MIMEMessage
from tkinter import *
from tkinter.messagebox import askokcancel, showinfo
import random


GREEN = "#9bdeac"
FONT_NAME = "Arial"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
# random_generator func is from the course and not my own generator project for simplicity

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def random_generator():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))
    for char in range(nr_symbols):
        password_list += random.choice(symbols)
    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    return password
    

def password_generator():
    random_password = random_generator()
    password_entry.insert(0, random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def validate_entry(validation):
    if validation != "":
        return True

def add_password():
    website_input = website_entry.get()
    username_input = username_entry.get()
    password_input = password_entry.get()
    website_validation = validate_entry(website_input)
    password_validation = validate_entry(password_input)
    if website_validation != True or password_validation != True:
        showinfo("Blank Field!", "Please do not leave any fields blank!")
    else:
        user_save = askokcancel("OK to Save", f"Save data entered for {website_input}?")
        if user_save:
            with open("passwords.txt", "a") as master_list:
                master_list.write(f"{website_input} | {username_input} | {password_input}\n")
        website_entry.delete(0, END)
        username_entry.delete(0, END)
        password_entry.delete(0, END)
    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Labyrinth - Password manager")
window.config(padx=50, pady=50, bg=GREEN)

# Setting up canvas with logl image
canvas = Canvas(width=500, height=300, bg=GREEN, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(250, 150, image=logo_image)
canvas.grid(column=1, row=0)

# Setting up GUI labels, input boxes, and buttons
# Could write a label creating func to pinput for these three labels?
website_label = Label(text="Website:", font=(FONT_NAME, 10), bg=GREEN)
website_label.grid(column= 0, row= 1)
website_entry = Entry(width=37)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

username_label = Label(text="Username:", font=(FONT_NAME, 10), bg=GREEN, justify="center")
username_label.grid(column=0, row=2)
username_entry = Entry(width=37)
username_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:", font=(FONT_NAME, 10), bg=GREEN)
password_label.grid(column=0, row=3)
password_entry = Entry(width=28)
password_entry.grid(column=1, row=3)
password_button = Button(text="Generate", command=password_generator)
password_button.grid(column=2, row=3)


add_password_button = Button(text="Add Password", command=add_password)
add_password_button.grid(column=1, row=4)







window.mainloop()