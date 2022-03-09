from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-600, 500)
        self.current_level = 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write((f"Level: {self.current_level}"), align="center", font=("Courier", 15, "normal"))

    def level_up(self):
        self.current_level += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 300)
        self.write("Game Over", align="center", font=("Courier", 20, "normal"))
