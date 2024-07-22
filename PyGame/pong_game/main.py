from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from net import Net
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
net = Net(screen.canvheight)

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # ball to bounce
        ball.bounce_y()

    # # Detect collision with right paddle
    # if ball.xcor() > 320:
    #     # right paddle hit
    #     if ball.distance(r_paddle) < 40:
    #         ball.bounce_x()
    #     # right paddle miss
    #     else:
    #         ball.reset()
    #         scoreboard.increase_score("l")
    #
    # # detect collision with left paddle
    # if ball.xcor() < -320:
    #     # left paddle hit
    #     if ball.distance(l_paddle) < 40:
    #         ball.bounce_x()
    #     # left paddle miss
    #     else:
    #         ball.reset()
    #         scoreboard.increase_score("r")

    # Detect collision with right paddle
    if any(ball.distance(coor) < 30 for coor in r_paddle.proximity):
        # right paddle hit
        ball.bounce_x()
    elif ball.xcor() > 390:
        ball.reset()
        scoreboard.increase_score("l")

    # Detect collision with left paddle
    if any(ball.distance(coor) < 30 for coor in l_paddle.proximity):
        # right paddle hit
        ball.bounce_x()
    elif ball.xcor() < -390:
        ball.reset()
        scoreboard.increase_score("r")


screen.exitonclick()