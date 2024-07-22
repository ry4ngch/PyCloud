from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.currentScore = 0
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.currentScore} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.currentScore += 1
        self.refresh()

    def game_over(self):
        self.home()
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.currentScore > self.high_score:
            with open("data.txt", mode="w") as data:
                data.write(str(self.currentScore))
            self.high_score = self.currentScore
        self.currentScore = 0
        self.refresh()
