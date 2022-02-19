import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class Brick():
    def __init__(self):
       self.bricks = []
       self.brick_number = 60

    def create_bricks(self,n):
        if n>38:
            self.bricks.append(Turtle("square"))
            self.bricks[n].shapesize(stretch_len=2, stretch_wid=0.5)
            self.bricks[n].penup()
            self.bricks[n].color('black', random.choice(COLORS))
            self.bricks[n].setpos(x=-380 + 40 * (n-40), y=200)
        elif n>19:
            self.bricks.append(Turtle("square"))
            self.bricks[n].shapesize(stretch_len=2, stretch_wid=0.5)
            self.bricks[n].penup()
            self.bricks[n].color('black', random.choice(COLORS))
            self.bricks[n].setpos(x=-400 + 40 * (n-19), y=210)
        else:
          self.bricks.append(Turtle("square"))
          self.bricks[n].shapesize(stretch_len=2,stretch_wid=0.5)
          self.bricks[n].penup()
          self.bricks[n].color('black',random.choice(COLORS))
          self.bricks[n].setpos(x=-380+40*n,y=220)

    def initial_stage(self):
        for n in range(self.brick_number):
            self.create_bricks(n)
