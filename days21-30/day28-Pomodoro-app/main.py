# Day 28 - Pomodoro app
# Using tkinter, create a GUI timer for the Pomodoro method
# Starting code (Constants section) and tomato img provided by Udemy course

import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(time_text, text="00:00")
    canvas_label.config(text="Pomodoro Timer")
    checkmark_label.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    
    if reps % 2 == 0:
        countdown(3)
        canvas_label.config(text="Break", fg=YELLOW)
    elif reps % 8 == 0:
        countdown(5)
        canvas_label.config(text="Long Break", fg=PINK)
    else:
        countdown(10)
        canvas_label.config(text="Work, bitch", fg="white")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if count < 10:
        seconds = f"0{count}"
    canvas.itemconfig(time_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        check_marks = ""
        sessions = math.floor(reps/2)
        for _ in range(sessions):
            check_marks += "✓"
        checkmark_label.config(text=check_marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=100, bg=GREEN)

canvas = Canvas(width=500, height=300, bg=GREEN, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(250, 150, image=tomato_image)
time_text = canvas.create_text(253, 175, text="00:00", fill="white", font=(FONT_NAME, 14, "bold"))
canvas.grid(column=1, row=1)


# Labels
canvas_label = Label(text="Pomodoro Timer", font=(FONT_NAME, 20, "bold"), fg="white", bg=GREEN)
canvas_label.grid(column=1, row=0)

checkmark_label = Label(text="✓", font=(FONT_NAME, 20, "bold"), fg=RED, bg=GREEN)
checkmark_label.grid(column=1, row=2)

# Button things
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=1)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=3, row=1)


window.mainloop()