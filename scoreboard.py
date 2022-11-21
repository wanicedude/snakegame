from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        self.high_score = 0
        self.goto(x=0, y=270)
        # self.write(f"SCORE: {self.score}", True, align='center', font=('candara', 24, 'bold'))
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(x=0, y=270)
        self.clear()
        self.write(f"SCORE: {self.score} High Score: {self.high_score}", True, align='center', font=('candara', 24, 'bold'))

    def scores(self):
        self.score += 1
        self.update_scoreboard()
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write(f"Game Over", align='center', font=('candara', 24, 'bold'))

