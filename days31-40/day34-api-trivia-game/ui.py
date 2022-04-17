from cgitb import text
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=800, height=650, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            400,
            305,
            width=700,
            text="questions go here",
            fill=THEME_COLOR,
            font=("Arial", 15, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        self.score_label = Label(self.window, text="score: 0", font=("Arial", 12), bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=self.true_image, command=self.true_click)
        self.true_button.grid(column=0, row=2)
        self.false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=self.false_image, command=self.false_click)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_click(self):
        self.quiz.check_answer("True")
        self.get_next_question()

    def false_click(self):
        self.quiz.check_answer("False")
        self.get_next_question()
        


    
