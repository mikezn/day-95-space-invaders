from turtle import Turtle
from bullet import Bullet
import time

class Gun(Turtle):
    def __init__(self, xy, gun_width, gun_height):
        super().__init__()
        self.gun_width = gun_width
        self.gun_height = gun_height
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=self.gun_height, stretch_len=self.gun_width)
        self.penup()
        self.start_pos = xy
        self.moving_left = False
        self.moving_right = False
        self.lives = 3
        self.score = 0
        self.goto(self.start_pos)


    def move_left(self, wall_left) -> None:
        if (self.xcor() - self.gun_width*10) <= wall_left:
            # extra function to snap player back to wall
            self.setx(wall_left + self.gun_width*10)
            self.stop_left()
        else:
            self.moving_left = True


    def stop_left(self) -> None:
        self.moving_left = False


    def move_right(self, wall_right) -> None:
        if (self.xcor() + self.gun_width * 10) >= wall_right:
            # extra function to snap player back to wall
            self.setx(wall_right - self.gun_width * 10)
            self.stop_right()
        else:
            self.moving_right = True


    def stop_right(self) -> None:
        self.moving_right = False


    def update_position(self):
        if self.moving_left:
            self.setx(self.xcor() - 5)
        if self.moving_right:
            self.setx(self.xcor() + 5)


    def fire_bullet(self) -> Bullet:
        return Bullet(owner='player', direction=1, pos=(self.xcor(), self.ycor()), bullet_width=.5, bullet_height=1)


    def hit(self) -> bool:
        self.lives-=1
        if self.lives == 0:
            return True
        else:
            self.goto(self.start_pos)


    def update_score(self, score):
        self.score+=score