# Udemy 100 Days Python - Day 31 Project
# French Flashcards

from gettext import translation
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
CANVAS_COLOR = "#B9F8D3"

window = Tk()
window.title("French Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Pandas to work with CSV
translation_data = pandas.read_csv("data/french_words.csv")
translation_dict = translation_data.to_dict(orient="records")


word_set = (random.choice(translation_dict))
french_word = word_set["French"]
english_word = word_set["English"]

def change_canvas():
    main_canvas.itemconfig(canvas_image, image=back_image)
    language_label.config(text="english", fg="white", bg=BACKGROUND_COLOR)
    word_label.config(text=english_word, fg="white", bg=BACKGROUND_COLOR)
    

# Choosing random word for card
def random_word():
    global card_timer
    window.after_cancel(card_timer)
    word_set = (random.choice(translation_dict)) 
    word_label.config(text=word_set["French"])
    language_label.config(text="french")
    window.after(3000, change_canvas)


# Canvas for card and back image setup
main_canvas = Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas_image = main_canvas.create_image(400, 300, image=front_image)
main_canvas.grid(column=0, row=0, columnspan=2)

"""
#Canvas for back side of card
back_canvas = Canvas(width=500, height=300, bg=CANVAS_COLOR, highlightthickness=0)
back_canvas.grid(column=1, row=0)

"""

# Labels
language_label = Label(main_canvas, text="french", font=("Arial", 20, "italic"), bg="white")
language_label.place(x=310, y=200)

word_label = Label(main_canvas, text=french_word, font=("Arial", 30, "bold"), bg="white")
word_label.place(x=260, y=300)

# Buttons
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, command=random_word)
wrong_button.grid(column=0, row=1)

correct_image = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_image, command=random_word)
correct_button.grid(column=1, row=1)

card_timer = window.after(3000, change_canvas)

window.mainloop()