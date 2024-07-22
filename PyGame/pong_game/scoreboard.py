from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 250)
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"{self.l_score}  {self.r_score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self, player):
        if player == "l":
            self.l_score += 1
        else:
            self.r_score += 1
        self.refresh()