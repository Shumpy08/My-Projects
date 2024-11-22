import turtle
from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_cord = random.randint(-380, 380)
        y_cord = random.randint(-380, 380)
        self.goto(x_cord, y_cord)
