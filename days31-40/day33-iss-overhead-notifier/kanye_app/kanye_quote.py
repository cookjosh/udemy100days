from re import U
from tkinter import *
import requests

# API func written by me
def get_quote():
    #Write your code here.
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()
    response_data = response.json()
    kanye_quote = response_data["quote"]
    canvas.itemconfig(quote_text, text=kanye_quote)



# Tkinter code provided from course
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Click for Kayne quote!", width=250, font=("Arial", 12, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()