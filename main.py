from turtle import Screen
import time
from gun import Gun
from alien import Alien
import random
from scoreboard import Scoreboard

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

# Set up scoreboard
scoreboard = Scoreboard(player, WALL_LEFT, WALL_RIGHT)

# Create aliens
aliens = []

# Block layout
rows = 2
cols = 8
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
        alien = Alien((x, y), alien_width, alien_height, score_value=100)
        aliens.append(alien)

# player paddle to move on arrow key press
screen.listen()
screen.listen()
screen.onkeypress(player.move_left, "Left")
screen.onkeyrelease(player.stop_left, "Left")
screen.onkeypress(player.move_right, "Right")
screen.onkeyrelease(player.stop_right, "Right")
screen.onkey(lambda: bullets.append(player.fire_bullet()), "space")


def main() -> None:

    game_is_on = True
    horde_direction = 1
    next_dir = 1
    y_move = 0
    alien_move_interval = 0.5
    last_alien_move_time = time.time()
    life_reset_duration = 1.0
    life_lost_time = 0

    while game_is_on:
        screen.update()
        player.update_position()

        # bullet move and collision detection
        for bullet in bullets[:]:
            bullet.move()
            if bullet.owner == 'player':
                for alien in aliens[:]:
                    if bullet.detect_collision(alien, 20):
                        player.update_score(alien.score_value)
                        bullet.destroy()
                        bullets.remove(bullet)
                        alien.destroy()
                        aliens.remove(alien)
                        break
            elif bullet.owner == 'alien':
                if bullet.detect_collision(player, 20):
                    bullet.destroy()
                    bullets.remove(bullet)
                    player.hideturtle()
                    life_lost_time = time.time()
                    if player.hit():
                        print("GAME OVER – The aliens have landed!")
                        game_is_on = False
                        break
            if time.time() - life_lost_time >= life_reset_duration:
                    player.showturtle()
            # detect if bullet has left the screen so it can be removed
            if bullet.off_screen(WALL_LEFT, WALL_RIGHT, WALL_TOP, WALL_BOTTOM):
                bullet.destroy()
                bullets.remove(bullet)

        # alien horde movement / fire bullet / check collision with player or bottom wall
        current_time = time.time()
        if current_time - last_alien_move_time >= alien_move_interval:
            last_alien_move_time = current_time
            if horde_direction != next_dir:
                y_move = (-alien_height*20) - spacing
            horde_direction = next_dir
            for alien in aliens:
                # Randomly let aliens shoot
                if random.random() < 0.05:  # 1% chance per frame (tweak this)
                    bullets.append(alien.fire_bullet())
                alien.move(horde_direction, y_move)
                if alien.wall_collide(WALL_LEFT, WALL_RIGHT) and horde_direction == next_dir:
                    next_dir*=-1
                #check if alien has invaded player space at bottom (game over)
                if alien.hit_player_space(player):
                    print("GAME OVER – The aliens have landed!")
                    game_is_on = False
                    break

            scoreboard.update_score_display(player)
            y_move = 0


        time.sleep(0.01)


if __name__ == "__main__":
    main()

screen.exitonclick()