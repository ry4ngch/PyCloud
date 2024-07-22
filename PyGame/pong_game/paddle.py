from turtle import Turtle


PADDLE_WIDTH = 5
GRID = 20


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=1)
        self.penup()
        self.setpos(pos)
        self.proximity = []
        self.register()

    def register(self):
        self.proximity = []
        # add the current turtle paddle
        self.proximity.append((self.xcor(), self.ycor()))
        for i in range(int(PADDLE_WIDTH/2)):
            # add the positive coordinates of the paddle
            self.proximity.append((self.xcor(), self.ycor() + GRID * i))

            # add the negative coordinates of the paddle
            self.proximity.append((self.xcor(), self.ycor() - GRID * i))

    def move_up(self):
        if self.ycor() + 3*GRID < 300:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)
            self.register()

    def move_down(self):
        if self.ycor() - 3*GRID > -300:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
            self.register()
