# Day 27 Project - Miles to Kilometers Converter
# Using tkinter, take user input for an arbitrary amount of miles
# Convert miles to kilometers on button click

import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=700, height=400)
window.config(padx=50, pady=50)

# User entry field
user_input = tkinter.Entry()
user_input.grid(column=1, row=0)


# Labels
miles_label = tkinter.Label(text="Miles", font=("Arial", 14, "bold"))
miles_label.grid(column=2, row=0)

filler_label = tkinter.Label(text="is equal to ", font=("Arial", 14))
filler_label.grid(column=0, row=1)

kilometer_number = tkinter.Label(text="0", font=("Arial", 16))
kilometer_number.grid(column=1, row=1)

km_label = tkinter.Label(text="Km", font=("Arial", 14, "bold"))
km_label.grid(column=2, row=1)

# Button
def button_click():
    calc_button["text"] = "Calculated!!"
    miles_number = user_input.get()
    kilometers = float(miles_number) * 1.609344
    kilometer_number["text"] = kilometers

    
calc_button = tkinter.Button(text="Calculate", command=button_click)
calc_button.grid(column=1, row=2)


window.mainloop()