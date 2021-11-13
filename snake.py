import turtle


class Snake:
    def __init__(self):
        starting_position = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        for position in starting_position:
            self.add_segment(position)

    def add_segment(self, position):
        segment = turtle.Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.setpos(position)
        self.segments.append(segment)

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            self.segments[segment].setpos(x=self.segments[segment - 1].xcor(), y=self.segments[segment - 1].ycor())
        self.segments[0].forward(20)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def increase_tail(self):
        self.add_segment(self.segments[-1].position())
