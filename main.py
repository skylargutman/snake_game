from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
import time
from food import Food

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #detect collision with food
    if food.distance(snake.head) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
        print("Game Over!")

    #Detect collision with tail
    for segment in snake.segments[1:]:
        # if head collides with any segment in the tail then game over
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
            print("Game Over!")


screen.exitonclick()