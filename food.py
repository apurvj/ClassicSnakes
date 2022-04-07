from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.food_location()
        self.speed(0)

    def food_location(self):
        ran_x = random.randint(-270, 270)
        ran_y = random.randint(-270, 270)
        self.goto(ran_x, ran_y)

    