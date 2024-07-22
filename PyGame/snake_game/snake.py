from turtle import Turtle

XCOR_STEP = -20
YCOR = 0
START_SEG = 3
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.head = None
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for n_seg in range(START_SEG):
            pos = (n_seg*XCOR_STEP, YCOR)
            self.add_segment(pos)
        self.head = self.segments[0]

    def add_segment(self, pos):
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.goto(pos)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segments:
            seg.reset()
        self.segments.clear()
        self.create_snake()

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)