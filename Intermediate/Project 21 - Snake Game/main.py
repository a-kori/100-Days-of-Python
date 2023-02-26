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

# Binding arrow keys to control commands
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

# Letting the snake loose until 
# it hits a wall or its own tail
game_on = True
while(game_on):    
    screen.update()
    time.sleep(0.1)
    snake.move()









screen.exitonclick()
