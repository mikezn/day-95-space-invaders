from turtle import Turtle
from bullet import Bullet

class Gun(Turtle):
    def __init__(self, xy, gun_width, gun_height):
        super().__init__()
        self.gun_width = gun_width
        self.gun_height = gun_height
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=self.gun_height, stretch_len=self.gun_width)
        self.penup()
        self.goto(xy)
        self.moving_left = False
        self.moving_right = False


    def move_left(self) -> None:
        self.moving_left = True


    def stop_left(self) -> None:
        self.moving_left = False


    def move_right(self) -> None:
        self.moving_right = True


    def stop_right(self) -> None:
        self.moving_right = False


    def update_position(self):
        if self.moving_left:
            self.setx(self.xcor() - 5)
        if self.moving_right:
            self.setx(self.xcor() + 5)


    def fire_bullet(self) -> Bullet:
        bang = Bullet(owner=self, pos=(self.xcor(), self.ycor()), bullet_width=.5, bullet_height=1)
        return bang