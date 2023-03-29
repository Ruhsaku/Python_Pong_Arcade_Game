from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        # self.speed()

    def move(self):
        new_x = self.xcor() + 0.2
        new_y = self.ycor() + 0.2
        self.goto(new_x, new_y)

