from turtle import Turtle

PADDLE_XPOS = 350.0
PADDLE_WIDTH = 20.0


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(PADDLE_XPOS, 0.0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
