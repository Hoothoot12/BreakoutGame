from turtle import Turtle

class Paddle():
     def __init__(self):
       self.player = Turtle("square")
       self.player.st()

     def paddle(self):
       self.player.penup()
       self.player.color("white")
       self.player.shapesize(stretch_wid=5, stretch_len=1)
       self.player.setpos(x=0, y=-200)
       self.player.seth(90)
       return self.player

     def player_left(self):
       if self.player.xcor()<=350:
         self.player.goto(self.player.xcor()-20,-200)

     def player_right(self):
       if self.player.xcor()>=-350:
         self.player.goto(self.player.xcor()+20,-200)