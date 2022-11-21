from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        self.goto(x=0, y=270)
        self.write(f"SCORE: {self.score}", True, align='center', font=('candara', 24, 'bold'))
        self.hideturtle()

    def update_scoreboard(self):
        self.goto(x=0, y=270)
        self.write(f"SCORE: {self.score}", True, align='center', font=('candara', 24, 'bold'))

    def scores(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"Game Over", align='center', font=('candara', 24, 'bold'))

