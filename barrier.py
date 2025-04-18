from turtle import Turtle

class Barrier(Turtle):
    def __init__(self, xy, barrier_width, barrier_height):
        super().__init__()
        self.barrier_width = barrier_width
        self.barrier_height = barrier_height
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=self.barrier_height, stretch_len=self.barrier_width)
        self.penup()
        self.start_pos = xy
        self.lives = 3
        self.goto(self.start_pos)


    def hit(self):
        self.lives-=1
        # change color
        # destroy when no lives
        if self.lives == 0:
            return True


    def destroy(self):
        self.clear()
        self.reset()
        self.hideturtle()