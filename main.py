import time
from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
from brick import Brick

screen=Screen()
screen.setup(width=800,height=500)
screen.bgcolor("black")
screen.tracer(0)

display=Scoreboard()
paddle=Paddle()
player=paddle.paddle()

ball=Ball()

screen.listen()
screen.onkey(paddle.player_left,"Left")
screen.onkey(paddle.player_right,"Right")

brick=Brick()

is_on=True
while is_on==True:
  time.sleep(ball.movespeed)
  screen.update()
  ball.movement(player)
  if ball.ycor() < -250 or display.score==60 :
    ball.reset()
    is_on=False

screen.exitonclick()
