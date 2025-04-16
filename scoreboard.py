from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 60, 'normal')

class Scoreboard(Turtle):
    def __init__(self, player, wall_left, wall_right):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player_lives = player.lives
        self.player_score = player.score
        self.left_align = wall_left + 100
        self.right_align = wall_right - 100
        self.update_score_display(player)


    def update_score_display(self, player):
        self.player_score = player.score
        self.player_lives = player.lives
        self.clear()
        self.goto(self.left_align, 200)
        self.write(f'{self.player_lives}', align=ALIGNMENT, font=FONT)
        self.goto(self.right_align, 200)
        self.write(f'{self.player_score}', align=ALIGNMENT, font=FONT)