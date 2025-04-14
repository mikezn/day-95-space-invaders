from turtle import Turtle

MOVE_DIST = 3

class Bullet(Turtle):
    def __init__(self, owner, pos, bullet_width, bullet_height):
        super().__init__()
        self.bullet_width = bullet_width
        self.bullet_height = bullet_height
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=self.bullet_height, stretch_len=self.bullet_width)
        self.penup()
        self.goto(pos)
        self.owner = owner


    def move(self):
        new_y = self.ycor() + MOVE_DIST
        self.goto(self.xcor(), new_y)