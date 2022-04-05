# Day 27 Exercises - Tkinter

import tkinter

# Initiating and setup settings of the GUI window
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=1000, height=800)
window.config(padx=100, pady=100)

# Labels
my_label = tkinter.Label(text="Sample Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

my_label["text"] = "New Text"
my_label.config(text="New Text") # These are two options to set properties of labels


# Buttons
## In video challenge - change label text upon button click
def button_click():
    my_label["text"] = "I've been clicked!"
    user_name = input.get() # These two lines are for next in video challenge
    my_label["text"] = user_name # Take Entry field and apply string to label on button click

    
button = tkinter.Button(text="My Button", command=button_click)
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry
input = tkinter.Entry()
input.grid(column=3, row=2)










window.mainloop() # loop that keeps program from exiting