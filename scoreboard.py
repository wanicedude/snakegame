from turtle import Turtle

# with open("snakegame/data.txt") as TAT:
#     # for x in TAT:
#     TOT = TAT.write()
#     TATA = [int(x) for x in TOT.split()]
#     DATA = TATA [0]
#     print(DATA)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        with open("snakegame/data.txt") as data:
            self.high_score = int(data.read())
        # self.high_score = DATA
        self.goto(x=0, y=270)
        # self.write(f"SCORE: {self.score}", True, align='center', font=('candara', 24, 'bold'))
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(x=0, y=270)
        self.clear()
        self.write(f"SCORE: {self.score} High Score: {self.high_score}",
                   True, align='center', font=('candara', 24, 'bold'))

    def scores(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snakegame/data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write(f"Game Over", align='center', font=('candara', 24, 'bold'))
