from turtle import Turtle
from bullet import Bullet

MOVE_DIST = 10

class Alien(Turtle):
    def __init__(self, xy, alien_width, alien_height):
        super().__init__()
        self.alien_width = alien_width
        self.alien_height = alien_height
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=self.alien_height, stretch_len=self.alien_width)
        self.penup()
        self.goto(xy)
        self.direction = "right"


    def move(self, direction, y_move):
        self.goto(self.xcor()+(MOVE_DIST*direction), self.ycor() + y_move)


    def wall_collide(self, wall_left, wall_right):
        # locate side edges of alien
        side_right = (self.xcor() + (self.alien_width*20/2))
        side_left = (self.xcor() - (self.alien_width*20/2))

        if side_right >= wall_right or side_left <= wall_left:
            print(side_right, wall_right, side_left, wall_left)
            return True
        else:
            return False


    def destroy(self):
        self.clear()
        self.reset()
        self.hideturtle()



    def fire_bullet(self) -> Bullet:
        return Bullet(owner='alien', direction=-1, pos=(self.xcor(), self.ycor()), bullet_width=.5, bullet_height=1)