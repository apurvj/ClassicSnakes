from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.score = 0
        self.goto(x=0, y=270)
        self.color("white")
        self.hideturtle()
        self.write(arg=f"Score: {self.score}", align="center", font=('Courier', 20, 'normal'))

    def incr_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", align="center", font=('Courier', 20, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over!", align="center", font=('Courier', 50, 'normal'))
