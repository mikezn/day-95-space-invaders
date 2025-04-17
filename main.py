from turtle import Screen
import time
from gun import Gun
from alien import Alien
from barrier import Barrier
import random
from scoreboard import Scoreboard

SCREEN_WIDTH = 855
SCREEN_HEIGHT = 600

WALL_LEFT = ((SCREEN_WIDTH/2)*-1)
WALL_RIGHT = SCREEN_WIDTH/2
WALL_TOP = (SCREEN_HEIGHT/2)-100
WALL_BOTTOM = ((SCREEN_HEIGHT/2)*-1)

ALIEN_WIDTH = 2
ALIEN_HEIGHT = 2
ALIEN_SPACING = 10
ALIEN_Y_LOC = WALL_TOP - (ALIEN_HEIGHT / 2)

BARRIER_Y_LOC = WALL_BOTTOM + 100

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


def batch_create(object, y_loc, object_width, object_height, rows, cols, spacing, **kwargs) -> list:
    # this func is to create a batch of barriers or aliens in rows and columns
    # calculate total length of batch to find their starting point so the batch is centered
    batch_length = (cols * object_width * 20) + ((object_width - 1) * cols)
    start_x = -batch_length / 2
    start_y = y_loc - (object_height / 2)
    batch = []
    for row in range(rows):
        for col in range(cols):
            x = start_x + col * (object_width * 20 + spacing)
            y = start_y - row * (object_height * 20 + spacing)
            obj = object((x, y), object_width, object_height, **kwargs)
            batch.append(obj)
    return batch


# Set up barriers and aliens
barriers = batch_create(Barrier, y_loc=BARRIER_Y_LOC, object_width=4, object_height=1, rows=1, cols=1, spacing=60)
aliens = batch_create(Alien, y_loc=ALIEN_Y_LOC, object_width=ALIEN_WIDTH, object_height=ALIEN_WIDTH, rows=2, cols=8, spacing=ALIEN_SPACING, score_value=100)
    

# player paddle to move on arrow key press
screen.listen()
screen.listen()
screen.onkeypress(lambda: player.move_left(WALL_LEFT), "Left")
screen.onkeyrelease(player.stop_left, "Left")
screen.onkeypress(lambda: player.move_right(WALL_RIGHT), "Right")
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

            for barrier in barriers[:]:
                if bullet.detect_collision(barrier, 20):
                    bullet.destroy()
                    bullets.remove(bullet)
                    if barrier.hit():
                        barrier.destroy()
                        barriers.remove(barrier)
                        print(barrier.lives)
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
                y_move = (-ALIEN_HEIGHT*20) - ALIEN_SPACING
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