from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as f:
            self.high_score = int(f.readline())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score

        with open("data.txt", mode="w") as f:
            f.write(str(self.high_score))

        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()