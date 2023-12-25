from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen._root.resizable(False, False)
screen.setup(800, 600)
screen.title("Pong game")
screen.tracer(0)

paddle_right = Paddle(isLeft=False)
paddle_left = Paddle(isLeft=True)
ball = Ball()
scoreboard = Scoreboard()

screen.tracer(1)
screen.listen()
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")

while True:
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
    if (ball.xcor() >= 320 or ball.xcor() <= -320) and (
            ball.distance(paddle_left) < 50 or ball.distance(paddle_right) < 50):
        ball.bounce_x()
    if ball.xcor() > 340 or ball.xcor() < -340:
        screen.tracer(0)
        if ball.xcor() > 340:
            ball.reset_position()
            scoreboard.increase_left_score()
        if ball.xcor() < -340:
            ball.reset_position()
            scoreboard.increase_right_score()
        screen.tracer(1)


screen.exitonclick()
