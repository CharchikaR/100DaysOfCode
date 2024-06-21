from turtle import Screen
import time

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.go_up)
screen.onkeypress(key="Down", fun=r_paddle.go_down)
screen.onkeypress(key="w", fun=l_paddle.go_up)
screen.onkeypress(key="s", fun=l_paddle.go_down)

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move_ball()

    # Detect a collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect a collision with the paddle
    if (ball.xcor() == 330 and ball.distance(r_paddle) < 63) or (ball.xcor() == -330 and ball.distance(l_paddle) < 63):
        ball.bounce_x()

    # Detect ball going out of bounds and starting again new towards other player
    if ball.xcor() > 400:
        ball.reset_pos()
        scoreboard.l_point()

    if ball.xcor() < -400:
        ball.reset_pos()
        scoreboard.r_point()





screen.exitonclick()
