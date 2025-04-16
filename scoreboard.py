from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 80, 'normal')

class Scoreboard(Turtle):
    def __init__(self, player):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player_lives = player.lives
        self.player_score = player.score
        self.update_score_display(player)


    def update_score_display(self, player):
        self.player_score = player.score
        self.player_lives = player.lives
        self.clear()
        self.goto(-100, 200)
        self.write(f'{self.player_lives}', align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f'{self.player_score}', align=ALIGNMENT, font=FONT)