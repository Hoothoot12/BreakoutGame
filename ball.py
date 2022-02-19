from turtle import Turtle
import random
from paddle import Paddle
from brick import Brick
from scoreboard import Scoreboard

paddle = Paddle()

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.display=Scoreboard()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.setpos(0, 0)
        self.n = 1
        self.k = 1
        self.bricks = Brick()
        self.bricks_number = self.bricks.brick_number
        self.bricks.initial_stage()
        self.movespeed=0.0001
        self.random_direction()

    def random_direction(self):
        random_factor1 = random.randint(0, 1)
        random_factor2 = random.randint(0, 1)
        if random_factor1 == 0:
          self.bounce_x()
          if random_factor2 == 0:
              self.bounce_y()

    def bounce_x(self):
        self.k *= -1.0

    def bounce_y(self):
        self.n *= -1.0

    def move(self):
        new_x = self.xcor() + 2 * self.k
        new_y = self.ycor() + 2 * self.n
        self.goto(new_x, new_y)

    def movement(self, player):
        self.move()
        if self.ycor() > 240:
            print(self.ycor())
            self.sety(240)
            self.bounce_y()

        elif self.ycor()>190:
          if self.xcor()>380:
              self.setx(380)
              self.bounce_x()
          elif self.xcor()<-380:
              self.setx(-380)
              self.bounce_x()
          else:
            self.bricks_collision()

        elif self.xcor() > 390:
            self.setx(390)
            self.bounce_x()

        elif self.xcor() < -390:
            self.setx(-380)
            self.bounce_x()

        elif (self.ycor() > -200 and self.ycor() < -180) and (self.xcor()<player.xcor()+55 and self.xcor()>player.xcor()-55):
            self.bounce_y()

        elif self.ycor()<-240 or self.display.score==60:
            self.display.result()

    def bricks_collision(self):
        for u in range(self.bricks_number):
          if self.bricks.bricks[u].isvisible() is True:
            if self.bricks.bricks[u].distance(self)<18 :
               self.bricks.bricks[u].ht()
               self.bounce_y()
               self.display.Score_up()

    def reset(self):
        self.setpos(0, 0)
        self.movespeed=0.0001
        self.bounce_x()
