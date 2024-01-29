# ------------------------------------------------------------------------------------------------ #
#                                Build Pong: The Famous Arcade Game                                #
# ------------------------------------------------------------------------------------------------ #


from turtle import Screen, Turtle
import time
from classes.paddle import Paddle
from classes.ball import Ball
from classes.scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.title("World Famous Pong Game")
screen.tracer(0)
screen.setup(width=800, height=600)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle
    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(l_paddle) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()

    # Detect when R paddle misses
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    # Detect when L paddle misses
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()
