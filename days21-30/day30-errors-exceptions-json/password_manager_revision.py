# Udemy 100 Days of Code - Day 29 Project
# GUI Password Manager - WARNING, not for actual use
# !! Saves data to a plaintext txt file !!
# Takes user input for service, username, and password (or generates random password)
# Writes all inputs to txt file, prompts success dialogue box, and clears entry fields
# Also includes simple func to validate user has not left service or password entries blank

from email.mime.message import MIMEMessage
from tkinter import *
from tkinter.messagebox import askokcancel, showinfo
import json
import random



GREEN = "#9bdeac"
FONT_NAME = "Arial"

# ------------------------------ SEARCH FUNCTION ---------------------------------#
# Went with different approach than course
# Instead of popup with requested info
# Fill in password field with requested password

def account_search():
    website = website_entry.get()
    try:
        with open("passwords.json", "r") as master_list:
                data = json.load(master_list)     
    except FileNotFoundError as error_message:
        print("No file exists yet. Please enter a new entry.")
    except KeyError as error_message:
        print(f"No account for {error_message} found. Please create a new entry for this service.")
    else:
        # put successful account search code here
        saved_password = data[website]["password"]
        saved_username = data[website]["email"]
        password_entry.insert(0, saved_password)
        username_entry.insert(0, saved_username)


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
    new_entry = {
        website_input: {
            "email": username_input,
            "password": password_input,
        }
    }
    website_validation = validate_entry(website_input)
    password_validation = validate_entry(password_input)
    if website_validation != True or password_validation != True:
        showinfo("Blank Field!", "Please do not leave any fields blank!")
    else:
        try:
            with open("passwords.json", "r") as master_list:
                data = json.load(master_list)     
        except FileNotFoundError as error_message:
            print("Creating new file...")
            with open("passwords.json", "w") as master_list:
                json.dump(new_entry, master_list, indent=4)
        else:
            data.update(new_entry)
            with open("passwords.json", "w") as master_list:
                json.dump(data, master_list, indent=4)
        finally:
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
website_entry = Entry(width=28)
website_entry.grid(column=1, row=1, columnspan=1)
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

search_button = Button(text="Search", width=7, command=account_search)
search_button.grid(column=2, row=1)







window.mainloop()