from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.l_Score = 0
        self.r_score = 0
        self.goto(-100, 240)
        self.update_screen()

    def increase_left_score(self):
        self.l_Score += 1
        self.update_screen()

    def increase_right_score(self):
        self.r_score += 1
        self.update_screen()

    def update_screen(self):
        self.clear()
        self.goto(-100, 240)
        self.write(self.l_Score, align="center", font=("Arial", 40, "normal"))
        self.goto(100, 240)
        self.write(self.r_score, align="center", font=("Arial", 40, "normal"))


