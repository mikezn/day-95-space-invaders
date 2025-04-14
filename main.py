from turtle import Screen
import time
from gun import Gun
from alien import Alien

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

# Create aliens
aliens = []

# Block layout
rows = 2
cols = 2
alien_width = 2
alien_height = 2
spacing =  10

# calculate total length of alien horde to find their starting point so the horde is centered
horde_length = (cols*alien_width*20) + ((alien_width-1)*cols)
start_x = -horde_length/2
start_y = WALL_TOP - (alien_height/2)

# generate blocks
for row in range(rows):
    for col in range(cols):
        x = start_x + col * (alien_width*20 + spacing)
        y = start_y - row * (alien_height*20 + spacing)
        alien = Alien((x, y), alien_width, alien_height)
        aliens.append(alien)

# player paddle to move on arrow key press
screen.listen()
screen.listen()
screen.onkeypress(player.move_left, "Left")
screen.onkeyrelease(player.stop_left, "Left")
screen.onkeypress(player.move_right, "Right")
screen.onkeyrelease(player.stop_right, "Right")
screen.onkey(lambda: bullets.append(player.fire_bullet()), "space")


game_is_on = True


def main() -> None:
    horde_direction = 1
    next_dir = 1
    y_move = 0
    while game_is_on:
        screen.update()
        player.update_position()
        for bullet in bullets:
            bullet.move()

        if horde_direction != next_dir:
            y_move = (-alien_height*20) - spacing
        horde_direction = next_dir
        # print(horde_direction, next_dir)
        for alien in aliens:
            alien.move(horde_direction, y_move)
            if alien.wall_collide(WALL_LEFT, WALL_RIGHT) and horde_direction == next_dir:
                next_dir*=-1
                print(next_dir)
        y_move = 0
        time.sleep(0.01)


if __name__ == "__main__":
    main()

screen.exitonclick()