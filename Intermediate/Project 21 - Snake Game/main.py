from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Setting up the sreen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Creating the scoreboard, the snake and the first food piece
score = Scoreboard()
snake = Snake()
food = Food()

# Binding arrow keys to control commands
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

# Letting the snake loose until it hits a wall or its own tail
while(True):

    # Updating the screen and moving
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detecting collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        score.increase()
        food.locate_randomly()
    
    # Detecting collision with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290:
        break
    if snake.head.ycor() > 290 or snake.head.ycor() < -290:
        break

    # Detecting collision with the tail
    collided = False
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            collided = True
            break
    if collided:
        break

score.end_game()
screen.exitonclick()
