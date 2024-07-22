from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


def run_game():
    game_is_on = True
    while game_is_on:
        screen.update()
        # delay the animation by 0.1 sec
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            scoreboard.game_over()

        # Detect collision with tail.
        # for index, segment in enumerate(snake.segments):
            # if index > 0:
            #     if snake.head.distance(segment) < 10:
            #         game_is_on = False
            #         scoreboard.game_over()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

    continue_game = screen.textinput(title="Continue Game?",
                                     prompt="Do you want to play another round? [y/n]").lower() == "y"
    if continue_game:
        snake.reset()
        scoreboard.reset()
        run_game()


run_game()


screen.exitonclick()