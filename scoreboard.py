from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
      super().__init__()
      self.penup()
      self.pencolor("red")
      self.color("red")
      self.ht()
      self.score=0

    def Score(self):
        self.setpos(x=-300,y=-160)
        self.write(arg=f"Score:{self.score}",font=30)

    def Score_up(self):
        self.score+=1
        self.clear()
        self.Score()

    def result(self):
        self.clear()
        self.setpos(x=-80, y=80)
        self.write(arg="Game Over", font=FONT)
        self.setpos(x=-120, y=50)
        self.write(arg=f"Your score is {self.score}", font=FONT)
