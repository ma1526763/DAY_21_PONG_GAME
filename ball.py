import random
from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(0, random.randint(-200, 200))
        self.x_cor = 10
        self.y_cor = 10
        self.direction = random.randint(1, 4)

    def move(self):
        if self.direction == 1:
            self.goto(self.xcor() + self.x_cor, self.ycor() + self.y_cor)
        if self.direction == 2:
            self.goto(self.xcor() + self.x_cor, self.ycor() - self.y_cor)
        if self.direction == 3:
            self.goto(self.xcor() - self.x_cor, self.ycor() + self.y_cor)
        if self.direction == 4:
            self.goto(self.xcor() - self.x_cor, self.ycor() - self.y_cor)

    def check_wall_collision(self):
        return True if abs(self.ycor()) >= 290 else False

    def change_direction_y(self):
        self.y_cor *= -1

    def change_direction_x_l(self):
        self.x_cor = -10

    def change_direction_x_r(self):
        self.x_cor = 10

    def reset_ball(self):
        self.direction = random.randint(1, 4)
        self.goto(0, random.randint(-200, 200))
