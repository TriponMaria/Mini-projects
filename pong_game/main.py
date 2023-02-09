from ball import Ball
from paddle import Paddle
from turtle import Screen
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

# This function trace turn off the animation
screen.tracer(0)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_l.up, key="Up")
screen.onkey(paddle_l.down, key="Down")
screen.onkey(paddle_r.up, key="w")
screen.onkey(paddle_r.down, key="s")

# After we create the paddle we turn on the animation
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.l_point()
    elif ball.xcor() < -380:
        ball.refresh()
        scoreboard.r_point()

screen.exitonclick()