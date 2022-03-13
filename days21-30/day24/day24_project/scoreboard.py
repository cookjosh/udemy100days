# Starting code from course for day24

from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
with open("highscore.txt") as file:
    highscore = int(file.read())

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = highscore
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
        self.goto(0, 0)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
