from turtle import Turtle

class Player(Turtle):
    def __init__(self, ycoord):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.shapesize(2, 2)
        self.sety(ycoord)
        self.setheading(90)

    def move_up(self):
        self.forward(50)

    def move_down(self):
        self.backward(50)

    def move_right(self):
        x_coord = self.xcor()
        y_coord = self.ycor()
        self.setposition(x_coord + 50, y_coord)

    def move_left(self):
        x_coord = self.xcor()
        y_coord = self.ycor()
        self.setposition(x_coord, y_coord + 50)