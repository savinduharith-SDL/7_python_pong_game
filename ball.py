from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.home()
        self.x_move_distance = 3
        self.y_move_distance = 3
        self.color("white")

    def move(self):
        new_x = self.xcor() + self.x_move_distance
        new_y = self.ycor() + self.y_move_distance
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move_distance *= -1

    def bounce_x(self):
        self.x_move_distance *= -1
        self.increase_speed()

    def reset_position(self):
        self.x_move_distance = 3
        self.y_move_distance = 3
        self.home()
        self.bounce_x()

    def increase_speed(self):
        self.x_move_distance += 1
        self.y_move_distance += 1




