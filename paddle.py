from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.pos = position
        self.create_paddle()

    def create_paddle(self):
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.shapesize(4, 1)
        self.goto(self.pos)

    def move_up(self):
        if self.ycor() < 280:
            self.goto(self.xcor(), self.ycor()+40)

    def move_down(self):
        if self.ycor() > -280:
            self.goto(self.xcor(), self.ycor()-40)

