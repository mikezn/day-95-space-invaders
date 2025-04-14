from turtle import Screen
import time
from gun import Gun

SCREEN_WIDTH = 855
SCREEN_HEIGHT = 600

WALL_LEFT = ((SCREEN_WIDTH/2)*-1)
WALL_RIGHT = SCREEN_WIDTH/2
WALL_TOP = (SCREEN_HEIGHT/2)-100
WALL_BOTTOM = ((SCREEN_HEIGHT/2)*-1)

bullets = []

# Set up screen
screen = Screen()
screen.title("👾 SPACE INVADERS 👾")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.tracer(0)

# Create new player
player = Gun((0, WALL_BOTTOM+15), gun_width=2, gun_height=1)

# player paddle to move on arrow key press
screen.listen()
screen.listen()
screen.onkeypress(player.move_left, "Left")
screen.onkeyrelease(player.stop_left, "Left")
screen.onkeypress(player.move_right, "Right")
screen.onkeyrelease(player.stop_right, "Right")
screen.onkey(lambda: bullets.append(player.fire_bullet()), "space")

print(bullets)

game_is_on = True


def main() -> None:
    while game_is_on:
        screen.update()
        player.update_position()
        for bullet in bullets:
            bullet.move()
        time.sleep(0.01)


if __name__ == "__main__":
    main()

screen.exitonclick()