from turtle import Turtle

PADDLE_XPOS = 350.0
PADDLE_WIDTH = 20.0
MOVE_DISTANCE = 40.0

class Paddle(Turtle):
    def __init__(self,isLeft):
        super().__init__()
        paddle_position = 0
        if isLeft:
            paddle_position = PADDLE_XPOS * -1
        else:
            paddle_position = PADDLE_XPOS
        self.goto(paddle_position, 0.0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)

    def up(self):
        self.forward(MOVE_DISTANCE)
    def down(self):
        self.backward(MOVE_DISTANCE)