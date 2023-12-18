from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen._root.resizable(False, False)
screen.setup(800,600)
screen.title("Pong game")

paddle_right = Paddle()



screen.exitonclick()