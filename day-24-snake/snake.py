from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.all_segments = []
        self.create_snake()
        self.head = self.all_segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.all_segments.append(new_segment)

    def extend(self):
        self.add_segment(self.all_segments[-1].position())

    def move(self):
        for segment in range(len(self.all_segments) - 1, 0, -1):
            new_x = self.all_segments[segment - 1].xcor()
            new_y = self.all_segments[segment - 1].ycor()
            self.all_segments[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset_snake(self):
        for segment in self.all_segments:
            segment.goto(1000,1000)

        self.all_segments.clear()
        self.create_snake()
        self.head = self.all_segments[0]
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.head.forward(MOVE_DISTANCE)
            self.move()

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.head.forward(MOVE_DISTANCE)
            self.move()

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.head.forward(MOVE_DISTANCE)
            # self.move()

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.head.forward(MOVE_DISTANCE)
            self.move()