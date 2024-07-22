from turtle import Turtle
FONT = ("Courier", 26, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.setpos(-280, 250)
        self.hideturtle()
        self.level_up()

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.home()
        self.write("Game Over!", align="center", font=FONT)