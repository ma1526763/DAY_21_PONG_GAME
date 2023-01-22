from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0
        self.pos = position
        self.create_score()
        self.show_score()

    def show_score(self):
        self.write_score_1()

    def create_score(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(self.pos)

    def update_score(self, player):
        if player == 1:
            self.score_1 += 1
            self.write_score_1()
        else:
            self.score_2 += 1
            self.write_score_2()

    def write_score_1(self):
        self.clear()
        self.write(f"{self.score_1}", font=("Arial", 34, "normal"))

    def write_score_2(self):
        self.clear()
        self.write(f"{self.score_2}", font=("Arial", 34, "normal"))


