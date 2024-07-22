from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        # inherit all methods and attributes from the Turtle class
        super().__init__()
        self.shape("circle")
        self.penup()

        # make a 10 x 10 circle (a shape takes on 20 x 20 pixel)
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)

        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)


