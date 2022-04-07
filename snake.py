from turtle import Turtle
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
U = 90
D = 270
L = 180
R = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in STARTING_POSITIONS:
            self.add_segments(i)

    def add_segments(self, pos):
        tim = Turtle("square")
        tim.pu()
        tim.color("red")
        tim.goto(pos)
        self.segments.append(tim)

    def extend_segments(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            n_x = self.segments[seg - 1].xcor()
            n_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(n_x, n_y)
        self.head.fd(MOVE)
        time.sleep(0.09)

    def up(self):
        if self.head.heading() != D:
            self.head.setheading(U)

    def down(self):
        if self.head.heading() != U:
            self.head.setheading(D)

    def left(self):
        if self.head.heading() != R:
            self.head.setheading(L)

    def right(self):
        if self.head.heading() != L:
            self.head.setheading(R)
