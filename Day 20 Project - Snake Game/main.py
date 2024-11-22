from turtle import Screen
from food import Food
from Snake import Snake
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.title("Shumpy's Snake Game")
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
head = snake.segments[0]

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if head.xcor() > 380 or head.xcor() < -380 or head.ycor() > 380 or head.ycor() < -380:
        is_game_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if head.distance(segment) < 10 :
            is_game_on = False
            scoreboard.game_over()
screen.exitonclick()
