
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
from turtle import Turtle

class Snake:

    def __init__(self):
        self.length = 2
        self.segments = []
        self.xcoor = 0
        self.ycoor = 0
        self.create_snake()
        self.head = self.segments[0]



    def create_snake(self):
        for i in range(self.length):
            s = Turtle(shape="square")
            s.penup()
            s.setpos(x=self.xcoor, y=self.ycoor)
            s.color("white")
            self.xcoor -= 20
            self.segments.append(s)

    def add_segment(self, position):
        s = Turtle("square")
        s.color("white")
        s.penup()
        s.goto(position)
        self.segments.append(s)

    def extend(self):
        self.add_segment(self.segments[-1].position())




    def move(self):

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)












