from turtle import Screen
from screen_setup import ScreenSetup
from paddle import Paddle
from score import ScoreBoard
from ball import Ball
import time

def reset():
    time.sleep(.5)
    ball.reset_ball()
    return 0.1

screen = Screen()
screen.tracer(0)
sr = ScreenSetup(screen)
ball = Ball()
paddle_1 = Paddle((380, 0))
paddle_2 = Paddle((-387, 0))
score_1 = ScoreBoard((-120, 240))
score_2 = ScoreBoard((80, 240))

sr.screen_key_listen_1(paddle_1, paddle_2)
sleep_time = 0.1
while True:
    screen.update()
    time.sleep(sleep_time)
    ball.move()
    if ball.check_wall_collision():
        ball.change_direction_y()
        sleep_time *= 0.9
    if paddle_1.distance(ball) < 50 and ball.xcor() >= 340:
        ball.change_direction_x_l()
        sleep_time *= 0.9
    if paddle_2.distance(ball) < 50 and ball.xcor() < -360:
        ball.change_direction_x_r()
        sleep_time *= 0.9
    if ball.xcor() > 430:
        score_1.update_score(1)
        sleep_time = reset()
    if ball.xcor() < -430:
        score_2.update_score(2)
        sleep_time = reset()
screen.exitonclick()
