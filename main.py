import turtle
import time
import snake as s
from food import Food
from scoreboard import ScoreBoard

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

snake = s.Snake()
food = Food()
scoreboard = ScoreBoard()

screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.add_score()
        snake.increase_tail()

    if snake.segments[0].xcor() > 280 or snake.segments[0].ycor() > 280 \
            or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
