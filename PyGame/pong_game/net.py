from turtle import Turtle

SPACE = 20
NO_OF_SPACE = 8

class Net(Turtle):
    def __init__(self, screen_height):
        super().__init__()
        # self.shape("square")
        # self.shapesize(stretch_wid=3, stretch_len=0.5)
        self.color("white")
        self.penup()
        self.screen_height = screen_height
        self.goto(x=0, y=-screen_height)
        self.setheading(90)
        self.draw()

    def draw(self):
        for _ in range(int((self.screen_height*2)/NO_OF_SPACE)):
            self.forward(SPACE)
            self.pendown()
            self.forward(int((self.screen_height*2 - SPACE*(NO_OF_SPACE - 1))/10))
            self.penup()
