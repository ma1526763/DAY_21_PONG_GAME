from turtle import Turtle

class ScreenSetup(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.sr = screen
        self.screen_setup()
        self.create_dashed_line()

    def screen_setup(self):
        self.sr.title("PONG GAME")
        self.sr.bgpic("black.png")
        self.sr.setup(800, 600)

    def create_dashed_line(self):
        self.penup()
        self.shape("square")
        self.color("white")
        self.hideturtle()
        self.goto(0, -380)
        self.setheading(90)
        self.pensize(2)
        for i in range(24):
            self.pendown()
            self.forward(17)
            self.penup()
            self.forward(17)

    def screen_key_listen_1(self, paddle_1, paddle_2):
        self.screen.listen()
        self.screen.onkeypress(key="Up", fun=paddle_1.move_up)
        self.screen.onkeypress(key="Down", fun=paddle_1.move_down)
        self.screen.onkeypress(key="w", fun=paddle_2.move_up)
        self.screen.onkeypress(key="W", fun=paddle_2.move_up)
        self.screen.onkeypress(key="s", fun=paddle_2.move_down)
        self.screen.onkeypress(key="S", fun=paddle_2.move_down)