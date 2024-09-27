FONT = ("Courier", 18, "normal")
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level=1
        self.penup()
        self.goto(-250,250)
        self.hideturtle()
        self.display_level()
    def display_level(self):
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)

    def update_level(self):
        self.level+=1
        self.clear()
        self.display_level()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over", align="center", font=FONT)
        #self.hideturtle()
