import turtle
from turtle import Turtle, Screen
import time

SCREEN_WIDTH = 855
SCREEN_HEIGHT = 600

# Set up screen
screen = Screen()
screen.title("👾 SPACE INVADERS 👾")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.tracer(0)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.01)

screen.exitonclick()