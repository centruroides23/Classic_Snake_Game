from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Times New Roman", 14, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.write(f"Your Score is: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Your Score is: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.write(f"Your Score is: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


