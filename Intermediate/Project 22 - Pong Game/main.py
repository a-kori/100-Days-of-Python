from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time
import gui

# Setting up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Drawing a dashed line separating the two players
gui.draw_dashed_line(screen.window_height())

# Creating the ball, the scoreboard, the left and the right paddle
ball = Ball()
left_paddle = Paddle(screen.window_width(), screen.window_height(), is_left=True)
right_paddle = Paddle(screen.window_width(), screen.window_height(), is_left=False)
left_score = Score(is_left=True)
right_score = Score(is_left=False)
screen.update()

# Binding keys to control commands
screen.listen()
screen.onkey(key="w", fun=left_paddle.move_up)
screen.onkey(key="s", fun=left_paddle.move_down)
screen.onkey(key="Up", fun=right_paddle.move_up)
screen.onkey(key="Down", fun=right_paddle.move_down)

# Let the ball lose with a gradually increasing speed.
# If it 'flew out of the screen', increment the oponent's score
start_sleep = 0.005
while(True):
    ball.move((left_paddle, right_paddle))
    
    if ball.xcor() > 410:
        ball = Ball()
        ball.x_increment = -1
        left_score.increase()
    
    if ball.xcor() < -410:
        ball = Ball()
        ball.x_increment = 1
        right_score.increase()

    screen.update()
    time.sleep(start_sleep / ball.move_speed)

screen.exitonclick()
