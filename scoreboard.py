from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 20)

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.sety(270)
        self.pencolor("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.penup()
        self.sety(0)
        self.pendown()
        self.write("GAME OVER!", align=ALIGN, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

