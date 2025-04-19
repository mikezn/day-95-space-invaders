from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 40, 'normal')

class Scoreboard(Turtle):
    def __init__(self, player, wall_left, wall_right):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player_lives = player.lives
        self.player_score = player.score
        self.left_align = wall_left + 50
        self.right_align = wall_right - 400
        self.update_score_display(player)


    def update_score_display(self, player):
        self.player_score = player.score
        self.player_lives = player.lives
        lives_text = ""
        for i in range(self.player_lives):
            lives_text += "❤"
        self.clear()
        self.goto(self.left_align, 200)
        self.write(f'{lives_text}', align='left', font=FONT)
        self.goto(self.right_align, 200)
        self.write(f'score: {self.player_score}', align='left', font=FONT)


    def game_over(self):
        # self.clear()
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)