from turtle import Screen
from snake import Snake
import time

# Setting up the sreen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Creating the snake
snake = Snake()

game_on = True
while(game_on):    
    screen.update()
    time.sleep(0.1)
    snake.move()









screen.exitonclick()
