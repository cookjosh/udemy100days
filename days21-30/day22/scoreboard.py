from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.goto(-50, 150)
        self.write(self.left_score, align="center", font=("Courier", 25, "normal"))
        self.goto(50, 150)
        self.write(self.right_score, align="center", font=("Courier", 25, "normal"))

    def right_point(self):
        self.right_score += 1
        self.goto(50, 150)
        self.write(self.right_score, align="center", font=("Courier", 25, "normal"))
        self.goto(-50, 150)
        self.write(self.left_score, align="center", font=("Courier", 25, "normal"))


    def left_point(self):
        self.left_score += 1
        self.goto(50, 150)
        self.write(self.right_score, align="center", font=("Courier", 25, "normal"))
        self.goto(-50, 150)
        self.write(self.left_score, align="center", font=("Courier", 25, "normal"))


